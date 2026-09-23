# E-006：PSD读写与重新渲染的区别

2026-09-11，D-003的前置检查。全部样本由check.cjs自行创建，使用色块和OLD/NEW文字，无第三方模板、图片或客户文件。

## 可复现步骤

临时环境安装ag-psd和@napi-rs/canvas；实际版本见results.json。设置PSD_TEST_DEPS为node_modules路径，运行`node check.cjs`。默认使用/tmp/gefei-psd-check/node_modules，临时目录可能被清理。

三个样本：正面单对象、仿射倾斜单对象、两个独立对象。每个PSD预置OLD智能对象源数据、图层像素与合成缓存；再只替换嵌入源文件为NEW并保存、重新读入。脚本预期源文件变化而合成缓存不变，使用SHA256验证。

结果：3/3源文件替换且变换元数据保留；3/3合成缓存没有变化。这是序列化库行为的可重复负面检查，不是渲染器故障率或商品模板通过率。

## 边界

- ag-psd自己写自己读，尚未被Photoshop/Photopea打开确认；不称独立PSD兼容验证。
- cached-output.png是保存于PSD内的旧合成缓存，不是重新渲染结果。
- slanted仅仿射变换，不是完整透视/曲面变形验证；没有位移贴图、滤镜、蒙版等复杂素材。
- 输出不用于证明不同PSD工具谁的视觉质量更好；没有实际用户配置计时。
- Chrome打开Photopea在20秒超时；未执行Photopea脚本、未产生真实渲染基准。

下一步应使用正常运行的Photopea或Photoshop重新编辑并导出样本，确认输出内容确实变化，再补明确许可的真实模板。不能用Canvas平面合成代替这个步骤。

续测更新：Photopea已打开slanted-before.psd并用replacement.png替换智能对象，画布OLD→NEW且目视保留倾斜。PNG导出窗口已到达，但保存时操作连接失效，未确认落盘。其余两例尚未运行。详见../../reports/psd-rendering-preflight-2026-09-11.md。
