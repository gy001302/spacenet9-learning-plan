# SpaceNet9 算法学习计划（代码理解导向）

> 目标：不是泛泛学 CV，也不是只会看比赛介绍，
> 而是 **通过循序渐进的算法学习，最终能看懂 SpaceNet9 相关代码与方案。**

## 适合对象

- 已有 GIS 基础
- 已有 Python 基础
- 每天可投入约 2 小时
- 希望通过 SpaceNet9 这类任务进入遥感配准算法

## 这套计划的核心思想

本计划不再以“先看比赛、再看方案”为主线，而是改成：

1. **先学 SpaceNet 背后的算法对象**
   - correspondence
   - offset / displacement
   - warp
   - global transform / local deformation

2. **再学从对应点到位移场的主要建模方法**
   - translation
   - affine
   - homography
   - TPS
   - sparse → dense interpolation

3. **再学鲁棒估计与匹配算法**
   - outlier / inlier
   - RANSAC
   - 传统特征与现代 matcher

4. **最后回到 SpaceNet 代码里定位这些算法是如何出现的**

也就是说：

> 你每天学的内容，都应该能回答：
> **“这块算法在 SpaceNet 代码里会出现在哪里？”**

## 每天学习结构

每天建议按下面 4 层来学：

1. **今日算法问题**
2. **今日概念讲解**
3. **今日最小代码例子**
4. **今日 SpaceNet 映射**

## 目录结构

- `week-01/`：配准问题建模与位移场
- `week-02/`：几何变换模型与鲁棒估计
- `week-03/`：对应点获取：传统特征到现代 matcher
- `week-04/`：从 sparse correspondence 到 dense field
- `week-05/`：分割/高度先验与 patch 工程
- `week-06/`：回到 SpaceNet：看懂第 4 / 2 / 1 名
- `week-07/`：复现准备（可选增强）
- `week-08/`：研究提升（可选增强）

## 每周最低要求

每周至少留下：
- 3 份日笔记
- 1 张流程图 / 对比图
- 1 份周总结
- 1 次自测

## 使用建议

- **整块 2 小时时间**：学主线、看代码、做最小实验
- **碎片时间**：看术语卡、问题卡、流程卡
- 如果当天时间不够，优先级永远是：
  1. 今日算法问题
  2. 今日最小代码例子
  3. 今日总结
