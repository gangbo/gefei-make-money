# 第二批需求方向清单（约 100）· 2026-11-05

> 面向：个人独立开发者 · **仅在线工具站**（不做实体/电商 SKU）  
> 美国需求优先（America/New_York）  
> **本批不使用 Semrush / 外贸侠**（共享积分耗尽）；**不编造**搜索量 / KD  
> 量级代理：Google Trends 相对兴趣 + SERP/导航站供给密度 + X indie 发帖信号  
> 已排除立项/在建：`onlinepollmaker.com`、`chartseat.com`、InvoiceNeat、tiktomato  
> 已排除你否决：llms.txt generator、EXIF remover、name tag generator、UUID 单独押注  
> 相对第一批：**刻意换一批种子**，不重复 pitch 同表项

---

## 1. 本批怎么挖（方法诚实说明）

| 来源 | 实际做了什么 | 局限 |
|---|---|---|
| **X（Grok Bot `x` 命名空间）** | `search_posts_all` 多组：`I built` + tool/generator；`no signup`/`runs in your browser`/WASM；`just shipped` free tool。近 7 日「online tool / free generator」类帖约 **722** 条计数 | 噪声大；多为印巴/全球 indie 自推，不等于 US 搜索量 |
| **Google Trends US** | 复用今日早间笔记 `trends-rising-raw.md`（US · Past 30d · Rising）；WebSearch 抓到 DocuSign 相关 rising 含 **free signature generator +250%**；公共目录页（toosli / fwip / omnikitbolt）作供给旁证 | 直接 `trends.google.com` fetch **429**；`pytrends` 因 urllib3 `method_whitelist` 报错未能拉新 rising 表 |
| **公开导航站** | The Free Tools Directory（类别密度 + Recently Added）；AlternativeTo Online Services 新品；Toolify AI 图类（红海示警）；Product Hunt Productivity 榜（偏大产品，作负向过滤） | 目录=供给，不是需求量；AI 图生成类目录极密 → 本批不当主推 |

**筛选原则（同第一批方法论）**  
1) 关键词形工具 > 品牌叙事；2) 页面/文件/协作/本地隐私 **胜过纯聊天可替代**；3) 剔实体、重 SaaS 套件主打、纯 AI wrap、第一批已列且未换楔子的项；4) 地板意图：Semrush 回来后 **US ≥1K** 才值得深筛——本批只用代理信号标注「像/不像」。

---

## 2. 方向表（100 · 新批次）

标签：`新`=相对第一批表未主推；`老`=老意图换楔子；信号：`X` / `Trends` / `Dir`（导航站）

