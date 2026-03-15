# 书籍与参考资料总表

> 目标：从 GIS 过渡到 SpaceNet 源码理解。  
> 原则：主线教材、辅助教材、查阅书分开；能给官方/稳定链接的尽量给准确链接。

## 一、主线教材

### 1. OpenCV 官方教程
- 主页：https://docs.opencv.org/4.x/d9/df8/tutorial_root.html
- 用途：CV 几何、图像变换、特征匹配、homography、基础图像处理
- 备注：这是当前阶段最重要的 CV 实操主线之一

### 2. PyTorch 官方教程
- 主页：https://pytorch.org/tutorials/
- Beginner 入口：https://pytorch.org/tutorials/beginner/basics/intro.html
- 用途：补齐 tensor、Dataset/DataLoader、训练/推理循环、checkpoint、模型阅读

### 3. SpaceNet9 官方仓库
- 链接：https://github.com/SpaceNetChallenge/SpaceNet9
- 用途：作为最终代码理解落点

## 二、辅助教材

### 4. scikit-image 文档与例子
- 主页：https://scikit-image.org/docs/stable/
- transform API：https://scikit-image.org/docs/stable/api/skimage.transform.html
- robust matching example：https://scikit-image.org/docs/stable/auto_examples/transform/plot_matching.html
- 用途：用更小更干净的例子理解 transform / registration / RANSAC

### 5. Kornia 文档
- 主页：https://kornia.readthedocs.io/en/latest/
- geometry transform：https://kornia.readthedocs.io/en/latest/geometry.transform.html
- 用途：连接经典几何变换与 PyTorch 实现

### 6. TorchGeo 文档
- 主页：https://torchgeo.readthedocs.io/en/stable/
- 仓库：https://github.com/microsoft/torchgeo
- 用途：遥感 + PyTorch 的工程化补充

## 三、书籍（建议角色）

### 7. Gonzalez & Woods《Digital Image Processing》
- 英文版出版页（Pearson 作者页可能变动，给出作者主页）：https://www.imageprocessingplace.com/
- Open Library 检索页：https://openlibrary.org/search?q=Digital+Image+Processing+Gonzalez+Woods
- 作用定位：**图像处理查阅书 / 基础补充书**，不是当前主线教材
- 适合查：滤波、增强、边缘、形态学、图像表示

### 8. Richard Szeliski《Computer Vision: Algorithms and Applications》
- 在线书主页：https://szeliski.org/Book/
- PDF（作者主页提供）：https://szeliski.org/Book/drafts/SzeliskiBook_20100903_draft.pdf
- 作用定位：**CV 算法总览级参考书**
- 适合查：几何、matching、registration、multi-view 等大图景

### 9. Hartley & Zisserman《Multiple View Geometry in Computer Vision》
- 图书页：https://www.robots.ox.ac.uk/~vgg/hzbook/
- 作用定位：**更高阶几何参考书**
- 备注：对当前阶段不是主教材，但后期查 homography / projective geometry 很有价值

## 四、论文 / 模型官方入口（按需查）

### 10. SuperPoint
- 论文页：https://openaccess.thecvf.com/content_cvpr_2018_workshops/w9/html/DeTone_SuperPoint_Self-Supervised_Interest_CVPR_2018_paper.html

### 11. LightGlue
- 仓库：https://github.com/cvg/LightGlue
- 论文：https://arxiv.org/abs/2306.13643

### 12. LoFTR
- 仓库：https://github.com/zju3dv/LoFTR
- 论文：https://arxiv.org/abs/2104.00680

### 13. RoMa
- 仓库：https://github.com/Parskatt/RoMa
- 论文：https://arxiv.org/abs/2305.15404

## 五、使用建议

### 现在主攻
1. OpenCV 官方教程
2. PyTorch 官方教程
3. 你的学习计划仓库
4. SpaceNet9 仓库

### 作为辅助
5. scikit-image
6. Kornia
7. TorchGeo

### 作为查阅书
8. Gonzalez & Woods
9. Szeliski
10. Hartley & Zisserman
