"""Non-destructive IthacaHome build check.

The site is maintained as plain HTML/CSS/JS; do not regenerate it from an
obsolete V10 design script. This command validates files without rewriting them.
"""
from pathlib import Path
from collections import Counter
from bs4 import BeautifulSoup
root = Path(__file__).resolve().parent
pages = ['index.html','plaza-east.html','summerhill.html','neighborhood.html','contact.html','privacy.html']
seen = Counter()
for name in pages:
    text=(root/name).read_text(encoding='utf-8')
    soup=BeautifulSoup(text,'html.parser')
    assert soup.select_one('main') and soup.select_one('h1'), f'{name}: missing main/h1'
    for asset in ['/assets/site.css','/assets/v14.css','/assets/site.js']:
        assert asset in text and (root/asset.lstrip('/')).is_file(), f'{name}: missing {asset}'
    for image in soup.select('main img[src]'):
        src=image['src']; seen[src]+=1
        assert src.startswith('/assets/'), f'{name}: unexpected remote image {src}'
        if '/property-gallery/' not in src:
            assert (root/src.lstrip('/')).is_file(), f'{name}: missing {src}'
assert max(seen.values(),default=0)==1, f'Duplicate photos: {[x for x,n in seen.items() if n>1]}'
print(f'OK: {len(pages)} pages; {len(seen)} distinct images; no destructive file changes.')