| # | 方向名/关键词 | 新/老 | 信号 | 一句话做什么 | 为何页/文件/本地胜过聊天 | 粗楔子 vs 现有 | 粗可做性 |
|---|---|---|---|---|---|---|---|
| 1 | image compress to exact KB (form upload) | 新 | X Dir | 压到表单要求的精确 KB（20/50/100） | 表单拒图要可下载文件；聊天给不出合规文件 | 打「SSC/银行/签证表单精确 KB」长尾 | 高 |
| 2 | WebP ↔ JPG/PNG batch (local) | 新 | X Dir | 批量 WebP 互转 | 隐私图不该上传；要 ZIP 下载 | 「无上传/批处理」对 Convertio 类 | 高 |
| 3 | AVIF → JPG/PNG (browser) | 新 | X Dir | 新格式兼容转换 | 同文件隐私 | 比 HEIC 红海略窄（HEIC 你已谨慎） | 中高 |
| 4 | WebM → MP4 (local remux/encode) | 新 | X | 浏览器录屏 WebM 转 MP4 | 文件流处理；聊天无法转码 | 屏幕录制刚需；ffmpeg.wasm | 中 |
| 5 | MOV → MP4 (iPhone video, local) | 新 | Dir | iPhone 视频兼容导出 | 大文件隐私 | 与 WebM 同引擎多落地页 | 中 |
| 6 | GIF → MP4 / MP4 → GIF (local) | 新 | Dir | 动图体积与平台互换 | 编码器任务 | 创作者上传限制驱动 | 中 |
| 7 | video compress under email size (local) | 新 | X | 压到可邮件附件大小 | 大文件；算力在用户端 | 强调「给客户发样片」场景 | 低–中 |
| 8 | browser screenshot mockup generator | 新 | X | 截图套浏览器/设备框 | 视觉排版导出 PNG | 无水印/无注册对付费 mockup 站 | 高 |
| 9 | 3D product / apparel mockup (browser) | 新 | X | 书/包装/服饰简单 3D 贴图 | 交互预览 + 导出 | 轻量版，不做完整 Printful | 中 |
| 10 | App Store / Play feature graphic maker | 新 | Dir | 按官方尺寸出商店图 | 模板填字出图 | 尺寸合规检查器+模板 | 高 |
| 11 | social safe-zone / crop guide (Reels/Stories) | 新 | Dir | 上传图看裁切安全区 | 视觉叠加层 | 可挂 YouTube thumb 相邻页 | 高 |
| 12 | Instagram grid planner (preview) | 新 | Dir | 九宫格预览再发 | 布局预览 | 轻量无账号 | 中 |
| 13 | LinkedIn carousel PDF/PNG maker | 新 | X | 多页轮播导出 | 分页设计 | 模板+字数提示 | 中 |
| 14 | X/Twitter thread splitter + composer | 新 | X | 长文切帖预览 | 字数/线程结构 | Threadly 类；隐私草稿本地 | 高 |
| 15 | Discord ANSI colored text generator | 新 | X | 生成 Discord 彩色代码块 | 特殊转义字符 | 极窄刚需、供给少 | 高 |
| 16 | barcode generator (EAN-13/UPC/Code128) | 新 | X Dir | 商品条码 PNG/SVG | 打印文件 | 无水印批量 | 高 |
| 17 | price tag / shelf label PDF (barcode+price) | 新 | Dir | 价签排版打印 | Avery/标签 PDF | 小店场景 | 高 |
| 18 | SKU / lot / serial number bulk generator | 新 | Dir | 规则化批量编码 | CSV 导出 | 库存/轻制造 | 高 |
| 19 | coupon / promo code bulk generator | 新 | Dir | 批量优惠码 | CSV；防重复 | 电商运营工具页 | 中 |
| 20 | DTF / print halftone underbase generator | 新 | X | 服装数码印前处理 | 双层 PNG 导出 | 印花店付费替代 | 中 |
| 21 | passport / visa photo maker (country sizes) | 新 | Dir Trends旁证 | 各国证件照尺寸+打印版 | 精确像素/DPI 文件 | 表单拒照刚需；隐私本地 | 高 |
| 22 | free signature draw → PNG/SVG | 新 | Trends(+250% 旁证) Dir | 手写签名透明底 | 嵌入文档的文件 | DocuSign rising 旁证「免费签名」意图 | 高 |
| 23 | signature embed into PDF (local) | 新 | Dir X | 签名盖到 PDF 页 | PDF 二进制处理 | 无账号轻签；合规免「法律效力」承诺 | 中 |
| 24 | PDF merge / reorder / split (local, not compress-first) | 新 | X Trends(pdf combiner rising) | 合并拆分重排 | 隐私办公文件 | Trends pdf combiner +50–70%；强调本地 | 中 |
| 25 | PDF → images ZIP (local) | 新 | Dir | 每页导出图 | 批处理 | 与合并成套 | 中 |
| 26 | images → PDF (local) | 新 | Dir | 扫描件合订 | 文件输出 | 表单/作业场景 | 高 |
| 27 | PDF page number / stamp / letterhead | 新 | Dir | 页码抬头水印自有文档 | PDF 编辑 | 「给合同盖自己抬头」 | 中 |
| 28 | OCR screenshot → text (on-device) | 新 | X | 截图识字 | 不愿上传截图 | WASM/本地模型；多语言 | 中 |
| 29 | redact PDF / black-out (local) | 新 | Dir | 涂黑敏感区再导出 | 隐私红线 | 律师/HR 场景 | 中 |
| 30 | RAR/7z/TAR → ZIP (browser extract) | 新 | Dir | 解压重打 ZIP | 归档二进制 | 「公司电脑不让装 WinRAR」 | 中 |
| 31 | file hash MD5/SHA256 (local) | 新 | Dir | 校验下载完整性 | 大文件本地算 | 开发/安全教学 | 高 |
| 32 | diff text / JSON / CSV side-by-side | 新 | Dir | 双栏差异 | 结构化对比 UI | 比聊天贴 diff 清晰 | 高 |
| 33 | cron → next runs + human English | 老楔 | — | （第一批有）本批**不重复推荐** | — | skip | — |
| 34 | iCal / .ics meeting invite generator | 新 | Dir | 一键下载日历邀请 | 日历文件标准 | 无账号发「加入日历」 | 高 |
| 35 | RRULE recurrence builder (explain) | 新 | Dir | 可视化重复规则 | 易错语法 | 开发者+产品经理 | 高 |
| 36 | working-hours overlap (multi city) | 新 | Dir | 多城工作时段重叠 | 可视化时间条 | 远程团队；广告少版 | 高 |
| 37 | on-call rotation generator | 新 | X旁 | 值班表轮转导出 | 表格+ICS | 小团队替代 PagerDuty 排班 | 中 |
| 38 | SLA uptime “nines” calculator | 新 | Dir | 可用性换算宕机分钟 | 公式+表 | SRE 入门页 | 高 |
| 39 | sales tax calculator by US ZIP | 新 | Dir 词市旁证 | 按邮编估销售税 | 查表+金额 | 小卖家结账数学；数据源是难点 | 中 |
| 40 | US paycheck / take-home estimator | 新 | Trends旁(tax calc) | 粗算税后到手 | 州税率表单 | 年更税表；免冒充报税软件 | 中 |
| 41 | overtime / no-tax-on-overtime explainer calc | 新 | Trends rising 旁证 | 政策词计算器 | 数字结果页 | 窗口随政策；要免责声明 | 中 |
| 42 | markup vs margin calculator | 新 | Dir | 零售加价率互算 | 一页公式 | 电商卖家 | 高 |
| 43 | break-even units calculator | 新 | Dir | 盈亏平衡销量 | 图表 | 小生意计划 | 高 |
| 44 | freelance rate card / day→project quote | 新 | X | 时薪→项目报价 PDF | 导出报价单 | 「scope creep buffer」楔子 | 高 |
| 45 | change order / scope creep letter | 新 | X | 变更单模板 PDF | 文档 | 挂报价工具内页 | 高 |
| 46 | pentest SOW / engagement letter generator | 新 | X | 安全测试委托范围 PDF | 字段多的正式文档 | Reddit 需求旁证；垂直窄 | 中 |
| 47 | privacy policy / cookie banner HTML generator | 新 | Dir | 勾选生成政策页+横幅代码 | 可复制代码 | 小站合规起步；非法务替代 | 中 |
| 48 | CCP / security headers generator | 新 | Dir | 生成安全头配置 | 配置文本 | 站长工具箱 | 高 |
| 49 | CORS header playground | 新 | Dir | 交互试 CORS | 调试即时反馈 | 开发者常青 | 高 |
| 50 | Subresource Integrity (SRI) hash generator | 新 | Dir | CDN 脚本完整性哈希 | 本地哈希 | 前端安全小工具 | 高 |
| 51 | PWA manifest + icon pack generator | 新 | Dir | manifest.json + 多尺寸图标 | 打包下载 | 建站配套 | 高 |
| 52 | .gitignore generator (stack presets) | 新 | Dir 新品 | 按语言/IDE 勾选生成 | 文本文件 | Free Tools Directory 新上 | 高 |
| 53 | EditorConfig / Prettier / tsconfig generator | 新 | Dir | 项目配置向导 | 下载配置 | 开发者 onboarding | 高 |
| 54 | Docker Compose / Nginx / Caddyfile generator | 新 | Dir | 常见服务编排模板 | 配置文件 | 表单→YAML；勿过度复杂 | 中 |
| 55 | OpenAPI / Swagger lite editor + mock | 新 | Dir | 粘贴规范校验 | IDE 式反馈 | 轻量，非 Stoplight | 中 |
| 56 | SQL formatter + explain plan lite | 新 | Dir | 美化 SQL | 格式化 UI | 开发者工具站内页 | 高 |
| 57 | curl ↔ fetch / HTTPie converter | 新 | Dir | 请求片段互转 | 代码转换 | 调试粘贴场景 | 高 |
| 58 | HAR viewer (local, privacy) | 新 | Dir | 本地看网络抓包 | 大 JSON 隐私 | 支持工单排障 | 中 |
| 59 | DNS / WHOIS / SSL expiry checker | 新 | Dir | 域名健康三件套 | 实时查询结果页 | 站长运维；需注意 WHOIS 源 | 中 |
| 60 | redirect chain / HTTP headers inspector | 新 | Dir | 跟跳转链 | 逐步可视化 | SEO/运维 | 高 |
| 61 | AGENTS.md / CLAUDE.md / Cursor rules generator | 新 | X | 按栈生成代理规则文件 | 多文件导出 | 「tired of re-explaining to agents」真实痛 | 高 |
| 62 | AI provider tool-def converter (OpenAI↔Anthropic↔Gemini) | 新 | X | 工具定义 schema 互转+校验 | 结构化校验 | 开发者垂直；供给新 | 中高 |
| 63 | “will AI quote my page?” content score | 新 | X | URL→可被引用性评分 | 抓取+规则打分 | GEO/AEO 新意图；勿虚假承诺 | 中 |
| 64 | multi-LLM website access checker | 新 | X | 测各模型能否抓你站 | 多端探测报告 | 营销站长 | 中 |
| 65 | token counter + cost by model | 老楔 | — | 第一批已有；本批不重复 | — | skip | — |
| 66 | prompt→style card from image URL | 新 | X | 猜图 prompt / 风格卡 | 导出卡片 | AI 画师；质量不稳标实验 | 低 |
| 67 | colorblind simulator (UI/gamedev) | 新 | X | 模拟色盲看 UI | 实时滤镜 | 无障碍+游戏美术 | 高 |
| 68 | pixel art converter / palette constrain | 新 | X | 图转像素风 | 画布导出 | 独立游戏 | 中 |
| 69 | hex / square grid map generator | 新 | X | 六角网格导出 | SVG/PNG | 战棋/桌宠 | 中 |
| 70 | CSS → Tailwind class converter | 新 | X | 粘贴 CSS 出 utility | 转换结果 | 前端迁移 | 中 |
| 71 | Flexbox / Grid visual builder | 新 | X | 拖拽出布局代码 | 可视化 | 教学+复制代码 | 高 |
| 72 | glassmorphism / neumorphism CSS generator | 新 | X | 特效 CSS | 实时预览 | 设计玩具流量 | 高 |
| 73 | FAQ accordion / review widget embed builder | 新 | X | 生成可嵌入 HTML | 复制即用代码 | Carrd/落地页站长 | 高 |
| 74 | email signature HTML generator | 新 | Dir | 公司邮件签名 | HTML 片段 | 中小企业；注意邮件客户端兼容 | 高 |
| 75 | mailto / sms: / WhatsApp click-to-chat link builder | 新 | Dir | 深链参数拼装 | 一键复制链接 | 营销落地页 | 高 |
| 76 | Depop / Etsy bio + title char counter | 新 | X | 平台字数与模板 | 平台限制计数 | 二手卖家垂直 | 高 |
| 77 | recipe scaler / baker’s % calculator | 新 | Dir | 份量缩放 | 精确小数 | 烘焙刚需 | 高 |
| 78 | cocktail ABV / dilution calculator | 新 | Dir | 酒精度估算 | 公式 | 酒吧爱好者 | 中 |
| 79 | meal plan weekly printable PDF | 新 | Dir | 一周膳食表打印 | PDF | 家庭场景；季节内容 | 中 |
| 80 | grocery list shared (link, no account) | 新 | Dir | 分享链协作清单 | 多人勾选 | 隐私短链/本地优先 | 中 |
| 81 | TDEE / macro calculator | 新 | X Dir | 热量与宏量 | 数字结果+导出 | 健身红海；打「无登录/打印」 | 中 |
| 82 | running pace / race predictor | 新 | Dir | 配速与完赛预测 | 公式表 | 跑者工具 | 高 |
| 83 | one-rep max / training zone HR | 新 | Dir | 力量与心率区间 | 计算器 | 健身站内页 | 高 |
| 84 | sleep cycle / caffeine half-life calculator | 新 | Dir | 睡眠周期与咖啡因 | 时间结果 | 轻健康；免医疗承诺 | 高 |
| 85 | paint / tile / concrete / board-foot calculator | 新 | Dir | DIY 用量估算 | 材料数量 | 家装搜索稳定 | 高 |
| 86 | roof pitch / stair / fence post calculator | 新 | Dir | 施工几何计算 | 尺寸输出 | 承包商/DIY | 中 |
| 87 | HVAC BTU / room sizing calculator | 新 | Dir | 制冷制热粗算 | 公式 | 免安装承诺 | 中 |
| 88 | solar panel / generator size calculator | 新 | Dir Trends(solar gen rising) | 光伏/发电机粗选型 | 功率结果 | Trends 家用太阳能相关上升；工具非卖货 | 中 |
| 89 | EV vs gas cost / home charging cost | 新 | Dir | 能耗费用对比 | 图表 | 购车决策辅助 | 中 |
| 90 | commercial RE: NOI / cap rate / DSCR suite | 新 | Dir 新品 | 商用物业指标计算器套件 | 多计算器同站 | Free Tools Directory 新上 Altyst 类；可做更轻 US 版 | 中 |
| 91 | rent vs buy / refinance break-even | 新 | Dir | 购房决策粗算 | 图表+表 | 房市内容；数据免责 | 中 |
| 92 | GPA / final grade needed calculator | 新 | Dir | 成绩与 GPA | 学校场景 | 学生常青 | 高 |
| 93 | rubric / lesson plan / flashcard PDF maker | 新 | Dir | 教师打印件 | PDF 批量 | 课堂；与 poll/分组相邻但不同 | 中 |
| 94 | classroom seating chart (rows, not banquet) | 新 | — | 教室行列座位表 | 打印布局 | **与 chartseat 婚礼桌不同楔**；可后做内页或独立词 | 中 |
| 95 | bingo / word search / raffle ticket generator | 新 | Dir | 活动纸质游戏打印 | PDF | 派对/教室；季节可叠 | 高 |
| 96 | save-the-date / menu card / table number PDF | 新 | — | 婚礼印刷件（非排座） | 印刷 PDF | 可挂 chartseat 横向；本批作独立词评估 | 中高 |
| 97 | RSVP form → guest CSV (simple) | 新 | — | 轻量回执收集 | 协作表 | 别做成重型婚礼 SaaS | 中 |
| 98 | org chart / RACI / Eisenhower matrix maker | 新 | Dir | 管理可视化导出 | PNG/PDF | 办公模板工具 | 高 |
| 99 | Mermaid / flowchart editor → PNG/SVG | 新 | Dir | 图示导出 | 图形文件 | 文档作者；本地渲染 | 中高 |
| 100 | ADR / PRD / postmortem / runbook templates | 新 | X旁 | 工程文书模板生成 | Markdown/PDF | 开发团队流程；可挂 AGENTS.md 同站 | 高 |

