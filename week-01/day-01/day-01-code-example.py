"""
Day 1 code example: 用一个极简例子理解 SpaceNet9 的核心概念

你今天不用碰真实遥感数据，也不用碰 SAR。
这个脚本只做一件事：

1. 构造一张“原图”
2. 人为制造一个平移后的“目标图”
3. 人为指定几个 tiepoints
4. 根据 tiepoints 计算 offset
5. 生成一张 dense offset map
6. 用这个 offset map 检查 tiepoints 误差

它对应的是 SpaceNet9 的最基础骨架：
source image -> tiepoints -> offset map -> evaluation
"""

import numpy as np
import matplotlib.pyplot as plt


# =========================
# Step 1. 构造一张简单图像
# =========================
H, W = 80, 100
image = np.zeros((H, W), dtype=np.float32)

# 造几个亮块，方便观察
image[10:20, 15:25] = 1.0
image[35:50, 40:60] = 0.7
image[55:65, 75:90] = 0.9


# =========================
# Step 2. 构造“目标图”
# 假设真实位移是 dx=+6, dy=-4
# 含义：原图中的像素在目标图中向右 6、向上 4
# =========================
true_dx = 6
true_dy = -4

target = np.zeros_like(image)

for y in range(H):
    for x in range(W):
        ny = y + true_dy
        nx = x + true_dx
        if 0 <= ny < H and 0 <= nx < W:
            target[ny, nx] = image[y, x]


# =========================
# Step 3. 构造 tiepoints
# 这里假设我们人工知道 4 对对应点
# 格式模仿 SpaceNet9：
# source point (optical) -> target point (sar)
# =========================
source_points = np.array([
    [17, 12],
    [45, 40],
    [80, 60],
    [52, 45],
], dtype=np.int32)  # (x, y)

target_points = source_points + np.array([true_dx, true_dy])


# =========================
# Step 4. 从 tiepoints 计算位移
# 这就是最朴素的 offset 定义
# =========================
offsets = target_points - source_points

print("Source points:\n", source_points)
print("Target points:\n", target_points)
print("Offsets (dx, dy):\n", offsets)


# =========================
# Step 5. 构造 dense offset map
# shape = (2, H, W)
# channel 0 存 dx
# channel 1 存 dy
#
# 这里为了简化，假设整张图位移都一样
# 这相当于一个最简单的“全局平移模型”
# =========================
offset_map = np.zeros((2, H, W), dtype=np.float32)
offset_map[0, :, :] = true_dx  # dx map
offset_map[1, :, :] = true_dy  # dy map


# =========================
# Step 6. 在 tiepoints 上做“评分”
# 这模仿 SpaceNet9 的评测思想：
# 在 tiepoints 位置读取预测位移，再跟真值比较
# =========================
def evaluate_tiepoints(src_pts, tgt_pts, pred_offset_map):
    errors = []
    for (sx, sy), (tx, ty) in zip(src_pts, tgt_pts):
        pred_dx = pred_offset_map[0, sy, sx]
        pred_dy = pred_offset_map[1, sy, sx]

        gt_dx = tx - sx
        gt_dy = ty - sy

        err = np.sqrt((pred_dx - gt_dx) ** 2 + (pred_dy - gt_dy) ** 2)
        errors.append(err)

        print(
            f"point=({sx},{sy}) | pred=({pred_dx:.1f},{pred_dy:.1f}) | "
            f"gt=({gt_dx},{gt_dy}) | err={err:.3f}"
        )

    return float(np.mean(errors))


mean_error = evaluate_tiepoints(source_points, target_points, offset_map)
print("\nMean tiepoint error:", mean_error)


# =========================
# Step 7. 可视化
# =========================
fig, axes = plt.subplots(1, 4, figsize=(16, 4))

axes[0].imshow(image, cmap="gray")
axes[0].set_title("Source image")
for x, y in source_points:
    axes[0].plot(x, y, "ro")

axes[1].imshow(target, cmap="gray")
axes[1].set_title("Target image")
for x, y in target_points:
    axes[1].plot(x, y, "go")

axes[2].imshow(offset_map[0], cmap="coolwarm")
axes[2].set_title("dx map")

axes[3].imshow(offset_map[1], cmap="coolwarm")
axes[3].set_title("dy map")

for ax in axes:
    ax.set_axis_off()

plt.tight_layout()
plt.show()


# =========================
# 你今天需要从这个例子里理解什么？
#
# 1. tiepoints 是“已知对应点”
# 2. offset = target - source
# 3. offset map 是给每个像素一个(dx, dy)
# 4. 评测时可以在 tiepoints 位置读取 offset，再和真值比较
# 5. 如果整张图位移不一致，就不能用这种“整图常数 offset map”，
#    后面才需要 affine / local reg / TPS / sparse->dense interpolation
# =========================
