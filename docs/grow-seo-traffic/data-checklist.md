# SEO 选品数据清单

## 当前任务：sayblablabla.com 趋势核对（2026-09-12）

只核对竞品Semrush已有流量趋势及构成，不做完整SEO机会或优化。用户已授权Chrome读取。

| 数据 | 用途/范围 | 状态 | 来源 |
| --- | --- | --- | --- |
| 域名概览及至少3–9月同口径趋势 | 全球/根域/桌面，一年逐日估算 | ready | 原始CSV及source-notes |
| 主要词及页面 | CA/NO桌面9月11；覆盖约55%当前全球估算流量 | partial-ready | 两国Positions/Pages人工摘录；其他国家与历史页面未查 |
| 域名注册日期 | 区分注册与上线 | partial-ready | 用户称3月，尚未独立核验；官方上线3月已在S-051 |
| 实际安装/收入/第一方访问 | 不在本轮可核实范围 | missing | 竞品非自有，不能用自然估算代替 |

当前足够做全球趋势和CA/NO当前构成的有限分析；不支持完整增长归因、市场/SEO机会或实际盈利结论。保存位置raw/2026-09-12/actor-traffic/。

## 当前任务：NeatTyping 来源与 Google 趋势（2026-09-11）

- 目标：https://neattyping.com/；已上线打字工具。用户要求查询当前流量主要来自哪里，并查看 Google 流量趋势；本次只做来源和总体趋势分析。
- 授权：用户明确要求代为读取，沿用已登录浏览器的只读获取授权，允许在本资料库保存相关数据。
- 默认范围：全球、全部设备、无查询或页面筛选；Google 搜索类型为 Web。计划最近 3 个月，至少 28 天；优先比较完整的最近 28 天与前 28 天。
- 当前状态：**数据达到本次来源排序与 Google 总体趋势分析的要求。** GSC 为 ready，GA4 为 partial-ready：只在最后几天观察到有记录，来源行之和与总计不一致，不计算互斥渠道份额、不外推整月。未获得技术与竞品数据，不做优化方案或修改。

| 数据项 | 用途与范围 | 获取方式 | 状态 | 保存位置与限制 |
| --- | --- | --- | --- | --- |
| 站点身份与已有基线 | NeatTyping，Statcounter 项目 13221620 | 前轮 S-026 已读取 | ready | [前轮快照](../01-sources/analytics/2026-09-11/statcounter-traffic-snapshot.md)；只有会话总量，没有来源 |
| 全站流量渠道及具体来源 | GA4 2026-08-14—09-10，33 个来源/媒介 | 已登录 GA4 原始 CSV | partial-ready | [来源导出](raw/2026-09-11/neattyping/ga4/traffic-acquisition-source-medium.csv)；曲线只有最近几天有数据，行之和与总计不一致；只用于近期来源排序。Statcounter 明细仅 Entire Log (2 hours) |
| 国家分布 | GA4 2026-08-14—09-10 活跃用户，全部设备 | 已登录 GA4 原始 CSV | partial-ready | [国家导出](raw/2026-09-11/neattyping/ga4/demographics-country.csv)；与来源同样有采集覆盖限制，指标是活跃用户 |
| Google 搜索总体趋势 | 2026-06-09—09-08，92 天；最近 28 天与前 28 天及最近 7 天比较 | 已登录 GSC 原始 CSV | ready | [3 个月数据](raw/2026-09-11/neattyping/gsc-3months/图表.csv)；Web、全球、全部设备，无其他过滤；数据截止 09-08 |
| 查询与页面 | 最近 28 天 2026-08-12—09-08 及近 3 个月，查询、页面、国家、设备 | 已登录 GSC 原始 CSV | ready | [28 天查询](raw/2026-09-11/neattyping/gsc-28days/查询数.csv)、[页面](raw/2026-09-11/neattyping/gsc-28days/网页.csv)；查询可见行与属性总量分开核对 |
| 当前线上产品 | 公开首页与已存在项目资料，确认主题 | 项目记录 / 公开页面 | partial-ready | 本次不做代码、SERP 竞品或技术 SEO 审计；不据总体趋势推断原因或实施修改 |

