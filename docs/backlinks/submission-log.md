# PuzzleBento 外链投稿记录

每投一个平台就在这里追加一行，包括失败的：注册不了、发不了帖、被拒，都写清楚原因，方便以后跳过或重试。日历见 [submission-calendar.md](submission-calendar.md)。

注册邮箱统一为 `bq2ynt4q@mail.grokbot.com`，密码存在 Gary 的 vault 里，本文件不写任何密码。时间为 America/New_York。

状态取值：`已上线`（链接已公开可见）、`已提交`、`待审核`、`待验证邮件`、`注册受阻`、`发帖受阻`、`被拒`、`跳过`。

| 日期 | 日历天 | 平台 | 账号 | 链接所在页面 | 落地页 | 锚文本 / 标题 | 链接属性 | 状态 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-11-23 | 1 | itch.io | puzzlebento | [puzzlebento.itch.io](https://puzzlebento.itch.io) | https://puzzlebento.com/games/2048/ | 资料页 Website 字段（不支持自定义锚文本）+ bio 里写 "Play 2048 online free at PuzzleBento…" | nofollow | 已上线 | 注册当下不强制邮件验证，但随后发来验证邮件，已在 11-23 晚点击确认，邮箱显示 Verified。没有建游戏项目，也没有上传文件。资料设置在 `/user/settings`。 |
| 2026-11-23 | 1 | Game Jolt | puzzlebento | [gamejolt.com/@puzzlebento](https://gamejolt.com/@puzzlebento) | https://puzzlebento.com/games/sudoku/ | 资料页 Website 字段 + bio "Free online sudoku in your browser, from easy to expert — no sign-up…" | nofollow noopener | 已上线 | 注册时有 reCAPTCHA 图片验证（已过）；必须点邮件授权链接后才能登录，未授权一周内删号。资料编辑页是 `/dashboard/profile/edit`。可见性在登录状态下确认。没有发帖、没有建游戏项目。 |
| 2026-11-23 | 1 | Carrd | PuzzleBento（邮箱登录） | [puzzlebento.carrd.co](https://puzzlebento.carrd.co/) | https://puzzlebento.com/ | PuzzleBento | 无 rel（dofollow） | 已上线 | 注册有 reCAPTCHA（已过）。免费版必须先点邮件验证链接，站点才会真正上线（验证前显示 Not online yet / Page not found），验证后自动重新发布。用 Blank Page 模板，页面有标题、一句介绍和一个文字链接，底部带 "Made with Carrd"。自定义域名为 Pro 功能。 |
| 2026-11-23 | 1 | About.me | - | - | https://puzzlebento.com/ | PuzzleBento games | 未知 | 注册受阻 | `about.me/signup` 跳到 `/signup/start`，只有 Facebook 和 Google 两种注册方式，没有邮箱注册，专用邮箱注册不了。免费版提供 about.me/用户名 页面。如果以后要做，需要 Gary 用自己的 Google 账号登录。 |
| 2026-11-23 | 1 | Ko-fi | PuzzleBento（puzzlebento） | [ko-fi.com/puzzlebento](https://ko-fi.com/puzzlebento) | https://puzzlebento.com/ | 社交链接图标（无锚文本）+ About 里纯文本 "Play at puzzlebento.com." | nofollow noopener noreferrer | 已上线 | 注册无验证码，但要输入邮件里的 4 位验证码。Settings > Profile 里的 Website 字段保存后公开页不显示，必须在 "Your social links" 加自定义链接才会出现（图标形式）。About 只能写纯文本。没有绑定收款，页面会提示 payment setup。 |
| 2026-11-24 | 2 | indiexpo | puzzlebento | [indiexpo.net/en/games/2048-online-puzzle-cupcake](https://www.indiexpo.net/en/games/2048-online-puzzle-cupcake) | https://puzzlebento.com/games/2048/ | 标题 "2048 Online - Puzzle & Cupcake"（标题上限 30 字符，已缩短）；Website 字段 + 描述正文里的 URL | nofollow noopener | 已上线 | 注册无验证码，要点邮件确认链接才能用。个人资料页没有 bio 和网站字段，资料页 [/en/users/puzzlebento](https://www.indiexpo.net/en/users/puzzlebento) 只列出游戏标题，没有外链。游戏页的 Download 用外部链接，没有上传文件；站方提示 30 天内不满 15 个玩家会被归档。 |
| 2026-11-24 | 2 | フリーゲーム夢現 | - | - | https://puzzlebento.com/ja/games/sudoku/ | 数独 - 無料のオンラインナンプレ | 未知 | 注册受阻 | 我电脑上的浏览器打不开 freegame-mugen.jp（首页和 /publish/ 都报 ERR_HTTP2_PROTOCOL_ERROR，curl 握手后返回空响应），疑似屏蔽海外或云端 IP；用网页抓取工具能读到 /publish/ 页面。站规：要先注册账号，接受自有网站上的网页游戏，可以只投介绍不上传文件，每周限投 1 个，不欢迎一次性邮箱。之后可以开「经本机电脑转发流量」再试。 |
