# S-060：三项经营工具的Semrush前置采集

2026-09-13约22:58–23:06（Asia/Shanghai）；Chrome原生UI、用户已授权，Semrush代理 https://zh.semrush.fast.wmxpro.com/ 。浏览器扩展接口一次超时、一次列表失败；原生Chrome成功。无登录阻塞。

## 原始导出

| 文件 | UI/CSV口径 | 范围 |
| --- | --- | --- |
| stockie-overview-trend.csv | stockie.app / root domain / Worldwide，UI桌面 | 2025-09-13至2026-09-13 |
| catalogly-overview-trend.csv | cataloglyapp.com / root domain / Worldwide，UI桌面 | 同上 |
| gmcinspector-overview-trend.csv | gmcinspector.com / root domain / Worldwide，UI桌面 | 同上 |
| seed-keywords-us.csv | Keyword Overview Bulk，美国，2026-09月，3个seed | 搜索量有值，KD/intent/SERP字段缺 |

原文件分别为overview-trend-2026-09-13T14_58_41Z.csv、15_00_19Z.csv、15_01_20Z.csv，以及shopify-catalog-maker_bulk_us_2026-09-13_23-02-41.csv；通过UI下载，从Downloads原样复制，非生成模拟数据。

## 读到的有限数据

三站上述一年CSV的Organic Traffic所有日期为0（工具估算，不是实际访问为0）；截至09-13自然词数分别11、7、1。Stockie同期2026-06-13 Paid Traffic估算552，09-13为0，不解释为已证实停投或广告效果。

概览UI顶层为全世界，部分跳转链接继承NO库，故域名数值以导出中的Worldwide为依据，不将NO下方主题当全世界/美国关键词。无需从零流量推无客户：Shopify App Store路径的分发和搜索不包含在独立官网根域。

美国seed导出：stocky alternative量0、shopify catalog maker量20、google merchant center audit量10；三者KD和intent为空，不能写成KD=0/容易排名。CPC是广告估算，不是我们获客成本。

后补单词页：https://zh.semrush.fast.wmxpro.com/analytics/keywordoverview/?q=stocky%20alternatives&db=us ：标题/国家/桌面/2026-09-13已核对，量10、全球40、KD与intent不可用；变化摘要shopify stocky alternative量20。未打开Keyword Magic或固定SERP，因此不把摘要当完整词池。

六变体批量查询出现输入与提交不一致，曾提交非业务文字“在寻找3~5个商机”；未导出/采信该批。setValue也未驱动批量模型，改用地址栏单词页恢复有效查询。其余五变体未完成。

## 充分性

域名趋势ready（仅能描述三站估算）；关键词partial-ready；主要页面/页面词、Keyword Magic、固定美国SERP及转化归因missing。没有据此形成SEO机会/天花板/自然获客结论。此轮商业候选依据S-059购买与迁移事实独立比较，未启动注册、安装或产品实测。未采的SEO细节保留作后续可进入性门槛，不宣称完成流量验证。
