#!/usr/bin/env python3
"""Audit V7 site photography: unique placements, existence, and visual near matches.

Run from repository root after all gallery assets are checked out.
"""
from pathlib import Path
from collections import Counter
from PIL import Image
import json, sys, hashlib
import numpy as np
root=Path(__file__).resolve().parent.parent
manifest=json.loads((root/'photo-manifest.json').read_text())
paths=[record['src'] for record in manifest]
duplicates={src:count for src,count in Counter(paths).items() if count>1}
missing=[];checked=[]
for src in paths:
 path=root/src.lstrip('/')
 if path.is_file():checked.append(path)
 else:missing.append(src)

# Compute difference hash for a manual review of same image under different names.
def difference_hash(path):
 with Image.open(path) as im:
  a=np.asarray(im.convert('L').resize((9,8)))
  return sum(int(bit)<<i for i,bit in enumerate((a[:,1:]>a[:,:-1]).flatten()))
seen={};visually_similar=[]
for path in checked:
 try:seen[path]=difference_hash(path)
 except Exception as exc:print('IMAGE DECODE FAILURE:',path,exc);sys.exit(1)
items=list(seen.items())
for i,(a,h1) in enumerate(items):
 for b,h2 in items[i+1:]:
  hd=(h1^h2).bit_count()
  if hd<=5:visually_similar.append((str(a.relative_to(root)),str(b.relative_to(root)),hd))
print('Image placements:',len(paths))
print('Unique paths:',len(set(paths)))
print('Locally available:',len(checked))
print('Gallery assets missing in this checkout:',len(missing))
print('Near matches:',visually_similar or 'none')
assert not duplicates,f'Reused photo URLs: {duplicates}'
if missing:
 print('Gallery assets must be present in a full GitHub clone before public deployment:',', '.join(missing))
if '--strict' in sys.argv and (missing or visually_similar):sys.exit(1)
