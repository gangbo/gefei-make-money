# S-040：成熟导入工具的困难与现有能力

2026-09-12。公开网页人工摘录/翻译及官方说明，未实测、未查看用户订单。本批不是全量评价研究：Matrixify一星第1页10条、三星4条；Stock Sync一星第1页10条、三星第1页10条，共34个可见评价条目，其中2条无可见正文。部分条目与S-039重复，不计为新增独立用户。页面总评价数因缓存不同不一致，不据此推断增减。低星筛选存在选择偏差，不计算全体故障率。

## 来源和代表性反馈

### Matrixify一星
https://apps.shopify.com/excel-export-import/reviews?ratings%5B%5D=1

- Epic Offroad，2026-08-27：文件修正/界面门槛；开发者称存在必要校验。复用S-039，不算第二个样本。
- Velora，2026-04-06：报错不易处理及计费抱怨；开发者指向逐项结果文件，并解释需主动批准付费。
- HistoLab，2026-05-31：B2B公司合并/关联复杂和套餐门槛；超出商品文件输入范围。
- Natuross，2026-04-04：导出失败；开发者称Shopify接口返回服务错误，未独立复现。

### Matrixify三星
https://apps.shopify.com/excel-export-import/reviews?ratings%5B%5D=3

- Themakleding，2026-05-16：可用但慢/贵；开发者提到API限流，非已核实唯一原因。
- ExcellentSupply，2026-01-21编辑：描述被清空；商家归因列排序，开发者归因同商品行不相邻及空值覆盖，并称导入前已有警告。无原文件，不能裁定。
- Darren & Phillip，2025-06-30编辑：迁单后第三方履约重复触发；开发者称已补功能与文档，但外部系统仍有影响。旧问题不能当未修复缺口。
- peppermills，2026-06-09：无可见正文，不提取需求。

### Stock Sync一星
https://apps.shopify.com/stock-sync/reviews?ratings%5B%5D=1

- MA INTERIORS，2026-03-18：购买积分后等支持。
- wildernessdreams，2025-02-24：筛选配置与支持困难。
- BellGear，2024-10-16：读取错误工作表，价格/库存异常；开发者愿排查。
- DownUnderThunder，2024-10-16：供应商图片缺失；开发者称已恢复并怀疑源站可用性。
- Adventure Parts，2026-03-25编辑：特定供应商API库存字段未接入；单例，需厂商数据访问，非通用AI映射。
- Zelouf Fabrics，2024-06-19：字段对应与变体日志问题。历史反馈，不声称当前仍存在。

### Stock Sync三星
https://apps.shopify.com/stock-sync/reviews?ratings%5B%5D=3

- Pleasure Toy Hub，2026-07-02：feed不能用，未给细节，无法提取可自动解决的问题。
- ELITE FASHION，2025-09-11：线上/线下共用库存要求更快同步。
- Koy Resort，2024-07-26编辑：最初抱怨界面/限额/支持，后续明确得到协助并解决，不能只摘前半段。
- Maltashopper，2023-10-20：快速库存更新需要更及时支持，旧样本。
- 其余有2017—2022延迟/运行问题；年代久，不作为当前缺陷证明。My Store 2026-08-11无正文。

## 官方能力对照（当前文档声明，未实测）

1. Matrixify已有Dry Run：检查基本结构与格式；实际调用Shopify API仍可能产生预检未发现的错误。
https://matrixify.app/documentation/matrixify-import-export-job-options/

2. Stock Sync已有Preview Sync，无需有效订阅，支持新增/更新/删除前查看变更记录。
https://help.stock-sync.com/en/article/is-stock-sync-able-to-preview-sync-without-any-updates-51f6wk/

3. Stock Sync官方排障涵盖SKU匹配、筛选、工作表、库存位置和实际执行/预览区别；说明排障依赖文件与店铺状态。
https://help.stock-sync.com/en/article/troubleshooting-product-sync-not-working-correctly-1uiltjj/

4. Stock Sync更新指南称输入库存99%以上为零会暂停更新；已有确定性保护，不能把“防批量归零”当全新功能。
https://help.stock-sync.com/en/article/how-can-i-use-stock-sync-to-automatically-update-stock-levels-din7a1/

AI映射/MCP复用S-039，不重新检索冒充新证据。

## 研究推断与边界

配置理解、数据语义与执行可靠性在不同评价中重复出现，但所需解决方案不相同。AI可辅助解释和生成配置；无法仅凭文件决定商家的业务意图，也不能消除外部API、源站、第三方自动化问题。独立“解释错误/预检”工具还需证明用户愿额外上传数据/付费，以及明显优于既有AI与日志。

本批不足以证明新工具的可进入缺口。不能从低星推断产品整体不好、市场需求小、用户都不愿付费，或所有问题已解决。没有新SEO数据，没有完整错误样本，没有现场重现。
