# S-059：从购买与迁移证据寻找三项经营工具

采集：2026-09-13。范围：公开网页正文与检索结果的人工摘要，非完整榜单、商店评论导出或支付后台审计。先复用44候选去重，新增任务另见D-045/046/047。没有登录店铺、安装App、联系商家或付费。

## A. 采购单与收货：Stocky迁移

1. https://help.shopify.com/en/manual/products/inventory/transitioning-from-stocky ：当前官方正文确认Stocky自2026-08-31不能用于库存管理，之后至少90天可只读导出。旧采购单不会自动进入Shopify；历史状态/已收数量/供应商关系不能用原生采购单CSV导入，该CSV仅添加新草稿的商品行；供应商不能导出；Stocky API已停止。此前旧路径保留未来时态，采用此当前路径。
2. https://help.shopify.com/en/manual/migrating-to-shopify/migrating-retail ：原生Shopify已有采购单、库存、Flow低库存提醒等。不能将Stocky停用写成Shopify不提供采购单。
3. https://apps.shopify.com/stockie ：2026-09-13页面4.9/148评价；2021-07-19上架，Plutonian开发，官网https://www.stockie.app/。Basic4.99、Advanced9.99、Pro29.99、Pro Plus59.99美元/月，14天试用；采购单/收货/库存调整/PDF与CSV在Pro Plus。评价数不等于付费人数或收入。
4. https://apps.shopify.com/reviews/2285362 ：Woolyn，2026-07-15，称需要采购单而非预测，采购单只在最高档，觉得贵；使用4天，可能仍在试用，不能证明已扣款。开发者承认收到类似套餐反馈，未承诺改价。
5. https://apps.shopify.com/stockie/reviews ：读取第一页10条（2026-08-16至09-11），不是148条全部。DIANE'S BIKINIS使用4个月、称尝试多个替代；Mix It Up Home & Gift使用5个月，将采购、收货、条码列为日常用途；lovethatleaf称使用包含下单的高档方案、管理300–400产品（14天，不能认定已过试用）；近期5天/4天评论只计迁移试用。多条强调人工迁移与支持，属于进入成本的反证。未取得确切付款金额或MRR。
6. https://stockie.helpscoutdocs.com/article/135-how-purchase-orders-update-shopify-inventory ：官方说明Ordered、Receive、Edit、Close、Reopen等影响incoming/available数量，说明完整产品包含状态一致性，不是生成一张PDF。

## B. 批发商品目录：Catalogly / EasyCatalog

1. https://apps.shopify.com/catalogly ：当前4.5/43评价，2023-02-27上架，dApplication开发，官网https://cataloglyapp.com/。Pro9.99、Advanced19.99、Unlimited49.99美元/月；免费2目录/每份5页。产品数据→目录/批发清单/PDF或flipbook、价格覆写/CSV、刷新数据。厂商描述，未测分页/更新可靠性。
2. https://apps.shopify.com/catalogly/reviews?page=3 ：商家DS Custom Tackle于2025-11-06称节省时间、销售团队满意且值得付费档价格；没有提供金额/票据。首轮检索在其他locale同一评论出现，按同一条去重。LightBaba的免费档字体支持不计付款；2026-08-26 My Mom And Me使用约一年，反映持续使用但不证明确切套餐。
3. https://apps.shopify.com/easy-catalogs?locale=zh-CN&surface_detail=store-design-images-and-media-image-gallery&surface_inter_position=1&surface_intra_position=17&surface_type=category&surface_version=redesign ：检索正文显示2026-03-25评论自述支付年费179.99美元，同时抱怨作品保存/支持问题；此条未取得完整署名，不作我们已复现bug或普遍现象。2026-04-07 Pandr称商用目录促进业务，未审计增收数字。
4. https://apps.shopify.com/easy-catalogs/reviews?page=8&ratings%5B%5D=5 ：旧购买和长期使用补充，只看筛选五星页，存在选择偏差；不据此推总体满意度。
5. https://www.catalogmachine.com/resources/solutions/online-catalog-maker ：另一公开供给，CSV/Shopify数据、分层价格、批发下单；用途参照，未新增收入核验。

