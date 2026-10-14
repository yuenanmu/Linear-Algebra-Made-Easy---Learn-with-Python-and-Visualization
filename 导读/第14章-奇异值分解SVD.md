---
tags: [线性代数不难, 导读]
chapter: 14
type: 章节
progress: 未开始
---

> [!info] 本章速览
> **第 14 章 · 奇异值分解SVD**（Singular Value Decomposition）
> 难度 **高阶·压轴** ｜ 建议前置：11、13 ｜ 预计投入 **6–8 小时**
> 本书素材：1 个 notebook ｜ 4 篇正文 PDF ｜ 4 份 PPT 讲义

> [!tip] 三种素材怎么配合
> 1. **精读正文 PDF**：中文与英文正文内容对应，选一份精读，另一份只当“术语对照表”。
> 2. **PPT 讲义用来复习**：它是正文的图形压缩版，学完一节隔天翻一遍最划算。
> 3. **notebook 边跑边改**：每个 cell 都写了中文讲解；把参数改掉、预测图形、再运行验证。

## 本章资源矩阵

| 小节 | 主题 | 中文正文 | English | PPT | 代码 |
| --- | --- | --- | --- | --- | --- |
| 14-01 | LA_14_01_奇异值分解.pdf | [[LA_14_01_奇异值分解.pdf|中文]] | [[LA_14_01_SVD_EN.pdf|EN]] | [[LA_14_01_PPT_奇异值分解_中文.pdf|中]] [[LA_14_01_PPT_Singular_Value_Decomposition_EN.pdf|EN]] | 1 个 |
| 14-02 | LA_14_02_几何角度看SVD.pdf | [[LA_14_02_几何角度看SVD.pdf|中文]] | [[LA_14_02_SVD_Geometric_View_EN.pdf|EN]] | [[LA_14_02_PPT_几何视角看SVD_中文.pdf|中]] [[LA_14_02_PPT_Geometric_View_of_SVD_EN.pdf|EN]] | *无* |
| 14-03 | LA_14_03_四种奇异值分解.pdf | [[LA_14_03_四种奇异值分解.pdf|中文]] | [[LA_14_03_Four_Types_of_SVD_EN.pdf|EN]] | [[LA_14_03_PPT_四种奇异值分解_中文.pdf|中]] [[LA_14_03_PPT_Four_Flavors_of_SVD_EN.pdf|EN]] | *无* |
| 14-04 | LA_14_04_截断SVD.pdf | [[LA_14_04_截断SVD.pdf|中文]] | [[LA_14_04_Truncated_SVD_EN.pdf|EN]] | [[LA_14_04_PPT_截断型奇异值分解_中文.pdf|中]] [[LA_14_04_PPT_Truncated_SVD_EN.pdf|EN]] | *无* |

## 逐节素材与代码

### 14-01　奇异值分解

- 📖 **中文正文**：[[LA_14_01_奇异值分解.pdf]]
- 📘 **English text**：[[LA_14_01_SVD_EN.pdf]]
- 🖼️ **PPT（中）**：[[LA_14_01_PPT_奇异值分解_中文.pdf]]
- 🖼️ **PPT（EN）**：[[LA_14_01_PPT_Singular_Value_Decomposition_EN.pdf]]
- 💻 **代码**：
    - [[代码/14-奇异值分解SVD/LA_14_01_01.ipynb|两个格拉姆矩阵的谱分解还原SVD]]

### 14-02　几何角度看SVD

- 📖 **中文正文**：[[LA_14_02_几何角度看SVD.pdf]]
- 📘 **English text**：[[LA_14_02_SVD_Geometric_View_EN.pdf]]
- 🖼️ **PPT（中）**：[[LA_14_02_PPT_几何视角看SVD_中文.pdf]]
- 🖼️ **PPT（EN）**：[[LA_14_02_PPT_Geometric_View_of_SVD_EN.pdf]]
- 💻 **代码**：*本仓库未收录该节 notebook（正文 + PPT 已足够）*

### 14-03　四种奇异值分解

- 📖 **中文正文**：[[LA_14_03_四种奇异值分解.pdf]]
- 📘 **English text**：[[LA_14_03_Four_Types_of_SVD_EN.pdf]]
- 🖼️ **PPT（中）**：[[LA_14_03_PPT_四种奇异值分解_中文.pdf]]
- 🖼️ **PPT（EN）**：[[LA_14_03_PPT_Four_Flavors_of_SVD_EN.pdf]]
- 💻 **代码**：*本仓库未收录该节 notebook（正文 + PPT 已足够）*

### 14-04　截断SVD

- 📖 **中文正文**：[[LA_14_04_截断SVD.pdf]]
- 📘 **English text**：[[LA_14_04_Truncated_SVD_EN.pdf]]
- 🖼️ **PPT（中）**：[[LA_14_04_PPT_截断型奇异值分解_中文.pdf]]
- 🖼️ **PPT（EN）**：[[LA_14_04_PPT_Truncated_SVD_EN.pdf]]
- 💻 **代码**：*本仓库未收录该节 notebook（正文 + PPT 已足够）*

## 学完请自查

- [ ] 不看笔记，能用一句话说出本章每节在讲什么
- [ ] 能挑 1–2 个核心 notebook，从空白文件默写出来（不偷看）
- [ ] 改掉某个参数，先**预测**图形怎么变，再跑代码验证
- [ ] 在下面写下本章最反直觉的一点

### 我的笔记

> 卡住的地方 / 自己的例子 / 与前几章的联系，都写在这里。

---

[[线性代数不难·导读|🏠 总览]] · [[00-全书地图|🗺️ 全书地图]] · [[第13章-二次型·Cholesky·瑞利商|⬅ 第13章]] · [[第15章-图论与拉普拉斯矩阵|第15章 ➡]]
