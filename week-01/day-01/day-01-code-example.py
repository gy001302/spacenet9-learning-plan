import numpy as np

# Day 1: correspondence -> offset
source = np.array([[10, 10], [20, 15], [30, 25]])
target = np.array([[13, 8], [23, 13], [33, 23]])
offset = target - source

print("source:
", source)
print("target:
", target)
print("offset = target - source:
", offset)

# 你今天要理解：
# 1. correspondence 是 (source point, target point)
# 2. offset 是 correspondence 的向量表达
