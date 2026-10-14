# -*- coding: utf-8 -*-
"""生成 Obsidian 导读库：根索引 + 导读/ 下的指南与 15 张章节目录卡。
数据来源：_pdfinfo.json、_nbtitles.json（由仓库原始文件名解析）
运行：python _build_guide.py
"""
import io, json, os
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
GUIDE = '导读'

CH_ZH = {
    '01': '向量', '02': '矩阵', '03': '矩阵乘法的四种视角', '04': '行列式',
    '05': '逆矩阵', '06': '向量空间·线性组合与基底', '07': '线性方程组与初等行变换',
    '08': '几何变换', '09': '正交矩阵与QR分解', '10': '线性回归',
    '11': '特征值分解', '12': '数据矩阵·协方差与PCA', '13': '二次型·Cholesky·瑞利商',
    '14': '奇异值分解SVD', '15': '图论与拉普拉斯矩阵',
}
CH_EN = {
    '01': 'Vectors', '02': 'Matrices', '03': 'Four Views of Matrix Multiplication',
    '04': 'Determinants', '05': 'Inverse Matrices', '06': 'Vector Space, Linear Combination & Basis',
    '07': 'Linear Systems & Elementary Row Operations', '08': 'Geometric Transformations',
    '09': 'Orthogonal Matrices & QR Decomposition', '10': 'Linear Regression',
    '11': 'Eigenvalue Decomposition', '12': 'Data Matrix, Covariance & PCA',
    '13': 'Quadratic Forms, Cholesky & Rayleigh Quotient', '14': 'Singular Value Decomposition',
    '15': 'Graphs & Laplacian Matrix',
}
CH_DIR = {
    '01': '01-向量', '02': '02-矩阵', '03': '03-矩阵乘法四种视角', '04': '04-行列式',
    '05': '05-逆矩阵', '06': '06-向量空间-线性组合-基底', '07': '07-线性方程组-初等行变换',
    '08': '08-几何变换', '09': '09-正交矩阵-QR分解', '10': '10-线性回归',
    '11': '11-特征值分解', '12': '12-数据矩阵-PCA-协方差', '13': '13-二次型-Cholesky-瑞利商',
    '14': '14-奇异值分解SVD', '15': '15-图论-拉普拉斯矩阵',
}
CH_LEVEL = {
    '01': ('入门', '—'), '02': ('入门', '01'), '03': ('核心·难点', '02'),
    '04': ('入门', '02'), '05': ('入门', '04'), '06': ('核心', '01、02、03、05'),
    '07': ('核心', '05'), '08': ('入门', '03'), '09': ('进阶', '01、03、06'),
    '10': ('进阶·实战', '01、06、09'), '11': ('进阶·难点', '04、06、09'),
    '12': ('进阶·实战', '11'), '13': ('进阶', '11、12'), '14': ('高阶·压轴', '11、13'),
    '15': ('高阶·专题', '11、14'),
}
CH_HOURS = {
    '01': '6–8 小时', '02': '4–5 小时', '03': '6–8 小时', '04': '3–4 小时', '05': '3–4 小时',
    '06': '4–5 小时', '07': '4–5 小时', '08': '5–6 小时', '09': '5–6 小时', '10': '6–8 小时',
    '11': '5–7 小时', '12': '6–8 小时', '13': '4–5 小时', '14': '6–8 小时', '15': '6–8 小时',
}
# 章节名 → 文件名的合法化（去掉 Windows 不允许的字符）
def ch_file(num, ch):
    return '第%d章-%s' % (num, CH_ZH[ch])


def read_json(name):
    return json.load(io.open(name, encoding='utf-8'))


info = read_json('_pdfinfo.json')
nb = read_json('_nbtitles.json')

body = defaultdict(dict)
ppt = defaultdict(dict)
for i in info:
    if i.get('kind') == 'body':
        body[(i['ch'], i['sec'])][i['lang']] = i['name']
    elif i.get('kind') == 'ppt':
        ppt[(i['ch'], i['sec'])][i['lang']] = i['name']

