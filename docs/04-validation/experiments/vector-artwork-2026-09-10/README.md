# 矢量稿合成基线

入口：[结果报告](../../reports/vector-artwork-baseline-2026-09-10.md)。

复现：在独立Python环境安装 vtracer==0.6.15、resvg-py==0.5.0、pillow==12.3.0 和 environment.json 内所列 numpy 版本，然后运行 `python benchmark.py`。复跑会覆盖生成文件；先保存已有结果。代码无外部API调用。CairoSVG曾安装但系统缺Cairo，最终脚本使用resvg-py。

truth/：原创SVG和渲染真值；inputs/：PNG格式测试输入（JPEG条件先有损编码再解码保存）；outputs/：三方案SVG；renders/：同一渲染器输出；preprocessed/、upsampled/：实际中间输入；compare-*.png：全样本对照。

PROTOCOL.md记录运行前指标与运行后的探索补测。results-first-pass.json保存首轮40项；results.json保存最终三方案60项。不是100份独立样本。
