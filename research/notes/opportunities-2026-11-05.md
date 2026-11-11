# 商机清单 · 2026-11-05（America/New_York）

> 方法：按 new.web.cafe 笔记（Trends 飙升 / Breakout → Google SERP → 域名 DoH → 当天可上线 MVP）实操。  
> 数据源：`trends-rising-raw.md`（Google Trends US · Past 30 days · Related Rising，约 130 候选）+ Exploding Topics US Top100（2026-11-04）作补充。  
> 域名：Cloudflare DNS-over-HTTPS（A/NS）；**NXDOMAIN = 疑似可注册，未在注册商下单验证**。本机 dig/whois 不可用。  
> SERP：本回合 WebSearch 首页结果，不编造。

---

## 执行摘要

**怎么搜的**  
1. 读社群找需求 SOP，优先「工具 / generator / maker / 新模型名」而非纯体育新闻。  
2. 用 Trends 原始飙升词（secret santa / citation / pdf / resume / invoice / deadlock / nano banana / claude duet 等）+ Exploding Topics 高增长消费品词交叉。  
3. 对约 **45+** 个关键词做英文 Google SERP 抽检；对 **90+** 个 `.com` 变体做 DoH 解析。  
4. 淘汰：品牌官方垄断（Claude Duet 官网、Carsized、Pupsicle）、体育赛程、已有强工具海（Secret Santa 精确词、通用 wishlist）、版权高风险（South Park OC 主打）、SERP 全是 DR 巨头且无差异化切入的词。

**筛选规模**  
- Trends 原始相关飙升条目：~130  
- 进入 SERP/域名深筛：~45  
- 最终入选：**18**（目标 15–20）

**Top 5（优先动手）**

1. **Pro forma invoice（释义 + 生成器）** — Trends「what does proforma invoice mean」+4000%；首页多为 Investopedia / 政府站，缺好用免费生成器；`proformainvoicemeaning.com` / `proformainvoicegenerator.com` 均 NXDOMAIN。  
2. **Power bank with fan（对比评测站）** — Exploding Topics +6300%；首页多为品牌 PDP，缺独立对比站；`powerbankwithfan.com` NXDOMAIN。  
3. **Nano Banana 2.1 playground（新词落地页）** — Trends 全 Breakout；已有 Pollo/Felo 等套壳，窗口仍在；`nanobanana21playground.com` / `nanobanana21free.com` NXDOMAIN。  
4. **Google Docs 发票模板站** — 「how to make an invoice on google docs」+350%；首页是教程文，少专域模板库；`googledocsinvoice.com` / `invoicegoogledocs.com` NXDOMAIN。  
5. **Hall-effect joystick / stick fix（游戏配件工具站）** — Exploding Topics +6300% + Reddit 改装讨论密；`hallstickfix.com` NXDOMAIN（`halleffectjoystick.com` 已被占）。

---

## 商机表（18）