nbs = defaultdict(list)
for n in nb:
    p = n['file'].split('_')
    nbs[(p[1], p[2])].append((n['file'], n['title']))

chapters = sorted(set(k[0] for k in body))
TOTAL_NB, TOTAL_PDF = len(nb), len(info)
WRITTEN = []


def W(path, text):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    io.open(path, 'w', encoding='utf-8', newline='\n').write(text)
    WRITTEN.append(path.replace('\\', '/'))


def nb_link(f, title):
    return '[[代码/%s/%s|%s]]' % (CH_DIR[f.split('_')[1]], f, title)


def esc(t):
    """表格里用的安全文本"""
    return t.replace('|', r'\|')


# ============================================================ 章节卡
for idx, ch in enumerate(chapters):
    num = int(ch)
    secs = sorted(set(k[1] for k in body if k[0] == ch))
    nb_total = sum(len(nbs.get((ch, s), [])) for s in secs)
    ppt_cnt = sum(1 for s in secs if ppt.get((ch, s)))
    level, pre = CH_LEVEL[ch]

    L = []
    L.append('---')
    L.append('tags: [线性代数不难, 导读]')
    L.append('chapter: %d' % num)
    L.append('type: 章节')
    L.append('progress: 未开始')
    L.append('---')
    L.append('')
    L.append('> [!info] 本章速览')
    L.append('> **第 %d 章 · %s**（%s）' % (num, CH_ZH[ch], CH_EN[ch]))
    L.append('> 难度 **%s** ｜ 建议前置：%s ｜ 预计投入 **%s**' % (
        level, pre if pre != '—' else '无（本书起点）', CH_HOURS[ch]))
    L.append('> 本书素材：%d 个 notebook ｜ %d 篇正文 PDF ｜ %d 份 PPT 讲义' % (nb_total, len(secs), ppt_cnt))
    L.append('')
    L.append('> [!tip] 三种素材怎么配合')
    L.append('> 1. **精读正文 PDF**：中文与英文正文内容对应，选一份精读，另一份只当“术语对照表”。')
    L.append('> 2. **PPT 讲义用来复习**：它是正文的图形压缩版，学完一节隔天翻一遍最划算。')
    L.append('> 3. **notebook 边跑边改**：每个 cell 都写了中文讲解；把参数改掉、预测图形、再运行验证。')
    L.append('')
    L.append('## 本章资源矩阵')
    L.append('')
    L.append('| 小节 | 主题 | 中文正文 | English | PPT | 代码 |')
    L.append('| --- | --- | --- | --- | --- | --- |')
    for s in secs:
        k = (ch, s)
        zh = body[k].get('zh')
        en = body[k].get('en')
        p = ppt.get(k, {})
        got = nbs.get(k, [])
        c_zh = '[[%s|中文]]' % zh if zh else '—'
        c_en = '[[%s|EN]]' % en if en else '—'
        c_ppt = ''
        if p.get('zh'):
            c_ppt += '[[%s|中]]' % p['zh']
        if p.get('en'):
            c_ppt += (' ' if c_ppt else '') + '[[%s|EN]]' % p['en']
        c_ppt = c_ppt or '—'
        c_nb = '%d 个' % len(got) if got else '*无*'
        L.append('| %s-%s | %s | %s | %s | %s | %s |' % (
            ch, s, esc(zh or '-'), c_zh, c_en, c_ppt, c_nb))
    L.append('')
    L.append('## 逐节素材与代码')
    L.append('')
    for s in secs:
        k = (ch, s)
        zh = body[k].get('zh')
        en = body[k].get('en')
        topic = zh
        if topic and topic.startswith('LA_'):
            topic = topic.split('_', 3)[3].rsplit('.pdf', 1)[0]
        L.append('### %s-%s　%s' % (ch, s, topic))
        L.append('')
        if zh:
            L.append('- 📖 **中文正文**：[[%s]]' % zh)
        if en:
            L.append('- 📘 **English text**：[[%s]]' % en)
        p = ppt.get(k, {})
        if p.get('zh'):
            L.append('- 🖼️ **PPT（中）**：[[%s]]' % p['zh'])
        if p.get('en'):
            L.append('- 🖼️ **PPT（EN）**：[[%s]]' % p['en'])
        got = nbs.get(k, [])
        if got:
            L.append('- 💻 **代码**：')
            for f, t in got:
                L.append('    - %s' % nb_link(f, t))
        else:
            L.append('- 💻 **代码**：*本仓库未收录该节 notebook（正文 + PPT 已足够）*')
        L.append('')
    L.append('## 学完请自查')
    L.append('')
    L.append('- [ ] 不看笔记，能用一句话说出本章每节在讲什么')
    L.append('- [ ] 能挑 1–2 个核心 notebook，从空白文件默写出来（不偷看）')
    L.append('- [ ] 改掉某个参数，先**预测**图形怎么变，再跑代码验证')
    L.append('- [ ] 在下面写下本章最反直觉的一点')
    L.append('')
    L.append('### 我的笔记')
    L.append('')
    L.append('> 卡住的地方 / 自己的例子 / 与前几章的联系，都写在这里。')
    L.append('')
    L.append('---')
    L.append('')
    nav = ['[[线性代数不难·导读|🏠 总览]]', '[[00-全书地图|🗺️ 全书地图]]']
    if idx > 0:
        nav.append('[[%s|⬅ 第%d章]]' % (ch_file(int(chapters[idx - 1]), chapters[idx - 1]),
                                       int(chapters[idx - 1])))
    if idx < len(chapters) - 1:
        nav.append('[[%s|第%d章 ➡]]' % (ch_file(int(chapters[idx + 1]), chapters[idx + 1]),
                                       int(chapters[idx + 1])))
    L.append(' · '.join(nav))
    L.append('')
    W(os.path.join('..', GUIDE, ch_file(num, ch) + '.md'), '\n'.join(L))

