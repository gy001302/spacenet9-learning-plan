# Day 2 学习资料：从 tiepoints 到位移场

今天要解决的问题是：

> 为什么比赛只给少量 tiepoints，但最终却要求输出整张图的 offset map？

## 1. tiepoints 是 sparse correspondence
人工标注的 tiepoints，只覆盖少量位置，所以它们本质上是 **稀疏对应关系**。

## 2. 但任务目标是 dense field
SpaceNet9 最终要求的是：
- 对整张图每个像素给出位移

这意味着你必须从 sparse 的 correspondence，走向 dense displacement field。

## 3. 这就是后面所有算法存在的原因
- 如果假设整张图位移差不多，可以用简单全局模型
- 如果不同区域差异大，就需要更灵活的变换或插值

所以：
> 所有后面的 affine / homography / TPS / local reg，本质上都在回答同一个问题：
> **如何把稀疏对应关系扩展成全图位移场？**
