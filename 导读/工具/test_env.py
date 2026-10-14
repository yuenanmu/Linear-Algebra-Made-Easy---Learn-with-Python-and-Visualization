# -*- coding: utf-8 -*-
"""《线性代数不难》配套环境自检脚本。

用法（先激活你的环境）:
    python 导读/工具/test_env.py

它会检查：
  1. Python 版本是否合适
  2. 本书用到的库是否都装了
  3. 数据文件（.pkl）能否正常读取
  4. 中文字体是否能正常显示
  5. 画一张图、存一份文件，确认绘图链路通畅
"""
import os
import sys

OK, BAD, WARN = '[ OK ]', '[FAIL]', '[WARN]'
problems = []
warnings = []


def line(tag, msg):
    print('%s %s' % (tag, msg))


print('=' * 62)
print(' 《线性代数不难》环境自检')
print('=' * 62)

# ---------------------------------------------------------------- 1. Python
v = sys.version_info
line(OK if v >= (3, 9) else BAD, 'Python %d.%d.%d  (%s)' % (
    v.major, v.minor, v.micro, sys.executable))
if v < (3, 9):
    problems.append('Python 版本过低，请使用 3.10–3.12')
elif v >= (3, 14):
    warnings.append('Python 3.14 较新，个别科学计算库可能缺少安装包；'
                    '如遇安装失败请改用 3.12')

# ---------------------------------------------------------------- 2. 依赖库
LIBS = [
    ('numpy', '数值计算', True),
    ('pandas', '数据框 / 读取 .pkl', True),
    ('matplotlib', '绘图', True),
    ('seaborn', '统计图形 / 热图', True),
    ('networkx', '第 15 章 图论', True),
    ('sklearn', '第 10 章 回归', True),
    ('statsmodels', '第 12 章 PCA', True),
    ('sympy', '符号计算（求逆等）', True),
    ('scipy', '科学计算（可选）', False),
    ('jupyter', '打开 notebook（可选）', False),
]
print('-' * 62)
mods = {}
for name, why, need in LIBS:
    try:
        m = __import__(name)
        mods[name] = m
        ver = getattr(m, '__version__', '?')
        line(OK, '%-12s %-10s  %s' % (name, ver, why))
    except ImportError:
        if need:
            line(BAD, '%-12s %-10s  %s' % (name, '未安装', why))
            problems.append('缺少 %s（%s）' % (name, why))
        else:
            line(WARN, '%-12s %-10s  %s' % (name, '未安装', why))
            warnings.append('可选库 %s 未安装' % name)

if problems:
    print('-' * 62)
    print('👉 安装缺失的库（任选其一）：')
    print('   conda install -c conda-forge ' + ' '.join(
        p.split('（')[0].replace('缺少 ', '') for p in problems))
    print('   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ' +
          ' '.join(p.split('（')[0].replace('缺少 ', '') for p in problems))
    print('=' * 62)
    line(BAD, '环境不完整，请先补齐上面的库再运行本书代码。')
    sys.exit(1)

# ---------------------------------------------------------------- 3. 数据
print('-' * 62)
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
data_dir = os.path.join(root, '代码', '12-数据矩阵-PCA-协方差')
for fn, expect in [('X_df_iris.pkl', (150, 5)), ('X_df.pkl', (248, 8))]:
    path = os.path.join(data_dir, fn)
    if not os.path.exists(path):
        line(WARN, '找不到数据文件 %s（不影响前 11 章）' % fn)
        warnings.append('缺少数据文件 %s' % fn)
        continue
    try:
        import pandas as pd
        df = pd.read_pickle(path)
        shape = getattr(df, 'shape', None)
        if expect and shape == expect:
            line(OK, '%s 读取成功，形状 %s（与第 12 章描述一致）' % (fn, shape))
        else:
            line(OK, '%s 读取成功，形状 %s' % (fn, shape))
    except Exception as e:
        line(BAD, '%s 读取失败：%s' % (fn, e))
        problems.append('数据文件 %s 读取失败' % fn)

# ---------------------------------------------------------------- 4. 中文
print('-' * 62)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'PingFang SC',
                                   'Noto Sans CJK SC', 'Source Han Sans SC',
                                   'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

try:
    fig, ax = plt.subplots(figsize=(3, 2))
    ax.set_title('中文测试 向量与矩阵')
    ax.plot([0, 1], [0, 1])
    out = os.path.join(here, '_font_test.png')
    fig.savefig(out, dpi=80)
    plt.close(fig)
    line(OK, '中文字体设置完成（若图中方块请装中文字体）')
    os.remove(out)
except Exception as e:
    line(WARN, '字体测试出现异常：%s' % e)

# ---------------------------------------------------------------- 5. 数值
print('-' * 62)
try:
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    line(OK, 'numpy 一维数组：a.shape=%s，a[-1]=%s（第 1 章第一个 notebook 的内容）'
         % (a.shape, a[-1]))
    A = np.array([[1., 2.], [3., 4.]])
    line(OK, 'numpy 行列式 det=%s，逆矩阵计算正常' % round(float(np.linalg.det(A)), 4))
    ev = np.linalg.eigvalsh(np.cov(np.random.rand(4, 20)))
    line(OK, '对称矩阵特征值（eigh）：%s' % np.round(ev, 3))
except Exception as e:
    line(BAD, '数值计算测试失败：%s' % e)
    problems.append('数值计算失败')

# ---------------------------------------------------------------- 结论
print('=' * 62)
if problems:
    line(BAD, '环境有问题，见上方 [FAIL]')
    sys.exit(1)
line(OK, '环境 OK —— 可以开始学习了！')
if warnings:
    print('提醒：')
    for w in warnings:
        print('  · %s' % w)
print('下一步：打开 代码/01-向量/LA_01_01_01.ipynb 跑起来。')
print('=' * 62)
