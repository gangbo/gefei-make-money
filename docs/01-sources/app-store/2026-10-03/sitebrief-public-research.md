# S-084：现场报告竞品的公开研究入口

采集日期：2026-10-03。关联D-036 / SiteBrief。范围为公开官方网页及美国App Store正文；未购买、安装、实际操作或观看完整视频。

## 已核查来源

- Site Audit Pro iOS帮助：https://support.veamstudios.com/hc/en-us/categories/201754349-Site-Audit-Pro-for-iOS
- 添加问题官方教程：https://support.veamstudios.com/hc/en-us/articles/115000438349-How-do-I-add-Issues-to-a-Project （页面更新2024-07-04）。正文及截图说明项目摘要→问题列表→单条添加或从相册批量添加→编辑备注、分配及照片标注。旧教程不能证明当前版本界面完全一致。
- 官方收费：https://siteauditpro.com/pricing 。基础App与可选Cloud分开；Cloud试用不代表可免费获取付费基础App。
- 免费下载的Site Report Pro：https://apps.apple.com/us/app/site-report-pro-punchlist-app/id1246734455 。Free + In-App Purchases；不要与付费Site Report Pro+混淆。免费项目、导出和功能限制尚未实测，不承诺完整免费体验。
- 同类官网截图：https://www.sitereportpro.co.uk/ 。公开项目、问题、拍照、标注、报告预览等截图。
- 官方视频入口：https://www.sitereportpro.co.uk/videos.html 。仅核对入口和视频介绍，未播放评测。
- 官方PDF样例：https://www.sitereportpro.co.uk/support/sample-reports.html 。公开多种主题和四种版式密度的下载链接；本轮未逐份读取PDF。

## 研究建议（分析推断）

先看报告样例确定交付字段、照片大小和分页，再免费试用同类产品，用3个房间、5个问题跑一遍项目→照片→标注→PDF；对照Site Audit Pro公开教程。若决定正式开发，购买核心竞品作为研究费用有价值，但本轮没有授权或执行购买。公开资料不能替代当前版本的操作计时、断网和导出实测。

## 用户已明确的项目约束

所有App均面向全球。简单单机App的初始开发成本商业模型按用户指定的500美元计算；这是预算假设，不是已发生成本或工程工时保证。历史2000美元模型不再作为当前预算。项目名SiteBrief，开发目录/Volumes/work/ios/ios-sitebrief；用户要求仅写文档，代码由其在项目中开发。

## 2026-10-03 截图与PRD交付补充

用户授权将官方截图保存到项目并制作产品PRD。已交付 `/Volumes/work/ios/ios-sitebrief/docs/PRD.md`、`docs/competitor-screenshots.md` 与 `docs/assets/competitors/sources.json`。素材清单26张：4张Site Audit Pro教程图、22张Site Report Pro界面/宣传图。原图已下载，尺寸可读，人工组合预览核对内容，文件校验及文档本地链接检查通过；未验证Codex整份Markdown渲染，也未安装实测竞品。

Site Report Pro官网部分carousel图片alt与内容不一致，文件名与图注已按实际画面修正；原始URL保留于来源清单。PRD设计规则属于本项目建议，不是竞品已验证行为。没有购买、代码实现或修改候选商业状态。

## 2026-10-03 维护状态核查

同一基础App id430234732英国App Store当前显示10.7.3（24 Sept），前一条10.7.2（15 Sept）；10.0.0（5 May）说明为iOS26更新外观。日期页面省略年份，按本次2026-10-03采集及版本序列归入2026年。来源：https://apps.apple.com/gb/app/site-audit-pro/id430234732 。官网 https://siteauditpro.com/releasenotes/ios 也明确10.0.0外观更新，但其顶部仅10.7.0，更新滞后商店；不能用官网教程截图判断App停止维护。美区首次打开429，本轮使用同一App英国页，不混用Enterprise或其他同名App。

项目保存的4张Site Audit Pro图片来自2022—2024更新的官方教程；截图样式不能代表当前版本。Site Report Pro是另一产品，公开图片同样可能过时。当前最新版界面尚未实测；外观现代化与操作简化仍是SiteBrief设计建议，不能认定竞品未做或已验证差异。

## 12 首发范围调整与 Site Report Pro 对照

2026-10-03：用户希望首发功能较齐全，重视上线初期的付费机会。首版目标调整为能满足常见现场工作的一套完整工具。下列扩充为开发建议，尚未逐项锁定；不代表全部功能能在500美元假设内完成。本文原有可靠性与离线验收继续有效。

