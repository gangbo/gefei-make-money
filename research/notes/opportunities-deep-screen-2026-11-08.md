# 商机深筛 · 2026-11-08（America/New_York）

## 先给结论

**检查 21 个候选簇，留下 3 个优先验证切口 + 2 个观察项；0 个已满足全部立项门槛。**
不是“找到五个蓝海”。公开需求与收费产品能证明任务存在，**不能证明 Gary 的新站有 SEO 空位或会有人付钱**。本次没有 Semrush US 量/KD；所有候选的 US ≥1K、KD <55 都仍待核实。不能因此叫“已过关”。

排序（下一步验证优先级，不是马上写代码的顺序）：
1. **ZIP code territory map：跨州 ZIP-5 边界 + 私有 CSV + 交付导出包**（本批新发现）。
2. **Bank statement converter：银行 PDF → 可核验交易交付包**（复查 receipt/CSV 相邻意图，不是假装新发现）。
3. **PDF sewing pattern to A0：36 英寸宽印前检查与原比例排版**（本批新发现）。
4. App Store 截图批量发布前检查（旧截图方向收窄，观察）。
5. Image to cross stitch pattern：定尺寸、定耗时的图样简化（本批新发现，观察）。

## 范围与方法纠偏

已读 how-to-find-demand.md、batch1 百表、batch2 百表/过滤/短名单。旧 batch2 的计数有自相矛盾，“新”标签也包含 batch1 重复方向；不沿用其“57 个过筛”作为事实。

硬排除：ChartSeat、OnlinePollMaker、InvoiceNeat、tiktomato、neatSignature、neattyping、slickcalc、vocaldock 的现有方向，以及 UUID、cover letter、llms.txt、EXIF、名牌。**不推荐再建签名站，也不把 ChartSeat 的教室座位/婚礼印刷当新商机。** 本轮五项均不应硬塞入现有站；若最后立项，是新独立工具方向，但不代表现在要买域名。

- 先搜用户求助/重复手工劳动，再开竞争者功能页、价格页反证；目录仅作发现，未当需求证据。
- X 用公开 search_posts_all；查请求/抱怨而非 only “I built”。较可信需求片段主要在截图：有人询问 Adobe 替代，有人说一下午都在改尺寸。大量 maker 自推、设计师招揽、与工具无关 ZIP 政治帖均没算需求。
- Google Trends US Explore 本轮 HTTP 429。没有取得任何新 US 相对指数/飙升表，也未用旧签名 +250% 或印度 KB 表单需求代替美国证据。
- 所有引用页面本轮都尝试打开。成功页面和失败状态见 sources CSV；失败 Reddit 若只有搜索摘要，明确标搜索索引证据。没有登录、没有联系用户、没有提交任何表单。
- 仅查公开网页，没有打开外贸侠，没有用新 Semrush 量/KD。也没有声称外贸侠额度仍然没恢复——这次没有检查。
- 地域把握：ZIP 是明确 US；银行有美银/Chase 等竞争者支持但用户地域不完全可证；纸样有美国 Saint Paul 印店规则；截图/十字绣是英语全球需求，US 份额未知。

---

## 1. ZIP code territory map — 优先验证

**建站类型：NEW STANDALONE SITE。** 新于旧两批；不是卖地图印刷品。

### 精确搜索意图
- `zip code map maker`
- `create territory map from zip codes`
- `zip code map from spreadsheet`
- 长尾 `multi state zip code territory map` / `zip code map svg export`（长尾可能不到 1K；必须用根词核实量与盘面）。

