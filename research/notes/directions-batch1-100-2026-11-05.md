# 第一批需求方向清单（约 100）· 2026-11-05

> 面向：个人独立开发者（在线工具 / 内容工具站）  
> 范围：**不做电商、不做硬件联盟评测、不卖实体**  
> 已跳过：形式发票（InvoiceNeat 已上线）、Google Docs 发票模板、Nano Banana、风扇充电宝及同类实体带货  
> 先前短名单里 PDF 压缩 / APA·IEEE 引用 / 通用无登录简历：**本批不当作优先推荐**（未列入或仅在有明确不同切入时出现）  
> 本批目标：广度；**不编造搜索量/KD**；第二批再做 SERP / 域名 / 难度深筛  

---

## 1. 方法说明（第一批怎么挖）

按你定的两类来源扩候选：

1. **新需求**：以种子主题（invoice / quote / receipt / generator / maker / converter / calculator / checker / AI 产品名 / 季节词…）看 Trends Rising/Breakout、社群新词打法、公开趋势目录（如 tool 后缀词表）；适合「短窗口落地页 / 轻工具」。
2. **老需求做得更好**：稳定搜、但前排常要注册、要上传隐私文件、丑、慢——用无登录、浏览器本地（WASM）、更快、更专注长尾页去切。

辅助角度：Reddit/HN 对「必须上传/强制注册」的抱怨；已有站（如 InvoiceNeat、tiktomato）**内页横向拓展**；新品「非官方说明/对比」页（窗口短）。

**本回合工具局限（第二批可补）：**  
未安装 Ahrefs / Semrush / Treg 等 SEO·趋势连接器；Root Trends 页面拉取失败；无直接登录 Google Trends UI 批量导表。主要依据：既有笔记（`trends-rising-raw.md` / `opportunities-2026-11-05.md` / 找需求 SOP）、WebSearch、公开工具目录与投诉帖。**表中「为什么像需求」是定性理由，不是编造的量级数字。**

