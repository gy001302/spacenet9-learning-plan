# Day 2: 从 tie-points 到位移场 学习资料

## 资料清单

### 1. SpaceNet9 GitHub README
- 类型：官方/原生资料
- 出处：SpaceNet Challenge 官方仓库
- 链接：https://github.com/SpaceNetChallenge/SpaceNet9
- 为什么选它：这是理解输入、输出、评测方式的最权威入口。
- 它帮助理解 SpaceNet9 的哪一部分：明确 tie-points、2-channel transformation map、evaluation 的真实定义。
- 阅读时重点看什么：输入文件形式、输出对象、tie-points 的评分作用。

### 2. OpenCV feature matching + homography tutorial
- 类型：桥梁资料
- 出处：OpenCV 官方教程
- 链接：https://docs.opencv.org/4.x/d1/de0/tutorial_py_feature_homography.html
- 为什么选它：它能很直观地把“匹配点 → 几何关系 → 变换估计”串起来。
- 它帮助理解 SpaceNet9 的哪一部分：帮助建立 sparse correspondences 如何支持空间关系估计的直觉。
- 阅读时重点看什么：matched points、RANSAC、estimated transform 之间的关系。
- 暂时不用纠结什么：OpenCV API 细节。

### 3. OpenCV geometric transformations
- 类型：桥梁资料
- 出处：OpenCV 官方教程
- 链接：https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html
- 为什么选它：它是建立 affine / perspective / warp 直觉的低门槛材料。
- 它帮助理解 SpaceNet9 的哪一部分：帮助理解为什么后面会出现 warp、变换模型和位移表达。
- 阅读时重点看什么：图像空间变换的输入输出关系。
- 暂时不用纠结什么：具体函数参数。

### 4. Wikipedia: Image registration
- 类型：桥梁资料 / 总览资料
- 出处：Wikipedia
- 链接：https://en.wikipedia.org/wiki/Image_registration
- 为什么选它：适合快速建立总览和术语定位。
- 它帮助理解 SpaceNet9 的哪一部分：帮助你把 tie-points、registration、transformation、alignment 放进同一张概念图里。
- 阅读时重点看什么：注册问题的定义和常见术语。
- 暂时不用纠结什么：过多历史背景。

### 5. Day 2 教学版最小代码示例
- 类型：教学版最小代码
- 出处：本学习计划自带 `week-01/day-02/day-02-code-example.py`
- 链接/路径：`week-01/day-02/day-02-code-example.py`
- 为什么选它：它用最少代码展示 sparse → dense 的过渡。
- 它帮助理解 SpaceNet9 的哪一部分：帮助理解为什么最终输出对象是 2 通道 offset map。
- 阅读时重点看什么：`sparse_offsets`、`offset_map` 的结构，以及 `(2, H, W)` 的含义。
- 暂时不用纠结什么：这个 toy 方法是否足够真实。

## 使用建议
- 先看 SpaceNet9 README，再看教学代码示例。
- 外部资料优先看 OpenCV feature matching tutorial，其次再看 geometric transformations。
- 如果当天时间不够，优先保证：
  1. 1 份官方资料
  2. 1 个教学代码示例
  3. 1 段自己的总结
