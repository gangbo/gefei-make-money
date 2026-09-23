# S-064：发型预览并入TikTomato的产品与代码依据

2026-09-15，公开页及本地代码只读核对。用户“放音乐”按上下文理解为发型预览，已在对话说明，不当用户明确要求音频功能。未运行生成、登录后台、修改TikTomato代码或核对生产部署SHA。

- https://tiktomato.com/ 当前首页为老照片修复，导航另有放大和生成；页面说明积分包/会员、上传、异步结果、保存30天。首页FAQ与表单选项存在不同叙述，不影响本轮复用判断，不做修复。
- https://tiktomato.com/generate ：参考图最多4张，支持图生图/风格编辑；页面明确脸部等细节可能变化。因此现有能力不等于发型身份保持已通过。
- https://tiktomato.com/pricing 本轮网页抓取失败，不确认线上具体包价格。首页有$1起的描述，但不据此为发型定价。
- https://cutg.app/ ：已有网页自拍/发型/胡须/发色流程，说明品类不必须通过原生App交付；未实测。
- https://trustmrr.com/startup/cutg ：本轮页面标题近30天2672美元、累计6782、MRR23/1订阅，标注RevenueCat验证，更新09-14 06:07 AM时区未示。不能把App支付收入当网页变现证据；与S-063历史保留并列，不以两个缓存推趋势。

## 本地实现（不是部署证明）

定位到 /Volumes/work/saas/v3.tiktomato.com ，其页面文本/路由与线上一致，读root AGENTS，未改变该仓库。

- web/src/components/tools/image-generate-tool.tsx：submit先上传参考图，再createImageGenerate(prompt,image_urls,engine,aspect_ratio,resolution)，已有任务状态查询及结果查看。
- docs/credits-ledger.md：统一积分，任务预扣→完成结算，失败/取消释放；任务ID关联消费。
- web/src/i18n/locales/en/pricing.ts：文案明确各图片工具共用积分，成本依输出分辨率。
- docs/PROGRESS.md：已有认证、积分、支付、异步任务和原生iOS工程；记录历史生成成本与验证，但未核实当前结算价格，不作为发型成本实测。进度日期/条目更新存在不同时间，不当最新生产结论。
- 对web/src和PROGRESS搜索hairstyle/hair.style/发型没有匹配；仅限定范围，不能声称全仓库所有分支没有功能。

未取得：真实发型输出、身份保持率、当前模型账单/重试费用、客群重合、发型词流量、新增付款归因。足以支持承载方式的初步评估，不支持盈利或SEO结论。
