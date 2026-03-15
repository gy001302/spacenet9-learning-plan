# Week 1：从 GIS 到 CV：配准问题的数学对象

**本周目标：** 把 GIS 里的“空间对应”思维转成 CV/配准里的 correspondence、offset、warp、dense displacement field。

## 本周主问题

- 为什么配准问题和分类/检测不同？
- 为什么 correspondence 是核心对象？
- 为什么 SpaceNet 最终会落到 offset map？

## 本周流程图

```text
GIS 中的空间关系理解
    ↓
source / target 图像
    ↓
correspondence（对应关系）
    ↓
offset / displacement（位移）
    ↓
dense displacement field（稠密位移场）
    ↓
offset map（源码中的核心输出对象）
```

## 每日推进

- Day 1：从 GIS 视角过渡到配准问题视角
- Day 2：correspondence 与 offset
- Day 3：从稀疏对应到全局位移
- Day 4：dense displacement field 是什么
- Day 5：最小算法骨架例子
- Day 6：映射到最简单的 SpaceNet 风格代码
- Day 7：本周对象总图

## 本周结束后你应该会什么

- 能用自己的话解释这一周的核心算法对象
- 能把这一周学的对象映射到源码中的某个模块
- 能指出这一周内容在整个 SpaceNet 理解路线中的位置
