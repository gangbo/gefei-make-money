// Narrow negative test: changing linked payloads is NOT a render engine.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const deps=process.env.PSD_TEST_DEPS||'/tmp/gefei-psd-check/node_modules';
const psd=require(path.join(deps,'ag-psd')),cv=require(path.join(deps,'@napi-rs/canvas'));
psd.initializeCanvas(cv.createCanvas);
const dir=__dirname; const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
function art(color,text){let c=cv.createCanvas(160,120),x=c.getContext('2d');x.fillStyle=color;x.fillRect(0,0,160,120);x.fillStyle='#fff';x.font='bold 27px sans-serif';x.fillText(text,12,66);return c;}
const old=art('#a52332','OLD'),fresh=art('#116caf','NEW');fs.writeFileSync(path.join(dir,'replacement.png'),fresh.toBuffer('image/png'));
const cases=[{id:'front',slots:[[1,0,0,1,90,70]]},{id:'slanted',slots:[[1,.18,-.18,1,100,60]]},{id:'two-slots',slots:[[.8,.1,-.1,.8,30,50],[.8,-.1,.1,.8,210,110]]}];
let results=[];
for(const c of cases){
 const root=cv.createCanvas(420,300),ctx=root.getContext('2d');ctx.fillStyle='#e5e9ed';ctx.fillRect(0,0,420,300);
 const children=[],linkedFiles=[];
 c.slots.forEach((m,i)=>{
   const id=`00000000-0000-4000-8000-${String(i+1).padStart(12,'0')}`;
   const layer=cv.createCanvas(420,300),lx=layer.getContext('2d');lx.setTransform(...m);lx.drawImage(old,0,0);ctx.drawImage(layer,0,0);
   const xy=(x,y)=>[m[0]*x+m[2]*y+m[4],m[1]*x+m[3]*y+m[5]];
   children.push({name:`ART_${i+1}`,left:0,top:0,canvas:layer,placedLayer:{id,type:'raster',width:160,height:120,transform:[...xy(0,0),...xy(160,0),...xy(160,120),...xy(0,120)]}});
   linkedFiles.push({id,name:`art-${i+1}.png`,type:'png ',data:old.toBuffer('image/png')});
 });
 const before=psd.writePsdBuffer({width:420,height:300,canvas:root,children,linkedFiles});fs.writeFileSync(path.join(dir,c.id+'-before.psd'),before);
 const parsed=psd.readPsd(before);const oldComposite=parsed.canvas.toBuffer('image/png');
 const transforms=parsed.children.map(l=>l.placedLayer.transform);
 for(const f of parsed.linkedFiles)f.data=fresh.toBuffer('image/png');
 const saved=psd.writePsdBuffer(parsed);fs.writeFileSync(path.join(dir,c.id+'-payload-changed.psd'),saved);
 const after=psd.readPsd(saved);const preview=after.canvas.toBuffer('image/png');fs.writeFileSync(path.join(dir,c.id+'-cached-output.png'),preview);
 const row={id:c.id,slots:c.slots.length,psd_reopens:true,all_embedded_payloads_changed:after.linkedFiles.every(f=>hash(f.data)===hash(fresh.toBuffer('image/png'))),transform_metadata_preserved:JSON.stringify(transforms)===JSON.stringify(after.children.map(l=>l.placedLayer.transform)),composite_still_identical:hash(preview)===hash(oldComposite),before_sha256:hash(before),after_sha256:hash(saved)};
 results.push(row);
 if(!row.all_embedded_payloads_changed||!row.composite_still_identical)throw Error('Unexpected test outcome');
}
fs.writeFileSync(path.join(dir,'results.json'),JSON.stringify({node:process.version,ag_psd:require(path.join(deps,'ag-psd/package.json')).version,canvas:require(path.join(deps,'@napi-rs/canvas/package.json')).version,scope:'Self-authored serialization fixtures, NOT Photoshop/Photopea compatibility or visual-fidelity validation',results},null,2));
console.log(JSON.stringify(results,null,2));
