# 已核实多语种外链总记录库（2026-11-23）

面向已上线的小工具站和网页解谜合集，整理 **2026-11-23 已打开官方页（或官方帮助页）并补查 HTTP + 域名创建时间** 的外链渠道。核验时区为 America/New_York。

适用站点：

- [puzzlebento.com](https://puzzlebento.com/)：免费浏览器解谜／益智合集（含日语等语言版本）
- [chartseat.com](https://chartseat.com/)：座位表工具
- [onlinepollmaker.com](https://onlinepollmaker.com/)：在线投票工具
- [invoiceneat.com](https://invoiceneat.com/)：发票生成器
- [tiktomato.com](https://tiktomato.com/)

总库只放核实过的记录。付费站、未能确认免费的站、2024 年及之后注册的新域名、审核过严或死站，以及 Reddit，都不进入提交表。完整名录在 [site-pool.csv](site-pool.csv)，已排除项在 [excluded-log.md](excluded-log.md)。

## 总库统计（去重后 360 站）

| 状态 | 数量 |
| --- | ---: |
| 推荐-免费可用 | 87 |
| 可用-有门槛 | 215 |
| 排除-新域名/低流量 | 20 |
| 排除-付费 | 17 |
| 排除-审核过严 | 10 |
| 排除-垃圾站/死站 | 11 |
| **合计** | **360** |

| 语区 | 数量 |
| --- | ---: |
| EN / US-Global | 141 |
| EN / UK | 3 |
| EN / AU | 7 |
| EN / NZ | 2 |
| EN / IE | 1 |
| EN / SG | 1 |
| JA / 日本 | 56 |
| ZH-TW / 台湾 | 25 |
| ZH-HK / 香港 | 5 |
| FR / 法语区 | 18 |
| DE / 德语区 | 18 |
| ES / 西班牙语区 | 16 |
| IT / 意大利语区 | 14 |
| NL / 荷兰语区 | 10 |
| SV / 瑞典 | 7 |
| DA / 丹麦 | 1 |
| NO / 挪威 | 5 |
| FI / 芬兰 | 2 |
| PT / 葡萄牙 | 2 |
| KO / 韩国 | 26 |

可用合计 302 条（推荐 87 + 有门槛 215）；排除 58 条。本库未混入简体中文站，也未纳入 Reddit 作为可提交渠道。第 3 批在 219 站基础上新增 141 站，重点补西/意/荷/北欧、澳新爱新以及更多英语垂直社区与日韩补充。

**补查原免费目录的域名年份后，有 7 个曾出现在可提交清单里的渠道被降级为「排除-新域名/低流量」：** Puzzle Hub（tappypotato.com，2026-08-28）、Foundplay（foundplay.io，2026-10-04）、IgnLab GameHub（ignlab.net，2024-08-22）、I Love Web Games（ilovewebgames.com，2026-10-19）、SlowDen（slowden.com，2026-06-15）、All Daily Puzzles（alldailypuzzles.com，2026-11-13）、Best Digital Launch（bestdigitallaunch.com，2026-09-21）。它们的提交页多数仍在且声称免费，但按规则暂不优先投放，详见 [excluded-log.md](excluded-log.md) 和 [free-directories.md](free-directories.md)。第 3 批又将 Underskog（underskog.no，2025-04-15）按同一规则排除。

## 文档导航

| 文档 | 用途 |
| --- | --- |
| [site-pool.csv](site-pool.csv) | 去重后的完整总记录库（UTF-8 CSV），可用 GitHub 搜索或本地表格筛选 |
| [excluded-log.md](excluded-log.md) | 已排除站点避坑表（新域名、付费、审核过严、死站） |
| [free-directories.md](free-directories.md) | 仍保留的英语免费目录、内容页与开源导航（已同步新域名降级） |
| [en-forums-social.md](en-forums-social.md) | 英语区论坛、社媒、博客与垂直社区（含澳新爱新，仅推荐 / 有门槛） |
| [ja-tw-channels.md](ja-tw-channels.md) | 日语区 + 台湾／香港繁体渠道，突出 PuzzleBento 日语版 |
| [fr-de-ko-channels.md](fr-de-ko-channels.md) | 法语、德语、韩语区渠道，突出海外无需实名即可注册的优先项 |
| [es-it-nl-nordic-channels.md](es-it-nl-nordic-channels.md) | 西语、意大利、荷兰、北欧与葡萄牙语区渠道（第 3 批新语区） |
| [puzzlebento-competitors.md](puzzlebento-competitors.md) | PuzzleBento 的 12 个小型独立竞品，以及反查出的可复用渠道（部分平台已因新域名降级） |
| [submission-tracker.md](submission-tracker.md) | 五站点 × 高优渠道的勾选进度表 |

历史参考（2026-09-04 社区榜单，**费用与链接属性当时未经目标站独立核验**，且含大量 AI 导航，不能当成本目录的提交清单）：

- [外链渠道整理](../operations/web-cafe-backlinks-sync-2026-09-04.md)
- [601 条外链目录](../operations/web-cafe-backlinks-catalog-2026-09-04.md)

## 建议的冷启动顺序

不要一天把所有渠道交完。同一套产品说明可以复用，但短描述按站点改写，锚文本用品牌名或自然短语，不要全部精确匹配关键词。**先看域名年龄和状态标签，再动手。**

**第 1 周：先交老域名免费目录和资料页，每天 2–4 个。**

1. 准备素材：一句 tagline、80–150 词介绍、3–6 张截图、正方形 logo、产品域名邮箱。五个站各一份。需要多语种投放时，另准备日语／繁体／法语／德语／韩语，以及西语／意大利语／荷兰语／北欧语言短介绍。
2. GitHub Profile／README（若有仓库），以及 Crunchbase 公司资料（先搜索再创建；同一主体只需一个公司页）。也可同步做 GitLab Profile 与 Xing 资料页。
3. 仍保留的通用目录（均为 2023 年以前注册）：SaaSHub 验证、AlternativeTo（挂到真实竞品的 Alternatives）、Launching Next、PeerPush 免费排队、Uneed 免费排队（接受约 50 天等待）、Startup Stash 免费申请、SideProjectors 展示页。
4. Fazier：先读清免费档是否要徽章或回链，再提交。
5. 注册 Product Hunt 和 Peerlist 个人账号，把产品页填完整，**不要订在同一天发布**。Peerlist 放在某个周一；Product Hunt 选能整天回评论的日子。
6. 英语社媒保底：YouTube 频道简介、Bluesky、Mastodon（mastodon.social）、Tumblr、LinkedIn、X；可补 Facebook 主页、Neocities／Dreamwidth 介绍页。
7. **仅 PuzzleBento：** 优先在 itch.io、Game Jolt 托管或放可玩版本；HTML5 Game Devs Forum 的 Showcase 发试玩。第 3 批可再交 indiexpo、Lexaloffle、Ludum Dare、CodePen／OpenProcessing。不要再把 Puzzle Hub、Foundplay、IgnLab GameHub、I Love Web Games、SlowDen、All Daily Puzzles 当作本周必交项（均为 2024+ 新域名，已降级）。

**第 2 周：内容和场景，而不是再堆目录。**

- Chartseat：Pinterest 婚礼桌位／教室排座图；可写一篇不用表格做婚礼座位表的说明。
- Online Poll Maker、InvoiceNeat：Indie Hackers、Dev.to／Hashnode、LinkedIn 讲具体工作流（如何做一场免登录投票、如何开第一张发票）；荷兰语区可去 Higherlevel 做相关讨论（有门槛，禁止硬广）。
- PuzzleBento：Show HN 只介绍一个可玩的点；可与 itch 页互相引。法语区可去 Prise2Tete、Forum Enigmes 做相关分享。
- 若第 1 周已把 Product Hunt／Peerlist 页面准备好，第 2 周再正式发布。不要在 HN 里叫人 upvote。

**有余力时再做多语种（先用推荐渠道，发对应语言）：**

- 日本：フリーゲーム夢現、PLiCy（游戏）；Qiita、Zenn、note、はてなブログ、ProtoPedia、Jugem（内容）。
- 台湾：iT邦幫忙、方格子 VOCUS、痞客邦 PIXNET、Matters、噗浪 Plurk。不要再走已关站的 Xuite。
- 法语：OverBlog、CanalBlog、Piaille、Mastodon.fr。
- 德语：MastodonDE、Xing；论坛类需德语讨论，见有门槛表。
- 韩语：先走 Velog（GitHub／Google 即可）、Disquiet、GeekNews Show、RocketPunch；不要先碰需要韩国手机实名的 Naver、Clien、Ppomppu、TheQoo、FMKorea。
- 意大利语：indiexpo（仅 PuzzleBento）、Altervista、Libero Blog、Mastodon.uno。
- 瑞典／葡萄牙：Blogg.se、SAPO。西语、荷兰、北欧大型论坛先读规则，默认当有门槛渠道。

## 避坑

- 不要一天向大量目录灌同一锚文本、同一篇简介。
- 先读规则再发。Show HN、Product Hunt、Peerlist 都禁止拉票或纯广告。Whirlpool、Flashback、OzBargain、ForoCoches 等大型论坛对商业链接很严。
- 「免费」常有隐形成本：排队、徽章、回链、域名邮箱验证、人工审核。不愿意在自己站点挂对方徽章，就不要走那个免费档。
- **2024 年及之后注册的域名不要当作优先外链渠道**，即使提交页写免费。完整名单见 [excluded-log.md](excluded-log.md)。
- 不要买假评论或假 upvote。不要发 Reddit 带链帖（按要求排除）。
- 这五个站不是 AI 产品，不必优先投 AI 工具导航。
- PuzzleBento 不要包装成全新原创玩法；没有每日机制就不要投 daily game 目录。
- itch.io／Game Jolt／indiexpo 是托管分发，和「外链回到 puzzlebento.com」不是一回事。若目标是推广官网，记得在资料页填写官网，而不是只把游戏留在平台内。
- 交完后在 [submission-tracker.md](submission-tracker.md) 打勾，并记下实际 listing URL。价格和规则会变，付款或挂徽章前再打开一次官方页。
- 本仓库不自动向外提交或发帖；执行仍由站点所有者完成。

公开搜索只能看到被索引的部分外链。若要对某个最像的竞品做深挖，可用该站的 Ahrefs 或 Semrush 反向链接 CSV，按「可提交、仍在线、非垃圾、非 Reddit、确认免费、域名不是 2024+」再洗一轮。方法见 [puzzlebento-competitors.md](puzzlebento-competitors.md)。
