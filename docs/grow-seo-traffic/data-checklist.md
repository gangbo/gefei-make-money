# SEO 选品数据清单

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
