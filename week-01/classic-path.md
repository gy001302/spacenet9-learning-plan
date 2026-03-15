# Week 1 经典教程引导：从 GIS 到 CV 的问题建模

## 这一周你为什么需要经典教程
这一周不是学模型，而是学“问题怎么被表示”。这时候最重要的不是某个比赛方案，而是建立：
- 图像之间的对应关系是什么
- 几何变换与位移场是什么
- 配准与普通 CV 任务的区别是什么

## 推荐阅读顺序

### 必看 1：OpenCV Geometric Transformations
- 链接：https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html
- 作用：建立最基础的图像空间变换直觉，知道什么叫平移、缩放、旋转、warp。

### 必看 2：scikit-image transform 文档
- 链接：https://scikit-image.org/docs/stable/api/skimage.transform.html
- 作用：从 API 层面感受 affine / projective / warp 这些对象长什么样。

### 选看 3：Wikipedia Image Registration
- 链接：https://en.wikipedia.org/wiki/Image_registration
- 作用：做总览，知道 registration 在计算机视觉里属于什么问题。

## 这周看经典教程不是为了什么
- 不是为了背 OpenCV API
- 不是为了写炫技代码

## 这周看经典教程是为了什么
- 建立 source / target / correspondence / warp 的统一视角
- 让你回头看 SpaceNet 时，知道它不是在“分类”，而是在恢复空间关系

## 这周和 SpaceNet 的连接点
这周学完，你应该能更自然地看懂：
- `offset_map`
- `dx / dy`
- `transform`
- `registration`
这类变量和模块为什么会存在。

## 建议搭配书籍

- **Szeliski《Computer Vision: Algorithms and Applications》**
  - 主页：https://szeliski.org/Book/
  - 这一周用它做“大图景参考”，帮助你把 registration 放回 CV 全局框架中。
- **Gonzalez & Woods《Digital Image Processing》**
  - 作者主页：https://www.imageprocessingplace.com/
  - 这一周不作为主教材，只在需要补图像表示/基础处理直觉时查阅。
