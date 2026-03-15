# Day 1 学习资料：配准问题到底在解什么

今天先不从“比赛介绍”出发，而是从算法角度问：

> 配准任务到底在求什么？

## 1. 配准不是识别“这是什么”
在分类里，我们问“这张图是什么类别”；在检测里，我们问“目标在哪里”；在分割里，我们问“每个像素属于什么类别”。

但在配准里，我们问的是：

> 图 A 中的某个位置，在图 B 中对应哪里？

所以配准的核心对象不是类别，而是 **对应关系（correspondence）**。

## 2. 什么是 correspondence
如果 source 图里一个点 `(x, y)`，在 target 图里对应 `(x', y')`，那么这两个位置之间就构成一个 correspondence。

当你有很多 correspondence 时，就能开始问：
- 它们之间是否服从某种统一变换？
- 能不能把这种关系扩展到整张图？

## 3. 什么是 offset / displacement
如果 source 点是 `(x, y)`，target 点是 `(x', y')`，那位移就是：
- `dx = x' - x`
- `dy = y' - y`

所以位移本质上是：

> **对应关系的向量表达**

## 4. 什么是 offset map
如果对 source 图中每个像素都给出一个 `(dx, dy)`，那就得到一张 offset map。

它本质上就是一张 **dense displacement field（稠密位移场）**。

## 5. SpaceNet9 为什么输出 offset map
因为它的目标不是只给几个点配准对，而是要恢复整张图的空间对应关系。

也就是说，SpaceNet9 最后在求的不是：
- 一个类别
- 一组框
- 一张 mask

而是：

> **一张稠密位移场**

## 6. 今天你必须记住的一句话
> 配准任务的核心，是从 correspondence 出发，恢复 source 到 target 的空间映射关系；SpaceNet9 把这种空间映射关系编码成了 offset map。
