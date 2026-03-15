# Week 6：分割、patch inference 与先验辅助

**本周目标：** 理解为什么 SpaceNet 强方案里会出现 U-Net、building mask、height prior、patch stitching。

## 本周主问题

- 为什么大图必须 patch inference？
- 为什么 segmentation 不是最终任务，却会出现在 registration pipeline 里？
- building / height prior 为什么能提升稳健性？

## 本周流程图

```text
大图 / 跨模态图像
    ↓
patch inference
    ↓
segmentation / height prior
    ↓
filter trusted regions
    ↓
registration refinement
```

## 每日推进

- Day 1：patch inference
- Day 2：U-Net 与 segmentation 输出
- Day 3：building mask
- Day 4：height prior
- Day 5：加权拼接与边缘效应
- Day 6：映射到第 2 名方案
- Day 7：总结

## 本周结束后你应该会什么

- 能用自己的话解释这一周的核心算法对象
- 能把这一周学的对象映射到源码中的某个模块
- 能指出这一周内容在整个 SpaceNet 理解路线中的位置
