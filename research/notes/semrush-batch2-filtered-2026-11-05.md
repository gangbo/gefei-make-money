# Semrush 过滤后短名单 · 2026-11-05

规则：美国库 Keyword Overview；**过滤掉 US 量 ≤ 100 或未收录** 的词（含 0、20、40 档）。

## 已过滤（低量 / 无数据）
- packing slip generator — 40
- credit note generator — 20
- timesheet invoice calculator — 0
- payment reminder email generator — 0
- travel packing list generator — 20
- late fee invoice calculator — 20
- commercial invoice generator — 110 → **边缘保留线**：刚好 >100，见下方「保留」；若你想更严（如 ≥200）可再砍

## 保留（US 量 > 100）

| 关键词 | US 量 | KD | 建议 |
|---|---|---|---|
| purchase order generator | 390 | 13% | InvoiceNeat 内页优先 |
| packing list generator | 260 | 10% | InvoiceNeat / 货运文件 |
| christmas wishlist maker | 720 | 39% | 季节窗口 |
| secret santa generator | 33.1K | 58% | 量大但难，季节红海 |
| white elephant generator | 170 | 19% | 季节、相对好打 |
| cron expression generator | 1.3K | 36% | 独立开发者工具 |
| jwt decoder | 6.6K | 53% | 量大偏红海 |
| robots.txt generator | 2.4K | 55% | 偏红海 |
| llms.txt generator | 2.9K | 46% | 新词，可做 |
| AI token counter | ~210 | 38% | 可做轻量页 |
| EXIF remover | 1.0K | 37% | 本地隐私差异化 |
| HEIC to JPG | 246K | 32% | 极大红海，谨慎 |
| Open Graph preview | 260 | 31% | SEO 小工具 |

## 立项优先（过滤后）
1. purchase order generator  
2. packing list generator  
3. llms.txt generator  
4. cron expression generator  
5. EXIF remover  
6. christmas wishlist / white elephant（赶季节）  
7. Open Graph preview / AI token counter（轻量）

仍建议暂缓硬刚：HEIC to JPG、jwt decoder、robots.txt、secret santa（除非只做差异化极强的隐私本地版）。
