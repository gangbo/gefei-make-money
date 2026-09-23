# S-052：演员排练测试入口检查

2026-09-12，Chrome 与 Mac App Store 实际 UI 人工摘要，非完整导出或排练测试。

- Chrome 访问 https://sayblablabla.com/ ，菜单 Sign in 指向 /dashboard，实际重定向 https://sayblablabla.com/auth/sign-in 。页面描述查看排练统计和管理账户，提供 Google/Apple 登录；没有账户则下载 App 开始。未登录或创建账户，不能据此断言登录后全部功能。
- [blablabla 官方商店](https://apps.apple.com/us/app/blablabla-line-reader-tape/id6760597750)列 Mac 要求 macOS 13.1+ 和 M1+；[coldRead 官方商店](https://apps.apple.com/us/app/coldread/id1264354117)列 macOS 11+ 和 M1+，并提供免费8句。当前本机 uname -m 为 arm64。
- 本机 App Store 搜索 blablabla，实际出现中文标题“blablabla: 演员对戏与自录试镜”，iPhone/iPad 类结果，标注未针对 macOS 验证。点击免费“获取”一次后持续“正在载入”；AX 与截图均未显示完成、错误或身份验证。未点击付费订阅或试用。不能声称已安装。
- App Store 启动调用较慢；没有修改网络/商店账户设置。下载原因未知，不判断为竞品 bug。coldRead 仅核对官方兼容说明，未在本机获取。
- [原创6句文本](../../../04-validation/experiments/actor-rehearsal-2026-09-12/original-scene.txt)已独立保存；尚未上传或导入、未录音。六情形测试均未执行。

下一步从 App Store 获取状态继续，不重复研究收入/官网。若仍无法下载，保留设备访问阻塞，不将测试未完成用于市场判断。

## 后续：安装已完成，自动化启动未成功

用户反馈安装完成后复核：App Store 按钮实际显示“打开”。本地安装信息版本 2.7.1、标识 app.dryrun.ios。点击商店打开后，Computer Use 通过名称和 /Applications/Blablabla.app 均返回 Running application not found。按标识连接时出现安装目录与临时 Wrapper 同标识歧义；尝试安装内 Wrapper 路径返回 No compatible executable was found。后者是直接打开内部包装路径的结果，不能据此断言正常启动不兼容。

全局 UI 盘点一次超时并重置，随后可重新连接商店。限定检查最近25个诊断文件未找到匹配名称的崩溃报告，不证明不存在崩溃。进程读取受本地权限限制，未提权。原因尚未区分应用启动与自动化识别问题。

当前需要用户手动打开一次，确认是否能看到首页或系统提示；尚未登入、导入、录音或付费，排练测试仍0次。不要再次按未安装处理。

## 再续：已连接运行副本并完成前置流程

用户手动打开后，通过工具返回的临时Wrapper运行路径成功连接；无须重装。已完成E-008原生导入/角色/六句/舞台说明核对与点击排练一次，语音六情形未测。见[报告](../../../04-validation/reports/actor-rehearsal-preflight-2026-09-12.md)。原启动阻塞解除，不再要求重复打开。

## 平台复核（2026-09-12）

官方 https://sayblablabla.com/android 明确第一版Android在Google Play封闭测试，流程为加入Google Group→同账户加入测试→Play安装；未参加测试或安装。https://sayblablabla.com/press 同样列iPhone/iPad公开、Android closed beta。网页登录用途复用前轮Chrome实际观察：统计和账户管理；未登录内页，不能断言没有任何网页排练功能。本次web工具打开登录页返回安全解析错误，不当网站宕机。
