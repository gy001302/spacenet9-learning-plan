# Week 5：机器学习与 PyTorch 最小工作流

**本周目标：** 不是泛学深度学习，而是补到足以读懂 SpaceNet 相关模型与推理/训练代码。

## 本周主问题

- PyTorch 代码里最关键的数据流是什么？
- 训练脚本和推理脚本各负责什么？
- 读模型代码最少要掌握到什么程度？

## 本周流程图

```text
数据
    ↓
Dataset / DataLoader
    ↓
model(input) -> output
    ↓
loss / optimizer / checkpoint
    ↓
inference / evaluation
```

## 每日推进

- Day 1：tensor / shape / device
- Day 2：Dataset / DataLoader
- Day 3：model forward / checkpoint
- Day 4：训练 loop
- Day 5：推理 loop
- Day 6：最小 PyTorch 实验
- Day 7：映射到 SpaceNet baseline / 研究生方案

## 本周结束后你应该会什么

- 能用自己的话解释这一周的核心算法对象
- 能把这一周学的对象映射到源码中的某个模块
- 能指出这一周内容在整个 SpaceNet 理解路线中的位置