## 历史任务：AI 图片选品（2026-08-26）

- 分析目标：从 AI 图片相关需求中找出一个竞争相对较小、能够通过产品收费并有自然搜索获客空间的产品方向。
- 目标站点：新产品，尚无目标站点和第一方搜索数据。
- 初始市场与语言：美国 / 英语；这是为了开始采集所做的临时假设，最终结论前需要确认或做跨市场复核。
- 初始设备：桌面端；产品涉及图片工作流，最终结论前会检查移动端 SERP 是否明显不同。
- 数据日期：2026-08-26。
- 用户授权：已明确允许使用已登录的 Semrush 代理；Google Trends 可只读查看。
- 当前结论：**核心数据已满足美国英语市场的上线前选品判断。** 推荐报告见 `reports/2026-08-26-ai-image-product-opportunity.md`；盈利仍需用真实样片、落地页上传和付费意愿验证。

| 数据项 | 为什么需要 | 建议范围/口径 | 获取方式/授权 | 当前状态 | 来源与保存位置 | 备注 |
|---|---|---|---|---|---|---|
| 产品目标与约束 | 决定筛选标准 | AI 图片相关、竞争较小、以盈利为目标 | 用户对话 | `ready` | 本清单 | 本轮明确限定为美国英语桌面的上线前机会研究；开发周期和预算留到产品验证阶段 |
| 第一方搜索表现 | 已有站点的真实基线 | 最近 3 个月 | 不适用 | `unavailable` | — | 这是新产品选品，不要求虚构 GSC/Bing 数据 |
| 当前站点与页面 | 判断能否优化已有能力 | 路由、产品能力、页面 | 本地项目检查 | `unavailable` | — | 尚未选定产品，不存在目标站点；结论应标注为上线前研究 |
| AI 图片 seed 主题地图 | 避免只查一个泛词 | 通用生成、编辑、修复、格式/平台、垂直场景、商业工作流 | Semrush + 产品任务拆解 | `ready` | `raw/2026-08-26/semrush/keyword-magic/ai-image-seed-scan.md` | 扫描 11 个方向并收窄到 3 个候选 |
| Keyword Overview | 判断绝对需求与初步难度 | 美国数据库、英语、桌面；volume、KD、intent、CPC、SERP features、trend | 已登录 Semrush 代理，只读 | `ready` | `raw/2026-08-26/semrush/keyword-overview/candidate-overviews.md` | 三个主要候选均有 overview |
| Keyword Magic 长尾词 | 发现低竞争任务词 | broad / phrase / related / questions；volume、KD、intent、CPC | 已登录 Semrush 代理，只读 | `ready` | `raw/2026-08-26/semrush/keyword-magic/ai-image-seed-scan.md` | 房产编辑簇覆盖工具、软件、AI、服务和 HDR 长尾 |
| Google Trends | 区分增长、稳定和衰退 | 美国；过去 12 个月、过去 5 年；related/rising queries | Google Trends，只读 | `ready` | `raw/2026-08-26/google-trends/candidate-comparison.md` | 精确长尾采样稀疏，因此用较宽主题比较并标注限制 |
| 实时 SERP | 验证搜索意图和真实竞争 | Google 美国英语桌面；候选词前 5–10 个自然结果、SERP features | 公开搜索 / Computer Use | `ready` | `raw/2026-08-26/serp/google-us-desktop-real-estate-photo.md` | 已区分广告、AI Overview、论坛、视频和自然工具页 |
| SERP 竞品反查 | 找小站已经验证的关键词和页面 | 重点候选的前排小站；Organic Positions、Top Pages / URL keywords | Semrush 代理，只读 | `ready` | `raw/2026-08-26/semrush/competitors/real-estate-photo-competitors.md` | Autoenhance 完成 positions + top pages；Fotello 完成 domain overview |
| 商业与付费证据 | 避免只选有流量但不能赚钱的词 | 竞品定价、免费额度、付费墙、广告/CPC、用户评论与替代方案 | 竞品页面 + Semrush + SERP | `ready` | `raw/2026-08-26/competitor-products/pricing-and-positioning.md` | Autoenhance、AutoHDR、Fotello 和人工服务均有明确价格 |
| 产品交付可行性 | 估算毛利和 MVP 时间 | 输入输出、模型/API 成本、版权/隐私、人工审核、复用频率 | 竞品和技术研究 | `partial-ready` | `raw/2026-08-26/product-feasibility/real-estate-photo-workflow.md` | 竞品证明可交付；自有流水线的真实成本和返工率必须通过样片验证 |
| 候选机会池 | 最终比较和排序 | cluster、primary/secondary keywords、volume、KD、intent、trend、SERP、商业证据、产品适配度 | 汇总上述来源 | `ready` | `reports/2026-08-26-ai-image-product-opportunity.md` | 已给出优先、备选和不建议方向 |

