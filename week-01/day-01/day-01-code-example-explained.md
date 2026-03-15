# Day 1 配套代码例子讲解

你今天除了阅读资料，还可以看这个文件：

- `day-01-code-example.py`

它不是比赛代码，也不是遥感完整方案。  
它的作用只有一个：

> **用一个最小可运行例子，把 tiepoints、offset、offset map、评测逻辑讲明白。**

---

# 这个例子在模拟什么

它模拟的是 SpaceNet9 最最基础的骨架：

1. 有一张源图（source image）
2. 有一张目标图（target image）
3. 已知一些 tiepoints
4. 根据 tiepoints 可以得到位移
5. 可以构造 offset map
6. 可以在 tiepoints 位置检查误差

它故意不用真实遥感图，也不用 SAR，原因很简单：

> 你今天要先理解“机制”，不是先被数据复杂性打晕。

---

# 你看代码时重点看这几段

## 1. `true_dx` 和 `true_dy`
这里设置了：

- `true_dx = 6`
- `true_dy = -4`

意思是：

- 原图中的点到目标图里后
- x 方向右移 6
- y 方向上移 4

这就是最简单的位移模型。

---

## 2. `source_points` 和 `target_points`
这两组点就在模拟：

- optical 图里的点
- SAR 图里的对应点

也就是 tiepoints。

代码里：

```python
source_points = np.array([...])
target_points = source_points + np.array([true_dx, true_dy])
```

这句特别重要，因为它直接体现了：

> **对应点 = 原始点 + 位移**

---

## 3. `offsets = target_points - source_points`
这句是在算每个 tiepoint 的位移。

这就是今天最关键的定义：

> `offset = target - source`

也就是：

- 在目标图的位置
- 减去源图的位置
- 就得到位移

---

## 4. `offset_map`
这里构造了一个 shape 为 `(2, H, W)` 的数组：

```python
offset_map = np.zeros((2, H, W), dtype=np.float32)
offset_map[0, :, :] = true_dx
offset_map[1, :, :] = true_dy
```

这表示：

- 第 0 通道存 dx
- 第 1 通道存 dy

并且这里假设整张图所有像素位移都一样。

这相当于：

> **最简单的全局平移模型**

---

## 5. `evaluate_tiepoints(...)`
这是最值得你仔细看的函数。

它做的事情是：

1. 遍历每个 tiepoint
2. 在 offset map 对应位置读取 `pred_dx, pred_dy`
3. 计算真值 `gt_dx, gt_dy`
4. 比较误差

这和 SpaceNet9 的评测思想是对应的：

> 虽然你输出的是整张图，但评测时会在 tiepoints 位置检查预测位移是否正确。

---

# 这个例子帮助你理解什么

你今天至少要通过它理解 5 件事：

## 1. tiepoints 是什么
就是“源图点”和“目标图点”的对应关系。

## 2. offset 是什么
就是：

- `dx = target_x - source_x`
- `dy = target_y - source_y`

## 3. offset map 是什么
就是给每个像素都存一个 `(dx, dy)`。

## 4. 为什么评分可以只看 tiepoints
因为 tiepoints 是人工确认过的参考点，最适合拿来比较预测值与真值。

## 5. 为什么后面会需要更复杂的方法
这个例子里整张图位移都一样，所以一个常数 offset map 就够了。

但真实 SpaceNet9 并不是这么简单，真实情况可能是：

- 左边区域偏移一种模式
- 右边区域偏移另一种模式
- 建筑区域和空地的误差特征也不一样

所以后面才会出现：

- affine
- homography
- sparse→dense interpolation
- local registration
- refinement

---

# 你今天怎么用这个例子

## 最低要求
你就做两件事：

1. 打开代码看一遍
2. 看懂里面这几个变量：
   - `source_points`
   - `target_points`
   - `offsets`
   - `offset_map`

## 如果你愿意动手
你可以直接运行它。

如果环境里有 Python + numpy + matplotlib，大概率就可以跑：

```bash
python day-01-code-example.py
```

运行后你应该能看到：

- source image
- target image
- dx map
- dy map

---

# 今天看完代码后，你要能回答这几个问题

1. `source_points` 和 `target_points` 各代表什么？
2. 为什么 `offset = target - source`？
3. 为什么 `offset_map` 有 2 个通道？
4. 为什么评测时只在 tiepoints 上读 offset？
5. 如果整张图位移不一致，这个例子哪里就不够用了？

---

# 最后一句话

这份代码例子不是为了让你学会比赛实现，  
而是为了让你先把最底层机制看懂：

> **SpaceNet9 的本质就是：根据对应关系去恢复位移场。**
