# Day 1: SpaceNet9 到底在求什么空间关系

## 今日目标
今天不追模型细节，不硬啃冠军源码，只解决一个核心问题：

> **SpaceNet9 到底在求什么空间关系？**

你需要把比赛任务、配准对象、GIS 直觉三者连起来。

---

## 今日先后顺序（按这个来）
1. 先读 `repos/SpaceNet9/README.md`
2. 写清楚输入 / 输出 / 评测
3. 再理解 `source / target / correspondence / offset`
4. 用 GIS / 遥感语言重述一遍
5. 有余力再看最小代码例子

今天的主线是：**先任务，后概念，再代码。**

---

## 2 小时分配
- 30 分钟：读 SpaceNet9 README，弄清任务定义
- 35 分钟：读今日概念讲解，建立配准对象
- 25 分钟：做 GIS ↔ CV 概念对照表
- 20 分钟：回到仓库找这些对象在项目里的出现位置
- 10 分钟：写今日总结

### 时间够的话再做
- 20~30 分钟：看/跑最小代码例子

---

## 今日必须搞清楚的 4 个问题
- [ ] SpaceNet9 是什么任务？
- [ ] 为什么它的输出是 **2 通道位移场**，而不是分类结果或几个变换参数？
- [ ] tie-points 在评测里起什么作用？
- [ ] correspondence 和 offset 是什么关系？

---

## 今日任务清单
- [ ] 我读完了 `repos/SpaceNet9/README.md`
- [ ] 我能写出输入、输出、评测方式
- [ ] 我能解释 source、target、correspondence、offset
- [ ] 我做了一份 GIS ↔ CV 对照
- [ ] 我写下了至少 1 个没弄懂的问题
- [ ] 我完成了今天的总结

---

## 今日重点概念（按优先级）
### 第一优先级：必须懂
- source
- target
- correspondence
- offset / displacement

### 第二优先级：知道它存在即可
- warp
- dense displacement field
- offset map

> Day 1 不要求你把 warp 的实现讲透，只要求你知道它和“空间映射/变形”有关。

---

## 推荐项目阅读位置
- `repos/SpaceNet9/README.md`
- `spacenet9-learning-plan/GIS-to-SpaceNet-bridge.md`
- 有余力再看：`repos/SpaceNet9/src/baseline/README.md`

---

## 今日最低产出要求
你今天至少要交这 4 样：

### 1. 一句话任务定义
模板：
> SpaceNet9 是一个 ______ 问题，输入是 ______ 和 ______，输出是 ______，评测主要依赖 ______。

### 2. 4 个核心概念解释
- source：
- target：
- correspondence：
- offset：

### 3. 1 组 GIS ↔ CV 对照
模板：
> 在 GIS / 遥感里，我把 ______ 理解成 ______。

### 4. 1 个仍然没懂的问题
模板：
> 我现在还不明白 ______，因为 ______。

---

## 今天暂时不要求
- 不要求读懂网络结构
- 不要求跑训练流程
- 不要求读完 baseline 全部代码
- 不要求搞懂复杂 warp / 几何模型实现

第一天最重要的不是“读更多代码”，而是“不要把任务理解错”。

---

## 时间不够时的保底策略
如果今天时间被打断，按这个保底：
1. 先读 `repos/SpaceNet9/README.md`
2. 再读今日概念讲解里的前 4 节
3. 写出一句话任务定义
4. 写 100 字总结

只要这四步完成，Day 1 仍然算合格。

---

## 今天结束时你应该能说出这句话
> SpaceNet9 本质上是在做 optical 到 SAR 的跨模态图像配准，目标不是识别类别，而是恢复 source 到 target 的空间映射关系，并把这种关系表示成 2 通道 offset map。
