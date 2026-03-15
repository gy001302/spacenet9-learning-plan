# Week 2: PyTorch 推理与现代 matcher

**本周目标：** 让 PyTorch 不再成为阅读障碍，理解现代 matcher 的输入输出、patch 推理和张量流。

## 本周建议节奏

- 每天 2 小时
- 先抓主线，不逐行抠代码
- 每天结束要有书面输出（3~5 条笔记或一张流程图）

## 每日主题

- Day 1: PyTorch 张量、shape、device — 系统补一下 B,C,H,W、cpu/cuda、model.eval/no_grad。
- Day 2: Dataset / DataLoader — 读懂 __getitem__、batch、collate、patch dataset。
- Day 3: 传统特征与现代 matcher 对比 — 建立 SIFT/ORB 与 SuperPoint/LoFTR/RoMa 的代际差异。
- Day 4: LightGlue / LoFTR / RoMa — 分别理解它们大概怎么做匹配、输出什么、适用何处。
- Day 5: 读第3名和第5名推理代码 — 重点看 patch、预处理、matcher 输入输出、结果汇总。
- Day 6: patch inference 基础 — 理解大图为什么切块、为什么 overlap、边缘为什么降权。
- Day 7: 本周复盘 — 输出一张张量流图：图像→tensor→model→prediction→merge。
## 本周核心问题

- 传统特征与现代 matcher 的差别是什么？
- PyTorch 推理代码里最关键的数据流是什么？
- 为什么遥感大图经常必须 patch inference？

## 建议最低完成线

- 至少完成：看懂 1 个推理脚本 + 搞懂 matcher 输出和 tensor shape。