建议装（可选）：[Ahrefs](https://cursor.com/grok-bot/link/v1/plugin/add?id=56809965)、[Semrush](https://cursor.com/grok-bot/link/v1/plugin/add?id=56809983)、[Treg](https://cursor.com/grok-bot/link/v1/plugin/add?id=55647425)（含 SERP/趋势类 endpoint）。

---

## 2. 方向表（100）

| # | 方向名/关键词 | 新/老 | 种子主题 | 一句话为什么像需求 | 建议产品形态（个人可做） | 粗可做性 |
|---|---|---|---|---|---|---|
| 1 | commercial invoice generator | 老 | invoice | 进出口场景与形式发票相邻，商单字段需求明确 | InvoiceNeat 同引擎多文档类型 / 独立落地页 | 高 |
| 2 | packing list generator (shipping) | 老 | invoice / shipping | 货运文件常与发票一起要，模板站体验参差 | 无登录装箱单 PDF 生成 | 高 |
| 3 | packing slip generator | 老 | invoice | 电商卖家日常出单词，工具可极简 | 浏览器端 packing slip → PDF | 高 |
| 4 | bill of lading template generator | 老 | shipping docs | B/L 字段复杂但可用静态表单+PDF | 说明页 + 可填模板导出 | 中 |
| 5 | credit note / debit note generator | 老 | invoice | 会计纠错单据，与发票同一引擎 | InvoiceNeat 内页：Credit/Debit Note | 高 |
| 6 | purchase order (PO) generator | 老 | B2B docs | PO 搜索意图稳定，多数站要注册 | 无登录 PO 生成器 | 高 |
| 7 | delivery note / delivery receipt generator | 老 | invoice | 交付单据与收据相邻，长尾清晰 | 同引擎 Delivery Note | 高 |
| 8 | estimate vs quote vs invoice explainer + switcher | 老 | invoice | 小商家分不清文档类型；可挂互链 | 对比文 + 一键切换文档类型 | 高 |
| 9 | self-billing invoice generator | 新/老 | invoice | 特定行业（物流/平台）有搜，供给少 | 释义 + 专用字段生成器 | 中 |
| 10 | tax invoice / VAT invoice fields helper | 老 | invoice / tax | 跨境卖家填 VAT 字段常出错 | 国家切换 + 字段校验提示（非报税） | 中 |
| 11 | timesheet → invoice calculator | 老 | freelance | 自由职业者先记工时再开发票 | 工时表 → 金额 → 导出发票草稿 | 高 |
| 12 | mileage log + invoice adder | 老 | freelance | 里程报销与发票同场景 | 简单里程计算器 + 费用行 | 高 |
| 13 | late fee / interest on overdue invoice calculator | 老 | invoice | 「逾期怎么算」问答多，计算器切入干净 | 单页公式计算器 + 说明 | 高 |
| 14 | payment reminder email / letter generator | 老 | invoice | 催款文案需求稳定 | 模板生成器（多语气） | 高 |
| 15 | receipt OCR → CSV (local) | 老 | receipt | 抱怨上传小票到云端；本地识别是差异 | WASM/本地模型抽字段导出 CSV | 低 |
| 16 | expense / expense receipt maker (no signup) | 老 | receipt | 小店要「像真的」收据，常遇注册墙 | 浏览器收据生成 | 高 |
| 17 | expense refund receipt generator | 老 | receipt | 退货场景长尾 | 退款收据模板 | 高 |
| 18 | donation gift receipt generator | 老 | receipt / 季节 | 礼品季有峰值 | 隐藏价格的礼品收据 | 高 |
| 19 | simple poll maker (no login) | 新 | maker | Trends 相关 maker 有上升；课堂/群投票刚需 | 分享链投票，无账号 | 高 |
| 20 | christmas / holiday wishlist maker | 新 | maker / 季节 | 11–12 月季节窗口；精确 maker 词可占 | 无登录心愿单 + 分享链接 | 高 |
| 21 | secret santa name drawer (privacy-first) | 老 | maker / 季节 | 已有站多但可强调「不存名单」 | 本地抽签 / 可销毁链接 | 中 |
| 22 | white elephant / yankee swap generator | 新 | 季节 party | 北美节日局游戏词，工具形态明确 | 规则说明 + 抽签/顺序生成 | 高 |
| 23 | team randomizer / group splitter | 老 | maker | 课堂/活动分队高频 | 名单粘贴 → 随机分组 | 高 |
| 24 | bracket maker (tournament) | 老 | maker | 业余赛事/办公室比赛 | 拖拽对阵图 + PNG 导出 | 中 |
| 25 | seating chart / table planner maker | 老 | maker | 婚礼/宴会布置搜，多数 SaaS 重 | 轻量桌位图（座位拖拽） | 中 |
| 26 | name tag / badge generator (print) | 老 | generator | 活动打印名牌稳定需求 | PDF 名牌批量排版 | 高 |
| 27 | certificate of completion / appreciation generator | 老 | generator | 课程/志愿证明，模板站广告重 | 无水印证书 PDF | 高 |
| 28 | award certificate maker (school) | 老 | generator | 学校场景长尾 | 多模板证书生成 | 高 |
| 29 | letter of recommendation template generator | 老 | letter | 学生/职场文书，可模板化 | 问卷式生成推荐信草稿 | 中 |
| 30 | cover letter generator (no signup, local) | 老 | resume 相邻 | 「无注册」意图在涨；不做完整简历站 | 粘贴 JD → 信草稿（可本地） | 中 |
| 31 | resignation letter generator | 老 | letter | 明确意图、字段少 | 单页辞职信生成 | 高 |
| 32 | NDA generator (simple mutual) | 老 | legal lite | 创业早期常搜；重法律站吓人 | 免责声明 + 简易双边 NDA 模板 | 中 |
| 33 | freelance contract / MSA short template | 老 | contract | 与发票用户重叠 | 短合同生成 + PDF | 中 |
| 34 | SOW (statement of work) generator | 老 | B2B docs | 乙方交付范围文档 | 章节式 SOW 生成器 | 中 |
| 35 | meeting agenda + minutes template maker | 老 | meeting | 办公高频，Notion 模板外可要「一页导出」 | 议程/纪要双模板 | 高 |
| 36 | timezone meeting planner (world clock picker) | 老 | calculator / meeting | 远程团队刚需；不少站广告多 | 多时区重叠可视化 | 高 |
| 37 | business days / working days calculator | 老 | calculator | 「几个工作日」稳定搜 | 含假期开关的工作日计算器 | 高 |
| 38 | date duration / age exact calculator | 老 | calculator | 经典计算器词，可做更清晰结果页 | 精确年月日差 + 倒计时 | 高 |
| 39 | countdown page generator (share link) | 老 | maker | 活动倒计时落地页需求 | 生成可分享倒计时页 | 高 |
| 40 | cron expression generator + explainer | 老 | generator / devops | 开发者常搜；前排体验不一 | 可视化 cron + 下次运行预览 | 高 |
| 41 | crontab / crontab to English translator | 老 | converter | 读懂已有 cron 的刚需 | 表达式 → 自然语言 | 高 |
| 42 | JWT decoder (local, no paste to server) | 老 | checker / security | 隐私敏感；强调本地解码 | 纯前端 JWT 解析 | 高 |
| 43 | UUID / ULID / NanoID generator | 老 | generator | 开发者工具常青 | 批量生成 + 校验 | 高 |
| 44 | bcrypt / password hash playground (local) | 老 | generator | 教学与调试；勿存密码 | WASM 哈希演示 | 中 |
| 45 | regex tester with explanation | 老 | tester | 老词；可用「解释每步」差异化 | 正则测试 + 中英解释 | 中 |
| 46 | JSON ↔ YAML ↔ TOML converter | 老 | converter | 配置文件互转高频 | 本地格式转换 + 校验 | 高 |
| 47 | CSV ↔ JSON converter + schema guess | 老 | converter | 数据清洗入门刚需 | 粘贴转换、类型推断 | 高 |
| 48 | Base64 / URL encode-decode (batch) | 老 | converter | 超常青；可打包为「隐私工具箱」内页 | 本地编解码套件 | 高 |
| 49 | Unix timestamp ↔ human time (multi-TZ) | 老 | converter | 开发调试刚需 | 时间戳工具（含毫秒） | 高 |
| 50 | Open Graph / Twitter card preview + meta generator | 老 | SEO / generator | 发帖前预览；不少站要登录 | 填字段 → 预览卡片 + meta 标签 | 高 |
| 51 | favicon generator (SVG → multi-size ICO/PNG) | 老 | generator | 建站配套刚需 | 上传/画图标 → 打包下载 | 高 |
| 52 | OG image / social share image maker | 老 | maker | 博客/产品发帖配图 | 模板填标题出 PNG | 高 |
| 53 | robots.txt / llms.txt generator | 新/老 | SEO | AI 抓取说明（llms.txt）偏新；robots 偏老 | 勾选规则生成文本 | 高 |
| 54 | sitemap.xml generator (URL list → XML) | 老 | SEO | 小站站长刚需 | 粘贴 URL 列表出 sitemap | 高 |
| 55 | schema.org JSON-LD generator (FAQ/Product/Article) | 老 | SEO | 结构化数据配置易错 | 表单 → JSON-LD | 中 |
| 56 | meta description length checker + rewriter assist | 老 | checker | SEO 执行层工具 | 计数 + 多版本草稿 | 高 |
| 57 | UTM link builder | 老 | marketing | 投放同学日常 | 参数拼链接 + 二维码 | 高 |
| 58 | QR code generator (Wi-Fi / vCard / URL, no watermark) | 老 | generator | 老词但「无水印/无过期」仍被抱怨 | 本地 QR，多类型 | 中 |
| 59 | Wi-Fi QR + printable tent card | 老 | generator | 咖啡馆/民宿场景 | QR + 可打印小卡片 PDF | 高 |
| 60 | vCard / digital business card generator | 老 | generator | 展会后交换联系方式 | 生成 vcf + 简易页 | 高 |
| 61 | bill / expense splitter (local, shareable) | 老 | calculator | 聚餐分账；可端到端加密分享 | 无账号分账器 | 高 |
| 62 | tip calculator (multi-way split) | 老 | calculator | 北美场景稳定 | 小费+分人计算器 | 高 |
| 63 | percentage calculator (all variants) | 老 | calculator | 超高频；靠「一步说清题型」 | 多题型百分比计算器 | 高 |
| 64 | compound interest / savings calculator | 老 | calculator | 理财入门刚需 | 图表化复利计算器 | 高 |
| 65 | loan amortization schedule generator | 老 | calculator | 房贷/车贷表 | 还款表 CSV/PDF | 中 |
| 66 | currency converter (offline rates snapshot + disclaimer) | 老 | converter | 旅行/跨境；需注意汇率源 | 静态/定时拉取汇率页 | 中 |
| 67 | unit converter hub (length/weight/data) | 老 | converter | 工具站流量底座 | 分类单位转换 | 高 |
| 68 | color contrast (WCAG) checker | 老 | checker / a11y | 设计无障碍刚需 | 对比度检测 + 建议色 | 高 |
| 69 | palette generator from image (local) | 老 | generator | 设计师抽色；强调不上传 | 本地取色板 | 高 |
| 70 | CSS gradient / shadow / clip-path generator | 老 | generator | 前端常青 | 可视化 CSS 生成 | 高 |
| 71 | Tailwind color / class cheatsheet interactive | 老 | developer | 框架用户高频查询 | 可搜索 cheatsheet 小工具 | 高 |
| 72 | Markdown ↔ HTML converter + preview | 老 | converter | 写作/文档互转 | 分栏预览转换 | 高 |
| 73 | Markdown table generator | 老 | generator | README 表格痛苦点 | 可视化出 MD 表格 | 高 |
| 74 | Lorem / fake data generator (PII-safe) | 老 | generator | 开发填充数据 | 姓名/地址假数据批量 | 高 |
| 75 | .env / secrets redactor for screenshots (local blur) | 老 | privacy | 发帖前打码密钥的真实抱怨 | 本地图片打码/模糊 | 中 |
| 76 | EXIF / GPS metadata viewer + stripper | 老 | privacy / photo | 发图前去定位；上传站不信任 | 本地查看并清除 EXIF | 高 |
| 77 | HEIC → JPG/PNG (browser, no upload) | 老 | converter / photo | iPhone 照片兼容刚需；隐私敏感 | WASM 转换 | 中 |
| 78 | image resize / compress for forms (local) | 老 | image | 申请表「文件太大」高频痛点 | 本地压到目标 KB | 中 |
| 79 | remove image background (on-device model) | 新/老 | image / AI | 需求大；差异在「模型不下云」 | 浏览器端抠图（模型本地下载一次） | 低 |
| 80 | SVG optimizer / minify | 老 | optimizer | 前端资源优化 | SVGO 式在线优化 | 高 |
| 81 | PDF page reorder / rotate / split (local) | 老 | pdf | 与「压缩」不同：操作页序隐私同样敏感 | 本地 PDF 页工具（非压缩主打） | 中 |
| 82 | PDF unlock / decrypt when password known (local) | 老 | pdf | 自己文件解锁；忌帮破解 | 本地已知密码解锁说明+工具 | 中 |
| 83 | PDF stamp / watermark own docs (local) | 老 | pdf | 「给合同盖自己的章」 | 本地加水印/页码 | 中 |
| 84 | e-signature simple (draw → stamp PDF, local) | 老 | pdf / contract | 轻量签字需求；大厂要账号 | 手写签名嵌入 PDF | 中 |
| 85 | audio trim / convert to MP3 (ffmpeg.wasm) | 老 | audio | Discord/播客长度限制抱怨常见 | 本地剪辑转码 | 中 |
| 86 | video compress under size limit (local) | 老 | video | 上传限制驱动；算力在用户设备 | ffmpeg.wasm 压到目标大小 | 低 |
| 87 | subtitle SRT ↔ VTT converter | 老 | converter | 视频字幕格式互转 | 文本转换器 | 高 |
| 88 | YouTube thumbnail size / safe-zone checker | 老 | checker | 创作者预览 | 上传图看安全区 | 高 |
| 89 | hashtag / caption length counter (IG/X/TikTok) | 老 | social | 平台字数限制 | 多平台字数与标签整理 | 高 |
| 90 | AI token counter + cost estimator (by model) | 新 | AI / calculator | 调 API 成本透明需求；词表可本地 | 多模型 token/费用估算 | 高 |
| 91 | LLM system prompt / template library (niche vertical) | 新 | prompt | 「prompts」相关有热度；垂直比大而全好打 | 某垂直（客服/SEO）prompt 库 | 中 |
| 92 | AI text detector (client-lite / heuristic) | 老 | detector | 搜索大但难做准；可定位「启发式/教学」 | 说明局限的检测实验页 | 低 |
| 93 | AI humanizer（改写去 AI 味）落地页 | 新 | humanizer | 公开词表里 humanizer 量级显眼；合规与质量风险高 | 谨慎：仅作候选，需合规评估 | 低 |
| 94 | Claude Duet / Claude 新品 explained（非官方） | 新 | claude | Trends 上 Duet 等 Breakout 级；官方占首页但 FAQ/对比位可做 | 说明+对比+资格 FAQ（勿钓鱼登录） | 高 |
| 95 | MCP / agent skills explained + starter checklist | 新 | agent / MCP | 2026 开发者话题上升；教育向工具页 | 概念站 + 清单/模板 | 中 |
| 96 | model comparison matrix generator (DIY table) | 新 | AI | 「A vs B」长尾不断；可让用户自建对比表 | 可分享的模型对比表生成 | 中 |
| 97 | OpenRouter / multi-provider API key cost dashboard (BYOK) | 新 | AI infra | 多模型路由用户要算账 | 用户自带 key 的用量估算页 | 中 |
| 98 | packing list generator (travel) | 老 | travel / maker | 旅行打包清单工具在 2026 内容里反复出现 | 目的地/天数 → 清单 | 高 |
| 99 | packing cube / luggage weight estimator | 老 | travel | 行李额计算器场景清晰 | 物品勾选估重 | 高 |
| 100 | random name / team / pickup generator (classroom) | 老 | generator | 教师工具常青 | 随机点名/分组器 | 高 |

---

## 3. 刻意未列入（便于第二批对照）

| 方向 | 原因 |
|---|---|
| 风扇充电宝 / 车门辅助把手 / 美妆成分评测等 | 实体电商/联盟，超出个人工具能力边界 |
| Google Docs 发票模板站 | 你已明确跳过；且与 InvoiceNeat 抢意图 |
| Nano Banana 2.1 等 | 窗口过、你已有 tiktomato 相关页 |
| 通用 PDF 压缩/合并主打、APA7/IEEE 引用、无登录通用简历 | 先前短名单你判「不值得」；本批不作为推荐 |
| 体育赛程、纯新闻热点 | 工具站不匹配 |
| 需重算力冒充官方的 AI 视频站 | 成本与品牌风险高 |

---

## 4. 第二批筛选建议做什么

对第一批里你标「想继续看」的 15–30 条，逐条做：

1. **Google 搜精确词**：前 10 是谁、是否工具意图、有无「无注册/本地」空位。  
2. **Trends**：7 天 / 30 天 / 12 个月曲线，区分新尖峰 vs 老稳量。  
3. **域名**：Cloudflare DoH + 注册商确认（NXDOMAIN ≠ 一定能买）。  
4. **可做性复核**：能否当天～三天上线 MVP；是否必须服务器/模型 API。  
5. **与现有资产关系**：能挂 InvoiceNeat / tiktomato 内页的优先于新开站。  
6. **合规**：humanizer、法律模板、签名、PDF 解锁等单独过一遍风险。  
7. 可选：装上 Ahrefs/Semrush/Treg 后再看流量与竞品页，**不要在没 SERP 前按感觉排序投入开发**。

*生成：2026-11-05 · America/New_York · 第一批广度清单，非最终立项。*