| # | 关键词/商机名 | 发现来源 | 为什么像需求 | SERP 现状（本回合） | 域名情况 | 建议产品形态 | 风险/窗口 | 可做性 |
|---|---|---|---|---|---|---|---|---|
| 1 | proforma invoice meaning / generator | Trends · invoice · +4000% | 超高涨幅；搜索意图清晰（释义 + 出单） | 首页 Investopedia、trade.gov、HMRC、词典；**几乎没有轻量免费生成器专域** | `proformainvoicemeaning.com`、`proformainvoicegenerator.com`：**NXDOMAIN（疑似可注册）**；`proformainvoicetemplate.com` 已占用 | 释义文 + 浏览器端 PDF/HTML 发票生成器；当天可上 | 教育内容易被权威站压；用「模板+生成」差异化 | **高** |
| 2 | how to make an invoice on google docs | Trends · invoice · +350% | 教程意图 + 模板需求；可接广告/邮件 | MakeUseOf、Adobe、Square、模板站文章；**专域模板库少** | `googledocsinvoice.com`、`invoicegoogledocs.com`：**NXDOMAIN** | 可一键复制的 Docs 模板库 + 填写指南；当天 | 模板同质；需持续加行业模板 | **高** |
| 3 | apa 7 citation generator | Trends · generator · +50%（APA7） | 学生刚需；长尾「apa 7」仍有专域空间 | Scribbr、Citation.co、Citeory、apareferencegenerator 等；**巨头多但 apa7 精确域未全占** | `apa7generator.com`、`apa7citation.com`、`citationapa7.com`：**NXDOMAIN**；`apa7citationgenerator.com` NXDOMAIN | 单页 DOI/URL→APA7 引用；无登录导出 | Scribbr 难撼动；打「更快/无注册/本地」 | **中高** |
| 4 | ieee citation generator | Trends · generator · +40% | 工科引用刚需；比 MLA/APA 竞争窄 | TheLatexLab、EngCite、Huggle、IEEE 官方助手；**非 Scribbr 一家独大** | `ieee-citation-generator.com`：**NXDOMAIN**；`ieeecitationgenerator.com` 已占用 | DOI/BibTeX→IEEE 编号引用 + 导出 | 学术工具信任成本；需校对准确率 | **中高** |
| 5 | free resume builder no sign up / ATS resume prompts | Trends · resume · +60% / +350% | 「无注册」与「ATS 模板 prompt」双升 | Lanjut、LeanCV、Resume88 等一堆无登录站；**卷但长尾精确域空** | `freeresumebuildernosignup.com`、`atsresumebuilderfree.com`、`chatgptresumeprompts.com`、`atsresumeprompt.com`：**NXDOMAIN** | 浏览器端简历编辑器 + ATS prompt 库 | 赛道拥挤；靠「无上传隐私」+ prompt SEO | **中** |
| 6 | shrink pdf file size / pdf combiner free | Trends · pdf · +60% / +70% | 办公高频工具；隐私痛点真实 | Adobe、Smallpdf、iLovePDF 统治；也有 github.io 本地压缩 | `shrinkpdffilesize.com`、`compresspdfsize.com`、`pdfcombinerfree.com`、`pdfshrinkerfree.com`：**NXDOMAIN** | **本地 WASM** 压缩/合并（不上传）落地页 | 巨头难打流量；强调 privacy + 精确词 | **中** |
| 7 | nano banana 2.1（playground / free） | Trends · nano banana · **全 Breakout** | 典型新词窗口；模型名搜索暴涨 | Google 文档 + Pollo/Felo/ElevenLabs/Plimo 套壳；**仍可占专域+对比页** | `nanobanana21playground.com`、`nanobanana21free.com`、`nanobananaplayground.com`、`trynanobanana21.com`：**NXDOMAIN**；`nanobanana21.com` / `nanobanana21.ai` 已占用 | 新词站：能力说明、对比 Pro/2.1、API 入门、外链 playground | 窗口短；商标/政策风险；别冒充官方 | **高（快）** |
| 8 | claude duet / waitlist / explained | Trends · claude · Breakout（duet app +4650%） | 新品上线型搜索；FAQ/评测位 | 官方 claude.com + Help Center + Zapier 解读 | `claudeduetwaitlist.com`、`claudeduetexplained.com`、`claudestartupprogram.com`：**NXDOMAIN**；`claudeduet.com` 已占用 | 非官方解读站：是什么、资格、对比 Claude 主 App、startup program 说明 | **强品牌**；勿钓鱼登录；窗口以资讯为主 | **中（快）** |
| 9 | deadlock tier list / build maker | Trends · maker · +250% / +190% | 游戏站经典；补丁更新=内容刷新 | Tierspire、deadlocktier、DeadlockCalc、Vestigo、Breach 等**已有多家** | `deadlocktierlistmaker.com`、`deadlockherotierlist.com`、`valvedeadlockbuilder.com`：**NXDOMAIN**；`deadlockbuildmaker.com` 已占用 | 全英雄拖拽 tier + 出装；PNG 分享；贴合最新 patch | 供给已密；只有「最新 roster + 更好分享」才有机会 | **中低** |
| 10 | christmas wishlist / list maker | Trends · maker · +250% | 季节刚需；11 月正窗口 | Moonsift、WishApp、Happy Giftlist、Thingstogetme 等很多 | `christmaswishlistmaker.com`：**NXDOMAIN**；`christmaslistmaker.com` / `wishlistmaker.com` 已占用 | 无登录心愿单 + 分享链接；可叠 Secret Santa | 季节过后掉量；竞品成熟 | **中（季节）** |
| 11 | simple / free poll maker | Trends · maker · +50% | 轻工具；课堂/群投票 | `pollmaker.com` 等品牌在；长尾仍可切 | `simplepollmaker.com`、`freepollmakeronline.com`：**NXDOMAIN**；`pollmaker.com` / `freepollmaker.com` 已占用 | 无登录实时票选；分享 URL | 涨幅一般；功能需极简体验 | **中** |
| 12 | power bank with fan | Exploding Topics · +6300% | 硬件新品类搜索猛增 | Cavatina、Green Lion、SBS、HandFan 等 **PDP 为主**，缺强对比评测站；另有 vercel 数码站旁证 | `powerbankwithfan.com`、`bestpowerbankfan.com`：**NXDOMAIN** | 对比评测 + 参数表联盟站；当天静态站 | 联盟合规；季节（夏）波动 | **高** |
| 13 | car assist handle | Exploding Topics · +333% | 银发出行配件；购买意图强 | Vive、Stander HandyBar、Pelegon 等品牌站 | `carassisthandle.com`、`carassistgrip.com`、`seniorcarhandle.com`：**NXDOMAIN** | 「best car assist handle」评测 + 兼容车门说明 | 涨幅相对低；信任/安全文案要谨慎 | **中高** |
| 14 | hall effect joystick / stick fix | Exploding Topics · +6300% + Reddit | 漂移维修/改装刚需；社区讨论密 | HowToGeek、TheVerge、iTechGuides、TestPane + Reddit 改装帖；**专域工具站不多** | `hallstickfix.com`、`controllerhallfix.com`：**NXDOMAIN**；`halleffectjoystick.com` / `stickdriftfix.com` 已占用 | 兼容表 + 购买指南 + 简易 deadzone 说明页 | 硬件售后纠纷；别承诺「永久不漂」 | **高** |
| 15 | kojic acid body wash | Exploding Topics · +9700% | 美妆成分词爆发 | Women's Health、Health.com、Reddit SkincareAddiction、品牌 PDP | `kojicacidbodywash.com`、`kojicbodywash.com`：**NXDOMAIN** | 成分科普 + 安全提示 + 产品对比 | 功效宣传合规；别医美承诺 | **中高** |
| 16 | peel off lip liner | Exploding Topics · +7500% | TikTok/美妆病毒词 | Maybelline、Sacheu、Allure、NewBeauty | `peelofflipliner.com`、`peelofflipstain.com`：**NXDOMAIN** | 评测对比（Maybelline vs Sacheu）+ 用法 FAQ | 品牌广告强；靠评测长尾 | **中高** |
| 17 | steel tongue drum | Exploding Topics · +2400% | 乐器兴趣词；可做选购指南 | Tapadum、Hangdrum.fr、Sonodrum、Wiki；**可切入音阶选择器** | `steeltunguedrum.com`、`steeltunguedrums.com`、`tonguedrumguide.com`：**NXDOMAIN** | 音阶推荐小工具 + 尺寸选购指南 | 竞品有指南站；工具差异化 | **中高** |
| 18 | chicken shredder / banana matcha latte（内容或联盟） | Exploding Topics · +957% / +7500% | 厨房小工具 & 饮品趋势 | Chicken：Serious Eats + 弱博客 + Amazon；Banana matcha：食谱博客为主 | `bestchickenshredder.com`、`bananamatechalatte.com`、`bananabreadlatte.com`：**NXDOMAIN**；`chickenshredder.com` 仅 NS（疑似停放） | 联盟评测 **或** 食谱落地页（当天） | 厨房词竞争亚马逊；饮品词寿命看趋势 | **中高** |

