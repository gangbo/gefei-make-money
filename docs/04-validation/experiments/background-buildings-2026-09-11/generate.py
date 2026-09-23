"""Self-authored constrained geometry. Run using Python with bpy installed."""
import bpy, json, math, time, platform
from pathlib import Path
from mathutils import Vector
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'outputs'; OUT.mkdir(exist_ok=True)
PALETTES=[(.48,.16,.09,1),(.10,.25,.30,1),(.62,.43,.19,1)]
FACES=[(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]

def validate(p):
    for k,lo,hi in [('width',3.2,20),('depth',2.8,16)]:
        v=p[k]
        if isinstance(v,bool) or not isinstance(v,(float,int)) or not math.isfinite(v) or not lo<=v<=hi: raise ValueError(k)
    if type(p['floors']) is not int or not 1<=p['floors']<=8: raise ValueError('floors')
    if type(p['palette']) is not int or not 0<=p['palette']<3: raise ValueError('palette')

def make(p):
    validate(p)
    verts=[]; faces=[]; mids=[]; boxes=[]; placements=[]
    def box(name,c,s,m):
        x,y,z=c; a,b,h=[v/2 for v in s]; n=len(verts)
        verts.extend([(x-a,y-b,z-h),(x+a,y-b,z-h),(x+a,y+b,z-h),(x-a,y+b,z-h),
                      (x-a,y-b,z+h),(x+a,y-b,z+h),(x+a,y+b,z+h),(x-a,y+b,z+h)])
        faces.extend([tuple(n+i for i in f) for f in FACES]); mids.extend([m]*6)
        boxes.append({'name':name,'center':c,'size':s})
    w,d=p['width'],p['depth']; height=3*p['floors']
    box('body',(0,0,(height+.24)/2),(w,d,height-.24),0)
    box('base',(0,0,.12),(w+.24,d+.24,.24),1)
    for level in range(1,p['floors']+1):
        box('cornice',(0,0,level*3-.09),(w+.20,d+.20,.18),1)
    box('roof',(0,0,height+.06),(w+.12,d+.12,.12),2)
    # Roof parapets: no hidden interior requirement.
    for y in [-d/2,d/2]: box('parapet',(0,y,height+.25),(w+.20,.18,.38),1)
    for x in [-w/2,w/2]: box('parapet',(x,0,height+.25),(.18,d-.18,.38),1)
    for side,length in [('front',w),('back',w),('left',d),('right',d)]:
        count=max(1,int((length-.6)/1.8)); pitch=(length-.6)/count
        for level in range(p['floors']):
            for col in range(count):
                u=-length/2+.3+pitch*(col+.5); z=level*3+1.55
                if side=='front' and level==0 and abs(u)<1.3: continue
                ww=min(1.05,pitch-.36)
                placements.append({'side':side,'u':u,'z':z,'width':ww,'height':1.50,'wall_length':length})
                def facade(name,out,span,tall,zz,mat):
                    if side in ('front','back'):
                        center=(u,(-1 if side=='front' else 1)*(d/2+out),zz); size=(span,.06,tall)
                    else:
                        center=((-1 if side=='left' else 1)*(w/2+out),u,zz); size=(.06,span,tall)
                    box(name,center,size,mat)
                facade('window-trim',.035,ww+.14,1.50,z,1)
                facade('window-pane',.074,ww,1.30,z,3)
                facade('window-sill',.10,ww+.22,.10,z-.76,1)
    box('door-trim',(0,-d/2-.04,1.12),(1.30,.08,2.24),1)
    box('door',(0,-d/2-.14,1.08),(1.10,.05,2.12),4)
    box('canopy',(0,-d/2-.38,2.40),(1.70,.82,.12),2)
    mesh=bpy.data.meshes.new('building_mesh'); mesh.from_pydata(verts,[],faces); mesh.update()
    obj=bpy.data.objects.new(p['id'],mesh); bpy.context.collection.objects.link(obj)
    colors=[PALETTES[p['palette']],(.79,.73,.60,1),(.12,.14,.16,1),(.045,.11,.16,1),(.25,.09,.045,1)]
    for i,color in enumerate(colors):
        mat=bpy.data.materials.new(['wall','trim','roof','glass-painted','door'][i]); mat.use_nodes=True
        bs=mat.node_tree.nodes.get('Principled BSDF'); bs.inputs['Base Color'].default_value=color
        bs.inputs['Roughness'].default_value=.85 if i!=3 else .3
        mesh.materials.append(mat)
    for poly,mi in zip(mesh.polygons,mids): poly.material_index=mi
    bpy.context.view_layer.objects.active=obj; obj.select_set(True)
    # All modeled windows must fit facade and floors; door reserved corridor.
    assert all(abs(q['u'])+(q['width']+.22)/2<q['wall_length']/2 for q in placements)
    assert all(.2<q['z']-.81 and q['z']+.75<height for q in placements)
    return obj,boxes,placements

def render(p,angle,path):
    scene=bpy.context.scene; h=p['floors']*3; size=max(p['width'],p['depth'],h)
    points=[o.matrix_world @ Vector(c) for o in bpy.context.scene.objects if o.type=='MESH' for c in o.bound_box]
    low=Vector(tuple(min(v[a] for v in points) for a in range(3))); high=Vector(tuple(max(v[a] for v in points) for a in range(3)))
    target=(low+high)/2; camdata=bpy.data.cameras.new('camera'); cam=bpy.data.objects.new('camera',camdata); scene.collection.objects.link(cam)
    cam.location=target+Vector((math.cos(angle)*size*2, math.sin(angle)*size*2,size*1.5))
    cam.rotation_euler=(target-cam.location).to_track_quat('-Z','Y').to_euler(); camdata.type='ORTHO'; right=cam.rotation_euler.to_matrix() @ Vector((1,0,0)); up=cam.rotation_euler.to_matrix() @ Vector((0,1,0))
    projected=[((v-target).dot(right),(v-target).dot(up)) for v in points]
    camdata.ortho_scale=1.12*max(max(v[a] for v in projected)-min(v[a] for v in projected) for a in range(2))
    scene.camera=cam
    lightdata=bpy.data.lights.new('key','AREA'); light=bpy.data.objects.new('key',lightdata); scene.collection.objects.link(light)
    light.location=target+Vector((-size,-size,size*2)); light.rotation_euler=(target-light.location).to_track_quat('-Z','Y').to_euler(); lightdata.energy=1500*size*size/100; lightdata.shape='DISK'; lightdata.size=size
    scene.world.color=(.32,.32,.32)
    scene.render.engine='CYCLES'; scene.cycles.device='CPU'; scene.cycles.samples=12
    scene.render.resolution_x=400; scene.render.resolution_y=400; scene.render.resolution_percentage=100
    scene.render.image_settings.file_format='PNG'; scene.render.filepath=str(path)
    scene.view_settings.view_transform='Standard'; scene.render.film_transparent=False
    bpy.ops.render.render(write_still=True)
    bpy.data.objects.remove(cam,do_unlink=True); bpy.data.objects.remove(light,do_unlink=True)

if __name__=='__main__':
    results=[]
    for p in json.loads((ROOT/'inputs.json').read_text()):
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.context.scene.world=bpy.data.worlds.new('World')
        start=time.perf_counter(); obj,boxes,placements=make(p)
        mesh=obj.data; mesh.calc_loop_triangles()
        bounds=[[min(v.co[a] for v in mesh.vertices) for a in range(3)],[max(v.co[a] for v in mesh.vertices) for a in range(3)]]
        path=OUT/(p['id']+'.glb')
        bpy.ops.export_scene.gltf(filepath=str(path),export_format='GLB',use_selection=True,export_yup=True)
        elapsed=time.perf_counter()-start
        row={'input':p,'generation_export_seconds':elapsed,'bytes':path.stat().st_size,'source_triangles':len(mesh.loop_triangles),'source_bounds_z_up':bounds,'materials':5,'boxes':len(boxes),'windows':len(placements),'placement_checks':True}
        (OUT/(p['id']+'-placements.json')).write_text(json.dumps(placements,indent=2))
        # Re-import exported GLB; previews intentionally show delivered model.
        bpy.data.objects.remove(obj,do_unlink=True); start=time.perf_counter()
        bpy.ops.import_scene.gltf(filepath=str(path))
        row['blender_reimport_seconds']=time.perf_counter()-start
        start=time.perf_counter()
        for angle,suffix in [(-math.pi/3,'front'),(math.pi*2/3,'back')]: render(p,angle,OUT/(p['id']+'-'+suffix+'.png'))
        row['two_previews_seconds']=time.perf_counter()-start
        results.append(row); (ROOT/'results.json').write_text(json.dumps({'blender':bpy.app.version_string,'python':platform.python_version(),'platform':platform.platform(),'results':results},indent=2))
        print('RESULT',json.dumps(row),flush=True)
