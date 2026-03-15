# Week 1 术语卡

## 1. Optical image
光学遥感图像，接近普通卫星照片，通常是 RGB 三通道。

## 2. SAR image
雷达遥感图像，和 optical 成像机制不同，视觉外观差异大。

## 3. Registration
配准，让两张图在空间上建立对应关系。

## 4. Tiepoints
人工标注的对应点，是比赛评分的重要锚点。

## 5. Offset map
位移图。对每个像素都给一个 `(dx, dy)`。

## 6. Dense displacement field
稠密位移场，也就是整张图每个像素的位移关系。

## 7. Affine transform
仿射变换。能表达平移、旋转、缩放、剪切等全局变化。

## 8. Homography
单应性变换。比 affine 更灵活，常用于平面投影关系建模。

## 9. RANSAC
一种鲁棒估计方法，用来在有错配点时拟合较靠谱的几何模型。

## 10. Sparse to dense
从少量已知位移点，推断整张图的位移场。