---

## 明确淘汰（本回合看过但未入选）

| 词 | 原因 |
|---|---|
| secret santa generator | 首页已有 SecretSantaMatch、WishApp、开源静态页；精确 `.com` 多被占 |
| south park oc maker | 官方 Avatar Creator + AI 站；版权风险高 |
| qrcode generator | `qrcodegenerator.com` 已被占；巨头/老站多 |
| free ai video generator / sora 2 / heygen / krea / perchance | 品牌或精确域已被占；算力成本高，难当天 MVP 差异化 |
| ACS citation（精确 acscitationgenerator.com） | 已被 twincite 占用 |
| water bottle charms / pupsicle / carsized | 品牌垄断 SERP |
| NBA / 体育赛程 Trends | 窗口按场次死亡，不符工具站 |

---

## 建议执行顺序（当天可上）

1. 注册 Top5 里仍 NXDOMAIN 的 `.com`（先 DoH 再去注册商二次确认）。  
2. 优先上线：**发票生成器** 或 **power bank with fan 评测壳** 或 **nano banana 2.1 新词页**（看你更熟工具还是联盟/内容）。  
3. GSC + 索引；两周看曝光再加内页（横向拓展）。  
4. Deadlock / Christmas 仅在你能「追 patch / 追季节」时再做。

---

## 证据与局限

- Trends 原始：`/workspace/new-web-cafe-archive/notes/trends-rising-raw.md`  
- 找需求方法：`how-to-find-demand.md`  
- 域名：**仅 Cloudflare DoH**；NXDOMAIN ≠ 注册商保证可买（可能premium/保留）。  
- 未使用 Similarweb / Ahrefs KD（社群说 KD 可后置）；未登录 Google Ads 规划师洗量。  
- Exploding Topics 增长率为其站点口径（多年累计），与 Trends 30 天 Rising 不同尺度，表中已标注来源。

*生成时间：2026-11-05 约 02:30 America/New_York*