## 剩余验证项

1. **真实样片质量**：当前数据证明需求和付费，不证明我们的处理质量；需要房产摄影师的 bracket/RAW 批次做盲测。
2. **单位经济性**：市场价约 `$0.29–0.53/张`，需要实测推理、存储、重试和人工返工成本。
3. **付费意愿**：应以落地页上传率、预售和连续批次留存验证，而不是继续堆关键词数据。

本轮只读浏览器研究已完成，没有对 Semrush、Google Trends、Google Ads 或竞品账户执行任何写操作。

## D-023/D-024竞品前置筛选（2026-09-11）

授权Chrome代取。目标根域：unload.bot、catalogintake.com、sovran.ai、clipset.app；先全球概览、美国桌面排名/关键词，记录实际数据库与日期。

| 必需数据 | 状态 | 用途 |
| --- | --- | --- |
| 四域当前估算自然流量/词数与12月趋势 | missing | 当前规模与增长 |
| 主要商业词、非品牌词排名及Top Pages | missing | 检查流量是否属于目标业务 |
| 独立seed关键词Overview/Magic搜索量/KD/意图 | missing | 不用单站流量替代需求 |
| 两方向实时SERP和前排相关站点 | missing | 验证直接搜索竞品 |
| 产品上线时间/域名年龄区别 | partial-ready | Unload商店上线时间已有，其他待补 |
| 收入/真实购买 | partial-ready | 复用S-028，不能由流量推算 |

无自有新产品，第一方站内数据不适用；当前不足以下搜索天花板或增长机会结论。

### D-023/D-024本轮采集更新（S-037）

- ready：四域一年全球/根域自然流量及关键词历史CSV，已核对范围/列数；不是全站访问。
- partial-ready：美国桌面Sovran排名摘录；独立16条需求词，其中部分KD/意图/搜索量缺失；原始记录见[来源](raw/2026-09-11/opportunity-screen/source-notes.md)。
- missing：其余美国Positions、Top Pages及增长页面、独立SERP与相关前排竞品链、全球词量、三家产品上线日期。
- 当前仍不足以形成搜索空间或立项建议；继续数据采集，不因模型零估算淘汰，也不因低基数倍增晋级。

### S-038更新

partial-ready：Sovran/Clipset/Importier美国Top Pages可见数据、Importier/Raw2Ads全球当前概览、独立任务表达搜索结果与官方页核查；Importier应用上线日期ready。缺口：固定地域SERP及前排相关站排名证据链、全球词量、Clipset非美国流量归因、商业页历史。数据只足够描述当前观测，不开展选品SEO结论/方案。

### 2026-09-12接续清单

