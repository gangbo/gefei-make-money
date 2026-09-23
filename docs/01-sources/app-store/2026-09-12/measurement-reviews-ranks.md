# S-047：尺寸记录评价与商店排名

2026-09-12，部分采集。人工摘要；公开网页、Chrome原生UI；不是完整最新评价导出。关联D-035，复用S-045/046。

## 评价：任务、时间与边界

1. https://play.google.com/store/apps/details?hl=en_US&id=com.bigbluepixel.photomeasures ：已读正文3条可见评价。Ben Holloway，2024-11-13，常用于现场记录，希望一次导入多图和给导出文件命名；J. D.，2021-06-24，同样要求多图导入，另提照片边缘尺寸线难拖；匿名用户，2019-08-01，希望导出PDF前补页/备注、改文件名，避免回电脑再加工。三条不是近期全量样本，Android问题不能直接推广到iOS。批量导入由2个不同用户重复提出；命名由2个不同用户提出。未实测现版本。
2. https://apps.apple.com/us/app/photo-measures/id415038787?see-all=reviews ：美国可见评价节选。2024-04-28 Maggie-Giz反馈关闭照片后目录回到顶部；2024-01-04 nurseynurse899263738反馈复杂庭院无人机照片尺寸错位、导出拥挤。属于2024旧反馈，不能当2026仍未修复。还有多年工作使用的正面评价，已见S-045，不重复计新购买。
3. https://apps.apple.com/ca/app/my-measures-pro-ar-measure/id325962257 ：加拿大PRO独立AppID，非美国免费版。2025-10-15 JLHebert正面使用；Apr 30（页面未写年份）newf1自述推荐给多人；2024-01-09 BenBoCarter称为Bosch测距仪买Pro，后续照片传距连接不稳定。最新7.10 Jun 4说明修复选对象崩溃，7.09 2025-08-28已有LiDAR Room Scan。不能据旧差评说无人维护；未证实蓝牙问题已修复。
4. https://apps.apple.com/es/app/my-measures-ar-measure/id628109928?platform=watch&see-all=reviews ：仅检索正文，打开失败。2025-01-25 imac-i称用于很多工作、旧资料恢复失败；2024-08-08 Keoops称已付年费但编辑时重启。https://apps.apple.com/be/app/my-measures-ar-measure/id628109928?platform=iphone&see-all=reviews ：仅检索正文，2025-01-29 Loclaire23认为复杂。没有当前复现，费用投诉不能证明愿意买我们的产品。
5. https://play.google.com/store/apps/details/?hl=en-US&id=si.topapp.mymeasuresfree ：2025-05-23 Maria Wilton称免费版多年稳定用于保存家中尺寸。说明部分需求可被免费覆盖；未证明职业客户只需免费。

## 商店排名：实际UI查询

https://openaso.ai/rank-checker ，2026-09-12；美国US，默认产品分别选择准确ID。第三方页面自述调用Apple公共搜索端点，属于单次工具结果，未与实体iPhone个性化搜索交叉核对。不是关键词热度、月搜索量或排名历史。

| 词 | Photo Measures 415038787 | My Measures + AR Measure 628109928 |
| --- | --- | --- |
| photo measures | #1 / 返回162 | #6 / 返回162 |
| photo dimensions | #26 / 返回184 | 页面显示not in top 200 |
| measurement notes | 页面显示not in top 200 | #10 / 返回169 |

“not in top 200”为工具原文标签，不把未出现解释为零需求。产品名称与词重合，photo measures兼有品牌/描述性意图，尚未分离；另两个词可能混有其他用途，不能直接算目标市场。关键词热度需登录/key入口，未创建账户，没拿到Apple Ads popularity或搜索量。无需重复查询这6格。

## 排名/下载辅助来源

- https://www.appbrain.com/app/photo-measures/com.bigbluepixel.photomeasures ：打开正文显示Android近30天310下载（第三方估算，全球具体覆盖未明）、累计70K估算；索引为400且评分数量不一致，以正文记录，不能证明增长。历史图表需订阅未读。未乘价格当收入。
- 上述Google Play正文实际区域为Brazil (English United States)、显示R$14.99及付费效率#2；hl=en_US仅语言，不当美国榜位。
- https://openaso.ai/apps/415038787 ：缓存美国付费效率#33、525评分，不与此前实时#39/526拼成时间序列；三条所谓latest评论未给日期，且负评显示5星，日期/星级不采用。

## 采集失败与实际覆盖

Apple美国RSS两个公开URL均HTTP成功但feed无entry，原始JSON存[feed尝试](review-feed-attempts/)，这不代表没有评价。Chrome扩展创建tab超时，随后原生Chrome新建标签页成功完成两次查询。未安装APP、没有样本实测、新购买、搜索量或可用历史曲线。评价证据主要2024–2025，不能写成近期2026用户共识。