### 免费竞品核查

Site Report Pro（id1246734455）是免费下载加一次内购，不是无限制免费。官方购买帮助说明：免费最多3个项目，每个6条问题；完整版本提供更多项目、每项目最多500条问题、去除报告品牌。另一帮助页列自有Logo为购买后能力。美区Unlock列14.99美元，部分主题另外收费；Plus为单独付费App，官方说明功能与主题包含在内。

来源：[免费额度与购买](https://www.sitereportpro.co.uk/support/app-purchase.html)、[更多项目与Logo](https://www.sitereportpro.co.uk/support/add-more-projects.html)、[免费与Plus](https://www.sitereportpro.co.uk/support/free-vs-paid.html)、[美区内购](https://apps.apple.com/us/app/site-report-pro-punchlist-app/id1246734455)。仅公开核查，未安装实测。

Site Report Pro商店列同问题最多8图、标注、签名、排序筛选、PDF/Excel、备份和不要求线上服务。Site Audit Pro官方计划则把多图、完成状态、截止日期列入Cloud订阅；基础付费App仍可本地记录、标注与生成报告。来源：[Site Audit Pro计划](https://siteauditpro.com/pricing)。因此免费试用、本地多图和一次买断不能作为相对Site Report Pro的独有优势。

### 建议补齐的首发能力

| 能力 | 建议行为 | 验收补充 |
| --- | --- | --- |
| 批量建立问题 | 选照片后明确选择“全部加入当前问题”或“一张建立一个问题”；不自动猜分组 | 数量与归属准确，取消不留下半导入记录 |
| 搜索与筛选 | 按标题/备注/位置搜索；按位置、状态筛选；导出时明确选择全部或筛选结果 | 预览、统计、导出范围一致，清除筛选不丢问题 |
| 优先级与截止日期 | 优先级低/中/高，日期可为空；不做复杂通知系统 | 本地保存，报告可显示；不把逾期自动当已解决 |
| 复用记录 | 复制问题、复制项目作为下一次检查的起点 | 使用新标识，图片与状态按明确规则复制，修改不影响原件 |
| 常见标注工具 | 箭头、圈选外补矩形、文字与自由画笔 | 所有工具可撤销，重开可编辑，PDF方向与位置正确 |
| 简单署名签名 | 可选手绘签名或输入署名，默认指检查人签名 | 允许清除与跳过，正确进入PDF；不声明法律效力 |
| 常见报告版式 | 同一内容支持标准、紧凑、大图3种布局，而非堆叠大量主题 | 三种均通过长文字、多图和分页验收 |

原P1的复制与筛选建议提升为首发功能；本节的批量建问题、基础签名和三种版式替代原“后续”建议，但仍不加入团队云服务和复杂签名流程。Excel暂留后续，原因是现有单人交付主路径以PDF为主，需评估真实需求后决定是否提前。

### 新App上线机会的证据边界

Apple公开条款说明上线日期可能参与相关搜索排序，编辑对新App及重大更新有特别关注，但不保证展示、推荐或排名。没有找到固定蜜月期时长或上线后更容易付费的保证。来源：[Apple公开条款](https://developer.apple.com/support/downloads/terms/exhibits/Exhibits-to-Schedule-2-and-3-20250821-English-UK.pdf)、[搜索说明](https://developer.apple.com/app-store/search/)。用户观察保留为经营线索，不能解释为已核实算法规则。

观察上线表现时区分曝光、下载、完成报告、付费人数及比例：付费减少可能来自流量减少，也可能来自使用与购买转化变化。先让新用户在免费范围内完成一份可靠报告，再评价首发功能是否支持付费。

## 用户当前截图核查与本地转换

用户确定Site Report Pro为主要对标，提供12张本机截图；版本未知。当前内购页IMG_7384明确免费2项目×6问题，解锁¥98，并限制归档/复制/移动，与官网3项目有差异，以截图描述当前安装体验，不断言全球规则。覆盖列表/排序/设置目录/批量菜单/问题详情/分配；缺创建编辑、照片导入、实际标注工具、报告设置与PDF正文、设置子页。

12图本机sips转JPEG，1179×2556不变，5,945,170→2,954,796字节（减少50.3%）；解码尺寸校验及抽样视觉检查后按用户授权删除对应PNG。未调用MediaKit、未上传。本机项目docs/user-screenshot-review.md保存逐图审阅和补拍清单，PRD修正额度。截图非本助手操作实测，不据按钮推定免费能力；原官方26图保持独立。

## 第二批用户截图

新增17张（含处理时补入的7403签名菜单），累计29张。已审阅项目创建/资料、签名来源、标注引导与手绘、照片加入项目、PDF默认设置/签名/字段/页眉页脚/自由文本位置。仍缺问题字段编辑、生成PDF及成品/分享，客户/检查人展开字段与多选照片规则等。截图不是操作实测。新增17图本机sips压缩JPG，5,765,148→3,155,451字节（减少45.3%），验证后删除对应PNG；无MediaKit或上传。项目截图审阅与PRD同步，范围建议不等于竞品免费权益已验证。

2026-10-03素材清理：按用户授权移除SiteBrief项目中4张Site Audit Pro旧教程图，同时清理PRD/图库/来源清单引用。保留22张Site Report Pro官方参考和29张用户截图，文字竞品比较保留；历史26图交付记录不改写。

素材路径更新：按用户要求，项目29张用户截图从根目录移到docs/assets/competitors/，与22张官方图统一，共51张；文档链接与转换记录同步，未重编码图片。

第三批新增7张用户截图：Photos/Free Text/Excel/Drawing/Tags设置及issue1空详情；累计36张用户图，与22张官方图统一共58张。本地sips转JPG并验证后删除PNG，减少12.2%；无上传。编辑表单、实际PDF成品仍缺，项目文档同步。

## 第四批与实际PDF

用户提供4张新截图与Industrial Site 1.pdf（5页A4，1,369,496字节，2026-10-03生成）。已用Poppler渲染全5页并用pdfplumber提取核对；原PDF保留。新增截图覆盖问题编辑上下部、分享格式菜单、New PDF Report；累计40张用户图/统一62张。2张重复PNG以同参数重新转换并校验相同后清理，新4图本地sips压缩37.8%，删除原PNG。

主要路径已足够编写开发基线，无需继续穷举。实际报告显示Outside Valve描述/评论续到第5页无重复标题，附加照片较小；PRD补续页编号标题、照片可读尺寸、空字段隐藏等建议。此为单主题样例，不泛化所有主题；状态枚举/批量归属/备份恢复及异常仍未实测。详细项目docs/report-review.md。

参考PDF归档：按用户要求将项目根目录Industrial Site 1.pdf移至docs/assets/competitors/Industrial Site 1.pdf，文档链接同步，文件内容校验不变。

文档复核：基于已有S-084证据统一SiteBrief PRD与README，补实施行为和验收；不新增外部采集。来源区分40张用户图、22官方图、1份实际PDF；检查文件与哈希。详细项目docs/document-review.md，价格/平台等尚未确定，未编写代码。

## 第五批用户素材：Excel交付

S-084第五批新增4张Excel创建/列表/预览截图及1份XLSX成品，累计44张用户图、66张图片；本地转JPG归档、原XLSX校验不变。表格结构只读确认1表5问题22列及嵌入照片，未验证Excel显示；首版范围与商业候选状态不变。

来源为用户本机截图IMG_7426—7429和Industrial Site 1.xlsx；不是网页新采集。项目docs/user-screenshot-review.md与report-review.md记录逐图说明和表格结构，PRD只更新证据条目，不新增Excel首发要求。截图638,979→466,484字节（减少27.0%），macOS sips本机处理并删除对应PNG；XLSX移至docs/assets/competitors/，7,496,580字节，SHA256 dea39a6cfd15290e41b9b91f3b99b1900104213438f04e8ea5d72ef57dc8e311。没有竞品运行、购买、App代码或实际Excel兼容性验收。

## DEC-066：完整首发范围文档更新

2026-10-03 / DEC-066：用户认可SiteBrief完整首发，已扩充PRD与README：专业字段/评论、归档、标签/排序、跨项目整理、Excel/CSV、连续录入、模板/短语均为P0；默认高级信息折叠。补数据/备份/额度/验收规则，仅文档工作，无新外部采集或商业验证变化。

这是用户决策及实施规则更新，没有刷新商店网页。用户自述首版购买情况属于口述经验，未核对后台曝光或转化，不用于证明固定商店机制。当前开发范围以SiteBrief/docs/PRD.md为准，历史审阅中的后续建议保留时点并补当前范围说明。
