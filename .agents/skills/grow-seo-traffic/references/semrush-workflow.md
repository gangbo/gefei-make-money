# Semrush 工作流

## 使用目的

Semrush 是第三方估算数据，用来补充第一方 GSC/Bing 不能直接回答的问题：

- 一个主题或关键词簇的大致搜索量、KD、意图和 SERP features；
- 目标站点已经有可见排名的关键词和页面；
- 竞品页面、竞品关键词和关键词差异；
- 长尾词、问题词、匹配变体和近期趋势词的机会排序；
- 外链与域名权威基础。

Semrush 不能替代第一方搜索表现。不要把 Semrush traffic 当成真实流量。

## 入口与保存

默认代理入口：

```text
https://zh.semrush.fast.wmxpro.com/
```

保存到：

```text
docs/grow-seo-traffic/raw/YYYY-MM-DD/semrush/
```

记录：

- 实际 URL 或页面路径；
- 查询词或目标域名；
- 国家数据库、设备、语言、日期；
- 报告类型和过滤条件；
- 是否为导出、截图、AX 文本或手动记录；
- 是否受额度、登录、验证码、页面报错或字段缺失影响。

## 先判断任务类型

### 站点现状

目标是了解目标站已经有什么可见排名和页面基础。优先查：

- **Domain Overview**：Authority Score、Organic Traffic、Organic Keywords、Backlinks、Referring Domains、主要国家/设备口径。
- **Organic Positions**：目标站已排名关键词、排名、URL、volume、KD、intent、SERP features、更新时间。
- **Top Pages / Pages**：有关键词 footprint 的页面、关键词数、估算流量、主要关键词、引荐域名。
- **Organic Competitors**：搜索竞品，不等同于业务竞品。
- **Backlinks / Referring Domains**：只用于理解权威基础和外链缺口。

这些数据适合判断“已有页面怎么优化”，但不足以完成长尾关键词研究。

### 关键词与长尾机会

目标是建立可执行的关键词池。必须查：

- **Keyword Overview**：seed 词的目标市场 volume、global volume、KD、intent、CPC、competition、SERP features、趋势、关键词建议和问题词摘要。
- **Keyword Magic**：同一 seed 的 broad match、phrase match、exact match、related、questions；记录每个候选词的 volume、KD、intent、CPC、competition、results、updated。
- **Keyword Gap**：当有明确竞品时，比较目标站与竞品的 missing / weak / untapped 关键词。

seed 来源：

- GSC/Bing 已有查询；
- Google Trends rising terms；
- 当前产品/页面能力；
- 竞品品牌、替代方案和比较词；
- 用户语言、问题句式、使用场景；
- 目标语言和地区变体。

## 推荐采集顺序

1. 从第一方查询和产品页面列 seed clusters。
2. 用 Trends 找 rising terms，把它们加入 seed。
3. 对每个 seed 跑 Keyword Overview，保存概要。
4. 对每个 seed 跑 Keyword Magic：
   - broad match：找大词和相邻词；
   - phrase/exact：找页面标题和 H1 候选；
   - questions：找 FAQ、how-to、小节标题；
   - related：找非字面但同意图词。
5. 对明显脏的词做人工过滤：
   - 同形异义词，例如 splitter 可能是硬件、pitch 可能是体育；
   - 地名、本地服务、非目标行业；
   - 竞品导航词；
   - 用户意图与产品能力不匹配的词。
6. 把候选词映射到现有页面或新页面机会。
7. 按机会评分方法排序，不直接用 volume 最大排序。

## 扩展关键词机会的方法论

不要只查询目标域名已经排名的词。Semrush 的价值在于把“已有数据、竞品数据、SERP 数据和 seed 扩展”交叉起来，建立更完整的机会池。

### 竞品反推法

1. 先从目标 seed 的真实 SERP、Semrush Organic Competitors 和业务常识中选 3–8 个搜索竞品。
2. 对每个竞品查 **Organic Positions**，优先导出或记录：
   - 排名 1–20：竞品已经验证的核心意图；
   - 排名 21–50：竞品内容薄弱但需求存在的词；
   - volume 不低、KD 较低、intent 清晰、与目标产品能力匹配的词。
3. 对竞品的 **Top Pages / Pages** 逐页反查 URL keywords，找出一个页面实际覆盖的关键词簇。
4. 不把竞品品牌导航词直接当机会；只有 `alternative`、`vs`、`review`、`comparison` 等非导航比较意图才进入候选，并且必须确认适合法律与品牌风险边界。

### SERP 页面反查法

