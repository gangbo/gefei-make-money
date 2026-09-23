"""Synthetic technical benchmark. No customer or commercial-tool quality claims."""
from pathlib import Path
import io,json,time,re,csv,platform,importlib.metadata,xml.etree.ElementTree as ET
import numpy as np
from PIL import Image,ImageFilter,ImageDraw
import vtracer,resvg_py
ROOT=Path(__file__).resolve().parent
ART={
 'geometry':'<path fill="#16243b" d="M80 400L256 72L432 400H345L256 226L167 400Z"/><circle fill="#e86636" cx="256" cy="350" r="25"/>',
 'three_colors':'<circle fill="#1f5678" cx="218" cy="256" r="150"/><path fill="#e56a39" d="M218 106L430 256L218 406Z"/><circle fill="#edc44e" cx="218" cy="256" r="64"/>',
 'outline_letters':'<path fill="#172536" fill-rule="evenodd" d="M65 150H133Q190 150 190 202Q190 232 165 243Q198 260 198 295Q198 358 133 358H65ZM97 181V228H132Q156 228 156 204Q156 181 132 181ZM97 257V327H130Q164 327 164 294Q164 257 130 257ZM214 150H312V358H214ZM245 182V326H281V182ZM333 150H365L390 218L415 150H447L407 251L451 358H416L390 285L364 358H330L373 251Z"/>',
 'thin_lines':'<g fill="none" stroke="#142a3b" stroke-width="5"><path d="M70 80H220V220H430M70 180H165V300H420M70 420H280V350H420M300 80V150H420"/><circle cx="70" cy="80" r="14"/><circle cx="70" cy="180" r="14"/><circle cx="70" cy="420" r="14"/><circle cx="300" cy="80" r="14"/><circle cx="430" cy="220" r="14"/></g><path fill="none" stroke="#d14e36" stroke-width="3" d="M80 465L170 365L260 465L350 365L440 465"/>',
 'holes_gaps':'<path fill="#183246" fill-rule="evenodd" d="M70 70H442V442H70ZM110 110V402H402V110Z"/><circle fill="#183246" cx="256" cy="256" r="104"/><circle fill="white" cx="256" cy="256" r="74"/><rect fill="white" x="252" y="65" width="8" height="120"/><circle fill="white" cx="95" cy="95" r="4"/>'
}
for d in ['truth','inputs','preprocessed','outputs/default','outputs/clean4','renders/default','renders/clean4','outputs/upsample512','renders/upsample512','upsampled']:(ROOT/d).mkdir(parents=True,exist_ok=True)
def render(svg):
 return Image.open(io.BytesIO(resvg_py.svg_to_bytes(svg_string=svg,width=512,height=512,background='white',skip_system_fonts=True))).convert('RGB')
def metrics(a,b):
 a=np.asarray(a).astype(float);b=np.asarray(b).astype(float)
 am=np.min(a,axis=2)<240;bm=np.min(b,axis=2)<240
 union=am|bm;inter=am&bm
 return {'foreground_iou':float(inter.sum()/max(union.sum(),1)), 'foreground_mae':float(np.abs(a-b)[union].mean()) if union.any() else 0}
