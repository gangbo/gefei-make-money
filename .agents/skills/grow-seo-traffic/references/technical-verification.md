# 技术 SEO 上线验证

## 抓取与索引

- 直接请求无查询参数的 `robots.txt` 和 sitemap。
- 检查状态码、最终 URL、正文、`cache-control`、`Age`、`last-modified` 和 CDN cache status。
- 确认需要 `noindex` 的页面允许爬虫访问并在原始 HTML 中输出指令。
- 确认公开页面没有意外 noindex 或 robots 阻塞。

## URL 信号

- canonical 指向最终 200 URL；
- hreflang 双向、语言正确并包含 x-default（如项目使用）；
- sitemap 只包含 canonical、可索引 URL；
- 重定向不存在循环、链或跨域绕过；
- 不用每次构建时间伪造全站 lastmod。

## 页面与结构化数据

- 原始 HTML 的 title、description、H1、lang 与页面语言和意图一致；
- JSON-LD 的名称、URL、描述、语言和页面可见内容一致；
- 内部链接可以发现目标页面；
- 移动端不存在遮挡、横向溢出或工具不可用。

## 验证证据

把原始响应、headers、截图或检查摘要保存到
`docs/grow-seo-traffic/raw/YYYY-MM-DD/technical/`，并在 `data-checklist.md` 中记录实际采集时间、
来源和覆盖项。搜索引擎摘要可能滞后，不能用它证明部署失败；带查询参数的新缓存键也不能证明裸 URL
已更新。
