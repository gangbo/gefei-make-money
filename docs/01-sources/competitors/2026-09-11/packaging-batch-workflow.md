# S-020：包装与相邻商品样机的批量工作流程

采集2026-09-11。公开网页人工转述；官网供给、社区自述和二手收入线索分别标记。未登录、购买、使用收费API或操作PSD。复用S-016/017，不重复验证Blender可运行。

## 查询

`site.pacdora.com batch mockup multiple designs export`；`site.appsforlife.com boxshot batch rendering limitations artwork`；`packaging mockup batch designs automation reviews label variants`；`site.reddit.com packaging mockups "batch" Photoshop`；`site.bulkmockup.com packaging CSV pricing`；`site.sudomock.com PSD unsupported limitations`；`"Bulk Mockup" revenue founder customers`；`"packaging" "mockups" "revisions" "hours" designer`。

Stripe Directory的本地配置权限失败已在S-019记录，本轮复用该限制，不重复调用；Chrome连接故障也不作为用户未登录处理。

## A. Boxshot：多面匹配已有自动化

[官方批量教程](https://appsforlife.com/boxshot/tutorials/batch/rendering/)：先建场景、选变化的面，每个版本一个文件夹，再用文件名通配符匹配正面/背面等图稿。缺少或多重匹配会提示；用户改文件名后需返回重新添加文件夹。最后设置输出并排队。

这是明确的人工配置步骤，不证明配置复杂度普遍很高；命名规范以后可重复使用。不能把“自动匹配”“批量渲染”当作现有工具完全没有的功能。

## B. Bulk Mockup：小型收费供给

[官网](https://www.bulkmockup.com/)、[价格](https://www.bulkmockup.com/pricing/)：Photoshop CC 2022及以上，智能对象替换、尺寸对齐、多个智能对象、自定义命名和文件夹组织。页面列$15/月、$77/年，可在两台设备安装；不含Photoshop。未结账。

[月付购买入口](https://bulkmockup.gumroad.com/l/obfdg/?monthly=true)可到达但未读出正文，不据此确认真实结账金额。官网“2000+ people trust”和省时数据是厂商声明，不等于付费人数或实际计时。

[厂商客户故事](https://www.bulkmockup.com/how-bailey-uses-bulk-mockup/)为Etsy/POD用途，强调复用自有PSD和命名便利；所称卖家收入不是软件收入，亦未核验。

## C. SudoMock：网页/API也覆盖批量

[包装用途](https://sudomock.com/use-cases/packaging-mockups)：上传自有PSD、不同视角模板、配置设计区域、批量调用和回调；不是我们已实测的步骤。

[价格](https://sudomock.com/pricing)：页面按需渲染$0.10/张，最低余额$5，也有月度量级方案。不是我们的成本或推荐套餐，未付款。

[准备说明](https://sudomock.com/docs/psd-preparation)要求智能对象/文本层、图层命名等准备；[兼容矩阵](https://sudomock.com/docs/psd-compatibility)对部分特效列出限制及替代办法。两页对部分功能的表述不一致（准备页让栅格化部分效果，矩阵又列为支持），不能自行判断哪页等于实际效果；应以同PSD实测为准。没有把兼容缺陷当新产品机会或重启通用文件修复。

## D. 公开用户反馈（不是厂商销量）

1. [墙面装饰画批处理求助](https://www.reddit.com/r/photoshop/comments/1sdbdac/help_how_do_i_run_bulk_wall_art_mockups_in/)：读取主帖及作者多次更新。作者描述50–100设计×20样机，尝试普通教程会丢失倾斜透视；免费脚本配置花费5小时以上，随后明确自述已订阅Bulk Mockup并认为值得。属于同一个人的连续记录，只计一个案例；身份、订单和后续留存未核验。搜索与页面相对日期不同，不硬换算发布日期。
2. [多个智能对象自动化求助](https://www.reddit.com/r/photoshop/comments/1os4jqc/batch_automation_for_multiple_smart_object/)：用户自述跟随AI说明仍不知如何批量替换。公开求助，不是支付证据，也不是包装行业样本。
3. [小品牌包装视觉讨论](https://www.reddit.com/r/product_design/comments/1tzd2nr/how_are_small_brands_handling_packaging_visuals/)：主帖为转述创始人交流；两条可见回复涉及快速视觉预览和打印折叠样品。没有金额、批次或付款记录，不能证明高频专业采购。

## E. 收入线索（未核验，不能合并成多份证据）

搜索发现[FounderBase](https://founderbase.ai/interviews/bulk-mockup)写$13K/月，数个Starter Story转述页写$12K/月。可能来自同一访谈或不同时间；不是独立财务证据。原[YouTube访谈](https://www.youtube.com/watch?v=W48emwbUlUE)读取失败，未看仪表盘或完整视频。收入仅为待补线索，不写入已核验收入榜、不用于利润推算。

## 尚未完成

没有现成PSD与渲染输出对照、实际操作计时、包装客户订单或获客量数据。Pacdora未搜到明确跨SKU批处理资料，不等于其没有该功能。PrintMockup等只作为发现入口，不计入已验证候选。