> 注：表中 #33、#65 刻意标 skip，保证「约 100 个**可讨论方向**」时用相邻行补位；实际可盘点数 ≈ **98 个有效新方向**（见过滤文）。

**补位（写入有效池，替 skip）**  
| A | readable / Flesch / grade-level checker | 新 | Dir | 可读性评分 | 本地启发式 | 写作工具；非 AI 改写 | 高 |  
| B | X account restriction / shadowban checker | 新 | X | 查号是否被限流 | 探测报告 | 营销号运营；API 不稳风险 | 低 |

---

## 3. 本批从信号里看到的「别人在做什么」

1. **隐私本地转换器联盟在扩**：X 上大量「no upload / WASM」文件站（PDF/图/音视频）；导航站 fwip / omnikitbolt / toosli 产品形态高度同质 → 机会在 **精确长尾词 + 场景页**（证件照 KB、WebM、价签），不是再做一个万能工具箱首页。  
2. **签名/电子签周边升温**：Trends 旁证 free signature；目录普遍有 draw→PNG 与 PDF 盖章。  
3. **开发者「给 AI 写说明书」**：AGENTS.md / Cursor rules / 多厂商 tool schema 转换——聊天能写，但 **可下载标准文件 + 校验** 仍有站。  
4. **AI 图片大目录（Toolify 三千+）= 红海示警**：本批不主推文生图 playground。  
5. **商用房产计算器被目录新收录**：说明「浏览器计算器套件」仍在被收录；可切美国 NOI/cap rate 轻站。

---

## 4. 下一步（Semrush 额度回来后）

对短名单逐词：Keyword Overview US 量≥1K、KD、SERP 前 10、域名 DoH。在此之前 **禁止用虚构量级排序投入开发**。

*生成：2026-11-05 · America/New_York · batch2 广度清单*
