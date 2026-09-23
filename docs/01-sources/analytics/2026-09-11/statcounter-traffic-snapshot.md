# 自有项目 Statcounter 流量快照（2026-09-11）

来源 ID：S-026。采集时间约 2026-09-11 09:39 UTC（北京时间 17:39）。
来源：[Statcounter 已登录项目页](https://statcounter.com/)；[MCP 服务说明](https://api.statcounter.com/docs/mcp)。
范围：当前账号返回的 52 个项目，全项目后台表的 Sessions；FFHub 另有 7 天 MCP 汇总。此资料不改变新项目候选状态、停止方向或投入优先级。

## 数据来源与口径

- [MCP 项目清单](statcounter-projects-mcp.json)：保存服务返回的原始 JSON 文本，52 项；项目 URL、分组、时区、API 权限和最后记录时间来自 MCP。未返回截断或分页提示。
- [后台表摘录](statcounter-dashboard-extract.json)：读取原生 Chrome 中已登录项目页的可访问性文本，结构化整理今日、昨日、本月和历史累计四列。不是原始 CSV 导出，不包含逐日明细。
- [FFHub 7 天汇总](statcounter-ffhub-2026-09-04-to-10-mcp.json)：MCP 原始 JSON，2026-09-04 至 09-10，共 292 次会话、262 位去重访客、369 次浏览。
- 后台显示的比较指标为 Sessions（会话数），同一人可以产生多次会话。不将其直接写成独立访客 UV。所有项目返回时区均为 Asia/Hong_Kong。
- “昨天”为 2026-09-10；“本月”为 2026-09-01 至采集时刻，包含尚未结束的 09-11。今天的部分数据不用于与完整昨天直接判断升降。
- 初始计划比较最近 7 天。MCP 清单中仅 FFHub 的 api_access 为 true，其余 51 项为 false，故全项目比较改用网页已提供的本月累计和昨天；没有取得 52 项的完整 7 天排名，也未比较各站 PV 或去重访客。
- 本次完成数据读取，没有调用写入 Statcounter 的操作。账户中的项目可能包括历史站点，列表存在不等于仍在运营。

## 读取结果

52 项本月会话数合计 **48,632**，昨天合计 **4,368**。前三项本月合计 33,955，占 69.8%。

| 本月排名 | 项目 | 本月累计 Sessions | 昨天 Sessions |
| --- | --- | ---: | ---: |
| 1 | www.neattyping.com | 16,921 | 1,720 |
| 2 | myfemboyroommate.net | 11,151 | 655 |
| 3 | vocaldock.com | 5,883 | 576 |
| 4 | emojizoo.com | 2,775 | 211 |
| 5 | yaytext.app | 2,515 | 252 |
| 6 | freesubwaysurfers.com | 1,794 | 224 |
| 7 | onlymp3 | 1,639 | 131 |
| 8 | slickcalc.com | 1,245 | 118 |
| 9 | subwaysurfersunblocked.org | 982 | 161 |
| 10 | cursedtext.org | 832 | 56 |
| 11 | y2mate.ltd | 559 | 58 |
| 12 | neatsignature.com | 462 | 59 |
| 13 | ffhub | 436 | 22 |
| 14 | songtokaraoke.com | 370 | 28 |
| 15 | sprunkiinfected.org | 218 | 26 |
| 16 | invoiceneat.com | 218 | 20 |
| 17 | glitchtext.org | 137 | 8 |
| 18 | puzzlebento-com | 73 | 7 |
| 19 | hentaink.com | 69 | 7 |
| 20 | sprunkidash.net | 64 | 4 |
| 21 | twittervideodownloader.tools | 64 | 5 |
| 22 | escaperoad.world | 42 | 5 |
| 23 | letteravatar.com | 36 | 0 |
| 24 | temppic.sinancode.com | 29 | 2 |
| 25 | block-blast.best | 26 | 3 |
| 26 | fivenightsatscratch.com | 16 | 3 |
| 27 | sprunkimustard.net | 15 | 2 |
| 28 | chromakopiafontgenerator.org | 15 | 0 |
| 29 | fastfoodsimulator.app | 13 | 0 |
| 30 | superfishing.org | 10 | 1 |
| 31 | webfishing.app | 7 | 1 |
| 32 | sprunkincredibox.com | 5 | 1 |
| 33 | sinancode.com | 5 | 0 |
| 34 | sprunkr.xyz | 4 | 1 |
| 35 | neatheadshot.com | 1 | 1 |
| 36 | TikTomato.com | 1 | 0 |
| 37 | abgerny.pro | 0 | 0 |
| 38 | colorboxmustard.best | 0 | 0 |
| 39 | freemahjongtitans.com | 0 | 0 |
| 40 | misidegame.org | 0 | 0 |
| 41 | misideworld.com | 0 | 0 |
| 42 | suika-game.online | 0 | 0 |
| 43 | free.neatheadshot.com | 0 | 0 |
| 44 | 2048-cupcakes-5dn.pages.dev | 0 | 0 |
| 45 | markup-1nj.pages.dev | 0 | 0 |
| 46 | svg-preview.pages.dev | 0 | 0 |
| 47 | bmwlogo.fans | 0 | 0 |
| 48 | ad | 0 | 0 |
| 49 | flvto.net | 0 | 0 |
| 50 | pinterestvideodownloader.ltd | 0 | 0 |
| 51 | redditsave.xyz | 0 | 0 |
| 52 | ssstiktok.page | 0 | 0 |

## 分析与限制

- NeatTyping 在当前账号这 52 个项目中，本月累计和昨天的会话数均最多；myfemboyroommate.net、VocalDock 在两种窗口下均排第二、第三。
- EmojiZoo 与 YayText 为本月第四、第五，两者昨天分别 211、252 次会话；本月排序与单日排序不完全相同。
- SlickCalc 本月第八，昨天 118 次会话。此前用户自述每日约 200–300 的具体指标和周期未知，不能据此直接声称流量下降。
- TikTomato 在这个 Statcounter 项目中本月仅记录 1 次会话，最后 pageview 字段为 2026-09-03。统计接入是否覆盖改版后的站点尚未检查，不能据此断言真实流量为零或产品停止。
- 当前返回清单未找到 Sonelune；不代表该站没有流量。
- 没有读取收入、转化、成本或来源渠道，所以这只是流量体量比较，不能据此判断盈利能力、增长原因或投入回报。

本次没有新的经营决策；来源与进度已同步，候选状态保持原有决定。

