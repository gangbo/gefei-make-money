# E-005：受限背景建筑生成

入口：[报告](../../reports/background-buildings-baseline-2026-09-11.md)、[预设方案](plan.md)。仅本地技术实验，无AI模型、第三方素材或线上部署。

## 文件

- `inputs.json`：10组自拟参数。
- `generate.py`：Blender Python生成、GLB导出、重新导入、正反两面预览；最终修正规则。
- `verify.py`：独立trimesh解析、几何与材质检查、带深度缓冲的简单正交预览及总览拼图。
- `validate-gltf.cjs`：Khronos格式校验，完整报告在`gltf-validation.json`。
- `check-invalid.py`：11个无效参数拒绝检查；`invalid-results.json`为实测。
- `outputs/`：最终10个GLB、门窗位置记录、40张预览。
- `results.json`、`independent-results.json`：最终运行数据。
- `initial-*`：首轮或几何修正前留档，包括01模型、脚本、结果和问题预览。`initial-verify.py`使用有遮挡缺陷的画家算法，仅为失败记录，不作为当前校验器。
- `repreview.py`、`repreview.log`：中间取景修正操作；正常重现只需下面四个命令，不需运行它。

## 重现

使用Python 3.11、`bpy==4.5.6`、`trimesh==4.7.4`、`numpy==1.26.4`、`pillow==11.3.0`。Node使用`gltf-validator@2.0.0-dev.3.10`。实际依赖清单见`requirements-lock.txt`。运行前安装依赖，不安装到生产项目。

在本目录运行：

```sh
python generate.py
python verify.py
python check-invalid.py
node validate-gltf.cjs
```

若glTF依赖安装在其他位置，用`GLTF_VALIDATOR_MODULE`指定模块绝对路径。当前临时环境为`/tmp/gefei-blender-env`与`/tmp/gefei-gltf-check`，可能被系统清理。

Blender在受限环境读取硬件信息时曾在导入阶段崩溃；正常本机运行成功。这不能证明Linux容器部署兼容性。CPU预览400×400、12 samples，时长不代表高质量广告渲染。
