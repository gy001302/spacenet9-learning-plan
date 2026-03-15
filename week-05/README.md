# Week 5: 训练基础与可复现能力

**本周目标：** 从只会读推理代码，升级到能读训练脚本、理解 loss/optimizer/checkpoint。

## 本周建议节奏

- 每天 2 小时
- 先抓主线，不逐行抠代码
- 每天结束要有书面输出（3~5 条笔记或一张流程图）

## 每日主题

- Day 1: 训练循环基础 — 系统补 train/val loop、loss、optimizer、scheduler。
- Day 2: checkpoint 与实验流程 — 理解 best model、resume、保存权重。
- Day 3: 读 baseline 的 keypoint detection train.py — 抓输入、标签、loss、训练主循环，不深究网络细节。
- Day 4: 读研究生方案训练部分 — 看 keypoint_detection/train.py 和 config，理解遥感 keypoint detector 怎么训。
- Day 5: U-Net / segmentation training 复盘 — 建立“为什么 building segmentor 能训出来”的整体概念。
- Day 6: 最小可复现清单 — 整理如果自己复现第4名或轻量 baseline，需要哪些依赖/步骤。
- Day 7: 本周复盘 — 输出：推理脚本和训练脚本到底分别负责什么。
## 本周核心问题

- 训练脚本和推理脚本在职责上有什么区别？
- 要复现一个轻量方案，最少需要哪些 PyTorch 能力？
- 第1名为什么引入 depth / DEM，而不满足于纯几何拟合？

## 建议最低完成线

- 至少完成：读 1 个训练脚本并写出训练与推理的区别。
