# 游戏开发 AI Skill / MCP 调研（给个人开发者 Gary）

研究日：2026-11-10（America/New_York，EST）
范围：给 Cursor / Claude Code 等 AI 编程助手用的技能包（SKILL.md）、Cursor rules、skills 市场、编辑器 MCP。面向单指休闲 2D/2.5D 小游戏，引擎候选为 Godot / Unity / Cocos Creator，发布目标为微信小游戏、抖音小游戏等。
方法：WebSearch、逐个 URL 的 HTTP 状态检查（200 才列入主清单）、GitHub REST API 读取星数与 `pushed_at`、公开 X 搜索。不安装、不发帖、不编造星数或日期。
核验时间：2026-11-10 约 8:50 PM EST。星数与最近代码推送均来自当时的 `https://api.github.com/repos/{owner}/{repo}`；日期按 `pushed_at`（最近一次代码推送）换算到用户时区，不用会随加星而变动的 `updated_at`。

## 先给结论

**先装 [Awesome Gamedev Agent Skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills)，再按选定引擎加一个编辑器 MCP。若首发微信/抖音，还要单独补 Cocos 技能包，因为主流跨引擎包里没有 Cocos。**

前 3 推荐（按 Gary 的目标，不是按星数）：

1. **Awesome Gamedev Agent Skills**（必装）。77 个 SKILL.md + 路由器，覆盖 Godot 4.7、Unity 6.3 LTS，以及 `game-feel`（juice）、`game-ui-ux`、`create-game-assets`、关卡设计。同一套文件可用于 Cursor 和 Claude Code。这是当前最完整、也最适合先试的开源技能包。
2. **按引擎选一个编辑器 MCP，让助手能改场景、跑游戏，而不只改文本文件。** Godot 优先 [Godot AI](https://github.com/hi-godot/godot-ai)（维护更活跃，要求 Godot 4.7+）。Unity 优先官方 [Unity-Technologies/skills](https://github.com/Unity-Technologies/skills)（Cursor 可直接装）再加 [MCP for Unity](https://github.com/CoplayDev/unity-mcp)。
3. **若首发微信/抖音：补 [Cocos Creator Skill](https://github.com/hsiaozzz/cocos-creator-skill)，并配 [cocos-mcp-server](https://github.com/DaxianLee/cocos-mcp-server)。** 星数远低于 Godot/Unity 工具，但是现成且针对国内引擎的缺口补丁；官方跨引擎包目前列的是 Godot、Unity、Unreal、Phaser 等，不含 Cocos。

画面不好看，不必另找一个独立的 “juice skill 仓库”：上述第 1 项里已经有 `game-feel`、`game-ui-ux`、`create-game-assets`。像素图生成可再试 [SpriteCook skills](https://github.com/SpriteCook/skills)，有免费额度，但免费档每月约 40 积分（默认模型大约只能生成几张图），引擎导出和私有素材在付费档。

不要一上来就装星数最高的 [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)（约 3.8 万星）。它主要为 Claude Code 设计，当前 README 主路径是浏览器原型，对 Cursor + 微信/抖音小游戏不是最贴合的第一步。

X 上 2026 年 10–11 月有不少人转发 Awesome Gamedev Agent Skills，也有把 Claude Code Game Studios、Godot MCP、Unity MCP 放在一起的合集帖。这只能当发现线索；帖子里的星数往往过时或互相矛盾，下面一律以 GitHub API 为准。

---

## 使用建议（结合你现在的方向）

- **先定技能包，再定引擎 MCP。** 技能包教助手怎么写 GDScript/C#、怎么做按钮回弹和击碎反馈；MCP 让它打开编辑器、改节点、跑一局看控制台。两者互补，不是二选一。
- **微信/抖音首发时，Cocos 仍值得单独准备。** 即使你后面选 Godot 或 Unity，也要自己核实当前小游戏导出和广告 SDK 是否够用；不要假设跨引擎技能包已经覆盖国内小游戏发布。
- **Juice / UI 优先用现成 skill，而不是再让模型自由发挥一套默认蓝灰界面。** `game-feel` 里有屏幕震动、hit-stop、缓动回弹、粒子的引擎中性做法，并带 Godot 4.7 / Unity 6.3 示例。
- **本轮没有安装任何技能或 MCP，也没有改你的 Cursor 配置。** 下面只列出已核实存在的项目，供你决定后再装。

---

## 前 3 推荐详表

### 1. Awesome Gamedev Agent Skills（首选，必装）

- 准确名称：`gamedev-skills/awesome-gamedev-agent-skills`
- URL：[GitHub](https://github.com/gamedev-skills/awesome-gamedev-agent-skills)（HTTP 200）；市场页 [skills.sh](https://www.skills.sh/gamedev-skills/awesome-gamedev-agent-skills)（HTTP 200）；介绍页 [opensourcegames.dev](https://opensourcegames.dev/game-dev-agent-skills)（HTTP 200）
- 适用工具：Cursor、Claude Code、Codex、Gemini CLI、GitHub Copilot、Windsurf、Cline 等能加载 Agent Skills / `SKILL.md` 的助手。安装示例：`npx skills add gamedev-skills/awesome-gamedev-agent-skills`，Cursor 可用 `-a cursor`
- 用途：给助手一套按需加载的游戏开发手册。仓库 README 写明 **77 个技能 + 1 个 router**；Godot 16 个（含 `godot-gdscript`、`godot-ui-control`、`godot-animation`、`godot-2d-movement`、`godot-export` 等，基线 Godot 4.7），Unity 8 个（基线 Unity 6.3 LTS），另有跨引擎的 `game-feel`、`game-ui-ux`、`create-game-assets`、`level-design`、`audio-design`。路由器会先识别引擎再只加载相关技能，避免 70 多个文件同时进上下文。许可证 Apache-2.0
- 星数 / 最近代码推送：**8201 星**；最近推送 **2026-11-10 9:52 AM EST**
- 是否适合 Gary：**适合，而且应作为第一项。** 正好覆盖你要的单指休闲 2D、按钮/击碎反馈、关卡和导出。技能包本身不含 Cocos，也不等于已经支持微信/抖音发布。skills.sh 页面当时显示 “78 skills、约 75 万次安装”，安装次数是市场页自称，本轮未独立审计；“78” 与仓库 README 的 “77 + router” 可能是计数口径不同

### 2a. Godot AI（选 Godot 时的编辑器 MCP）

- 准确名称：`hi-godot/godot-ai`（Godot AI）
- URL：[https://github.com/hi-godot/godot-ai](https://github.com/hi-godot/godot-ai)（HTTP 200）
- 适用工具：Cursor、Claude Code、Codex 及其他 MCP 客户端。在 Godot 插件坞里可给常见客户端生成配置
- 用途：把助手连到**正在运行的 Godot 编辑器**。README 写明 46 个工具、120+ 操作，可建场景、改节点和脚本、接线信号、配置 UI、材质、动画、粒子、相机。需要 **Godot 4.7+** 和 `uv`。许可证 MIT。README 另有遥测活跃安装数字，那是项目自称，本轮未核实
- 星数 / 最近代码推送：**3485 星**；最近推送 **2026-11-10 9:56 AM EST**（当天仍在更新）
- 是否适合 Gary：**选 Godot 时适合，作为第 2 优先。** 比更早出现、星数更高的 Coding-Solo 方案维护更勤。代价是必须用 Godot 4.7+，并在本机跑编辑器插件

同类备选，不进前 3：

- [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp)（HTTP 200）：**6597 星**，可启动编辑器、运行项目、抓调试输出，支持 Cursor / Claude Code（`npx @coding-solo/godot-mcp`）。最近代码推送 **2026-04-16 7:37 PM EDT**，已约 7 个月没有推送，星数高不等于现在更该用
- [tomyud1/godot-mcp](https://github.com/tomyud1/godot-mcp)（HTTP 200，现亦称 Godlink MCP）：**453 星**，最近推送 **2026-10-17 10:01 AM EDT**。带 Godot 插件，强调直接读写场景和节点，需要 Godot 4.4+

### 2b. Unity 官方 Skills + MCP for Unity（选 Unity 时并列第 2）

**Unity Skills（官方技能包）**

- 准确名称：`Unity-Technologies/skills`
- URL：[GitHub](https://github.com/Unity-Technologies/skills)（HTTP 200）；[skills.sh](https://www.skills.sh/unity-technologies/skills)（HTTP 200）
- 适用工具：Cursor、Claude Code、GitHub Copilot、Cline 等。Cursor 安装：`npx skills add Unity-Technologies/skills`
- 用途：官方 Unity 工作流技能。README 示例包括修复像素画模糊/抖动、做 Tile Palette、内购、用 Unity CLI 装编辑器。skills.sh 列表可见 `ui-ugui`、`ui-uitk`、`2d-pixel-perfect`、`sprite-editor`、`optimize-web` 等，对 2D 休闲和像素表现有直接帮助。仓库由 Unity 自动发布，不接受 PR
- 星数 / 最近代码推送：**1238 星**；最近推送 **2026-11-06 11:35 AM EST**
- 是否适合 Gary：**选 Unity 时适合。** 这是官方、可在 Cursor 里直接用的技能包。注意：另一份官方插件 [unity-agent-plugin](https://github.com/Unity-Technologies/unity-agent-plugin)（HTTP 200；**629 星**；最近推送 **2026-11-10 3:46 PM EST**）README 写明面向 Claude Code、Codex、Grok、Antigravity、GitHub Copilot CLI，**没有把 Cursor 列为支持端**。在 Cursor 里应装 `Unity-Technologies/skills`，不要把两份仓库当成同一件事

**MCP for Unity（社区，星数最高的 Unity 编辑器桥）**

- 准确名称：`CoplayDev/unity-mcp`（MCP for Unity）
- URL：[GitHub](https://github.com/CoplayDev/unity-mcp)（HTTP 200）；文档站 [coplaydev.github.io/unity-mcp](https://coplaydev.github.io/unity-mcp/)（HTTP 200）
- 适用工具：任意 MCP 客户端，README 点名 Claude Desktop / Claude Code、Cursor、VS Code、Windsurf、Cline、Gemini CLI 等
- 用途：让助手在 Unity 编辑器里建场景、改 GameObject、编辑 C#、管资源、跑测试、构建。README 写 50 个工具入口；要求 Unity 2021.3 LTS 到 6.x，以及 Python 3.10+（`uv`）。许可证 MIT。最近发行说明写到 v10.3.0（2026-10-04）
- 星数 / 最近代码推送：**15867 星**；最近推送 **2026-10-30 2:15 PM EDT**
- 是否适合 Gary：**选 Unity 时适合，和官方 skills 一起用。** 它解决的是“编辑器控制”，官方 skills 解决的是“按 Unity 文档来写”

Unity MCP 的活跃替代：[IvanMurzak/Unity-MCP](https://github.com/IvanMurzak/Unity-MCP)（HTTP 200；站点 [ai-game.dev](https://ai-game.dev) 亦 200）。**4615 星**，最近推送 **2026-11-10 7:02 PM EST**。同时提供 MCP、可按项目生成 skills、以及运行时（进游戏内）能力。支持 Cursor / Claude Code。若你希望一套工具里同时有 MCP 和技能生成，可以评估它，而不必和 Coplay 重复安装两套桥

### 3. Cocos Creator Skill + cocos-mcp-server（首发微信/抖音时补上）

**Cocos Creator Skill**

- 准确名称：`hsiaozzz/cocos-creator-skill`
- URL：[https://github.com/hsiaozzz/cocos-creator-skill](https://github.com/hsiaozzz/cocos-creator-skill)（HTTP 200）；中文说明 [README.zh-CN.md](https://github.com/hsiaozzz/cocos-creator-skill/blob/master/README.zh-CN.md)
- 适用工具：同一份 `SKILL.md` 可用于 Cursor、Claude Code、Codex、GitHub Copilot、Gemini CLI 等。安装：`npx skills add hsiaozzz/cocos-creator-skill -a cursor`（或 `--all`）
- 用途：面向 **Cocos Creator 3.8.x / COCOS 4** 的工作流技能：确认版本 → 定位代码 → 编写 → 强制验证 → 提交前自查。含 API 速查、性能、多平台发布、3.8 到 COCOS 4 迁移，以及工程体检脚本。许可证 MIT
- 星数 / 最近代码推送：**23 星**；最近推送 **2026-09-11 2:17 AM EDT**（约两个月未推送）
- 是否适合 Gary：**若走 Cocos / 国内小游戏，适合作为技能层补丁。** 星数低、维护节奏一般，但它填的是大包没有的引擎空缺。不能单凭星数否定

**Cocos Creator MCP Server**

- 准确名称：`DaxianLee/cocos-mcp-server`
- URL：[https://github.com/DaxianLee/cocos-mcp-server](https://github.com/DaxianLee/cocos-mcp-server)（HTTP 200）
- 适用工具：README 写明已测 Claude 客户端、Claude CLI 和 Cursor；其他 MCP 客户端原则上可用
- 用途：Cocos Creator 3.8+ 编辑器 MCP 插件，开源版 README 称约 50 个工具，覆盖场景、节点、组件、预制体、资源。有中文文档。注意：仓库同时推广 VberAI 的 **Pro 版**（更多工具和模块），开源版与 Pro 不是同一完整度。许可证字段在 API 中为 `None`（未检测到 SPDX），商用前要自己读仓库许可说明
- 星数 / 最近代码推送：**1485 星**；最近推送 **2026-07-08 3:19 AM EDT**（约 4 个月未推送）
- 是否适合 Gary：**选 Cocos 时适合试用开源版，先不要被 Pro 页面带着走。** 维护间隔比 Godot AI / Unity 官方包更长，接入后要用自己的项目验证能不能稳定改场景、出预览

---

## 其他值得知道、但不进前 3 的项目

### SpriteCook Agent Skills（像素/UI 素材生成）

- 准确名称：`SpriteCook/skills`；Cursor 插件为 `SpriteCook/cursor-plugin`
- URL：[skills 仓库](https://github.com/SpriteCook/skills)（HTTP 200）、[cursor-plugin](https://github.com/SpriteCook/cursor-plugin)（HTTP 200）、[Claude 插件](https://github.com/SpriteCook/claude-plugin)（HTTP 200）、[Cursor 介绍](https://www.spritecook.ai/cursor)（HTTP 200）、[定价页](https://www.spritecook.ai/pricing)（HTTP 200）
- 适用工具：Cursor（官方插件 + 托管 MCP `https://mcp.spritecook.ai/mcp/cursor`，浏览器登录，不必先准备 API key）、Claude Code、以及其他能加载这些 SKILL.md 的助手
- 用途：教助手用 SpriteCook 生成像素或高清精灵、图块、UI kit、短动画，并尽量用 `reference_asset_id` 保持风格统一；另有 Godot 导出工作流 skill。技能仓库本身是 MIT；**生成服务是 SpriteCook 账号 + 积分**。定价页（本轮读取）：免费档每 30 天 40 积分、无需绑卡，含 MCP/API 和商用授权；默认模型约 12 积分/张，因此免费档大约只够几张图。Unity/Godot/sprite sheet 导出、私有素材、Edit with Agent 从 $8/月 的 Starter 档开始。免费生成会进公共画廊
- 星数 / 最近代码推送：skills 仓库 **55 星**，最近推送 **2026-10-22 12:15 PM EDT**；cursor-plugin **1 星**，同日推送
- 是否适合 Gary：**值得稍后试，不建议当成第一依赖。** 它直接对应“AI 做出来的界面很难看”，但免费额度很紧，且风格一致性取决于工作流，不是装上就自动变精美。可先用 Kenney 等成套免费素材，再加上面第 1 项里的 `create-game-assets` / `game-ui-ux`

### Game Dev Agentic Skills（更深的 Godot 技能库）

- 准确名称：`thedivergentai/Game-Dev-Agentic-Skills`（GDAS）
- URL：[GitHub](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)（HTTP 200）；[skills.sh](https://www.skills.sh/thedivergentai/game-dev-agentic-skills)（HTTP 200）
- 适用工具：可通过 `npx skills add thedivergentai/game-dev-agentic-skills` 安装，面向 Claude Code / Cursor 等
- 用途：偏 Godot 4.7+（兼 Bevy）的大型技能库，含 UI 主题、容器、Tween、粒子、2D 动画、输入、TileMap 等。体量很大。许可证 LGPL-3.0（与 Apache/MIT 技能包不同，嵌入或再分发时要自己看条款）
- 星数 / 最近代码推送：**949 星**；最近推送 **2026-10-16 4:58 PM EDT**
- 技能数量：仓库 README 徽章写 **184**；skills.sh 页面写 **229 skills**。本轮未逐个清点文件，不采用其中某一个当精确值
- 是否适合 Gary：**可作为 Godot 加深用的第二套，不要和 Awesome 包同时全量灌进同一个项目。** 先用带路由器的那套，避免技能互相抢上下文

### Claude Code Game Studios（星数最高，但不建议作为第一步）

- 准确名称：`Donchitos/Claude-Code-Game-Studios`
- URL：[https://github.com/Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)（HTTP 200）
- 适用工具：主要为 **Claude Code**（斜杠命令 / 多 agent 工作流）。不是一份轻量、即插即用的 Cursor skill 包
- 用途：GitHub 仓库简介仍写 “49 AI agents, 72 workflow skills”。当前 README 开头则是：在该仓库副本里用 Claude Code 描述游戏，生成一页 brief，再做出可双击打开的**浏览器原型**。两者表述不完全一致，本轮没有把整个模板跑一遍，所以不当成“已经替你接好 Godot/Unity/微信小游戏”
- 星数 / 最近代码推送：**38081 星**；最近推送 **2026-11-09 6:33 PM EST**
- 是否适合 Gary：**现在不优先。** 热度高、持续更新，但路径偏 Claude Code 和网页原型，和你要发布到微信/抖音、并用 Cursor 做 2D/2.5D 小游戏的目标不完全重合。以后若想用 Claude Code 快速试玩法，可以再单独评估

### Godogen（自主生成游戏流水线）

- 准确名称：`htdt/godogen`
- URL：[https://github.com/htdt/godogen](https://github.com/htdt/godogen)（HTTP 200）
- 适用工具：Claude Code、Codex；发布时选择引擎（Godot C# / GDScript、Bevy、Babylon.js、three.js）
- 用途：不是“给现有项目加技能”，而是一套生成器：先发布到新的游戏仓库，再让 agent 搭工程、生成素材、运行并用画面/录像验证。默认可用其配套的本地免费素材生成。不覆盖 Unity、Cocos，也不是微信/抖音发布工具
- 星数 / 最近代码推送：**7320 星**；最近推送 **2026-10-16 10:56 AM EDT**
- 是否适合 Gary：**暂不作为主工具。** 更像“放手让 agent 做一整个原型”，对你这种要自己把控玩法和发布渠道的项目，控制力不如“技能包 + 编辑器 MCP”

---

## 明确未采用或核验失败的条目

- **`jayesh-bansal/game-juice`**：搜索引擎和部分技能目录仍能搜到，但本轮访问 `https://github.com/jayesh-bansal/game-juice` 与 GitHub API 均为 **404**。不推荐、不写星数。juice 需求改用 Awesome 包中的 [`game-feel`](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/main/skills/disciplines/game-feel/SKILL.md)（HTTP 200，已读到正文，含震动、hit-stop、缓动示例）
- **[cursor.directory/rules/game-development](https://cursor.directory/rules/game-development)**：本轮请求返回 **429**，未核验页面内容，不列入推荐
- **GitHub WebFetch 抓到的星数经常是 0**：这是抓取页面的伪影，已全部改用 GitHub API。不要用网页抓取结果当星数

---

## 公开 X 讨论（只作线索）

本轮用 X `search_posts_all` 查了 2025 年以降的英文帖，主要信号如下。转发量和话术不能代替仓库核验。

- Awesome Gamedev Agent Skills 在 2026 年 10 月中下旬被多次介绍，例如 [Voxyz_ai 2026-10-24](https://x.com/Voxyz_ai/status/2114099613808353561)、[rammcodes 2026-10-21](https://x.com/rammcodes/status/2112979088705302587)、[naveendas96 2026-10-25](https://x.com/naveendas96/status/2114359712095625546)（该帖当时写 4.1K 星，已过时）、[Alvinzzz1122 2026-11-10](https://x.com/Alvinzzz1122/status/2120093532434354282)（该帖写 awesome 包 8089 星、godogen 7315 星，与数小时后的 API 数字接近但也不应再引用）
- 另有把 Claude Code Game Studios、godot-mcp、unity-mcp 放进“AI 游戏工作室工具清单”的合集帖，例如 [seele_ai_game 2026-03-24](https://x.com/seele_ai_game/status/2036259788594819369)、[froessell 2026-11-04](https://x.com/froessell/status/2117905384950423696)、[Mnilax 2026-10-13](https://x.com/Mnilax/status/2110039818524660135)。合集帖传播广，质量参差，且常把官方插件、社区 MCP、多 agent 模板混在一起

---

## 建议的实际安装顺序（供你决定后执行，本轮未执行）

1. 在将要做的游戏项目根目录安装 Awesome Gamedev Agent Skills（Cursor 用 `-a cursor`），先用一小段需求试路由器，例如“给点击按钮加回弹和击碎粒子，不要改玩法规则”
2. 引擎一旦选定：Godot 4.7+ 装 Godot AI；Unity 装官方 `Unity-Technologies/skills` 再接 MCP for Unity（或二选一评估 IvanMurzak）；Cocos 3.8+ 装 `hsiaozzz/cocos-creator-skill` 再试开源 cocos-mcp-server
3. 若像素角色/UI 仍不够用，再开 SpriteCook 免费档做小规模试验，不要一开始就订月费
4. 先不要全量安装 Claude Code Game Studios、GDAS、Godogen，以免技能和代理互相抢上下文

---

## 来源与核验记录

- GitHub REST API（星数、`pushed_at`、许可字段）：本轮对所列仓库逐个请求 `GET /repos/{owner}/{repo}`
- 仓库 README：本轮通过 GitHub API 读取，用于核对用途和兼容工具，不引用未出现在 README/文档中的能力
- URL 存活：对文中主链接做 HTTP 状态检查；主清单均为 200，失败项单独写出
- skills.sh 安装次数与技能个数：来自市场页当时展示，未做独立审计
- X：公开搜索，不作星数来源
- 时区：`pushed_at` 为 UTC。2026-11-01 之后为 EST（UTC-5）；4 月、7 月、9 月、10 月条目为 EDT（UTC-4）

