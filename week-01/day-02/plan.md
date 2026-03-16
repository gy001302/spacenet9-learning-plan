# Day 2: 从 tie-points 到 dense displacement field

## 今日目标
今天要解决的是 SpaceNet9 里一个非常关键的过渡：

> **为什么比赛只给少量 tie-points，但最终却要求输出整张图的 2 通道 offset map？**

你今天不是去学复杂模型，而是把下面这条链条彻底打通：

```text
tie-points（稀疏对应）
    ↓
offset（对应关系的向量表达）
    ↓
dense displacement field
    ↓
offset map（SpaceNet9 的核心输出对象）
```

---

## 今日先后顺序（按这个来）
1. 回看 `repos/SpaceNet9/README.md` 中的输入、输出、评测
2. 读今日学习资料，理解 sparse → dense 的问题本质
3. 看/跑今日最小代码例子
4. 看代码例子讲解，理解为什么它被选入
5. 回到 baseline / README，找这种对象在真实项目里的出现位置
6. 写总结

---

## 2 小时分配
- 25 分钟：回看任务定义与评测方式
- 35 分钟：读今日概念讲解
- 30 分钟：看/跑最小代码例子 + 阅读讲解
- 20 分钟：回到仓库找映射
- 10 分钟：写今日总结

### 时间够的话再做
- 15~20 分钟：补看 1 份外部桥梁资料

---

## 今日必须搞清楚的 5 个问题
- [ ] tie-points 为什么本质上是 sparse correspondence？
- [ ] offset 为什么是 correspondence 的向量表达？
- [ ] 为什么 SpaceNet9 不能只输出少量点，而要输出整图位移场？
- [ ] dense displacement field 和 offset map 是什么关系？
- [ ] 今天的 toy code 为什么虽然简单，但仍然值得学？

---

## 今日任务清单
- [ ] 我能解释 tie-points、offset、dense field 三者关系
- [ ] 我看懂/跑通了今天的最小代码例子
- [ ] 我知道这段代码的出处、选入原因、与 SpaceNet9 的关系
- [ ] 我能指出它在 SpaceNet9 哪类代码/输出对象里会再次出现
- [ ] 我写下了今天的总结和问题

---

## 今日代码示例学习
### 今日代码示例
- `week-01/day-02/day-02-code-example.py`
- `week-01/day-02/day-02-code-example-explained.md`

### 你今天看代码时重点看什么
- 稀疏点位移是怎么表示的
- 为什么可以先用“全局位移一致”的简化假设做教学演示
- `(2, H, W)` 或 `(dx, dy)` 这种组织方式在表达什么
- 这个 toy 示例与真实 SpaceNet9 输出对象的相似点是什么

### 暂时不要纠结什么
- 这个方法是否足够强
- 真实项目为什么不会这么简单
- 深度学习模型怎么训练

今天看代码的目的不是“追求性能”，而是**建立对象感**。

---

## 推荐项目阅读位置
- `repos/SpaceNet9/README.md`
- `repos/SpaceNet9/src/baseline/README.md`
- `spacenet9-learning-plan/LEARNING-MATERIAL-SELECTION.md`

---

## 今日最低产出要求
### 1. 一句话解释
模板：
> tie-points 是 ______，而 SpaceNet9 最终要求 ______，所以算法必须解决 ______。

### 2. 一段代码示例观察
模板：
> 这个示例把 ______ 简化成 ______，虽然不是真实方案，但它帮助我理解了 ______。

### 3. 一条与 SpaceNet9 的映射
模板：
> 这段代码里的 ______，在 SpaceNet9 中对应的是 ______。

### 4. 一个仍然没懂的问题
模板：
> 我现在还不明白 ______，因为 ______。

---

## 时间不够时的保底策略
1. 先读今日学习资料前 5 节
2. 再看今日代码示例讲解
3. 写一句 sparse → dense 的解释
4. 写 100 字总结

---

## 今天结束时你应该能说出这句话
> tie-points 只是稀疏对应关系，但 SpaceNet9 的目标是恢复整张图的空间位移分布，所以系统最终要从 sparse correspondence 走向 dense displacement field，并把它表示成 offset map。
