# Week 2 经典教程引导：几何模型与鲁棒估计

## 这一周最重要的经典线
这周你要建立两条经典能力线：
1. warp model 的表达能力差异
2. robust fitting 的必要性

## 推荐阅读顺序

### 必看 1：OpenCV Feature Matching + Homography
- 链接：https://docs.opencv.org/4.x/d1/de0/tutorial_py_feature_homography.html
- 作用：把“匹配点 → 估计几何模型 → RANSAC”这条链串起来。

### 必看 2：OpenCV Feature Matcher Tutorial
- 链接：https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html
- 作用：建立“匹配点不可靠”这个直觉，为 RANSAC 铺路。

### 必看 3：scikit-image robust matching example
- 链接：https://scikit-image.org/docs/stable/auto_examples/transform/plot_matching.html
- 作用：用更清楚的小例子理解 outlier / inlier / robust fitting。

### 选看 4：Affine transformation / Homography 相关百科
- 作用：补表达能力直觉，而不是背推导。

## 这周你最该学会的不是 API，而是判断
- 什么时候 translation 就够？
- 什么时候 affine 更合适？
- 什么时候 correspondence 里 outlier 会毁掉拟合？
- 为什么 RANSAC 是配准代码里高频出现的老朋友？

## 这周和 SpaceNet 的连接点
这周学完，你再看 SpaceNet，会更容易理解：
- 为什么最简单方案会从对应点直接估计 transform
- 为什么强方案会非常强调 robust fitting
- 为什么“有 matcher”不等于“可以直接注册成功”
