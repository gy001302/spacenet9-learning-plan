# Week 4: 第2名主干：global/local registration

**本周目标：** 进入完整 pipeline 核心：多 matcher、多尺度、全局+局部配准、refinement。

## 本周建议节奏

- 每天 2 小时
- 先抓主线，不逐行抠代码
- 每天结束要有书面输出（3~5 条笔记或一张流程图）

## 每日主题

- Day 1: 读 registration_pipeline 总览 — 先抓 run_full_registration_pipeline / run_registration_stage 两个入口。
- Day 2: global registration — 理解为什么先做全局估计，RANSAC 起什么作用。
- Day 3: local registration — 理解 crop 内局部估计、为什么能补偿非线性位移。
- Day 4: global + local 融合 — 读 weighted average / local weight map 聚合，理解 overlap 和融合。
- Day 5: matcher ensemble 与多尺度 — 理解为什么多 matcher、多尺度能提升稳健性。
- Day 6: refinement stage — 理解 coarse-to-fine pipeline 如何进一步修正位移。
- Day 7: 本周复盘 — 写一页：第2名为什么是“系统级”方案。
## 本周核心问题

- global registration 和 local registration 分别解决什么问题？
- 为什么第2名需要 refinement stage？
- 多 matcher、多尺度为什么能提升稳健性？

## 建议最低完成线

- 至少完成：讲清 global/local/refinement 三层关系。
