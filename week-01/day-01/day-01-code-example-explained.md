# Day 1 代码例子讲解

这个例子不是比赛代码，而是最小算法例子。

它只做一件事：
- 给出几组 source points 和 target points
- 直接计算 `offset = target - source`

你今天要通过它理解：
1. correspondence 是配准问题的基本对象
2. offset 是 correspondence 的向量表达
3. 后面的 offset map、本质上只是把这个思路扩展到全图
