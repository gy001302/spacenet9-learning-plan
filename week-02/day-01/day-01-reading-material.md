# Day 1 学习资料：translation 作为最简单的 warp model

今天要解决的问题：

> 如果整张图的位移完全一致，配准问题会变成什么？

答案是：
- 每个点都共享同一个 `(dx, dy)`
- 这时最简单的 warp model 就是 translation

translation 的意义不在于它强，而在于它是所有更复杂模型的起点。你只有先理解“整图同一位移”是什么，后面才能理解 affine 为什么更强、homography 为什么更灵活。
