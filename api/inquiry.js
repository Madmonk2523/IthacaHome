/** Vercel serverless endpoint. Set RESEND_API_KEY and CONTACT_FROM_EMAIL in Vercel. */
const EMAIL='rentals@ithacahome.com';
const TOLERANCE=120000;
const lastRequests=new Map(); // best-effort per warm function instance; production Turnstile recommended
function clean(value,limit){return typeof value==='string'?value.trim().slice(0,limit):'';}
function validEmail(value){return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value) && value.length<=180;}
function safeHtml(s){return s.replace(/[&<>"']/g,ch=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));}
module.exports=async function handler(req,res){
  res.setHeader('Content-Type','application/json; charset=utf-8');
  res.setHeader('Cache-Control','no-store');
  if(req.method!=='POST'){res.setHeader('Allow','POST');return res.status(405).json({error:'Method not allowed.'});}
  const type=req.headers['content-type']||'';
  if(!type.startsWith('application/json'))return res.status(415).json({error:'Expected a JSON form submission.'});
  const data=req.body&&typeof req.body==='object'?req.body:{};
  if(clean(data.website,200)){return res.status(200).json({ok:true});} // honeypot: quietly ignore bots
  const name=clean(data.name,120),email=clean(data.email,180),phone=clean(data.phone,40),property=clean(data.property,60),bedrooms=clean(data.bedrooms,6),moveIn=clean(data.moveIn,12),message=clean(data.message,3000);
  if(name.length<2 || !validEmail(email) || !['Plaza East','SummerHill','Either'].includes(property) || !['','2','3','4'].includes(bedrooms) || (property==='SummerHill'&&bedrooms==='4') || (moveIn&&!/^\d{4}-\d{2}$/.test(moveIn))){
    return res.status(400).json({error:'Please check the required fields and try again.'});
  }
  const ip=(req.headers['x-forwarded-for']||'').split(',')[0].trim()||'unknown';
  const now=Date.now();
  if(lastRequests.has(ip)&&now-lastRequests.get(ip)<30000)return res.status(429).json({error:'Please wait a moment before sending another inquiry.'});
  for(const [key,value] of lastRequests)if(now-value>TOLERANCE)lastRequests.delete(key);
  if(!process.env.RESEND_API_KEY || !process.env.CONTACT_FROM_EMAIL){
    return res.status(503).json({error:'Online inquiries are being configured. Please email rentals@ithacahome.com directly in the meantime.'});
  }
  lastRequests.set(ip,now);
  const content=[['Name',name],['Email',email],['Phone',phone||'Not supplied'],['Property',property],['Bedrooms',bedrooms||'Flexible'],['Move-in',moveIn||'Flexible'],['Message',message||'None']];
  const html=`<div style="font-family:Arial,sans-serif;max-width:620px;margin:0 auto"><h1>New IthacaHome leasing inquiry</h1>${content.map(([label,value])=>`<p><strong>${label}:</strong><br>${safeHtml(value).replace(/\n/g,'<br>')}</p>`).join('')}</div>`;
  try{
    const response=await fetch('https://api.resend.com/emails',{method:'POST',headers:{'Authorization':`Bearer ${process.env.RESEND_API_KEY}`,'Content-Type':'application/json'},body:JSON.stringify({from:process.env.CONTACT_FROM_EMAIL,to:[process.env.CONTACT_TO_EMAIL||EMAIL],reply_to:email,subject:`IthacaHome inquiry — ${property} — ${name.replace(/[\r\n]/g,' ')}`,html})});
    if(!response.ok){const txt=await response.text();console.error('Resend failure',response.status,txt.slice(0,300));return res.status(502).json({error:'We could not deliver your inquiry. Please email rentals@ithacahome.com directly.'});}
    return res.status(200).json({ok:true});
  }catch(error){console.error('Inquiry request error',error?.message);return res.status(502).json({error:'Unable to deliver your message right now. Please email rentals@ithacahome.com directly.'});}
};