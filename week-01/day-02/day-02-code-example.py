import numpy as np

H, W = 5, 6

# 已知少量 sparse correspondences：
# key = (row, col) in source image
# value = (dx, dy)
sparse_offsets = {
    (1, 1): (2, -1),
    (4, 3): (2, -1),
}

# 教学版简化假设：整张图共享同一个位移
shared_dx, shared_dy = 2, -1

# 构造 dense offset map
# 这里用 shape = (2, H, W)
# channel 0 表示 dx，channel 1 表示 dy
offset_map = np.zeros((2, H, W), dtype=np.float32)
offset_map[0, :, :] = shared_dx
offset_map[1, :, :] = shared_dy

print("Known sparse correspondences:")
for key, value in sparse_offsets.items():
    print(f"  source pixel {key} -> offset {value}")

print("\nDense offset map (dx channel):")
print(offset_map[0])

print("\nDense offset map (dy channel):")
print(offset_map[1])
