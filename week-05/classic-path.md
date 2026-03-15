# Week 5 经典教程引导：PyTorch 最小工作流

## 这一周的核心目标
不是学完整深度学习，而是补到：

> **足以读懂 SpaceNet 中的模型、推理脚本、训练脚本。**

## 推荐阅读顺序

### 必看 1：PyTorch Quickstart
- 链接：https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
- 作用：建立最小端到端工作流感觉。

### 必看 2：PyTorch Tensor Tutorial
- 链接：https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html
- 作用：解决 shape / device / tensor 读代码障碍。

### 必看 3：PyTorch Datasets & DataLoaders
- 链接：https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html
- 作用：看懂 Dataset / DataLoader 是怎么把数据送进模型的。

### 必看 4：Saving and Loading Models
- 链接：https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html
- 作用：看懂 checkpoint、state_dict、权重加载。

### 选看 5：Transfer Learning for CV
- 链接：https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
- 作用：把训练/验证 loop 补完整。

## 这一周看这些教程的目标
不是为了学一门完整框架，而是为了做到：
- 能读 tensor shape
- 能读 model forward
- 能读 Dataset / DataLoader
- 能读 inference / training loop
- 能看懂 checkpoint 是怎么来的

## 这周和 SpaceNet 的连接点
这周学完后，你应该能更自然地看：
- segmentor
- geopose
- keypoint detector
- baseline training script
- patch inference 代码
