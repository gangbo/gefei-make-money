# 第二轮：把出版与 Bubble 生态收窄到具体任务

> 当前状态更新：用户指出 PDF 修复规模不明、真实错误样本难获取；后续已停止 PDF 修复和 Bubble 深度维护。下文为当时研究，不再代表开发建议。见[DEC-004](../../decisions.md)与[进度表](../../STATUS.md)。

日期：2026-09-10。承接[12 个收入榜候选](../../02-candidates/reviews/revenue-led-opportunities-2026-09-10.md)。老照片处理已属于用户产品，排除新项目立项；本轮不以访谈为前提，使用公开问题、现有产品和购买后评价。

## 决策

优先验证“出版 PDF 的特定上传错误诊断与修复”，而不是通用涂色书生成。Bubble 方向本轮暂缓开发：文档、翻译和未使用资源检查已有覆盖；历史孤立文件清理虽有痛点，但数据可见性和误删边界尚未解决。

优先验证不等于直接立项。出版 PDF 修复已有直接竞品 BookReady；我们没有它的收入数据，也没有证据证明能比它做得更好。本轮找到的是一条具体、有外部行为线索、可以做对比测试的候选。

## 七个任务的筛选

| 具体任务 | 谁在什么时候需要 | 已有方案与证据 | 结果 |
| --- | --- | --- | --- |
| 涂色图批量清理、排版、导出 KDP PDF | 出版者完成插图后 | 前轮已核查 BookCoversLab、Prepressly、KDPPreflight | 淘汰基础功能复制，免费与付费供给都存在 |
| 出版 PDF 上传错误诊断与修复 | 作者/排版接单者提交 IngramSpark 文件时遇到格式错误 | 多个公开求助；BookReady 收费修复并有使用评价 | **保留做对比测试**，重点检查可自动修复范围和交付质量 |
| 把 KDP 文件转换为其他印刷平台版本 | 同一书需要跨平台发行 | 公开跨平台求助；BookReady 已提供多平台检查 | 合并到 PDF 候选，不把平台数量当差异；暂不做万能格式转换 |
| Bubble 交接文档自动生成 | 开发者维护/移交复杂项目 | 旧求助存在；Buildprint 已有文档及广泛工程工具 | 暂缓，无明确缺口 |
| Bubble 静态文本提取、翻译、写回 | 应用扩展多语言时 | Textonomy 和免费 CSV 翻译工具已有覆盖 | 淘汰简单翻译/替换复制 |
| Bubble 未使用字段、工作流清理 | 大项目维护与整理 | 原生优化、公开脚本、Buildprint 检查均存在 | 暂缓；引用关系检查存在难点，不能把“没找到引用”当“可删除” |
| Bubble 历史孤立上传文件排查 | 文件占用累积且无法人工检查 | 多个用户求助；官方文件存储机制与预防方案可查 | 观察，不先开发删除工具；需确认是否能枚举全部相关引用与文件 |

## 第一候选：出版 PDF 修复

### 独立问题线索