计划补全球关键词与相关搜索结果；先复用S-037/038，不重复四域历史。Chrome短暂被用户操作中断，用户已回复用完，恢复采集。另发现Matrixify官方MCP已覆盖供应商文件AI映射和导入，单列供给证据，不作为搜索量结论。新增比较Matrixify/Stock Sync，避免仅用新小站推断品类大小。

S-039更新：ready=3个独立种子全球量（1.1K/3.3K/110）；partial-ready=成熟供给与使用评价；missing=固定SERP排名、成熟竞品自然流量/商业页历史、Clipset全球45来源。不能输出完整SEO机会结论。

S-039末尾补采Matrixify全球概览3969/1443词（报表09-11）；Stock Sync及历史仍缺。

### D-024新增参照Wideframe（09-12）

官网/YC目录出现原素材整理→Premiere工程交付供给；仅准备查根域全球当前自然流量。需要历史、商业词/页面和独立使用证据才可判断增长。不能把YC、100美元标价或作者推荐语当收入。本轮不试用。

S-041：Wideframe全球根域当前概览partial-ready（276流量/404词、报表09-11）。历史、子域、商业页/关键词仍missing，不据此输出增长或SEO机会结论。

### S-042视频前置核查结束（09-12）

ready：Wideframe根域Worldwide一年CSV；partial-ready：美国09-10主要页面人工摘录，包含try子域；missing：独立trywideframe.com根域历史、页面历史、完整词表/SERP与收入归因。见[数据口径](raw/2026-09-12/video-workflow/history-and-pages.md)。没有完整SEO机会结论，D-024因商业适配不足转备选，未完成缺口归档、不继续主动补查。

### D-028教程工具：09-12数据清单（S-043）

已获授权Chrome代取，复用旧方法。本轮先核对小规模收费样本Guidejar。需根域全球一年自然历史、主要商业页/品牌词占比、独立需求词量与固定地域SERP；收入证据另存，不用访问推收入。Guidejar全球概览651/1498词，历史CSV已获取；主要页面采集中。独立关键词/SERP、页面增长历史、第一方获客归因仍missing；大型Guidde/Scribe历史未采，不作全面SEO机会结论。

S-043本轮结束：Guidejar一年Worldwide CSV ready，美国09-10主要页面partial-ready；[记录](raw/2026-09-12/tutorial-workflow/source-notes.md)。独立业务词/SERP、历史页面及归因仍missing。当前商业判断依据订阅与用户反馈，不输出SEO机会方案。

## 2026-09-13 新一轮商业候选：采购单、批发目录、GMC检查

仅研究竞品与获客条件，非自有站SEO优化；候选尚未开发，无第一方搜索数据可提供。市场暂定英语/美国，域名趋势采用全球桌面另记，不能混算。

| 数据项 | 范围/用途 | 状态 | 取得方式与保存 |
| --- | --- | --- | --- |
| 竞品身份与产品定位 | Stockie、Catalogly、GMC公开扫描工具；匿名收入产品域名未知 | partial-ready | 官网/Shopify页面，S-059已归档 |
| 域名趋势 | 各代表站近一年全球桌面自然估算 | ready（限定三站） | 已授权Chrome/Semrush代理；本批commerce-screen目录 |
| 业务词 | stocky alternative、shopify catalog maker、google merchant center audit，美国volume/KD/intent | partial-ready（量有值，KD/intent缺） | Keyword Overview/Keyword Magic |
| 主要页/词 | 前排页面→相关域名或URL反查 | missing | 当前不能判断SEO可进入性 |
| 实时SERP | 目标词的市场/设备与结果类型 | missing | 普通研究检索不足当固定市场排名 |
| 第一方获客/付费归因 | 竞品后台不可得 | missing | 不能以自然估算换算付费率或预测收益 |

可独立开展商业购买和自动化范围比较；SEO数据不够时不下关键词或流量机会结论。

S-060完成前置部分采集，原始4份CSV及口径已保存；固定SERP、主要页/词与完整词池仍缺，不形成SEO方案。
