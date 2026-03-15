# 从 GIS 过渡到 SpaceNet 源码：算法学习计划

> 目标不是“了解一个比赛”，而是：
>
> **从已有 GIS 基础出发，补齐 CV、机器学习、配准算法与 PyTorch，最终能看懂 SpaceNet 相关源码。**

## 这套计划解决什么问题

很多 GIS 背景的学习者会遇到同一个断层：

- GIS / 遥感基础不差
- Python 也能用
- 但一看到 SpaceNet、matcher、registration pipeline、U-Net、RANSAC、offset map 这些源码和算法实现，就会卡住

卡住的原因通常不是“不会编程”，而是中间断了一层：

1. **CV 的问题建模方式**
2. **机器学习 / 深度学习的最小工作流**
3. **配准算法的核心对象与几何模型**
4. **PyTorch 代码阅读与最小实验能力**

这套计划就是专门填这条鸿沟。

## 总路线：从 GIS 走到 SpaceNet 源码

```text
GIS / 遥感基础
    ↓
CV 如何表示图像关系（correspondence / warp / displacement）
    ↓
配准算法（translation / affine / homography / TPS / sparse→dense）
    ↓
鲁棒估计与匹配（RANSAC / feature matching / learned matcher）
    ↓
机器学习与 PyTorch 最小工作流
    ↓
分割、patch inference、先验辅助
    ↓
SpaceNet 方案与源码理解
```

## 学习目标分解

### 第一层：问题建模
你要先知道 SpaceNet 代码到底在求什么，不然看到变量也只是“看见名字”。

### 第二层：算法骨架
你要学会：
- correspondence
- offset
- dense displacement field
- warp model
- global vs local registration
- sparse→dense

### 第三层：代码映射
你要能把一个算法问题映射到源码中：
- 这里在做什么估计？
- 这里的输入输出是什么？
- 为什么要有这个模块？

### 第四层：工程化理解
你要看懂：
- patch inference
- segmentation 先验
- refinement
- pipeline 组织方式

## 每周学习结构（统一模板）

每周都是一个完整主题单元，而不是零碎任务堆积。每周固定包含：

1. **本周主题**
2. **本周主问题**
3. **本周流程图**
4. **每日推进位置**
5. **最小代码例子**
6. **周末总结与自测**

## 时间分配

### 主学习时间（每天约 2 小时）
- 读概念讲解
- 看/跑最小代码例子
- 回到 SpaceNet 代码找映射
- 写总结

### 碎片时间（3~15 分钟）
- 术语卡
- 问题卡
- 流程图卡
- 微阅读

## 目录导览

- `week-01/`：从 GIS 到 CV：配准问题的数学对象
- `week-02/`：几何变换模型与鲁棒估计
- `week-03/`：从传统特征到现代 matcher
- `week-04/`：从 sparse correspondence 到 dense field
- `week-05/`：机器学习与 PyTorch 最小工作流
- `week-06/`：分割、patch inference 与先验辅助
- `week-07/`：把算法映射回 SpaceNet 方案与源码
- `week-08/`：复现准备与代码理解闭环

## 最终结果

学完后，你应该能做到：

- 从算法角度解释 SpaceNet 在求什么
- 看懂 correspondence / offset / warp / registration 相关代码
- 看懂为什么会有 RANSAC、matcher、sparse→dense、local reg
- 看懂为什么第 2 名方案会引入 segmentation / height prior
- 具备继续深入看 SpaceNet 代码和改造 baseline 的能力


## 书籍与参考资料

- 见 `BOOKS-AND-REFERENCES.md`
- 其中区分了：主线教材、辅助教材、查阅书、模型/论文官方入口