rows=[];manifest=[]
for name,body in ART.items():
 svg='<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">'+body+'</svg>'
 (ROOT/'truth'/f'{name}.svg').write_text(svg)
 truth=render(svg);truth.save(ROOT/'truth'/f'{name}.png')
 for condition in ['clean512','small128','jpeg64','paper128']:
  size=512 if condition=='clean512' else 64 if condition=='jpeg64' else 128
  inp=truth.resize((size,size),Image.Resampling.LANCZOS)
  if condition=='jpeg64':
   buf=io.BytesIO();inp.save(buf,format='JPEG',quality=35);buf.seek(0);inp=Image.open(buf).convert('RGB')
  if condition=='paper128':
   a=np.asarray(inp).astype(float);x=np.linspace(0,1,size)[None,:,None]
   a=a*(0.82+0.18*x);inp=Image.fromarray(a.clip(0,255).astype('uint8'))
  sid=f'{name}-{condition}';ip=ROOT/'inputs'/f'{sid}.png';inp.save(ip)
  manifest.append({'id':sid,'source':f'truth/{name}.svg','condition':condition,'input_size':size,'license':'Original programmatic artwork created for this benchmark; reusable by project owner','input_metrics':metrics(truth,inp.resize((512,512),Image.Resampling.LANCZOS))})
  for method in ['default','clean4','upsample512']:
   start=time.perf_counter();source=ip
   if method=='clean4':
    p=inp.filter(ImageFilter.MedianFilter(3)).quantize(colors=4,method=Image.Quantize.MEDIANCUT).convert('RGB')
    source=ROOT/'preprocessed'/f'{sid}.png';p.save(source)
   if method=='upsample512':
    source=ROOT/'upsampled'/f'{sid}.png';inp.resize((512,512),Image.Resampling.LANCZOS).save(source)
   op=ROOT/'outputs'/method/f'{sid}.svg'
   try:
    vtracer.convert_image_to_svg_py(str(source),str(op))
    elapsed=time.perf_counter()-start;out=op.read_text();im=render(out);im.save(ROOT/'renders'/method/f'{sid}.png')
    paths=[e.attrib.get('d','') for e in ET.fromstring(out).iter() if e.tag.endswith('}path')]
    mm=metrics(truth,im)
    rows.append({'id':sid,'method':method,'condition':condition,'seconds':round(elapsed,5),'bytes':op.stat().st_size,'paths':len(paths),'commands':sum(len(re.findall('[MmLlHhVvCcSsQqTtAaZz]',d)) for d in paths),'embedded_bitmap':'<image' in out,**mm,'pixel_screen_pass':mm['foreground_iou']>=.98 and mm['foreground_mae']<=8,'error':None})
   except Exception as e: rows.append({'id':sid,'method':method,'condition':condition,'error':str(e)})
(ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2))
(ROOT/'results.json').write_text(json.dumps(rows,indent=2))
(ROOT/'environment.json').write_text(json.dumps({'python':platform.python_version(),'platform':platform.platform(),'packages':{p:importlib.metadata.version(p) for p in ['vtracer','resvg-py','pillow','numpy']}},indent=2))
with (ROOT/'results.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(next(r for r in rows if not r['error']).keys()));w.writeheader();w.writerows(rows)
# Contact sheets retain all 20 cases; each design has four conditions x four columns.
for name in ART:
 sheet=Image.new('RGB',(1280,4*282+32),'#dddddd');draw=ImageDraw.Draw(sheet)
 for col,label in enumerate(['Truth','Input (enlarged)','VTracer default','Median + 4 colors','Upsample then trace']):draw.text((col*256+8,8),label,fill='black')
 for row,condition in enumerate(['clean512','small128','jpeg64','paper128']):
  sid=f'{name}-{condition}';y=32+row*282
  files=[ROOT/'truth'/f'{name}.png',ROOT/'inputs'/f'{sid}.png',ROOT/'renders/default'/f'{sid}.png',ROOT/'renders/clean4'/f'{sid}.png',ROOT/'renders/upsample512'/f'{sid}.png']
  for col,f in enumerate(files):
   if f.exists():sheet.paste(Image.open(f).convert('RGB').resize((256,256)),(col*256,y))
  draw.text((8,y+258),condition,fill='black')
 sheet.save(ROOT/f'compare-{name}.png')
summary={}
for method in ['default','clean4','upsample512']:
 rr=[r for r in rows if r['method']==method and not r['error']]
 summary[method]={'completed':len(rr),'pixel_screen_pass':sum(r['pixel_screen_pass'] for r in rr),'median_seconds':float(np.median([r['seconds'] for r in rr])),'median_paths':float(np.median([r['paths'] for r in rr])),'median_commands':float(np.median([r['commands'] for r in rr])),'mean_iou':float(np.mean([r['foreground_iou'] for r in rr])),'mean_mae':float(np.mean([r['foreground_mae'] for r in rr]))}
(ROOT/'summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
