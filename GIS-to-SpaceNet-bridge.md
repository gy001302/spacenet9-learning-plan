# 从 GIS 到 SpaceNet 源码：过渡桥梁

这份文档专门回答一个问题：

> 你已经有 GIS / 遥感基础，为什么看 SpaceNet 源码还是会卡？

因为 GIS 与 SpaceNet 源码之间，中间还隔着 4 层能力：

1. **CV 如何表示图像间关系**
   - correspondence
   - warp
   - displacement field

2. **配准算法与几何模型**
   - translation / affine / homography / TPS
   - sparse → dense
   - global / local registration

3. **机器学习与深度学习最小工作流**
   - 训练 / 推理 / checkpoint / evaluation
   - segmentation 为什么会出现在配准系统里

4. **PyTorch 代码阅读能力**
   - Dataset / DataLoader
   - tensor / shape / device
   - patch inference

## GIS 已有能力怎么迁移

### 你已经有的能力
- 坐标与空间关系意识
- 栅格数据理解
- GeoTIFF / CRS / geotransform 基础
- 遥感图像常识

### 需要新增的能力
- 从“地理空间关系”过渡到“图像 correspondence”
- 从“栅格值”过渡到“dense displacement field”
- 从“空间分析”过渡到“warp model / registration pipeline”
- 从“脚本处理数据”过渡到“读 ML / PyTorch 源码”

## 这套教程怎么用

- Week 1~4：补齐 CV / 配准算法骨架
- Week 5~6：补齐 ML / PyTorch / patch / segmentation
- Week 7~8：回到 SpaceNet 方案与源码

## 学习时要一直问自己的 3 个问题

1. 这个概念在 GIS 中有没有相近直觉？
2. 这个算法对象在 SpaceNet 代码里会以什么变量/模块出现？
3. 我学完这一块后，离“看懂源码”近了哪一步？
