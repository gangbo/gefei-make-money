const fs = require('node:fs');
const path = require('node:path');
const validator = require(process.env.GLTF_VALIDATOR_MODULE || 'gltf-validator');
(async () => {
  const inputs = JSON.parse(fs.readFileSync(path.join(__dirname, 'inputs.json'), 'utf8'));
  const reports = [];
  for (const p of inputs) {
    const file = p.id + '.glb';
    const bytes = fs.readFileSync(path.join(__dirname, 'outputs', file));
    const report = await validator.validateBytes(new Uint8Array(bytes), {uri: file, maxIssues: 1000});
    reports.push({id: p.id, report});
  }
  fs.writeFileSync(path.join(__dirname, 'gltf-validation.json'), JSON.stringify(reports, null, 2));
  console.log(reports.map(x => ({id:x.id, issues:x.report.issues})));
  if (reports.some(x => x.report.issues.numErrors)) process.exitCode = 1;
})().catch(e => { console.error(e); process.exitCode=1; });
