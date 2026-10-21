"""Non-destructive verification; does not regenerate older designs."""
from pathlib import Path
import re
root=Path(__file__).parent
pages=['index.html','plaza-east.html','summerhill.html','neighborhood.html','contact.html','privacy.html']
images=[]
for page in pages:
 s=(root/page).read_text()
 assert '/assets/site.css' in s and '/assets/site.js' in s
 images+=re.findall(r'<img\\b[^>]*\\bsrc=["\\\']([^"\\\']+)',s)
assert len(images)==len(set(images)),'Repeated photo references'
print('IthacaHome source validated')
