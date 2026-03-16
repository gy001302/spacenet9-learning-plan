# Day 2 学习资料：从 tie-points 到位移场

今天要解决的核心问题是：

> **为什么比赛只给少量 tie-points，但最后却要求输出整张图的 offset map？**

---

## 1. tie-points 是 sparse correspondence
SpaceNet9 提供的 tie-points 不是整张图每个像素的对应关系，而只是少量人工标注的关键对应点。

所以从算法对象上看，tie-points 本质上是：

> **sparse correspondence（稀疏对应关系）**

它们告诉你：
- optical 图上的某些位置
- 在 SAR 图上对应到哪里

但只覆盖了少量位置。

---

## 2. offset 是 correspondence 的向量表达
如果 optical 图上的一个点 `(x, y)` 对应到 SAR 图上的 `(x', y')`，那它的位移就是：
- `dx = x' - x`
- `dy = y' - y`

所以 correspondence 回答的是：
- “谁对应谁？”

offset 回答的是：
- “应该往哪移、移多少？”

也就是说：

> **offset = correspondence 的向量化表达。**

---

## 3. 为什么不能只停留在 sparse points
如果任务只要求你在 tie-points 上给答案，那输出一个稀疏点集就够了。

但 SpaceNet9 要求的不是：
- 几个对应点
- 一个全局标签
- 一组很少的参数

而是：

> **对整张 optical 图输出像素级位移场。**

这就意味着：
- 你不能只知道少量点怎么对齐
- 你需要为整张图恢复空间映射关系

---

## 4. dense displacement field 是什么
如果你对整张图每个像素都给一个 `(dx, dy)`，那就得到了一张：
- dense displacement field
- 或者叫 offset map

所以从 Day 1 到 Day 2，逻辑链条是：

```text
correspondence
    ↓
offset
    ↓
sparse offsets（少量点）
    ↓
dense displacement field（整图位移场）
```

这条链条非常重要，因为后面你学的：
- affine
- homography
- TPS
- local registration
- learned dense prediction

本质上都在回答一件事：

> **如何把稀疏对应扩展成整图的空间位移表达？**

---

## 5. 用 GIS / 遥感语言怎么理解
如果用 GIS / 遥感直觉来翻译：

- tie-points：两幅图中少量已知的同名点/对应点
- offset：从源图位置到目标图位置的位移向量
- dense displacement field：整张图上的局部位移/形变描述
- sparse → dense：从少量已知约束，推广到整张图的空间关系估计

所以你今天其实不是在学一个陌生问题，而是在把已有空间直觉翻译成 CV / registration 语言。

---

## 6. 为什么今天的最小代码例子值得学
今天的代码示例故意非常简单：
- 已知少量 sparse correspondences
- 假设全局位移一致
- 直接构造一张 dense offset map

它不是为了模拟真实比赛难度，而是为了教学。

它被选入的原因是：
1. 它能最直观地展示 sparse → dense 这个核心过渡
2. 它能让你先看懂 offset map 长什么样
3. 它能帮你建立“输出对象感”，为后面看 baseline 做准备

所以今天不要问“它强不强”，要问：

> **它有没有把问题对象讲清楚？**

---

## 7. 它和真实 SpaceNet9 的关系
今天的 toy code 当然比真实项目简单很多。

真实 SpaceNet9 不会直接假设全局位移完全一致；
它需要处理：
- 跨模态差异
- 局部变化
- 更复杂的几何和纹理关系
- 真实推理与评测流程

但这个 toy code 和真实项目共享一个关键点：

> **最后都要把“空间对应关系”表达成位移场 / offset map。**

这就是它值得放在 Day 2 的原因。

---

## 8. 今天先不要急着学的东西
今天先不要钻进这些地方：
- 哪种插值最好
- 哪种网络结构更强
- 怎么训练 dense predictor
- 如何处理复杂局部非刚性变形

这些都会在后面出现。

Day 2 的目标只有一个：

> **确认你已经理解 sparse correspondence 为什么必须走向 dense displacement field。**

---

## 9. 今天必须记住的一句话
> tie-points 只是稀疏对应关系，但 SpaceNet9 的目标是恢复整张图的空间位移分布，所以算法最终必须从 sparse correspondence 走向 dense displacement field，并把它表示成 offset map。

---

## 10. 读完后自测
请用自己的话回答：
1. 为什么 tie-points 只能算 sparse correspondence？
2. 为什么 offset 是 correspondence 的向量表达？
3. 为什么 SpaceNet9 的目标不能停留在少量点上？
4. dense displacement field 和 offset map 有什么关系？
5. 为什么今天这个非常简单的 toy code 仍然值得学？