1. 对每个核心 seed 打开 Semrush SERP 或实时搜索结果。
2. 记录排名靠前的页面 URL，尤其是小站、工具页、列表页、问答页和专题页。
3. 用 Semrush 查询这些 URL 或所属域名的 Organic Positions / Pages，反推出这些页面获得可见性的长尾词。
4. 如果同一个页面覆盖多个近义词，把它们合并为一个 intent cluster，不为每个长尾词单独创建页面。

### SERP 竞品关键词闭环

当用户要求调查竞品、SERP 截图或“查看前排竞品的关键词”时，执行完整闭环：

1. **抓 SERP**：用目标市场、语言、设备和无个性化参数打开每个查询的实时结果页，保存截图、AX 文本或页面文本、查询 URL 与 meta。
2. **校正结果类型**：手动区分 Sponsored、AI Overview、自然结果、视频、论坛、本地包、购物和其他 SERP features；把广告和自然排名边界写入抽取表。
3. **选竞品页面**：优先选择自然结果前 5–10 个中与目标项目页面形态相近的页面；小站、专门工具页、专题页和问题页优先于大站首页、视频和论坛。
4. **查 Semrush**：对选中的域名和关键 URL 依次查 Organic Positions、Top Pages / Pages；若工具支持 URL/subfolder/root domain 维度，页面级查询优先于纯域名查询。
5. **抽关键词**：保存 keyword、rank、volume、KD、intent、SERP features、traffic、URL、数据日期和国家数据库。另生成一个过滤后的相关关键词表。
6. **合并聚类**：把同一页面覆盖的近义词归为 intent cluster，标记 primary keyword、secondary keywords、目标页面、产品适配度和证据来源。
7. **回查 SERP**：对低 KD、高相关或趋势上升的长尾词再看 SERP，确认没有同形异义、本地服务、纯导航、视频/论坛主导或产品能力不匹配。
8. **产出建议**：把“可优化现有页”“建议新建页”“只适合 FAQ/段落”“不建议做”的词分开，不把竞品所有排名词都当机会。

保存建议：

- SERP 原始资料：`docs/grow-seo-traffic/raw/YYYY-MM-DD/serp/`
- Semrush 竞品资料：`docs/grow-seo-traffic/raw/YYYY-MM-DD/semrush/competitors/`
- 竞品页面抽取表：`google-<market>-<device>-competitor-pages*.csv`
- 竞品关键词抽取表：`semrush-competitor-organic-positions-extracted.csv`
- 相关关键词过滤表：`semrush-competitor-<topic>-keywords-filtered.csv`

若 Semrush 页面报错、额度耗尽、URL 输入错位、表格保留旧查询或只返回空白状态，保存错误截图/AX 文本和 meta，不覆盖成功批次；重试时使用更稳定的地址栏 set value、UI 搜索或较小批次，并在清单中标为 `partial-ready` 或 `unclear`。

### Keyword Gap 法

当有明确竞品时，使用 **Keyword Gap**：

- `Missing`：竞品有排名、目标站没有排名，适合找新页面或新模块；
- `Weak`：目标站也有排名但明显弱于竞品，适合优化现有页面；
- `Untapped`：多个竞品共有而目标站没有，优先级通常高于单一竞品独有词；
- `Unique`：目标站独有词通常用于保护优势，不一定是扩张机会。

Keyword Gap 结果必须再经过 intent、SERP 和产品能力过滤。不要因为竞品有排名就默认值得做。

### Keyword Magic 分组法

在 Keyword Magic 中不要只看默认列表。按分组和匹配类型轮流扩展：

- **broad match**：发现相邻需求和上游/下游概念；
- **phrase match**：发现标题、H1 和落地页主词候选；
- **exact match**：确认核心词本身的需求强度；
- **related**：发现非字面但同意图的替代表达；
- **questions**：发现 FAQ、how-to、比较、故障排查和教程机会；
- 左侧分组：优先点击高频修饰词组，记录哪些组是相关、边缘或脏词。

常见修饰词模式：

- 价格/门槛：free、online、no signup、open source、trial；
- 质量/能力：best、fast、accurate、professional、advanced；
- 动作：create、generate、convert、extract、remove、edit、download、compress；
- 场景：for beginners、for mobile、for business、for teachers、for developers；
- 格式/平台：文件类型、设备、系统、集成平台、语言地区；
- 比较：alternative、vs、compare、review；
- 问题：how to、why、fix、can I、what is。

这些模式只是扩展方向，不能凭空臆造关键词；每个候选都要回到 Semrush 查 volume、KD、intent 或保存为待验证 seed。

### 修饰词矩阵法

为每个产品或主题建立矩阵：

```text
核心对象 × 用户动作 × 使用场景 × 约束/修饰词 × 平台/格式/语言
```

例如把已有页面能力、用户问题、竞品页面标题、Trends rising terms 和站内搜索词拆成组件，再组合成 seed。组合词必须用 Keyword Overview / Keyword Magic 验证，不把矩阵本身当作搜索需求证据。

