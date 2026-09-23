# 实验索引

2026-09-15：[D-048商业验证草案](experiments/hairstyle-2026-09-15/paid-validation-plan.md)已写，尚未执行；质量、成本、获客、同队列付款分别验证，不把四宫格好看当盈利证据。

2026-09-15 E-009续：用户接受轻微姿势/表情变化，授权四宫格测试。内置工具单次生成4种发型，非4次生成后拼接；目测样式可区分、人物可辨认。图片与提示词见docs/04-validation/experiments/hairstyle-2026-09-15/four-hairstyles.png及grid-prompt.md。生产计费未验证，状态不变。

E-009 / D-048：[内置发型前置测试](reports/hairstyle-preflight-2026-09-15.md)，09-15，1个合成人物+2次独立编辑；短发有脸部细节漂移，换色目测较稳。已完成本轮有限测试，未验证真实自拍、生产模型成本或付款。

当前没有新项目的真实付费验证。模拟实验只作为技术观察复用，不作为市场证据。

| 实验 ID | 关联候选 | 已完成与结果 | 边界/状态 | 文件 |
| --- | --- | --- | --- | --- |
| E-001 | D-002 | Bannerbear 公共演示一次长文本提交，观察到生成结果 | 只看到部分输出；不是完整质量验收；已结束 | [观察报告](reports/image-automation-feasibility-2026-09-10.md) |
| E-002 | D-002 | 6 组模拟输入 × 3 尺寸；12 生成、6 拒绝；观察到断词和构图问题 | 无真实商品/客户/AI 调用；不是 12/18 商业成功率；已结束 | [脚本](experiments/template-layout-2026-09-10/test_render.py)、[结果](experiments/template-layout-2026-09-10/results.json)、[总览](experiments/template-layout-2026-09-10/contact-sheet.png) |
| E-003 | 自有 VocalDock | 历史附加流程实验草案 | 未执行，用户要求暂停；低价包已试过，不重启草案 | [草案](../projects/vocaldock-paid-workflow-experiment.md) |
| E-004 | D-014 | 20个合成输入、3条路径、60个输出；固定降噪减色未稳定改善，放大增加路径复杂度 | 本地基线已结束；商业工具和人工编辑时间待补 | [报告](reports/vector-artwork-baseline-2026-09-10.md) |
| E-005 | D-019 | 10组自拟参数生成GLB；独立读取及Khronos校验通过；修正共面与预览问题 | 受限技术基线已完成；无引擎/客户验收或付费验证 | [报告](reports/background-buildings-baseline-2026-09-11.md) |
| E-006 | D-003 | 自建3个PSD，源文件替换成功但合成缓存仍旧，确认读写不等于渲染 | 前置检查完成；Photopea/Photoshop真实渲染和竞品基准未完成 | [报告](reports/psd-rendering-preflight-2026-09-11.md) |
| E-007 | D-030 | PhotoTag免费3图实际生成，页面文字归档 | 暂停（DEC-027）；导出/通用对照/20张未完成，不再主动补齐 | [报告](reports/stock-keywords-phototag-preflight-2026-09-11.md) |
| E-008 | D-039 | blablabla 2.7.1 原创6句解析正确，舞台说明分离；点击推进至完成页一次 | 前置流程完成，语音六情形未测；无付款/音频质量结果 | [报告](reports/actor-rehearsal-preflight-2026-09-12.md) |


下一次新实验至少记录：候选 ID、假设、样本来源、对照方案、成本/时间上限、成功与停止条件、原始结果、结论。真实输入与模拟输入分开。
