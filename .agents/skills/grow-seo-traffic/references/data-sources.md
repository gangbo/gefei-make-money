# 数据来源与获取方式

## 保存规则

把获得的资料按原样保存到：

```text
docs/grow-seo-traffic/raw/YYYY-MM-DD/<source>/
```

保留用户提供或平台导出的原格式，不覆盖旧批次，不要求转换。同步更新
`docs/grow-seo-traffic/data-checklist.md`，记录：

- 来源；
- 获取日期；
- 数据覆盖周期；
- 市场、语言和设备；
- 过滤条件；
- 文件或截图位置；
- 是否足以支撑当前判断。

## 获取渠道选择

按以下顺序选择：

1. 目标项目中已经保存的数据；
2. 专用连接器或官方 API；
3. 用户直接上传、粘贴或提供链接；
4. 经用户允许，使用 `computer-use:computer-use` 操作已登录浏览器；
5. 公开网页搜索；
6. 需要 X 平台近期讨论时调用全局 `$xai-call-grok`。

对于 GSC、Bing、Semrush 等登录平台，不要只告诉用户“请导出”。同时询问是否允许 Agent 使用其已登录
浏览器代为获取。用户明确要求代取时直接执行；否则先获得许可。

Computer Use 只用于读取、筛选、下载和截图。确认资源、日期、国家数据库、设备和过滤条件后再保存。
不要修改平台设置或提交外部变更。未登录时请用户自行完成登录；不要索取密码；验证码由用户完成。

## Google Search Console

优先获取：

- Performance → Search results；
- 日期、查询、页面；
- 国家、设备和搜索结果呈现；
- Page indexing 与未索引原因；
- URL Inspection 示例；
- sitemap 状态、上次读取时间和发现 URL 数。

建议最近 3 个月，最低 28 天。最近几天可能不完整。查询表和页面表不能假设逐行对应。

用户可以提供导出、截图、复制文本、链接或已登录浏览器会话。用户允许时，通过 Computer Use 打开其
GSC，选择正确资源和时间范围，依次读取或导出日期、查询、页面及索引数据，并保存页面筛选条件截图。

## Bing Webmaster Tools

优先获取：

- Search Performance 的日期、查询和页面；
- 国家与设备；
- Index Explorer；
- Site Scan；
- URL Inspection；
- sitemap。

Bing 与 Google 分开分析。Bing 中的排名和索引不能证明 Google 状态正常。

用户允许时，通过 Computer Use 使用其已登录的 Bing Webmaster Tools，确认 site URL 后获取上述报告。

## Semrush 代理、Ahrefs 与其他研究工具

Semrush 默认通过以下代理入口获取：

`https://zh.semrush.fast.wmxpro.com/`

它是 Semrush 的访问代理，不是独立的数据来源。仍把结果标记为 Semrush 第三方估算，并在数据清单中记录：

- 实际访问的代理 URL；
- 国家数据库、语言和设备；
- 数据日期与查询日期；
- 使用的报告和过滤条件；
- 截图或导出的保存位置。

根据任务获取：

- Keyword Overview 或关键词研究；
- Organic Positions、Pages、Competitors；
- Keyword Gap；
- SERP features、趋势、难度与目标市场搜索量；
- 必要时的外链数据。

使用 Semrush 做关键词机会时，必须区分两类任务：

- **站点现状**：查 Domain Overview、Organic Positions、Top Pages、Competitors、Backlinks，用来了解目标站点已经排名的关键词、页面和外链基础。
- **关键词/长尾机会**：查 Keyword Overview 和 Keyword Magic，用 seed 词、Trends rising terms、GSC/Bing 查询、竞品词和用户语言变体扩展关键词池，记录 volume、KD、intent、CPC、SERP features、questions、broad/phrase/exact/related match。

只拿 Organic Positions 或 Top Pages 不能算完成长尾关键词研究，因为它们主要显示目标站点已经有可见排名的词，不代表目标主题的完整搜索需求。

Semrush 关键词研究的详细流程见 [Semrush 工作流](semrush-workflow.md)。

第三方数字是估算，不是真实站点流量。记录国家数据库、设备和数据日期。

用户允许时，通过 Computer Use 打开上述代理并使用其现有登录状态。先确认目标国家数据库和设备，再获取
关键词、竞品或 gap 数据；不要购买套餐、修改项目或创建持续追踪配置。

如果目标项目或用户明确提供其他 Semrush 入口，以其指定为准。如果代理不可访问、要求重新输入凭据、
出现验证码或展示的数据口径不清，停止并让用户接管或提供导出；不要索取密码，也不要静默换成另一数据源。