# ============================================================ 00 全书地图
L = []
L.append('---')
L.append('tags: [线性代数不难, 导读, 地图]')
L.append('type: 总览')
L.append('---')
L.append('')
L.append('# 🗺️ 全书地图：15 章知识依赖')
L.append('')
L.append('> [!abstract] 怎么用这张地图')
L.append('> 箭头表示「**先学过 A，再学 B 才顺**」。每张卡片都可以点击跳转。')
L.append('> 想走最短路径，就顺着 [[02-学习路线图与节奏|学习路线图]] 里的主线走。')
L.append('')
L.append('```mermaid')
L.append('flowchart LR')
L.append('    C01["第1章 向量"] --> C02["第2章 矩阵"]')
L.append('    C02 --> C03["第3章 矩阵乘法<br/>四种视角 ⭐难点"]')
L.append('    C02 --> C04["第4章 行列式"]')
L.append('    C04 --> C05["第5章 逆矩阵"]')
L.append('    C03 --> C06["第6章 向量空间<br/>线性组合·基底"]')
L.append('    C05 --> C06')
L.append('    C05 --> C07["第7章 线性方程组<br/>初等行变换"]')
L.append('    C03 --> C08["第8章 几何变换"]')
L.append('    C06 --> C09["第9章 正交矩阵<br/>QR分解"]')
L.append('    C09 --> C10["第10章 线性回归"]')
L.append('    C09 --> C11["第11章 特征值分解"]')
L.append('    C11 --> C12["第12章 数据矩阵<br/>协方差·PCA"]')
L.append('    C11 --> C13["第13章 二次型<br/>Cholesky·瑞利商"]')
L.append('    C13 --> C14["第14章 SVD ⭐压轴"]')
L.append('    C11 --> C15["第15章 图论<br/>拉普拉斯矩阵"]')
L.append('```')
L.append('')
L.append('> [!note] Mermaid 不显示？')
L.append('> 上图需要 Obsidian 自带渲染（一般默认可用）。若看不到，直接看下面的表格。')
L.append('')
L.append('## 三条学习主线')
L.append('')
L.append('| 主线 | 路径 | 学完能做什么 |')
L.append('| --- | --- | --- |')
L.append('| **A 最小可用线**（新手必走） | 01 → 02 → 03 → 04 → 05 → 06 → 07 | 看懂矩阵算式，会解线性方程组，建立几何直觉 |')
L.append('| **B 数据科学线** | A + 09 → 10 → 11 → 12 → 14 | 手写最小二乘、PCA、SVD 降维，理解它们的来龙去脉 |')
L.append('| **C 图形与图论线** | A + 08 → 09 → 14 → 15 | 明白旋转/缩放/投影矩阵、谱聚类、拉普拉斯矩阵 |')
L.append('')
L.append('## 15 章一览')
L.append('')
L.append('| 章 | 主题（中） | 主题（英） | 难度 | 前置 | 代码 |')
L.append('| --- | --- | --- | --- | --- | --- |')
for ch in chapters:
    num = int(ch)
    secs = sorted(set(k[1] for k in body if k[0] == ch))
    cnt = sum(len(nbs.get((ch, s), [])) for s in secs)
    level, pre = CH_LEVEL[ch]
    L.append('| [[%s|第%d章]] | %s | %s | %s | %s | %d |' % (
        ch_file(num, ch), num, CH_ZH[ch], CH_EN[ch], level, pre, cnt))
