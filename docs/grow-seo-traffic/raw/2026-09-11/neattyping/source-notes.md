# NeatTyping 后台采集说明

- 采集日期：2026-09-11，Asia/Shanghai。
- 获取方式：用户授权的已登录 Chrome 后台只读浏览、CSV 下载。原始 CSV 保持下载内容，计算结果在 reports 单独保存。
- 站点：neattyping.com；Statcounter 13221620；GA4 553114644；GSC 域资源 sc-domain:neattyping.com。

## GA4 原始导出与网页摘录

- [来源/媒介 CSV](ga4/traffic-acquisition-source-medium.csv)：33 行，日期注释 20260814—20260910，所有用户。CSV 不含网页总计行。
- [国家/地区 CSV](ga4/demographics-country.csv)：103 行，与来源同周期。指标是活跃用户，不能与 Sessions 或 GSC 点击混用。
- [流量获取报告](https://analytics.google.com/analytics/web/#/a252704894p553114644/reports/explorer?params=_r.explorerCard..selmet%3D%5B%22sessions%22%5D%26_r.explorerCard..seldim%3D%5B%22sessionSourceMedium%22%5D&r=lifecycle-traffic-acquisition-v2)。
- 网页总计摘录：5,486 次会话、2,724 次感兴趣的会话、4,527 名活跃用户。主要使用完整数据提示可见。
- 网页来源头部：直接访问 1,992；bing / organic 1,650；(not set) 1,254；(data not available) 779；yahoo / organic 160；cn.bing.com / referral 153；google / organic 142。均与 CSV 对应行一致。
- 日期选择虽是 28 天，但图表可见非零记录只集中在末端几天。首页过去 7 天与此 28 天报告的活跃用户总数同为 4,527。未核查 GA4 安装日期，不能把图上的零值解释为历史实际没有访问。
- 来源行 Sessions 合计为 6,541，高于网页总计 5,486。按网页渠道分组摘录也无法加总至总计：Organic Search 2,327；Direct 1,992；Unassigned 1,300；Cross-network 779；Organic Social 75；AI Assistant 14；Referral 2。此次保留差异，没有修改 GA4 配置或确定差异原因。
- 国家活跃用户各行合计 4,537，网页总计 4,527。分析不将国家行作为互斥用户集合，只引用各国家原始值及网页展示的比例，不将各行相加作新总计。
- 本次仅分析流量，CSV 内的关键事件不视为购买，不用收入列判断实际经营收入。

## GSC 原始导出

- [效果报告](https://search.google.com/search-console/performance/search-analytics?resource_id=sc-domain%3Aneattyping.com)。筛选为网络搜索、全球、全部设备，无查询或页面过滤。采集时显示约 6 小时前更新。
- [近 3 个月原始 ZIP](gsc-3months/original.zip)及同目录解压 CSV：2026-06-09—09-08，共 92 个连续日期。网页总计 789 点击、5,212 展示、15.1% CTR、平均排名 61.4。
- [最近 28 天原始 ZIP](gsc-28days/original.zip)及同目录解压 CSV：2026-08-12—09-08，共 28 天。网页总计 573 点击、1,294 展示、44.3% CTR、平均排名 36.4。
- 两个 ZIP 均包含图表、查询数、网页、国家/地区、设备、搜索结果呈现、过滤器。近 3 个月查询导出 904 行，最近 28 天查询 207 行、页面 43 行、国家 60 行。
- 28 天独立导出的每日记录与 3 个月导出最后 28 行完全相同。每日求和与网页点击、展示总计完全一致。
- 最近 28 天查询可见行只合计 477 点击，低于属性总计 573。没有把差额 96 点击归类为非品牌，也没有通过页面维度加总还原属性总量。

## Statcounter 获取边界

- [来源报告](https://statcounter.com/p13221620/traffic-sources/)显示 BASIC 与 Entire Log (2 hours)，不能作为整月来源样本。此项目无 MCP 统计访问权限，已使用网页替代。
- 有机搜索详情页面未完成图表加载。可访问性树含不合理的数字，截图仍显示加载状态，因此详情数字没有用于报告，也没有当成真实搜索引擎份额。
- 本次来源排序使用已成功下载的 GA4 CSV；长期 Google 趋势使用 GSC 原始 CSV。

## 计算口径

- 28 天：2026-08-12—09-08，对比 2026-07-15—08-11。
- 7 天：2026-09-02—09-08，对比 2026-08-26—09-01。
- 点击、展示按日求和；CTR = 总点击 / 总展示；环比 = 本期 / 前期 − 1。
- 周是以 GSC 最新日期向前切分的连续 7 天区间，不等同于自然周。
- 平均排名近似值按每日展示加权，由已四舍五入的每日排名计算，标记为 approximate。此值还会随查询、国家、页面构成改变，不能解释为同一关键词排名变化。
- Google 品牌词仅精确匹配 `neattyping`、`neat typing`、`neattyping.com`。三项合计 477，占属性总点击 573 的 83.25%；这是可确认的下限。

分析见 [来源与趋势报告](../../../reports/2026-09-11-neattyping-sources-google-trend.md)，派生数值见 [metrics.json](../../../reports/2026-09-11-neattyping-metrics.json)。
