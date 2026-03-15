# Week 1: 任务理解与配准主线

**本周目标：** 建立 SpaceNet9 任务地图，理解 tiepoints、offset map、跨模态配准、稀疏到稠密这条主线。

## 本周建议节奏

- 每天 2 小时
- 先抓主线，不逐行抠代码
- 每天结束要有书面输出（3~5 条笔记或一张流程图）

## 每日主题

- Day 1: 认识 SpaceNet9 任务 — 读比赛 README，写出输入/输出/评分。理解 optical→SAR registration 不是分类任务。
- Day 2: 图像配准是什么 — 建立 registration 的基本概念：source/target、全局与局部变换、对应点与误差。
- Day 3: RANSAC、Affine、Homography — 重点搞懂为什么匹配点需要去错、何时使用 affine/homography。
- Day 4: 从 tiepoints 到 offset map — 理解为什么比赛最终要交 dense offset map，而不是只交匹配点。
- Day 5: 读最简单方案：本科生方案 — 只抓主流程：matcher → transform → dense offset。
- Day 6: 读第4名方案：sparse→dense 路线 — 重点理解 matcher_roma.py、tiepoints_to_sparse.py、sparse_to_dense.py 三段怎么接。
- Day 7: 本周复盘 — 画出一张总流程图：两张图 → 匹配点 → 过滤/插值/变换 → dense offset map。
## 本周核心问题

- SpaceNet9 的输入、输出、评分分别是什么？
- 为什么它属于跨模态图像配准而不是分类/检测？
- 为什么最后必须输出 dense offset map？

## 建议最低完成线

- 至少完成：读 README + 写出任务定义 + 画一张主流程图。