L.append('')
L.append('## 名词对照（中文 ↔ English）')
L.append('')
L.append('| 中文 | English | 出现在 |')
L.append('| --- | --- | --- |')
for zh_term, en_term, where in [
    ('向量 / 标量 / 内积', 'vector / scalar / inner product', '第 1 章'),
    ('范数（L1、L2、L∞）', 'norm', '第 1 章'),
    ('转置 / 形状', 'transpose / shape', '第 2 章'),
    ('分块矩阵乘法', 'block matrix multiplication', '第 3 章'),
    ('行列式', 'determinant', '第 4 章'),
    ('逆矩阵 / 伴随矩阵', 'inverse / adjugate', '第 5 章'),
    ('向量空间 / 线性组合 / 基底', 'vector space / linear combination / basis', '第 6 章'),
    ('初等行变换', 'elementary row operations', '第 7 章'),
    ('仿射变换 / 剪切 / 镜像', 'affine transformation / shear / reflection', '第 8 章'),
    ('正交矩阵 / 格拉姆-施密特正交化 / QR 分解', 'orthogonal matrix / Gram–Schmidt / QR decomposition', '第 9 章'),
    ('线性回归 / 最小二乘', 'linear regression / least squares', '第 10 章'),
    ('特征值分解（EVD）/ 谱分解', 'eigenvalue decomposition / spectral decomposition', '第 11 章'),
    ('协方差矩阵 / 主成分分析（PCA）', 'covariance matrix / principal component analysis', '第 12 章'),
    ('二次型 / 正定性 / 瑞利商', 'quadratic form / positive definiteness / Rayleigh quotient', '第 13 章'),
    ('奇异值分解（SVD）/ 截断 SVD', 'singular value decomposition / truncated SVD', '第 14 章'),
    ('邻接矩阵 / 度矩阵 / 拉普拉斯矩阵 / 谱聚类', 'adjacency / degree / Laplacian / spectral clustering', '第 15 章'),
]:
    L.append('| %s | %s | %s |' % (zh_term, en_term, where))
L.append('')
L.append('---')
L.append('')
L.append('导航：[[线性代数不难·导读|🏠 总览]] · [[02-学习路线图与节奏|📅 学习路线图]]')
L.append('')
W(os.path.join('..', GUIDE, '00-全书地图.md'), '\n'.join(L))

io.open('_guide_chapters.json', 'w', encoding='utf-8').write(
    json.dumps({'chapters': chapters, 'files': WRITTEN}, ensure_ascii=False, indent=1))
print('已生成 %d 个文件' % len(WRITTEN))
for f in WRITTEN:
    print('  +', f)