1. [封面上传错误](https://www.reddit.com/r/selfpublish/comments/1vb8zcn/im_trying_to_load_my_cover_to_ingramspark/)：原作者表示已向 GetCovers 额外付费取得 IngramSpark 封面，仍遇到 ICC 配置相关提示；尝试转换器后仍未解决，等待供应商响应。本轮已打开正文和回复。这支持“已投入资金且希望尽快完成”，但不证明其还愿意再购买我们的工具。
2. [内页和封面同时报错](https://www.reddit.com/r/selfpublish/comments/1sq2oop/help_uploading_files_to_ingram_spark/)：作者使用 Google Docs 与 Canva，难以理解错误；后续回复说与封面设计师一起解决。这个反证说明有些问题可以通过解释和原服务商修复，不一定需要新软件。
3. 两帖的搜索发布日期与正文相对时间不完全一致，不推算精确发生日或近期需求增长；保留链接作为任务证据。

### 直接竞品

[BookReady](https://www.bookready.net/)已提供免费检查、错误说明和付费修复，覆盖封面与内页；不能把“解释报错”“自动修复”“多个平台”当作未被满足的功能。

[定价页](https://www.bookready.net/pricing)：单文件 $9；作者 Pro 为 $12/月或 $69/年；Formatter/Agency $79/月，含白标报告。以上仅为公开标价；套餐是否卖出、收入与利润均未知，不采纳其客户能转售赚钱的推算。

[Trustpilot 原评论](https://www.trustpilot.com/review/bookready.net)本轮显示 9 条，混有 ARC 书评服务等其他业务，不能全部算 PDF 客户。Stephen 和 Joni 的评论描述文件修复价值；另有评价提及人工响应和帮助。因此已有用户价值线索，但自动交付比例未知。全为正向的小样本，未找到能支撑差异化的集中差评。

### 可以验证的第一版边界

候选流程：上传 PDF、选择目标平台与封面/内页、粘贴报错 → 给出定位明确的诊断 → 仅对已实现且能验证的错误生成修复副本 → 前后对照与检测结果 → 下载。

最先比较“特定色彩/文件规范错误”的处理；不承诺重做构图、任意字体补全、修正所有印刷问题或保证平台接受。这里的限制来自尚未验证的技术能力，不是市场宣传建议。技术规则应以当前平台文档为准，不直接采用论坛回复或竞品文案。

下一项可执行验证应是同一批有已知错误的合法样本，与 BookReady 的免费检查和可信检测工具对照：有没有误报、漏报；能否修复后保留文字与图形；是否引入新的问题。先验证几类明确错误，再决定开发。合成样本只证明规则覆盖，不等于实际客户成功率。

当前没有上传文件、试用付费修复或生成原型；不要把本轮网页研究称作效果实测。

### 获客入口与局限

候选入口是用户的具体报错，例如 `PDF contains ICC color profiles`，再结合 IngramSpark、Canva 等上下文。公开问题证明这种表述存在；本轮未测搜索量、排名难度或广告成本，不声称获客容易。

读取的 r/selfpublish 帖内版规明确限制自我推广和 AI 生成发言；它可作为研究来源，不能直接当成可批量推广渠道。本轮未发帖或私信。若现有结果足以满足、没有流量入口或效果优势，则停止候选。

## Bubble 方向为何下调

- [Textonomy](https://www.textonomy.com/)已把识别文本、创建 App Text ID、替换和同步串起来，扩展免费，平台 Beta 免费、后续标价 $25/月，不能视为已有 $25 订阅收入。
- [免费 CSV 翻译工具](https://forum.bubble.io/t/free-bubble-app-text-translation-tool/331216)早已有公开发布；“AI 翻译 CSV”不足以收费差异化。
- [Buildprint 文档](https://docs.buildprint.ai/)及[计费说明](https://docs.buildprint.ai/billing-and-usage-b5l3i)显示已有工程工具与付费计划；未取得当前具体价目。其未使用字段检查还有[公开发布说明](https://forum.bubble.io/t/announcing-buildprint-ai-build-on-bubble-with-claude-code-and-codex/391193?page=40)。
- [2025 年原生优化问题帖](https://forum.bubble.io/t/optimize-application-issues-is-this-working/370704)确有大应用检查与人工清理反馈，但“原生功能有问题”不能自动推导第三方检查器有机会。
- [历史孤立文件求助](https://forum.bubble.io/t/possible-to-find-and-delete-orphaned-files/307845)中用户提到成千文件无法人工判断；[上传器改进建议](https://forum.bubble.io/t/picture-uploader-delete-unused-files-from-storage/383171)提到反复配置清理工作流。这是重复问题线索，尚无已核实的软件付费证据。
- [Bubble 官方文件说明](https://manual.bubble.io/help-guides/data/files)区分存储文件与数据库中的 URL。开发排查器需要处理多处引用和外部用途；删除更需完整判断。没有找到竞品不表示一定可实现。

不建议因为 Nocodable 有收入就切进一个我们尚不熟悉的生态，先制作几百个组件。公开渠道清晰只解决了“去哪里观察”，不替代产品优势。

## 本轮范围

更新已有产品档案和上轮候选；筛七项任务，打开用户问题、产品、价格和评论。未购买服务、注册新账户、修改生产项目或联系客户。本报告是商业筛选，不是平台技术规范、金融预测或已通过的产品验证。
