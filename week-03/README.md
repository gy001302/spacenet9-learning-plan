# Week 3: 分割、Patch 推理与辅助先验

**本周目标：** 理解 segmentation/height 等先验为什么能提升配准质量，并补齐 patch-based 遥感推理思维。

## 本周建议节奏

- 每天 2 小时
- 先抓主线，不逐行抠代码
- 每天结束要有书面输出（3~5 条笔记或一张流程图）

## 每日主题

- Day 1: 语义分割基础 — 理解 encoder-decoder、mask 输出、为什么建筑 mask 可以过滤匹配。
- Day 2: 读第2名 building segmentor — 抓 process_image 主流程，理解 crop、pad、weight、merge。
- Day 3: 光学与 SAR 跨模态差异 — 专门补一下 SAR 的外观机制、speckle、为什么跨模态难。
- Day 4: 高度/地物先验为什么有效 — 理解 building filter、height filter 与可信匹配区域的关系。
- Day 5: 读第2名配置文件与 test.sh — 理解完整 pipeline 的模块连接关系，不急着抠 registration 实现。
- Day 6: Patch 级推理再复盘 — 把第2名和第3/5名里的 patch 思想对齐起来。
- Day 7: 本周复盘 — 输出：为什么高排名方案不会盲目全图匹配。
## 本周核心问题

- 为什么 building / height 先验能帮助配准？
- 为什么高排名方案不做“盲目全图匹配”？
- 分割在这里是最终任务还是辅助模块？

## 建议最低完成线

- 至少完成：看懂第2名 test.sh 和 building segmentor 的角色。
