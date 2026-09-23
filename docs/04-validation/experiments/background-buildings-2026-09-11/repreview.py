import bpy, json, time, math
from generate import ROOT, OUT, render
r=json.loads((ROOT/'results.json').read_text())
for row in r['results']:
    p=row['input']; bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.context.scene.world=bpy.data.worlds.new('World')
    bpy.ops.import_scene.gltf(filepath=str(OUT/(p['id']+'.glb')))
    start=time.perf_counter()
    for angle,suffix in [(-math.pi/3,'front'),(math.pi*2/3,'back')]: render(p,angle,OUT/(p['id']+'-'+suffix+'.png'))
    row['two_previews_seconds_initial']=row['two_previews_seconds']
    row['two_previews_seconds']=time.perf_counter()-start
(ROOT/'results.json').write_text(json.dumps(r,indent=2))
