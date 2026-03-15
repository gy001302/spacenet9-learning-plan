# Week 1 流程图卡（文字版）

## 卡片 1：任务主链
optical 图 + SAR 图
→ 已知/可估计部分对应点
→ 需要恢复空间对应关系
→ 输出 dense offset map
→ 在 tiepoints 位置评测误差

## 卡片 2：最简单方案的骨架
matching
→ 得到 tiepoints
→ 估计全局变换（例如 affine）
→ 生成整张图的 offset map

## 卡片 3：更灵活的一条路线
matching
→ sparse offsets
→ 插值 / 局部建模
→ dense offset map

## 卡片 4：为什么先学这些骨架？
因为后面的所有方案（第4名、第2名、第1名）虽然复杂度不同，但本质都绕不开：
- 怎么找对应关系
- 怎么去掉错误匹配
- 怎么把 sparse 关系变成 dense 位移场
