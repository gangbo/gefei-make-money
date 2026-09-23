# S-062：跨榜单消费者用途线索池

2026-09-13；复用S-061，网页人工摘要/初筛推断分列，不是完整原始榜单导出。美国iOS付费前25和安卓付费前22沿用S-061，不重复当新样本。

## 本轮补采范围

- https://apps.apple.com/jp/iphone/charts/36?chart=top-paid ：日本iPhone All Apps Paid，返回前25，重点摘录第11–25。Oldi #12、Koala #15、瞬间英作文#16、护理考试#17、有机化学#18、YoungPhoto#20、FlashSCORE#25。无历史增长数据。
- https://apps.apple.com/de/iphone/charts/36?chart=top-paid ：德国相同口径，返回前25，重点摘录第9–25。高尔夫资格#10、驾照#16、露营指南#19、HealthFit#20、步道集章#22、儿童阅读#23、Intake#24。
- https://www.appbrain.com/stats/google-play-rankings/top_grossing/application/us ：美国Android应用畅销榜，页面09-13更新，读取可见1–57。大部分为大平台；#23 onX Hunt、#30 Tipsy Chat、#49 OOC、#54 Cleanup等仅用途线索。第三方排名/安装估算不当收入，无历史。
- https://www.toolify.ai/Best-trending-AI-Tools ：正确大写路径，标题August 2026，读取前25项。Hint占星、Wanderboat旅行、Emochi角色聊天、Studocu学习、Rodin 3D、DaVinci图片、PixAI动漫等。榜单宣称月访问增长，估算口径未独立核验，不能当订阅或获客证明。前轮小写/另一入口的旧文章不混用。https://www.toolify.ai/Best-AI-Tools-Category 仅确认分类入口，未做全分类导出。
- https://trustmrr.com/category/mobile-apps 搜索摘要作为定位；进一步按hairstyle、tattoo查询具名详情。不是覆盖1852项，具体收入见S-063。

## 25个用途合并初筛（判断，不是25个市场验证）

| 用途 | 榜单/参照 | 本轮去向与原因 |
| --- | --- | --- |
| 发型/发色预览 | 收入榜CutG/HairStudio | 入选；有具名小产品收入，须验证成本与效果 |
| 手机夜拍/复古相机 | S-061 2AM；日本Oldi/YoungPhoto | 入选；使用与内购参照另查Dazz |
| 衣橱和出行搭配 | S-061 Stylebook | 入选；具体购买与日常用途 |
| 读谱/音程练习 | S-061 Tenuto、日本FlashSCORE | 入选；可确定性验收、离线成本低 |
| 通知筛选和提醒 | S-061 BuzzKill | 入选；近期明确购买，系统维护风险 |
| 乐谱库 | S-061 MobileSheets | 暂不提名；文件标注/硬件交互范围需再拆 |
| 桌面组件/表盘 | S-061 OneUI/Glass Widgets | 未提名；主题持续供给和获客未查 |
| 电子书阅读 | S-061 ReadEra | 未提名；格式兼容与已有阅读器差异未知 |
| NFC自动化 | S-061 NFC Tools | 未提名；硬件用例和权限未核对 |
| 采样做节拍 | 日本Koala | 未提名；实时音频工程和音乐体验较重 |
| 旅行英语 | 日本Help me Travel | 未提名；内容创作者渠道依赖未查 |
| 英语造句练习 | 日本瞬间英作文 | 未提名；课程内容与版权来源未查 |
| 护理资格备考 | 日本考试App | 未提名；本地题库授权和更新成本未知 |
| 有机化学练习 | 日本有机化学 | 未提名；学科验证/内容制作需补 |
| 高尔夫资格 | 德国DGV | 未提名；官方内容与授权依赖 |
| 驾照考试 | 德国Führerschein | 未提名；地区题库许可未知 |
| 露营地点指南 | 德国ADAC | 未提名；地点数据覆盖成本 |
| 步道集章 | 德国Harzer Wandernadel | 未提名；地理范围与数据入口未查 |
| 儿童阅读游戏 | 德国Antolin | 未提名；内容体系/学习效果未查 |
| 饮食记录 | 德国Intake | 未提名；未取得付费和输入准确性证据 |
| 手机相册清理 | 安卓畅销Cleanup | 未提名；误删、系统覆盖与渠道未查 |
| 角色聊天/互动故事 | 安卓Tipsy/OOC、Toolify Emochi | 未提名；长会话成本和内容运营较重，仍非永久排除 |
| 星座娱乐 | Toolify Hint | 未提名；页面混人工专家，尚缺小范围收入拆分 |
| 个性化行程 | Toolify Wanderboat | 未提名；真实地点时效及推荐可靠性未查 |
| 纹身预览 | 收入榜Try Tattoo 3D/Tattoo AI | 未提名；有小额收入但3D与定位价值需补，详S-063 |

不因人群非职业而淘汰。老照片、自有音频能力、演员/教程与旧停止项不重新提名。新增5项是候选阶段，未安装/开发/获客测试。没有声称完成所有国家、iOS免费榜或整个AI导航站。
