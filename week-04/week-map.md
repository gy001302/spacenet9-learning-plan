# Week 4：从 sparse correspondence 到 dense field

**本周目标：** 把配准最关键的一步吃透：如何从少量对应关系走向全图位移场。

## 本周主问题

- 为什么 sparse matching 不等于 dense registration？
- affine 路线和 sparse→dense 插值路线有什么区别？
- local registration 为什么会出现？

## 本周流程图

```text
sparse correspondence
    ↓
稀疏位移估计
    ↓
全局几何模型 / 插值 / 局部建模
    ↓
dense displacement field
    ↓
offset map
```

## 每日推进

- Day 1：sparse displacement
- Day 2：global transform 路线
- Day 3：interpolation / TPS 路线
- Day 4：local deformation 直觉
- Day 5：最小 sparse→dense 实验
- Day 6：映射到第 4 名方案
- Day 7：总结

## 本周结束后你应该会什么

- 能用自己的话解释这一周的核心算法对象
- 能把这一周学的对象映射到源码中的某个模块
- 能指出这一周内容在整个 SpaceNet 理解路线中的位置
