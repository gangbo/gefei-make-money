"""Independent trimesh GLB parsing; Pillow orthographic preview, no bpy import."""
import json, math, time, platform
from pathlib import Path
import numpy as np
import trimesh
from PIL import Image, ImageDraw
ROOT=Path(__file__).resolve().parent; OUT=ROOT/'outputs'

def independent_preview(scene,p,angle,path):
    # glTF uses Y-up. Simple opaque flat-color renderer; not an engine test.
    camera=np.array([math.cos(angle)*2,1.5,math.sin(angle)*2]); camera/=np.linalg.norm(camera)
    right=np.cross(np.array([0,1,0]),camera); right/=np.linalg.norm(right); up=np.cross(camera,right)
    triangles=[]; points=[]
    for node in scene.graph.nodes_geometry:
        matrix,key=scene.graph[node]; geo=scene.geometry[key]
        v=trimesh.transform_points(geo.vertices,matrix)
        mat=geo.visual.material
        color=np.array(getattr(mat,'baseColorFactor',[180,180,180,255])[:3],dtype=float)
        for f in geo.faces:
            xyz=v[f]; normal=np.cross(xyz[1]-xyz[0],xyz[2]-xyz[0]); normal/=max(np.linalg.norm(normal),1e-12)
            if np.dot(normal,camera)<=0: continue
            xy=np.stack([xyz@right,xyz@up],axis=1); points.extend(xy)
            light=np.array([-.5,.8,.4]); light/=np.linalg.norm(light)
            shade=.55+.45*max(0,float(normal@light)); c=tuple((np.clip(color*shade,0,255)).astype(int))
            triangles.append((xyz@camera,xy,c))
    a=np.array(points); center=(a.min(0)+a.max(0))/2; scale=340/max(np.ptp(a,axis=0))
    pixels=np.full((400,400,3),[232,237,242],dtype=np.uint8)
    zbuffer=np.full((400,400),-np.inf)
    for depth,xy,c in triangles:
        xy=(xy-center)*scale; xy[:,1]*=-1; xy+=200
        xmin=max(0,int(np.floor(xy[:,0].min()))); xmax=min(399,int(np.ceil(xy[:,0].max())))
        ymin=max(0,int(np.floor(xy[:,1].min()))); ymax=min(399,int(np.ceil(xy[:,1].max())))
        if xmin>xmax or ymin>ymax: continue
        xx,yy=np.meshgrid(np.arange(xmin,xmax+1)+.5,np.arange(ymin,ymax+1)+.5)
        a,b,cpoint=xy
        denom=(b[1]-cpoint[1])*(a[0]-cpoint[0])+(cpoint[0]-b[0])*(a[1]-cpoint[1])
        if abs(denom)<1e-9: continue
        u=((b[1]-cpoint[1])*(xx-cpoint[0])+(cpoint[0]-b[0])*(yy-cpoint[1]))/denom
        v=((cpoint[1]-a[1])*(xx-cpoint[0])+(a[0]-cpoint[0])*(yy-cpoint[1]))/denom
        w=1-u-v; z=u*depth[0]+v*depth[1]+w*depth[2]
        zb=zbuffer[ymin:ymax+1,xmin:xmax+1]; mask=(u>=-1e-7)&(v>=-1e-7)&(w>=-1e-7)&(z>zb)
        zb[mask]=z[mask]; pixels[ymin:ymax+1,xmin:xmax+1][mask]=c
    Image.fromarray(pixels).save(path)

rows=[]
for r in json.loads((ROOT/'results.json').read_text())['results']:
    p=r['input']; start=time.perf_counter(); scene=trimesh.load(OUT/(p['id']+'.glb'),force='scene',process=False)
    triangles=0; minimum_area=float('inf'); finite=True; winding=True; watertight=True; positive_volume=True
    material_names=[]; colors_preserved=True
    expected_colors=dict(zip(["wall","trim","roof","glass-painted","door"],[[[.48,.16,.09],[.10,.25,.30],[.62,.43,.19]][p["palette"]],[.79,.73,.60],[.12,.14,.16],[.045,.11,.16],[.25,.09,.045]]))
    for key,g in scene.geometry.items():
        triangles+=len(g.faces); minimum_area=min(minimum_area,float(g.area_faces.min()))
        finite &= bool(np.isfinite(g.vertices).all() and np.isfinite(g.vertex_normals).all())
        winding &= bool(g.is_winding_consistent)
        # GLB splits UV/normal seam vertices. Merge coincident positions only for topology check.
        welded=g.copy(); welded.merge_vertices(); watertight &= bool(welded.is_watertight)
        positive_volume &= bool(welded.volume>0)
        material_names.append(g.visual.material.name)
        colors_preserved &= bool(np.max(np.abs(g.visual.material.baseColorFactor[:3]/255-np.array(expected_colors[g.visual.material.name])))<=1/255)
    b=np.array(r['source_bounds_z_up']); transformed=np.array([[b[0,0],b[0,2],-b[1,1]],[b[1,0],b[1,2],-b[0,1]]])
    err=float(np.max(np.abs(scene.bounds-transformed)))
    checks={'readable':True,'bounds_under_1mm':err<.001,'triangles_match_source':triangles==r['source_triangles'],
            'finite':finite,'no_degenerate_faces':minimum_area>1e-10,'consistent_winding':winding,
            'welded_primitives_watertight':watertight,'positive_volume':positive_volume,'triangles_budget':triangles<=30000,
            'file_budget':r['bytes']<=2_000_000,'base_colors_preserved':colors_preserved,'materials_preserved':set(material_names)=={'wall','trim','roof','glass-painted','door'}}
    row={'id':p['id'],'triangles':triangles,'material_names':material_names,'bounds_error_m':err,'minimum_triangle_area':minimum_area,'checks':checks,'parse_check_seconds':time.perf_counter()-start}
    rows.append(row)
    for angle,suffix in [(-math.pi/3,'front'),(math.pi*2/3,'back')]:
        # Blender x,y,z -> glTF x,z,-y changes viewing angle sign.
        independent_preview(scene,p,-angle,OUT/(p['id']+'-independent-'+suffix+'.png'))
(ROOT/'independent-results.json').write_text(json.dumps({'trimesh':trimesh.__version__,'python':platform.python_version(),'results':rows},indent=2))
# Contact sheets group front/back for every case.
for kind,label in [('', 'Blender GLB reimport'),('independent-','Independent GLB / trimesh')]:
    sheet=Image.new('RGB',(1600,5*430),'#f4f6f8'); draw=ImageDraw.Draw(sheet)
    for i,p in enumerate(json.loads((ROOT/'inputs.json').read_text())):
        col=(i%2)*800; top=(i//2)*430
        draw.text((col+12,top+8),f"{p['id']} | {p['width']} x {p['depth']} m | {p['floors']} floors | {label}",fill='#151e29')
        for j,suffix in enumerate(['front','back']):
            sheet.paste(Image.open(OUT/(p['id']+'-'+kind+suffix+'.png')).convert('RGB'),(col+j*400,top+30))
    sheet.save(ROOT/('contact-sheet-'+('blender' if not kind else 'independent')+'.png'))
print(json.dumps(rows,indent=2))
