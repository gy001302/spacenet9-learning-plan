# Week 2：几何变换模型与鲁棒估计

**本周目标：** 理解 translation / affine / homography / TPS 的表达能力差异，以及 RANSAC 为什么存在。

## 本周主问题

- 什么情况下平移就够？
- affine 与 homography 各解决什么问题？
- 为什么匹配点不能直接拿来拟合？

## 本周流程图

```text
correspondence
    ↓
选择 warp model
    ├─ translation
    ├─ affine
    ├─ homography
    └─ 更灵活局部模型 / TPS
    ↓
robust fitting（RANSAC）
    ↓
更可信的几何关系
```

## 每日推进

- Day 1：translation
- Day 2：affine
- Day 3：homography
- Day 4：outlier / inlier
- Day 5：RANSAC
- Day 6：几何模型在 SpaceNet 代码里的位置
- Day 7：模型比较

## 本周结束后你应该会什么

- 能用自己的话解释这一周的核心算法对象
- 能把这一周学的对象映射到源码中的某个模块
- 能指出这一周内容在整个 SpaceNet 理解路线中的位置
