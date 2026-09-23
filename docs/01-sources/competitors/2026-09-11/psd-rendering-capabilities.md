# S-021：PSD渲染能力与实验入口

2026-09-11，公开官方资料人工摘要。查询：`site.github.com Agamnentzar ag-psd smart objects rendering updating image data`、`site.psd-tools.readthedocs.io smart object rendering compositing limitations`、`site.photopea.com api smart object scripts replace contents`。

- [ag-psd](https://github.com/Agamnentzar/ag-psd)：PSD读写不自动重绘合成数据；部分色彩模式及特性有限制。核查README和本地安装类型/实现。[相关问题147](https://github.com/Agamnentzar/ag-psd/issues/147)描述更换智能对象后整图未更新，不作为独立市场需求。
- [Photopea智能对象脚本](https://www.photopea.com/tuts/edit-smart-objects-with-a-script/)：文档给出通过脚本编辑智能对象的路线。
- [消息API](https://www.photopea.com/api/live)、[脚本参考](https://www.photopea.com/learn/scripts)：外部页面可传二进制文件和脚本，编辑器可返回导出图。仅文档核查，未实跑，不推定商用成本。

Chrome尝试打开Photopea超时，未进入账号操作。测试资产全部自建，没有从未知许可的免费模板站获取图片。E-006仅本地读写层检查，产物见[报告](../../../04-validation/reports/psd-rendering-preflight-2026-09-11.md)，不是商业PSD或完整渲染基准。
