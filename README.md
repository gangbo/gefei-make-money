# 个人开发者选品与经营资料库

公开的研究资料库。先保存可复用资料，再提取需求，筛选能低成本完成的项目，并记下已上线产品、已否决方向和当前方向。

**当前决策以下面一节和 [CURRENT-DECISIONS.md](CURRENT-DECISIONS.md) 为准。** `docs/` 里 2026-10 及更早的进度、候选和报告保留当时结论，入口仍是 [研究进度](docs/STATUS.md)。

## 当前决策（2026-11-08）

### 已上线

- [chartseat.com](https://chartseat.com/zh)：Gary 报告已上线。历史上线文档和检查报告是当时快照。
- [onlinepollmaker.com](https://onlinepollmaker.com/)：Gary 报告已上线。

这两项不再当作新商机提出。

### 2026-11-08 明确否决

- ZIP / 邮编区域地图（ZIP / postal-code sales territory maps）
- 银行流水 PDF 转 CSV
- 缝纫纸样 PDF（拼接 / 拼版）

理由：AI Agent 可以直接完成，或方向不符合当前标准。深筛报告曾把这三项列为优先验证；该排序已被这次决定覆盖，报告正文仍按当时记录保留。

### 此前已否决，继续排除

UUID、cover letter、llms.txt、EXIF remover、name tags。

### 当前方向

单指休闲解压小游戏。

- **首选：**「颜色弹药 + 像素清场」。参考 Pixel Flow! 的像素确定性清场，做原创小网页。
- **备选：** 2D 箭头疏通，做成低压力短局。

依据：[美日韩单指休闲解压小游戏研究](research/notes/casual-stress-relief-games-us-jp-kr-2026-11-08.md)。

### 2026-11-05 批次的旧计数

该批方向表、过滤数、短名单和 Semrush 过关表都是**历史快照，未经复核**。11-08 深筛已指出第二批过滤计数自相矛盾，「57 个过筛」等旧数字不作当前事实。

## 目录结构

```text
CURRENT-DECISIONS.md      2026-11-08 已上线、已否决与研究约束
research/notes/           2026-11 SEO 工具筛选、商机深筛/重筛、小游戏研究
docs/                     2026-09 至 2026-10 选品资料库
├── STATUS.md             当时进度与下次工作入口
├── decisions.md          决策历史与淘汰原因
├── 00-methodology/       方法论与阶段规则
├── 01-sources/           来源索引、榜单、竞品与社区摘录
├── 02-candidates/        需求候选、台账与历史筛选报告
├── 03-feasibility/       输入、交付、成本、竞争和获客筛选
├── 04-validation/        实验索引、脚本、样本与复盘
├── projects/             已有产品、经营数据和口述记录
├── operations/           运营经验、推广与外链资料
└── grow-seo-traffic/     SEO 专项原始数据，保留固定路径
```

## 文档索引

按时间和主题读：SEO 工具需求（11-05，历史快照）→ 已否决方向（11-08 深筛与重筛）→ 小游戏方向（11-08，当前）。

### 1. SEO 工具需求（2026-11-05，历史快照，未经复核）

| 文档 | 内容 |
| --- | --- |
| [how-to-find-demand.md](research/notes/how-to-find-demand.md) | Gary 整理的找需求方法笔记，供后续筛选引用。文内指向的会员帖原文未入库。 |
| [trends-rising-raw.md](research/notes/trends-rising-raw.md) | Google Trends 相关飙升查询原始摘录。 |
| [opportunities-2026-11-05.md](research/notes/opportunities-2026-11-05.md) | 当天商机清单（入选 18 项）及当时淘汰词。 |
| [directions-batch1-100-2026-11-05.md](research/notes/directions-batch1-100-2026-11-05.md) | 第一批约 100 个在线工具方向。 |
| [directions-batch2-100-2026-11-05.md](research/notes/directions-batch2-100-2026-11-05.md) | 第二批约 100 个方向。 |
| [directions-batch2-filtered-2026-11-05.md](research/notes/directions-batch2-filtered-2026-11-05.md) | 第二批过滤结果。文内「保留 57」等计数是当时快照。 |
| [directions-batch2-shortlist-2026-11-05.md](research/notes/directions-batch2-shortlist-2026-11-05.md) | 过滤后的 20 项短名单，当时尚无 Semrush 量。 |
| [semrush-scan100-queue.md](research/notes/semrush-scan100-queue.md) | 全批 Semrush 扫描队列与预淘汰项。 |
| [semrush-scan100-partial.md](research/notes/semrush-scan100-partial.md) | 全批扫描的部分 Keyword Overview。 |
| [semrush-filtered-shortlist-2026-11-05.md](research/notes/semrush-filtered-shortlist-2026-11-05.md) | 进行中的过滤短名单（US ≥1K 且 KD&lt;55）；积分用尽，约 17 个词未查。 |
| [semrush-batch2-priority-2026-11-05.md](research/notes/semrush-batch2-priority-2026-11-05.md) | 第二批优先词深筛。 |
| [semrush-batch2-filtered-2026-11-05.md](research/notes/semrush-batch2-filtered-2026-11-05.md) | 低量过滤后、US 量 &gt;100 的保留表。 |
| [semrush-batch2-1k-plus-2026-11-05.md](research/notes/semrush-batch2-1k-plus-2026-11-05.md) | US 量 ≥1K 的短名单。当时倾向的 llms.txt、EXIF 等已在当前决策中排除。 |

### 2. 已否决方向（2026-11-08）

| 文档 | 内容 |
| --- | --- |
| [opportunities-deep-screen-2026-11-08.md](research/notes/opportunities-deep-screen-2026-11-08.md) | 21 个候选簇深筛。当时前三是邮编地图、银行流水 PDF、缝纫纸样 PDF；这三项现已否决，正文保留为历史研究。 |
| [opportunities-deep-screen-sources-2026-11-08.csv](research/notes/opportunities-deep-screen-sources-2026-11-08.csv) | 深筛来源表。 |
| [opportunities-rescreen-2026-11-08.md](research/notes/opportunities-rescreen-2026-11-08.md) | 按「AI Agent 能否直接完成」重筛。25 个意图簇里 0 个通过完整立项；并写明上述三项不要复活。 |
| [opportunities-rescreen-sources-2026-11-08.csv](research/notes/opportunities-rescreen-sources-2026-11-08.csv) | 重筛来源与取证状态。 |
| [CURRENT-DECISIONS.md](CURRENT-DECISIONS.md) | 已上线站点、否决名单和研究约束的决策记录。 |

### 3. 单指休闲解压小游戏（2026-11-08，当前方向）

| 文档 | 内容 |
| --- | --- |
| [casual-stress-relief-games-us-jp-kr-2026-11-08.md](research/notes/casual-stress-relief-games-us-jp-kr-2026-11-08.md) | 美、日、韩公开证据。首选颜色弹药 + 像素清场（参考 Pixel Flow!），其次 2D 箭头疏通。 |
| [casual-stress-relief-games-us-jp-kr-2026-11-08-games.csv](research/notes/casual-stress-relief-games-us-jp-kr-2026-11-08-games.csv) | 12 款游戏的地区证据与商店链接。 |
| [casual-stress-relief-games-us-jp-kr-2026-11-08-sources.csv](research/notes/casual-stress-relief-games-us-jp-kr-2026-11-08-sources.csv) | 来源、口径、日期和读取状态。 |
| [casual-games-source-checks-2026-11-08/checks.json](research/notes/casual-games-source-checks-2026-11-08/checks.json) | 美国 App Store 页面抓取状态（HTTP、最终 URL、标题）。 |
| [casual-games-source-checks-2026-11-08/market-page-checks.json](research/notes/casual-games-source-checks-2026-11-08/market-page-checks.json) | 榜单与报道页抓取状态（含 Appfigures 403）。 |

**原始页面快照未入库。** `casual-games-source-checks-2026-11-08/` 里的 `*.html` 是商店页、榜单页和报道页的原始 HTML，体积大，本仓库只保留上述两份检查 JSON。研究报告正文仍按写作时描述该目录含 HTML；那些快照不在本仓库。

## 从哪里开始（docs/ 资料库）

| 想知道什么 | 入口 |
| --- | --- |
| 2026-10 及更早做了什么 | [STATUS](docs/STATUS.md) |
| 某榜单是否查过、数据能否复用 | [来源索引](docs/01-sources/INDEX.md) |
| 当时的需求、暂缓或停止原因 | [候选台账](docs/02-candidates/INDEX.md)、[决策记录](docs/decisions.md) |
| 怎样判断能否低成本做 | [阶段规则](docs/00-methodology/workflow.md)、[可行性模板](docs/03-feasibility/README.md) |
| 实际做过哪些实验 | [实验索引](docs/04-validation/INDEX.md) |
| 已做过哪些产品和尝试 | [项目档案](docs/projects/portfolio.md) |

## 方法与历史资料

- [Web.Cafe 需求挖掘方法](docs/00-methodology/demand-discovery-methods-web-cafe.md)、[数据来源网站](docs/00-methodology/web-cafe-demand-discovery-websites-2026-09-04.md)。
- [工作用途需求方法](docs/00-methodology/professional-user-demand-discovery.md)、[X/Reddit 方法实践](docs/00-methodology/demand-discovery-practice-2026-09-10.md)。历史访谈建议按当前约束调整。
- [12 个收入/支付榜候选](docs/02-candidates/reviews/revenue-led-opportunities-2026-09-10.md)、[图片采购首轮研究](docs/02-candidates/reviews/image-work-demand-research-2026-09-10.md)。
- [出版与 Bubble 七项筛选](docs/03-feasibility/reviews/narrow-workflow-opportunities-2026-09-10.md)。PDF/Bubble 深度维护已停止，正文保留历史判断。
- [SEO 数据清单](docs/grow-seo-traffic/data-checklist.md)、[历史 AI 图片研究](docs/grow-seo-traffic/reports/2026-08-26-ai-image-product-opportunity.md)。房产方向历史建议不可直接当作当前立项。
- [首个 100/1,000 美元经验](docs/operations/banbri-first-100-to-1000-dollars.md)、[出海运营经验](docs/operations/sophie-miaomiao-operator-to-overseas-products.md)。
- [外链渠道整理](docs/operations/web-cafe-backlinks-sync-2026-09-04.md)、[601 条外链目录](docs/operations/web-cafe-backlinks-catalog-2026-09-04.md)。

## 使用原则

资料按来源和日期保存，候选按稳定 ID 跟进。每次研究结束更新来源、候选、决策和进度。原始导出、人工摘要、厂商宣传、个人观点与分析推断明确区分；缺失资料写明，不补成已采集。

同一历史周期不重复抓取；做当前决策时按需要刷新价格、功能或最新月份，并保留旧记录。本项目不自动外联、发帖或执行推广。

本仓库是公开资料库：不放入会员文章原文、凭据或密钥。商店页面原始 HTML 快照也不入库。
