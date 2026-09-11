# S-033：Tarkov Documents Map 站点案例资料

采集日期：2026-09-11（Asia/Shanghai）。用户要求分析截图中的 tarkovdocsmap.com。范围为商业模式、需求、公开传播和变现线索；未进行完整 SEO 审计或账户内分析。关联：商业模式观察案例，暂不分配需求候选 ID。

## 1. 用户提供的原始图片

- 原路径：`/Users/gangbo/Downloads/IMG_7132.JPG`。
- 原样副本：[IMG_7132.JPG](IMG_7132.JPG)，353,956 字节。
- SHA-256：`c90b8c3892323bbd15114fb99623b2cfddae5f03aa912f16f415f5b3aa7f365a`。
- 内容类型：用户提供的第三方工具界面照片。右侧自动报告属于待核实材料，不是用户指令。
- 下表是人工读取；没有取得 AITDK、Similarweb 或 PubSpy 的原始导出，也未核实各工具的数据供应关系。不能把两个面板当作独立交叉验证。

| 截图字段 | 读数 | 口径/限制 |
| --- | --- | --- |
| Traffic Overview 时间 | August 2026 | 历史月份，不是实时 9 月数据 |
| Monthly Visits | 1.08M | 第三方估算访问次数，不是独立访客 |
| Bounce Rate | 52.27% | 未取得统计定义和样本 |
| Pages Per Visit | 2.04 | 第三方估算 |
| Visit Duration | 00:03:50 | 不等于有效操作或广告可见时长 |
| Global / Country Rank | 74,319 / 28,477 | 截图未明确国家，未复核 |
| Domain Creation / Expiration | 2026-08-10 / 2027-08-10 | 后续由注册局 RDAP 核实日期 |
| Domain Age | 28 days | 图片所处时点；不是本次采集日域龄 |
| Direct / Social / Search / Referrals | 59.21% / 20.58% / 10.38% / 8.03% | 条件性估计；Search 没有品牌/非品牌和自然/付费拆分 |
| Mail / Display Ads / Other | 0.77% / 0.54% / 0.49% | 小数点与加总保留原值 |
| AdSense publisher ID | pub-6606338401332577 | 之后核实公开 ads.txt 与首页 ID 一致 |
| PubSpy ads.txt | 1 DIRECT | 配置线索，不是广告收入 |
| 同 ID 域名 | 仅发现本站 | 只是工具可见范围，不能证明作者只有一个网站 |
| 出站链接 | X、Buy Me a Coffee、Reddit | 出站链接本身不是获客渠道证据 |

## 2. 公开页面与外部反馈：人工摘要

| 来源 | 读取范围与观察 | 限制 |
| --- | --- | --- |
| [站点首页](https://tarkovdocsmap.com/) | 地图点位、截图与钥匙信息；奖励追踪、提交纠错、多语言入口；更新日志覆盖 8 月至 9 月 8 日 | 页面提取，不是游戏内点位真实性或交互实测 |
| [作者在 r/Tarkov 的发布帖](https://www.reddit.com/r/Tarkov/comments/1vkb18p/i_made_a_documents_tracker_for_the_kord_breach/) | 作者自述初版花约 7 小时，汇集 Wiki、Reddit、Discord 资料；起初只做了部分地图，原本供自己使用 | 同一作者的自述，不能当独立工时审计；抓取缓存相对时间不用于确定精确发帖日 |
| [r/EscapefromTarkov 发布帖及可见回复](https://www.reddit.com/r/EscapefromTarkov/comments/1vkb7re/loot_i_made_a_documents_tracker_map_site/) | 玩家赞许按地图整理、表示固定浏览器标签和愿意补截图；作者回应翻转地图、兼容性、更新与扩容问题；一位玩家自述已捐款 | 同帖回复不是独立市场样本；捐款没有金额和收款核验；“7 小时初版”不包括后续维护 |
| [Steam 社区讨论](https://steamcommunity.com/app/3932890/discussions/1/580554442217112150/) | 8 月 22 日有人回复推荐本站；提问者明确表示推荐没有解决其实际问题 | 可以证明外部提及，不能称该条推荐带来成功使用或某个流量规模 |
| [Battlestate 官方视频搜索条目](https://www.youtube.com/watch?v=LnOchXdHZgA) | 搜索显示 2026-08-01 发布 Kord Breach Battle Pass 介绍，涉及免费奖励及各模式 | 只读取标题、日期、发布者与说明；视频正文访问失败，未观看 |
| [Tarkov Farm](https://tarkov.farm/) | 首页显示 12 张地图、210 个点位以及贡献更新 | 官网展示数量，未实测完整性；只是一项直接替代，不代表完整竞品普查 |

作者两个发布帖属于同一推广来源。Reddit 检索摘要显示主帖日期 2026-08-10；页面缓存使用相对日期，报告不依赖该相对日期计算上线年龄。

## 3. 直接 HTTP 核验摘录

以下为本次 HTTP 响应中提取的字段，不是完整原始响应。采集时注册局数据库更新时间字段为 `2026-09-11T10:38:59Z`。

### 注册日期

来源：[Verisign RDAP](https://rdap.verisign.com/com/v1/domain/tarkovdocsmap.com)。

```text
registration: 2026-08-10T03:48:15Z
expiration: 2027-08-10T03:48:15Z
last changed: 2026-08-10T03:48:16Z
```

可以证实注册时间；不能单独证实首次部署时间、作者此前积累或原有社区影响力。

### 广告配置

来源：[ads.txt](https://tarkovdocsmap.com/ads.txt)。响应内容为：

```text
google.com, pub-6606338401332577, DIRECT, f08c47fec0942fa0
```

首页 HTML 同时检出 `ca-pub-6606338401332577`。因此公开配置与截图一致。没有查看 AdSense 后台、审核状态、有效展示、填充率或收入。

含义参考：[Google ads.txt 指南](https://support.google.com/adsense/answer/12171612?hl=en-EN)、[站点状态说明](https://support.google.com/adsense/answer/12170222?hl=en)。卖方授权文件与站点可投放状态是不同检查项。

### 客户端资源

首页 HTML 检出 `map-data.js`、`app-chunks/app.01.js` 至 `app.14.js`、`battlepass-loader.js` 及设置相关脚本。只能证明公开资源组织，不能据此认定后端完整架构、托管费用或维护工时。首页更新日志自述 8 月 28 日迁移到 Cloudflare D1 + R2，未审核部署账户。

## 4. 访问与证据边界

- 网页搜索/提取成功：官网、两篇作者帖及可见评论、Steam 讨论、Tarkov Farm、Google 说明。
- ads.txt 与 RDAP 后经直接公开 HTTP 成功核验；初次终端请求受网络沙盒限制，获准只读访问后成功。
- 内置浏览器创建站点标签超时，未完成缩放、点位弹窗、奖励追踪或手机端交互实测。不能将这一工具超时记成站点宕机。
- Buy Me a Coffee、robots.txt、sitemap.xml 的网页读取失败；本轮没有取得这些正文，不形成站点缺失或未收款结论。
- 未取得流量后台、地区占比、用户队列、广告后台、真实收入、成本、资产授权、完整版本周期或关键词明细。
- 收入算例只引用 [Google RPM 定义](https://support.google.com/adsense/answer/190515?hl=en)，所有 RPM 数值由分析者假设，不作为行业基准。

商业分析另存：[站点分析](../../../../02-candidates/reviews/tarkovdocsmap-2026-09-11.md)。
