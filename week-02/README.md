# Week 2：几何变换模型与鲁棒估计

**本周目标：**
理解从 correspondence 到变换模型的核心算法链：

- translation
- affine
- homography
- 为什么需要更灵活的模型
- 为什么匹配点不能直接拿来拟合，必须要有鲁棒估计（RANSAC）

## 本周核心问题
- 什么情况下全局平移够用？
- 什么情况下必须引入 affine / homography？
- 为什么匹配点中会有错配？
- RANSAC 到底解决了什么问题？

## 建议最低完成线
- 能解释 translation / affine / homography 的表达能力差异
- 能用自己的话解释 RANSAC 的作用
- 能看懂一个“有/无 RANSAC”的最小对比例子

## 每日主题
- Day 1：translation 作为最简单的 warp model
- Day 2：affine 为什么比 translation 强
- Day 3：homography 再往前多走了一步
- Day 4：为什么 correspondence 里会有 outlier
- Day 5：RANSAC 到底在做什么
- Day 6：把几何模型映射回 SpaceNet 代码
- Day 7：本周总结与模型比较
