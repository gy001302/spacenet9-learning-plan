# Day 1 学习资料：SpaceNet9 到底在求什么

今天先不要一头扎进模型结构。先把任务本身看清楚。

核心问题只有一个：

> **SpaceNet9 到底在求什么空间关系？**

---

## 1. 先从比赛任务本身出发
SpaceNet9 不是分类、检测、分割竞赛。

它给你两张来自不同传感器的图：
- 一张 optical 图像
- 一张 SAR 图像

要求你输出一张 **2 通道 transformation map / offset map**：
- 第 1 个通道：x 方向位移
- 第 2 个通道：y 方向位移

也就是说，它不是问：
- 这张图里是什么类别？
- 这个目标在哪里？
- 每个像素属于什么类别？

而是在问：

> **optical 图上的这个位置，在 SAR 图里应该对应到哪里？**

这就是配准问题。

---

## 2. 配准的核心对象不是类别，而是 correspondence
如果 source 图里一个点 `(x, y)`，在 target 图里对应 `(x', y')`，这就是一个 **correspondence（对应关系）**。

配准任务最核心的问题，不是“识别内容”，而是：

> **找到两张图之间的空间对应关系。**

在 SpaceNet9 里，这种对应关系因为是 optical ↔ SAR 的跨模态关系，所以会比普通同模态图像更难。

---

## 3. 什么是 source / target
在 Day 1，你先用最简单的方式理解：

- **source**：你准备被移动/被对齐的那张图
- **target**：你希望对齐到的那张参考图

在 SpaceNet9 的描述里，可以先粗略理解为：
- optical 是 source
- SAR 是 target

更严谨地说，任务要预测 optical 图上每个像素应该向哪里移动，才能和 SAR 对齐。

---

## 4. 什么是 offset / displacement
如果 source 图上的点是 `(x, y)`，它在 target 图上的对应点是 `(x', y')`，那么位移就是：
- `dx = x' - x`
- `dy = y' - y`

所以：

> **offset / displacement = correspondence 的向量表达。**

一对 correspondence 说明“谁对应谁”；
一组 `(dx, dy)` 说明“应该往哪移、移多少”。

---

## 5. 什么是 offset map / dense displacement field
如果你只知道少量点的位移，那只是稀疏信息。

如果你能为 source 图中的每个像素都给出一个 `(dx, dy)`，那就得到了一张：
- offset map
- dense displacement field（稠密位移场）

这正是 SpaceNet9 最后想要的输出对象。

所以它本质上不是输出“几个参数”，而是输出：

> **整张图上的空间位移分布。**

---

## 6. tie-points 为什么重要
SpaceNet9 的评测不是让你把整张图看起来“像是对齐了”就算通过。

它会在人工标注的 tie-points 上检查：
- 你预测的位移
- 和真实参考位移

之间差了多少。

所以 tie-points 可以理解成：

> **评测时用于检验配准是否准确的关键对应点。**

它们不是全部空间关系，但它们是评分时真正被拿来对比的锚点。

---

## 7. 用 GIS / 遥感语言怎么理解
如果你有 GIS / 遥感基础，Day 1 可以这样对照：

- **correspondence**：两幅图里同一地物/同一位置的对应关系
- **offset**：从 source 像素到 target 像素的位移向量
- **dense displacement field**：整张图上的局部位移/形变描述
- **registration**：把两份空间上不一致的数据重新对齐

所以你不是完全从零开始。你已经有“空间关系”的直觉，只是现在要把它翻译成 CV / 配准语言。

---

## 8. Day 1 不要急着搞懂的东西
今天先别把精力花在这些地方：
- 网络结构细节
- 训练策略
- 复杂 warp 实现
- 冠军方案里的工程技巧

第一天的任务不是“掌握方案实现”，而是：

> **确认你知道这个任务到底在求什么。**

---

## 9. 今天必须记住的一句话
> SpaceNet9 本质上是在做 optical 到 SAR 的跨模态图像配准，目标是恢复 source 到 target 的空间映射关系，并把这种关系编码成 2 通道 offset map。

---

## 10. 读完后自测
请用自己的话回答：
1. SpaceNet9 的输入是什么？
2. 输出为什么是 2 通道图，而不是一个分类标签？
3. correspondence 和 offset 有什么关系？
4. tie-points 在评测里起什么作用？
5. 如果用 GIS 语言解释 dense displacement field，你会怎么说？
