import numpy as np

pts = np.array([[0,0],[1,2],[3,4]])
dx, dy = 5, -2
pts2 = pts + np.array([dx, dy])
print('source:
', pts)
print('target:
', pts2)
print('all offsets equal?:
', pts2 - pts)
