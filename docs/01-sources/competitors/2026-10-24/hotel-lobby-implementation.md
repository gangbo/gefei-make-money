# S-092：Hotel Lobby 实现核查

采集日期：2026-10-24（Asia/Shanghai）。范围：Eachlabs hotel-room 公开模型页、Readme、输入 schema、页面内公开元数据、公开工作流；7个其他站点的模型/流程声明；可灵官方指南及 fal 接口。类型：网页人工摘要＋Eachlabs原始HTML与提取JSON。没有登录后台、付费生成、读取服务端代码或执行日志。没有核验收入、流量、成片成功率。技术调查，不新建商业候选。

## Eachlabs：能确认与不能确认

- 模型页：https://www.eachlabs.ai/eachlabs/eachlabs/hotel-room
- 工作流：https://www.eachlabs.ai/ai-flows/hotel-lobby-studio-video
- 已保存原始HTML：eachlabs-hotel-room-page.html；从公开页面提取：eachlabs-hotel-room-public-metadata.json。
- model slug 是 hotel-room，provider/family 显示 eachlabs，不是底层视频模型名称。外层工作流只有一个 hotel-room 节点；单节点不等于内部一次模型推理。
- 输入：user_photo 必填，替换左侧；user_photo_2 可选，替换右侧，留空仅替换左侧；duration 4–15秒，默认15；resolution 480p/720p/1080p，默认480p。没有公开通用 prompt 或参考视频上传参数。
- 价格描述明确包含 character sheets 和 audio；duration 参数说明视频与音轨按相同时长裁剪。可确认这些处理类别，但没有完整内部拓扑、图像模型、视频模型、调用次数、提示词或素材来源。
- 公开元数据 charge.variables 指向 output.total_cost，未披露成本组成；public_provider_name=false。仅描述公开字段，不据此猜具体供应商。
- 720p约0.32美元/秒＋0.22美元/次；1080p约0.78＋0.22；480p约0.14＋0.22。480p文案15秒约2.35，而公式约2.32，为近似口径。
- 工作流页显示约0.08美元/次，与模型详情明显冲突，不能作为实际成片成本。未支付测试核验账单。
- 结论：Eachlabs内部底层模型仍未查实。不能宣称是两次Motion Control、也不能宣称一定不是可灵。公开模型页/Readme/schema和外层工作流均未提供足够证据。若要确定，需要官方披露内部模型清单或包含子任务模型ID的执行记录。

## 其他网站：站方声明，不等于后台调用已独立验证

| 网站 | 公开声明 | 工作流信息与限制 |
| --- | --- | --- |
| aivideoswap.com/template/hotel-lobby | Kling 3.0 Omni Transformation | 明确两张人物照、左右对应、预设参考模板，7–15秒；声明双人已验证。未披露供应商、完整请求、是否有预处理，不能把网页标签等同于精确API路径 |
| hotellobby.me/about | Gemini 3.5 Flash、Nano Banana 2、MiniMax H3 Max Turbo，fal.ai | 检查照片→合成橙色双人场景→图生视频并生成新rap音频；不是精确复刻原音轨动作 |
| hotellobbytrend.app/blog/how-we-built-hotel-lobby-ai | Seedance 2.0 Mini；免费预览用GPT Image 2.5 | 两个人物参考＋四段定时动作提示词；文章未明确使用驱动视频；发布时自行加原曲。其自述单条15秒123 credits，按文中最高充值率折约1.23美元，不是独立核验价格 |
| hotellobbyvideo.net | 默认Wan 3.0，可选Seedance | 每张照片先重绘站姿人像；默认模板音乐/动作，可传参考视频和音频；未披露Wan具体端点、上游供应商和调用次数 |
| tryhotellobbyai.com | 照片送往Eachlabs及其模型供应商 | 证明上游平台声明，不能单凭界面断言调用hotel-room |
| hotellobbytrendai.com/terms/ | Kie.ai Seedance 2.5 | 条款明确双图参考生成15秒720p视频；具体端点和内部步骤未披露 |
| hotellobby.live/facts | Seedance 2 Mini | 两张照片、可选歌词/指令；浏览器本地照片检查和场景预览。无后台记录验证 |

这些网站不同域名不必然代表不同团队；没有验证商业规模。不要把搜到的营销页面当作原始爆款作者的制作记录。

## 可灵接口能力交叉核对

- 官方Motion Control：https://kling.ai/quickstart/motion-control-user-guide
- 官方Omni：https://kling.ai/quickstart/klingai-video-3-omni-model-user-guide
- fal多参考视频接口：https://fal.ai/models/fal-ai/kling-video/o3/pro/video-to-video/reference/api

Motion Control的单人物动作控制不能推广为所有可灵接口的限制。Omni官方明确多图/多元素与群体场景能力。fal的O3 reference端点公开接受video_url、image_urls、elements；视频输入时元素＋参考图总数最多4，视频3–15秒。它证明一个请求可以提供多人参考和视频，不证明某网站使用该端点，不保证双人动作精准对应或成片成功率。

同名Transformation供应商实现也可能不同：HiAPI教程https://www.hiapi.ai/en/blog/how-to-use-kling-3-0-omni-transformation-hiapi-api 声称仅prompt/video_urls/resolution，而其产品页又提subject图片。不能混用供应商schema，更不能仅凭相同型号名字编造可执行请求。

## 对此前对话的纠正与下一步

- 撤回“Hotel Lobby优先用Motion Control即可”的推荐；双人直接绑定缺乏支持。
- 撤回以“两次Motion Control＋合成”解释Eachlabs的推测，未获得事实支持。
- 下次若测试双人保留原片动作，先核多角色视频编辑/参考接口；若只需橙棚rap氛围，可独立测试图生视频/多参考提示词路线。两者质量目标不同。
- 不付费、不发邮件、不运行生成。当前结果是公开证据核查；Eachlabs内部模型仍未知，未完成服务端归因。
