---
tags: [线性代数不难, 导读]
chapter: 9
type: 章节
progress: 未开始
---

> [!info] 本章速览
> **第 9 章 · 正交矩阵与QR分解**（Orthogonal Matrices & QR Decomposition）
> 难度 **进阶** ｜ 建议前置：01、03、06 ｜ 预计投入 **5–6 小时**
> 本书素材：4 个 notebook ｜ 5 篇正文 PDF ｜ 5 份 PPT 讲义

> [!tip] 三种素材怎么配合
> 1. **精读正文 PDF**：中文与英文正文内容对应，选一份精读，另一份只当“术语对照表”。
> 2. **PPT 讲义用来复习**：它是正文的图形压缩版，学完一节隔天翻一遍最划算。
> 3. **notebook 边跑边改**：每个 cell 都写了中文讲解；把参数改掉、预测图形、再运行验证。

## 本章资源矩阵

| 小节 | 主题 | 中文正文 | English | PPT | 代码 |
| --- | --- | --- | --- | --- | --- |
| 09-01 | LA_09_01_2x2正交矩阵.pdf | [[LA_09_01_2x2正交矩阵.pdf|中文]] | [[LA_09_01_Orthogonal_Matrices_2x2_EN.pdf|EN]] | [[LA_09_01_PPT_正交_中文.pdf|中]] [[LA_09_01_PPT_Orthogonal_Matrices_EN.pdf|EN]] | *无* |
| 09-02 | LA_09_02_3x3正交矩阵.pdf | [[LA_09_02_3x3正交矩阵.pdf|中文]] | [[LA_09_02_Orthogonal_Matrices_3x3_EN.pdf|EN]] | [[LA_09_02_PPT_3x3正交矩阵_中文.pdf|中]] [[LA_09_02_PPT_3x3_Orthogonal_Matrices_EN.pdf|EN]] | *无* |
| 09-03 | LA_09_03_正交矩阵性质.pdf | [[LA_09_03_正交矩阵性质.pdf|中文]] | [[LA_09_03_Properties_of_Orthogonal_Matrices_EN.pdf|EN]] | [[LA_09_03_PPT_正交矩阵性质_中文.pdf|中]] [[LA_09_03_PPT_Properties_of_Orthogonal_Matrices_EN.pdf|EN]] | *无* |
| 09-04 | LA_09_04_施密特正交化.pdf | [[LA_09_04_施密特正交化.pdf|中文]] | [[LA_09_04_Gram_Schmidt_Orthogonalization_EN.pdf|EN]] | [[LA_09_04_PPT_格拉姆-施密特正交化_中文.pdf|中]] [[LA_09_04_PPT_Gram-Schmidt_Orthogonalization_EN.pdf|EN]] | 2 个 |
| 09-05 | LA_09_05_QR分解.pdf | [[LA_09_05_QR分解.pdf|中文]] | [[LA_09_05_QR_Decomposition_EN.pdf|EN]] | [[LA_09_05_PPT_QR分解_中文.pdf|中]] [[LA_09_05_PPT_QR_Decomposition_EN.pdf|EN]] | 2 个 |

## 逐节素材与代码

### 09-01　2x2正交矩阵

- 📖 **中文正文**：[[LA_09_01_2x2正交矩阵.pdf]]
- 📘 **English text**：[[LA_09_01_Orthogonal_Matrices_2x2_EN.pdf]]
- 🖼️ **PPT（中）**：[[LA_09_01_PPT_正交_中文.pdf]]
- 🖼️ **PPT（EN）**：[[LA_09_01_PPT_Orthogonal_Matrices_EN.pdf]]
- 💻 **代码**：*本仓库未收录该节 notebook（正文 + PPT 已足够）*

### 09-02　3x3正交矩阵

- 📖 **中文正文**：[[LA_09_02_3x3正交矩阵.pdf]]
- 📘 **English text**：[[LA_09_02_Orthogonal_Matrices_3x3_EN.pdf]]
- 🖼️ **PPT（中）**：[[LA_09_02_PPT_3x3正交矩阵_中文.pdf]]
- 🖼️ **PPT（EN）**：[[LA_09_02_PPT_3x3_Orthogonal_Matrices_EN.pdf]]
- 💻 **代码**：*本仓库未收录该节 notebook（正文 + PPT 已足够）*

### 09-03　正交矩阵性质

- 📖 **中文正文**：[[LA_09_03_正交矩阵性质.pdf]]
- 📘 **English text**：[[LA_09_03_Properties_of_Orthogonal_Matrices_EN.pdf]]
- 🖼️ **PPT（中）**：[[LA_09_03_PPT_正交矩阵性质_中文.pdf]]
- 🖼️ **PPT（EN）**：[[LA_09_03_PPT_Properties_of_Orthogonal_Matrices_EN.pdf]]
- 💻 **代码**：*本仓库未收录该节 notebook（正文 + PPT 已足够）*

### 09-04　施密特正交化

- 📖 **中文正文**：[[LA_09_04_施密特正交化.pdf]]
- 📘 **English text**：[[LA_09_04_Gram_Schmidt_Orthogonalization_EN.pdf]]
- 🖼️ **PPT（中）**：[[LA_09_04_PPT_格拉姆-施密特正交化_中文.pdf]]
- 🖼️ **PPT（EN）**：[[LA_09_04_PPT_Gram-Schmidt_Orthogonalization_EN.pdf]]
- 💻 **代码**：
    - [[代码/09-正交矩阵-QR分解/LA_09_04_01.ipynb|施密特正交化]]
    - [[代码/09-正交矩阵-QR分解/LA_09_04_02.ipynb|施密特正交化，自定义函数]]

### 09-05　QR分解

- 📖 **中文正文**：[[LA_09_05_QR分解.pdf]]
- 📘 **English text**：[[LA_09_05_QR_Decomposition_EN.pdf]]
- 🖼️ **PPT（中）**：[[LA_09_05_PPT_QR分解_中文.pdf]]
- 🖼️ **PPT（EN）**：[[LA_09_05_PPT_QR_Decomposition_EN.pdf]]
- 💻 **代码**：
    - [[代码/09-正交矩阵-QR分解/LA_09_05_01.ipynb|完全型QR分解]]
    - [[代码/09-正交矩阵-QR分解/LA_09_05_02.ipynb|经济型QR分解]]

## 学完请自查

- [ ] 不看笔记，能用一句话说出本章每节在讲什么
- [ ] 能挑 1–2 个核心 notebook，从空白文件默写出来（不偷看）
- [ ] 改掉某个参数，先**预测**图形怎么变，再跑代码验证
- [ ] 在下面写下本章最反直觉的一点

### 我的笔记

> 卡住的地方 / 自己的例子 / 与前几章的联系，都写在这里。

---

[[线性代数不难·导读|🏠 总览]] · [[00-全书地图|🗺️ 全书地图]] · [[第8章-几何变换|⬅ 第8章]] · [[第10章-线性回归|第10章 ➡]]
