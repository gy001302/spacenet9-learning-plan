import numpy as np

H, W = 5, 6
# 稀疏位移：只有两个点已知
sparse = {(1, 1): (2, -1), (4, 3): (2, -1)}

# 最简单情况：假设全局位移一致，就把全图填成同一个 offset
offset_map = np.zeros((2, H, W), dtype=np.float32)
offset_map[0, :, :] = 2
offset_map[1, :, :] = -1

print("Known sparse correspondences:", sparse)
print("Dense offset map dx:
", offset_map[0])
print("Dense offset map dy:
", offset_map[1])
