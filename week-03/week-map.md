# Week 3：从传统特征到现代 matcher

**本周目标：** 补齐“对应点是怎么来的”这条线：SIFT/ORB、SuperPoint、LightGlue、LoFTR、RoMa。

## 本周主问题

- 传统特征为什么会失败？
- learned matcher 带来了什么？
- 为什么 SpaceNet 方案经常 heavily rely on matcher？

## 本周流程图

```text
图像对
    ↓
提取/构建对应关系
    ├─ 传统特征（SIFT / ORB）
    ├─ learned local features（SuperPoint）
    ├─ learned matcher（LightGlue）
    ├─ detector-free matching（LoFTR）
    └─ dense / robust matching（RoMa）
    ↓
correspondence set
```

## 每日推进

- Day 1：传统特征基线
- Day 2：局部特征学习
- Day 3：LightGlue
- Day 4：LoFTR
- Day 5：RoMa
- Day 6：matcher 对比实验
- Day 7：映射到 SpaceNet 第 3/4/5 名

## 本周结束后你应该会什么

- 能用自己的话解释这一周的核心算法对象
- 能把这一周学的对象映射到源码中的某个模块
- 能指出这一周内容在整个 SpaceNet 理解路线中的位置