### 观察到的事实
- [用户求助 r/gis](https://www.reddit.com/r/gis/comments/18gck86/looking_for_software_option_for_territory_mapping/)：手工在 Illustrator 做区域，希望移动服务基地后边界自动调整。**这是邻近区域划分任务，不等于证实 ZIP CSV 导出需求**；本轮抓到原文，发布时间未可靠核实。
- [r/Maps 精确 ZIP 列表求助](https://www.reddit.com/r/Maps/comments/t4bawh/can_someone_helpshow_me_how_to_make_a_territory/)：搜索索引有该提问，正文 fetch 500，curl 200 只有空壳。因此只作弱佐证，不引申购买意愿。
- [SimpleMapLab](https://www.simplemaplab.com/tools/map-with-zip-codes)，页面更新 Oct 19 2026：免费、CSV/粘贴数据；明确写 **暂不支持图片/数据导出**；用 centroid/county 聚合而非 ZIP 多边形。网页营销段有“export”描述，与 FAQ 不一致，按 FAQ 的限制记录，需实测。
- [Ultimaps 竞争者功能](https://ultimaps.com/use-cases/sales-territory-mapping/)：ZIP 边界是 Census ZCTA；其 ZIP 地图 **每张限一个州**，已有 CSV、分享和矢量导出。不能谎称市场没人做。
- [Ultimaps 实际 pricing 区](https://ultimaps.com/#pricing)：免费 PNG 带 attribution；单地图无品牌高分辨率 PNG/SVG/PDF **€12.50**，24 小时内可重导。这是有标价，不是已核实收入。
- [RandyMajors](https://www.randymajors.org/customgmap)：免费可从 ZIP 做边界图，Spreadsheet 工作流要求 Google Sheet 设为 anyone with link；免费上限 1,000 行。**跨州并非完全空白，私有本地 CSV 与矢量交付便利只是候选差异。**

### 候选未满足楔子（假设，非已证明）
把 `ZIP, rep` 私有 CSV 直接变成 **跨相邻州的 ZIP-5/ZCTA 边界图**，同时输出：干净 SVG/PDF + 无效 ZIP 清单 + 同一 ZIP 多个负责人冲突清单 + 来源版本。不要做 CRM、路线规划或地址清洗平台。

- 页面胜过聊天：真正地理 join、边界 dissolve、交互核对和正确矢量交付；聊天截图不等价。
- 变现：根词免费交互，专业导出按地图收费；已有 €12.50 单次产品证明收费模式存在，但不是 Gary 该照收的确定价格。
- 实现：中等。首版只选一个跨州 metro，按州载入简化 ZCTA 数据，不把几 GB 全美文件下载到浏览器。ZCTA≠USPS 官方投递边界；不能宣传精确邮政边界；数据许可、简化误差与保留 ZIP 前导零必须处理。
- **淘汰条件**：Ultimaps 或 RandyMajors 在同一私有 CSV 跨州导出任务已足够顺滑；或根词 US <1K / KD≥55；或 ZIP 数据授权成本吞掉单次客单价。
- 信心：任务存在 中；差异空位 中低；US 量 未知。**先验证，不先建。**

---

## 2. Bank statement PDF → 核验交付包

**建站类型：NEW STANDALONE SITE（潜在）。** 这是银行流水提取/审核，不是再造 InvoiceNeat 开票；不改 InvoiceNeat 首页去抢另一种意图。

### 精确搜索意图
`bank statement converter` / `bank statement pdf to csv` / `bank statement to excel`；更商业的 `bank statement reconciliation converter`。根词竞争很可能强，**无 KD 不说好打**。

### 事实与反证
- [Bookkeeping 用户需求](https://www.reddit.com/r/Bookkeeping/comments/1g56enx/not_in_bookkeeping_but_looking_for_a_bookkeeping/)：2024-10-16 的搜索索引原文，法律财务 discovery 成千页流水，手抄到 Excel，不要订阅/页数限制，愿为长期拥有的软件付费。**旧需求，不是 2026 新趋势。** 正文 fetch 500，curl 页面 200 空壳；原文依赖本轮搜索摘要，不能把随后跟帖里的厂商自推当独立推荐。
- [DocuClipper pricing](https://www.docuclipper.com/pricing/) 本轮实际打开：60 页档 **$29/月按月**或 **$20.30/月按年**。页面有用户引语称免费 AI 转换错误多，也已有余额勾稽/缺失月份报告。用户引语由厂商选取，**不等于独立准确率测评**。
- [FlowParse pricing](https://flowparse.io/pricing/)：每月 10 免费页；100 页一次性 **€5**。所以“只卖不订阅”也不是空白。
- [TinyToolAZ](https://tinytoolaz.com/bank-statement-converter/)：声称免费、本地处理、支持 Chase/BOA/Wells Fargo 等文字型 PDF。其准确性本轮没有用真实文件测试。
- [Fulla Ledger](https://fullaledgerbankstatements.com/guides/catch-up-bookkeeping)，更新 Oct 22 2026：**已经有行对源页审核、CSV/OFX/XLSX**。不能把“溯源/余额检查”单独叫独家差异。

### 真正可验证的窄切口
**只做文字型美国银行流水的浏览器内审核交付**：每行源页定位、跨页续行校正、余额异常定位、文件/页码保留，导出“交易 CSV + 未勾稽异常报告”。先不承诺所有银行/扫描件，不做法务判断/报税、不接 bank login。

- 缺口假设：免费本地工具的可核验性 vs 商业云审核工具的隐私/按页费；现有产品可能已覆盖这个组合，必须用同一套脱敏样本比较，而不是再讲 privacy 口号。
- AI 替代：LLM 能提表格，但少行、符号错误、跨页连续行需要复核。价值若只在“调用 OCR API”则淘汰；有确定性检查与审核 UI 才能考虑。
- 钱：一次性页包/一次项目导出包比低频订阅更合理，但已有 €5 竞争。真正买单点是节省复核小时，而非免费转 CSV。
- 单人风险：中高——银行模板、多列账单、异常和安全信任，远不是三天万能解析器。先 2–3 种文字 PDF 模板即可做证伪，不要承诺 enterprise 合规。
- **验收门槛**：先用公开/合成/获授权脱敏样本至少覆盖跨页续行、借贷符号、重复月份；逐笔人工金标。不能用“余额平了”冒充所有交易正确（漏一入一出也会平）。若无法比免费工具少复核工作，放弃。
- 信心：商业任务 中高；小站可切入 中低；US 量/KD 未知。

---

## 3. 缝纫 PDF → 36 英寸印前检查与拼版

**建站类型：NEW STANDALONE SITE（小实验），以后可扩纸样处理子页；不是 ChartSeat 子页。**

### 意图
`pdf sewing pattern to a0` / `a4 to a0 sewing pattern` / `sewing pattern pdf stitcher`。`pdf stitcher` 也有泛合并意图，要分 SERP；长尾是否达 1K 是本项最大疑问。

### 事实
- [用户遇到 36.5 英寸问题](https://www.reddit.com/r/sewing/comments/1qlxffl/trouble_using_pdf_stitcher_to_make_my_a4/)：已经用 PDF Stitcher，但输出 36.5×50，印店只能 36 宽，多出半英寸迫使分两张，换列又错位。本轮成功抓到完整请求；原帖日期只显示相对时间，不伪造发布日期。
- [美国 Saint Paul 的 Sewing Lounge 印前规则](https://www.sewinglounge.com/pdf-printing-faqs)：确实只能 36 英寸宽，顾客必须先自己把 Letter/A4 拼成 wide-format；支持按 size layer 打印。**真实美国工作流证据**，不是卖实体商品机会；本项目仅生成数字文件。
- [Spool & Spindle 原文](https://spoolandspindle.com/blogs/thoughts-from-the-spool/pdf-stitcher-the-skinny)，2023-07-18：说明拼后太宽、切分断在不好位置；手动把一个 pattern piece 对应页选出单独拼。印店不帮改文件，生成错无退款。加拿大印店，向美加发货，不能算 US 用户量。
- [PDFStitcher 文档](https://www.pdfstitcher.org/docs/page-tiling)：现有免费开源可以拼、裁/叠边距、层、page ranges；所以“网页可拼 PDF”本身没差异。
- [Pattern Projector](https://patternprojector.com/)：**免费开源网页版已能拼**，Chromebook/iPad 兼容不是新空位。

### 楔子
不要缩放整张图硬塞 36 英寸（衣服会变小）。做 **保原比例的拼图→裁空白→选纸样片段→36 英寸分版预览→输出**，给 1 英寸校准方格/明确标尺和跨页拼接标记；超宽时解释只能重排/分版，不偷偷缩放。先用人工框选片段，不做复杂 AI 识别纸样。

- 页面比聊天：真实 PDF 坐标、层与尺寸保留，连续几何视觉核对。
- 变现假设：少量免费预览，按图样/批量导出收费。**本轮没找到独立软件付费意愿，不能从大家花钱打印推断一定为转换付费。**
- 单人风险：中等；必须保护版权和原比例；桌面/浏览器 PDF 库的 layer 保留需测试，不能广告“100% 合身”。
- **淘汰条件**：同一 36.5 英寸样本在 Pattern Projector/PDFStitcher 已能轻松解决；或目标词 US 太小。若词量不达门槛，即使产品有趣也不立站。
- 信心：具体痛点 中高；US 搜索规模 低把握；支付意愿 未知。

---

## 4. App Store 截图批量 preflight（观察，不主推截图生成红海）

**类型：若未来做 app-dev 资源站，优先是站内免费获客页；现在没有合适现有 Gary 站，不必单买域名。**

- 词：`app store screenshot sizes` / `app store screenshot dimensions are wrong` / `app store screenshot generator`。它们不一定同一 SERP，不能堆在一页。
- [真实提问](https://www.reddit.com/r/iOSProgramming/comments/1mh5j15/tired_of_localizing_app_store_screenshots_one_by/)：2025-08-04 搜索结果，有逐语言手工本地化问题；本轮正文可读。
- X 独立请求 [AmeerHaio 2025-04-25](https://x.com/AmeerHaio/status/1915859257863639327)：找 Adobe 之外的工具。另一条 [Slothy 2026-07-22](https://x.com/Slothy_app/status/2079959871303106740) 提一下午改尺寸；作者是产品号，需求可信度比纯个人帖低，未证实 US。
- [Apple 官方规范](https://developer.apple.com/help/app-store-connect/reference/screenshot-specifications/) 本轮读到：禁止 alpha；相同 UI 只需最高要求尺寸，Apple 会向下缩放。**旧说法“必须每设备尺寸重导”夸大任务。** 官方也写 iPhone Duo 从 April 2027 对相关 SDK 开始要求截图，这只是未来规则，不是已观察的新词搜索热度。
- [AppScreens actual pricing](https://appscreens.com/pricing)：Pro 按年 $99（展示 $8.25/月），已含 80+ 语言/上传。
- [LaunchShots](https://launchshots.app/)：**免费本地 25 语言 ZIP 导出且无水印**；[Screenodon](https://www.screenodon.com/guides/screenshot-dimensions-are-wrong) 已有免费尺寸 checker；[ShotLattice](https://www.svensson.design/tools/shotlattice/) 已做 CSV copy、组合完整性/排版阻断、manifest。没有把它的 $29 当新定价结论（未打开独立 checkout）。
- 剩余假设：批量 ZIP 清单校验（locale 缺失/混尺寸/alpha/命名）、当前 Apple 规则版本报告，而非再做花哨设备框。**尚未证明比现有工具明显好。**
- AI：文件元数据与批量组合检查不适合纯聊天，但实现简单，付费也弱。
- 结论：能当免费流量工具，不能仅凭尺寸错误报怨就开独立付费站。排名第四是观察优先级，不是立项。

## 5. 定尺寸的 cross stitch pattern 简化器（观察）

**类型：若通过，NEW STANDALONE SITE；不卖绣品/线材。**

- 词：`cross stitch pattern generator` / `photo to cross stitch pattern`；窄切口 fixed-size logo/text readability。
- [用户原文](https://www.reddit.com/r/CrossStitch/comments/16zumq8/chat_help_w_pattern_generators/)：FlossCross 生成图样不是巨大就是模糊，字变得不可读，自己在 GIMP 简化相近颜色也不会。本轮成功读到；旧帖，不当新趋势。
- [FlossCross](https://flosscross.com/) 已经免费、无注册、本地、OXS 和 PDF 导出；**不能只卖“免费本地照片转十字绣”。**
- [Stitch Fiddle pricing](https://www.stitchfiddle.com/en/premium/pricing)：单月 $5，一年 $30，网页主标的 $2.50/月是年均价且非自动续费。强低价成熟竞争。
- [Stitchmate 功能/定价](https://stitchmate.app/features)，更新 Nov 2 2026：已经有文字/脸保留区、confetti 清理、耗用色/线程品牌、Pattern Keeper 输出等。PDF $5.99/图、5 图 $12/10 图 $20。**“去孤立针/更可绣”本身也被做了。**
- 剩余假设：从“我只有 6 英寸、最多 N 色、可用 N 晚”反推网格和阅读性，再让用户手工标脸/字保护区；必须盲测结果优于既有自动工具。
- AI替代：普通生成图不等于一针一格/符号图例，但独立工具的差异现在薄。
- 变现：图样 PDF 单次有标价，未核实收入；要证明比免费工具减少返工，否则放弃。
- 结论：**不推荐做通用 generator。** 只在“固定尺寸下文字仍清晰”的对比样本明显胜出时再深挖。US 份额/量未知。

---

## 21 个实际检查的候选簇与去留

| # | 候选 | 去留 | 原因 |
|---|---|---|---|
|1|ZIP territory map|优先验证1|跨州私有CSV+矢量交付组合差异，仍有强对手|
|2|银行流水转换|优先验证2|具体工作与收费存在；必须胜在核验工时，不是OCR壳|
|3|纸样A0/36英寸preflight|优先验证3|用户与美国印店同一边界问题；量和付费未知|
|4|App screenshots|观察4|免费25语言导出/尺寸检查已有，收窄批量preflight|
|5|Cross stitch generator|观察5|免费和低价非常完整，结果质量是唯一待验证点|
|6|Cut list optimizer|淘汰|免费满功能 CutListMachine/40件无限次 CutlistEvo；木工帖反对再收月费|
|7|Shipping label 4x6 crop|淘汰|LabelCrop免费批量、Suave已自动裁/条码校验；不要把无上传当 moat|
|8|Bingo generator|淘汰|BingoMix免费图文/随机/30张已解决教师旧抱怨|
|9|QIF/OFX/CSV互转|淘汰|OpenFile/开源本地转换供给；纯文件格式换壳缺收费点|
|10|Excel/CSV diff|淘汰|DiffSheets免费key matching；pythonandvba连容差/双键/报告都免费|
|11|GPX merge/privacy|淘汰|免费本地整套竞品多，隐私本身不足|
|12|DTF halftone|淘汰|AI Separations/Tshirt-Factory等免费knockout已覆盖；避免做印花卖货|
|13|Font identify|淘汰|强免费对手+字体库索引/许可门槛，不是便宜单人工具|
|14|Doubles round robin|淘汰|CourtsCaptain免费已有混双/水平/均等轮空；不是空白的尖楔|
|15|Booklet imposition|淘汰|BookletMaker完整免费核心+低价Pro，签帖/creep并非空位|
|16|Fillable PDF authoring|淘汰|Sejda/PDF24/免费对手成熟；与neatSignature边界也近，不再开站|
|17|Lithophane STL|淘汰|ItsLitho/3dp.rocks免费成熟，未找到付费缺口|
|18|Avery CSV mail merge|淘汰|Avery本身免费导入/校准，换UI不足|
|19|US passport photo|淘汰|IDPhoto4You免费；ImgTweak本地4x6安全边距已有。不把印度KB当US|
|20|Generic converters/PDF suite|淘汰|重复旧池，巨头和免费本地竞争密，无窄楔|
|21|Photo contact sheet|淘汰|[ContactSheetKit](https://www.contactsheetkit.com/contact-maker)免费PDF、[TextFaker](https://textfaker.com/tools/photo-contact-sheet-maker)本地网格；没找到比免费工具强的交付差异|

## 下一步：只有证据达到门槛才开发

1. Semrush 可用后首先查三个根词 `zip code map maker`、`bank statement converter`、`pdf stitcher` 及其精确意图；US≥1K、KD<55 是筛选条件，不是目前已知结果。若全不达标，接受本轮没有新站可做。
2. 同一任务对照免费/付费竞品，用合成或获授权脱敏素材，不上传用户私密数据。本轮未进行端到端正确性测试，所有产品功能是页面观察。
3. 分别测：跨州CSV地图矢量交付；源页定位与逐笔金标银行流水；36.5英寸纸样保原比例改版。不能只比“功能数量”。
4. 为地图导出和纸样输出标明数据/尺寸规则；为银行核验输出标明不确定/需人工复核。没有100%准确或政府/法律认可保证。
5. 别同时开五个站。**若要选一个最小验证，我会先试ZIP跨州导出；若要选最高潜在付费任务，银行流水更强但工程和信任成本显著更高。**

## 限制

Trends 429 未绕过网络封锁；部分 Reddit 500/超时/仅壳；一篇 Accounting 帖已被删，未当正向需求；无Semrush/新量/KD；无收入/域龄/排名权威数据。X信号不是US抽样。正文中的竞品价格仅来自本轮打开的官方价格/功能定价页，不沿用搜索摘要旧价格。

五项是候选，不是五个已确认机会。相较旧批次，这次最重要的产出是**淘汰伪差异**。

取证文件：opportunities-deep-screen-sources-2026-11-08.csv，44条来源记录（含失败/淘汰证据，不等于44条需求证明）。本批报告日期按 America/New_York；取证均在2026-11-08上午EST。
