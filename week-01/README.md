# Week 1：配准问题建模与位移场

**本周目标：**
不是先学模型名字，而是先把 SpaceNet9 背后的最核心算法对象搞清楚：

- 什么是 correspondence
- 什么是 offset / displacement
- 什么是 dense displacement field
- 为什么配准任务最后输出的是位移场，而不是类别或框

## 本周核心问题

- SpaceNet9 到底在求什么数学对象？
- 对应点和位移之间是什么关系？
- 为什么要从 sparse 对应关系走向 dense offset map？
- 如果整张图位移不一致，为什么简单全局平移不够？

## 本周建议最低完成线

- 能用自己的话解释：什么是 tiepoints、offset map、dense displacement field
- 能运行至少 1 个最小代码例子
- 能画出一张“对应点 → 位移场”的流程图

## 每日主题

- Day 1：配准问题到底在解什么
- Day 2：tiepoints、offset、位移场
- Day 3：全局平移模型为什么成立
- Day 4：为什么需要更一般的几何变换
- Day 5：SpaceNet 中最简单方案的算法骨架
- Day 6：第4名方案里的 sparse→dense 思路
- Day 7：本周总结与算法抽象
