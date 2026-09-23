# S-039：全球词量与成熟竞品AI能力

采集2026-09-12，用户授权Chrome，短暂操作冲突后用户回复用完，已恢复。Semrush为UI人工转录，web为公开官方页/评价摘录，不是原始CSV、付款核验或工具实测。

## 独立关键词概览

入口https://zh.semrush.fast.wmxpro.com/analytics/keywordoverview/ 。美国、桌面、报表日期09-12、USD；全球量取同页“全球搜索量”，显示为舍入K值，不按显示自行还原精确数。KD/CPC/意图属美国。

| 词 | 美国月量 | 全球月量 | 美国KD | CPC USD | 意图 |
|---|---:|---:|---:|---:|---|
| shopify product import | 70 | 1.1K | 40 | 9.09 | 信息 |
| video ad maker | 590 | 3.3K | 45 | 12.96 | 商务 |

Shopify相关词样本有WordPress迁移、Amazon/AliExpress导入、CSV教程，不能全部归为供应商文档转新商品。关键词概览的SERP分析容器未显示结果行，尚不能记录固定排名。视频广告制作词覆盖通用制作/模板编辑，不等于已有素材多版本交付；沿用S-038公开搜索结果解释范围，不据上述词量计算市场收入。

## 成熟参照：公开供给与使用评价

### Matrixify

https://apps.shopify.com/excel-export-import ：4.9分、1614条评价；基础20美元/月（每文件5000产品），50/200美元更高档，有免费计划。批量导入/导出、迁移、计划任务等范围较D-023宽，评价数不能归给“供应商PDF导入”，不能当付费用户数。

可见评价：Oglesby Media 09-11说为客户从WooCommerce迁入商品/变体/订单，使用2个月。Epic Offroad 08-27使用约18小时，抱怨Excel门槛、错误和修正文件耗时；开发者回应这是导入校验（双方陈述分开，未复现）。Rare Beauty Brands Wholesale 08-06使用超过6年，说导入导出可用但仍需手工。上述为个别用户自述，不形成总体差评结论。

### 关键官方反证：已经有AI映射及执行

https://matrixify.app/documentation/matrixify-mcp-server/
https://matrixify.app/tutorials/bulk-update-shopify-products-from-any-supplier-file-with-claude-ai-and-matrixify-mcp/

官方文档与教程明确描述：通过MCP连接Claude，读取供应商CSV/Excel/PDF，映射字段，生成导入文件、执行及追踪任务；支持按条码匹配、加价规则，示例还包含PDF图片。MCP有dry run能力（不写店铺）。教程要求用户监控可能出现的询问/确认，并在任务后核对结果。因此不能说已验证完全无人值守或准确无误。

https://matrixify.app/pricing/ ：AI MCP Jobs每日上限免费10、Basic100、Big1440、Enterprise不限；这是Matrixify任务额度，不是Claude推理费用。未核验用户采用率/实际质量。对研究的含义：不能继续以“传统工具没有AI映射”作为差异化前提；这是供给事实，不是SEO需求结论。

### Stock Sync

https://apps.shopify.com/stock-sync ：4.7分918评价；入门付费7美元/月起，存在供应商feed等附加收费。覆盖持续库存/供应商更新，和一次商品生成不是同一任务。Florida Lash Supply 07-02使用约1月评价，称设置应排除不想同步的图片/描述，正确配置后顺畅；仅单条自述。

https://help.stock-sync.com/en/article/ai-liquid-for-step-2-matching-column-r1nqk1/ ：官方说明在Matching Column的Smart Setting使用AI提示生成Liquid映射规则，例子包括拼字段、清HTML、缺失默认值。没有证据证明任意PDF完整抽取，这项能力不夸大成Matrixify同等全流程。

## 检索边界

web查询Shopify supplier catalog import AI Matrixify reviews、video ad variations bulk editor software及两站定向AI能力。结果用于发现官方资料，不宣称Google美国固定前排顺序。D-024发现Genyad、UAGenius、The Brief、AdLit相关线索，仅摘要，未核实规模/收入，未新增候选。搜索结果中的uniquifier与广告平台批量管理并非创意变体制作，不混计。

本轮未导入真实店铺、未连接MCP、未联系商家、未注册试用。尚缺固定SERP、直接竞品相关词流量、Clipset全球流量来源及页面历史。无新立项。

追加独立词：batch video editor，美国月量20、全球110、美国KD/意图不可用，CPC2.81美元，09-12桌面。不能把KD缺失当容易排名。相关结果未完成SERP读取。

最后补采：Matrixify全球概览（根域matrixify.app、全球选中、报表日期2026-09-11，采集09-12），自然流量估算3969、排名词1443。指标跳转URL为美国桌面，保留全球按钮口径；未导出确认Database，参考S-037同页面口径但不能当第一方月访问。未取得Stock Sync流量和两家历史。概览一度空白，重载后恢复，不是账户登录失败。