## C. Merchant Center商店/商品数据检查

1. https://trustmrr.com/startup/hidden-business-8 ：本轮正文MRR11,748美元、190活跃订阅、累计106,490美元；显示LemonSqueezy API验证，更新时间2026-09-11 08:52 AM（时区未示）。描述为扫描Shopify商店的GMC问题，标记2025年3月创立。页面匿名，没有公开域名、客户/套餐结构；不能把此收入归给任何下面的产品。创始人声称单一渠道，标签有Affiliate/Influencers/Partnerships，均无归因后台，不认定当前利润或纯自助程度。
2. https://www.gmcinspector.com/ ：公开标价19.99美元/报告、250美元/30天无限扫描；宣传扫描和修复建议。案例是厂商自选、未独立验证。既不是上述匿名产品的确认身份，也没有真实收入核验。
3. https://www.gmcauditpro.com/ ：30美元单次、75美元3次，宣传浏览器扫描、导出/申诉；不采信“完全如Googlebot扫描”“Google缓存比较”等为已实现技术或效果。
4. https://apps.shopify.com/shieldkit?surface_detail=store-management-security-security-other&surface_inter_position=1&surface_intra_position=22&surface_type=category&surface_version=redesign ：当前2评价/3.5分，29美元/月。Western Grace Collective于2026-07-08反馈付款图标误报、修复指引不匹配；开发者07-09称已改进，未复测。另一用户只是考虑升级，不能计已付费。此处用途是验证误报/支持风险，不是收入佐证。
5. https://support.google.com/merchants/answer/14999713?hl=en ：官方已有价格/库存自动更新，仍需定期提交数据；不能把简单比对当平台空白。
6. https://support.google.com/merchants/answer/15072729?hl=en ：官方给出Needs attention下载受影响产品CSV、比对商品数据与微数据的处理路径。证明有可导出的输入，不证明能解决所有封禁原因。

## 未入选、排除和工具限制

- 提醒工具：TrustMRR的Notifier旧快照MRR200美元/7订阅；不足以用小额样本支持此轮前三，Apptoto找到的客户案例金额属于客户公司，不当Apptoto收入。
- 赞助合作管理： https://trustmrr.com/startup/partners 数据缺失且API过期，不从“在售”推付费。
- AI广告报表： https://trustmrr.com/startup/autoady 正文称演示用户免费、尚无付费客户，且出现累计300美元口径冲突；排除作为购买证据。
- 发票小工具Faktur及通用提醒NudgeBell目前检索到极少销售，不凑入名单。它们不是被证明不能盈利。
- 无关目录、医疗提醒、旧D-026反馈工具搜索结果不新增候选，不重启旧方向。
- Stripe Directory精确命令：`stripe directory search 'inventory replenishment' --format json`，无过滤。首次受本地配置chmod权限限制，获工具提升权限后返回Unknown command directory。没有目录结果，没有安装/升级CLI或购买。其余发现来自上列网页。

研究检索采用词组组合（部分）：TrustMRR inventory/purchase order、agency reporting、reminders、Shopify wholesale；Stockie Shopify reviews purchase orders；Catalog Machine paid catalog；Shopify catalog worth/paid；GMC scanner pricing。普通检索排序不当美国固定SERP，细分来源事实与分析见报告。各页面只覆盖上述范围。

## 完成前复核补充

同日再次打开上述Shopify当前迁移文档、Catalogly商店和匿名TrustMRR页面。Shopify明确已有Sidekick补货建议和采购单草稿；采购单API尚未普遍开放，新的读取接口为developer preview。官方建议外部系统自己保存采购单，通过Transfers API的blank-origin transfer衔接收货。这个限制降低D-045的进入吸引力：不可承诺完整原生采购单双向同步，不将AI补货作为空白。