### Trends + KD 交叉法

Trends rising terms 只说明相对热度变化，不说明绝对搜索量和竞争难度。对每个 Trends 起势词：

1. 用 Keyword Overview 查目标市场 volume、KD、intent 和 SERP features；
2. 用 Keyword Magic 查 related/questions，找低 KD 长尾；
3. 如果 Semrush 无数据但 SERP 明显存在需求，标记为 early signal，不与有 volume/KD 的词混排；
4. 如果趋势词是新闻、短周期热点或非产品意图，降低优先级。

### 地区与语言变体法

同一个 seed 在不同国家数据库、语言和设备下可能机会完全不同：

- 目标市场必须单独查询，不把一个国家的 volume 直接套用到另一个国家；
- 非英语市场要同时考虑本地语言、英语查询和常见混合表达；
- 移动端、本地服务或地区词需要单独检查 SERP；
- 记录数据库和语言口径，避免把 global volume 当成本地需求。

### 低 KD 过滤法

低 KD 不是自动机会。低 KD 候选必须排除：

- 同形异义词和跨行业词；
- 地名、本地服务或招聘/课程/下载站等非目标意图；
- 纯导航词、竞品登录/官网词；
- 产品无法满足的需求；
- SERP 已被视频、图片、本地包、购物或新闻结果主导且目标页面形态不匹配的词。

过滤后保留“低 KD + 意图清晰 + 产品可满足 + SERP 有可进入页面形态”的词。

### 机会池整理法

最终不要交付一堆未归类关键词。把 Semrush 候选整理成：

- keyword cluster；
- primary keyword；
- secondary/supporting keywords；
- intent；
- target existing page or proposed new page；
- volume range；
- KD range；
- SERP features；
- evidence sources；
- confidence；
- next data needed。

同一 intent cluster 优先对应一个强页面，通过小节、FAQ、内部链接和结构化数据覆盖长尾，避免关键词蚕食。

## Computer Use 操作提示

使用已登录浏览器时：

- 不创建项目、不购买套餐、不修改设置、不提交外部变更；
- 每次查询前确认国家数据库和设备；
- 批量打开 Semrush 或 SERP 时，每次保存前检查地址栏、页面标题、搜索框值和表格首行是否与本次查询一致；
- 优先使用页面 UI 正常搜索；如果代理页面支持，也可以尝试稳定 URL：

```text
/analytics/keywordoverview/?q=<keyword>&db=<country>
/analytics/keywordmagic/?q=<keyword>&db=<country>
```

不同代理版本可能对路径、尾斜杠或参数敏感。若直达 URL 报错，改用 UI 搜索并保存报错截图/AX 文本。

SPA 页面可能在切换关键词时保留旧表格或输入焦点错位。保存前必须检查：

- 页面标题中的关键词是否与本次 seed 一致；
- 表格首行关键词是否语义相关；
- 是否显示 loading、报错、无数据或额度耗尽；
- 是否混入明显无关行业词。

如果额度用完或页面不稳定，停止继续消耗，把状态标记为 `partial-ready` 或 `unclear`，并列出下一轮优先查询词。

## 数据充分性

可标记为 `ready`：

- 已覆盖目标市场/设备；
- seed clusters 来自第一方查询、Trends、产品和竞品；
- 每个主要 cluster 至少有 Keyword Overview；
- 核心 cluster 有 Keyword Magic 的 broad/phrase/questions 或等价长尾数据；
- 候选词可读且能看到 volume、KD、intent 或至少 volume/KD；
- 已过滤明显脏词并记录过滤逻辑。

标记为 `partial-ready`：

- 只有部分 cluster 有 Keyword Magic；
- 只有 Keyword Overview 摘要，没有完整长尾表；
- 页面报错、额度耗尽或导出失败，但已有数据足以支撑有限范围；
- 只完成站点现状报告，还没完成长尾词池。

标记为 `missing` 或 `unclear`：

- 只有 Organic Positions / Top Pages，却要判断完整长尾机会；
- 看不到国家数据库、设备、日期或过滤条件；
- 截图/AX 文本看不清 volume、KD 或关键词；
- 查询词与页面标题/表格内容不一致。

## 输出要求

报告里要分开写：

- Semrush 已有排名发现；
- Semrush seed keyword volume/KD；
- Semrush long-tail/questions；
- Trends rising terms；
- SERP 观察；
- 第一方 GSC/Bing 验证。

对每个关键词机会至少记录：

- keyword；
- source；
- market/device；
- volume；
- KD；
- intent；
- supporting Trend/GSC/Bing/SERP signal；
- target existing page or proposed new page；
- product fit；
- confidence and data gaps。