## Google Trends

根据目标国家、语言和适当分类检查：

- 最近 12 个月；
- 最近 5 年；
- 热门与飙升相关查询。

Trends 的 0–100 是相对热度，不是绝对搜索量。

Google Trends 通常可以直接通过公开网页或 Computer Use 获取。记录查询词、国家、分类、时间范围和比较
组；不同批次的归一化指数不要直接拼接。

## X 平台

需要理解近期用户用语、问题、使用场景、热点或竞品讨论时，调用全局 `$xai-call-grok` 并启用
`x_search`。不要用普通网页摘要冒充 X 平台搜索结果。

### 关键词构造

从以下来源建立关键词簇：

- GSC/Bing 已有查询；
- Semrush/Trends 的候选词；
- 产品功能、任务和使用场景；
- 用户问题句式与痛点表达；
- 竞品、替代方案和比较词；
- 目标市场的语言与常用变体。

每个关键词簇独立搜索，并设置明确起止日期。默认先搜索最近 30 天；样本太少时扩大到 90 天并记录调整，
需要观察季节性或长期变化时再使用更长窗口。

要求结果保留：

- 实际查询词和日期范围；
- 帖子作者与发布日期；
- 原始 X 链接；
- 主要观点；
- 重复出现的用户问题或用语；
- Grok 归纳与 Agent 推断的明确区分。

把查询提示和结果保存到 `docs/grow-seo-traffic/raw/YYYY-MM-DD/x/`。若 `XAI_API_KEY` 不存在，请用户在
本机设置，不在对话、仓库或日志中接收或保存完整密钥。

X 信号只用于理解语言、痛点和近期选题。它不能替代第一方搜索表现、Semrush/Trends 需求证据或官方事实；
样本不足时在数据清单中标记 `unclear`。

## 实时 SERP 与竞品

Agent 通常直接搜索目标查询并保存必要的截图或笔记，记录：

- 查询；
- 市场、语言和设备；
- 检查日期；
- 结果类型；
- 排名页面；
- 真实竞品；
- 页面提供的实际产品价值。

用户要求“竞品”“SERP 前排”“截图”“查看他们的关键词”或等价任务时，实时 SERP 是必需数据。对每个目标查询：

1. 保存 SERP 截图、可读文本或 AX 树、查询 URL 和 meta 信息；
2. 区分广告、AI Overview、视频/短视频、论坛、本地包、购物结果和自然结果；不要把 Sponsored 当自然排名；
3. 抽取自然结果前 5–10 个页面 URL，优先保留工具页、产品页、专题页和小站页面；
4. 对明显不适合目标项目形态的结果做标记，例如 YouTube、Reddit、本地服务、商城或纯导航结果；
5. 把抽取表保存到 `docs/grow-seo-traffic/raw/YYYY-MM-DD/serp/`，字段至少包含 query、result type、position、domain、URL、title/snippet、备注；
6. 将这些域名或 URL 作为 Semrush 竞品反查输入，查看 Organic Positions、Top Pages / Pages 或 Keyword Gap。

优先检查页面本身，不只依赖摘要，也不要复制竞品措辞。SERP 中出现小站专门页时，优先反查它们的关键词；小站能排名通常比大品牌页面更能暴露可复制机会。

## 站内分析

GA4、StatCounter 或其他站内分析用于理解进入页面后的行为。搜索平台衡量搜索获客，站内分析衡量访问行为；口径不同，不强行对齐。

在流量很低时，不要因为少量转化或跳出数据过早判断漏斗。

## 当前项目

Agent 直接读取目标项目自己的：

- `AGENTS.md` 和项目说明；
- 路由、页面、metadata 与文案；
- robots、sitemap 和部署配置；
- SEO 相关测试；
- 工作日志和已有实验；
- 线上站点。

只读取目标项目自己的资料，不把复制 Skill 的来源项目当成业务上下文。

## 向用户询问

使用清晰、可执行的表达：

> 为了判断 **[具体问题]**，我还需要 **[平台/数据项]**，建议覆盖 **[时间范围]**，并能看到 **[维度、指标或过滤条件]**。你可以直接上传文件、发截图、粘贴内容或给链接；格式不限。也可以允许我使用你已登录的浏览器，只读查看并把数据保存到项目中。你希望采用哪种方式？缺少它会导致我无法判断 **[受影响决策]**。

一次优先询问 1–3 个阻塞项，但始终保留完整数据清单。
