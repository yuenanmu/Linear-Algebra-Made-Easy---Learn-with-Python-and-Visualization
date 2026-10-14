# -*- coding: utf-8 -*-
"""生成/执行 线性代数不难 仓库的文件整理方案。

用法:
    python _reorganize.py --dry     # 只打印计划
    python _reorganize.py --apply   # 用 git mv 真正执行
"""
import glob, io, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

BOOK = '书籍PDF'
NB = '代码'
CH_NAME = {
    '01': '01-向量', '02': '02-矩阵', '03': '03-矩阵乘法四种视角', '04': '04-行列式',
    '05': '05-逆矩阵', '06': '06-向量空间-线性组合-基底', '07': '07-线性方程组-初等行变换',
    '08': '08-几何变换', '09': '09-正交矩阵-QR分解', '10': '10-线性回归',
    '11': '11-特征值分解', '12': '12-数据矩阵-PCA-协方差', '13': '13-二次型-Cholesky-瑞利商',
    '14': '14-奇异值分解SVD', '15': '15-图论-拉普拉斯矩阵',
}

moves = []          # (src, dst)


def add(src, dst):
    if os.path.exists(src):
        moves.append((src, dst))
    else:
        print('  !! 源文件不存在，跳过:', src)


# ---------- 1. PDF ----------
special = []
for p in sorted(glob.glob('*.pdf')):
    m = re.match(r'LA_(\d\d)_(\d\d)_(.*)\.pdf$', p)
    if not m:
        special.append(p)
        continue
    ch, sec, rest = m.groups()
    kind = 'ppt' if rest.startswith('PPT_') else 'body'
    if rest.startswith('PPT_'):
        rest = rest[4:]
    if p.startswith('LA_00_'):
        kind = 'front'
    lang = 'zh' if re.search(r'[\u4e00-\u9fff]', rest) else 'en'
    sub = {'zh': '中文', 'en': 'English'}[lang]
    folder = {'body': '01-正文', 'ppt': '02-PPT讲义', 'front': '00-正文前'}[kind]
    add(p, os.path.join(BOOK, sub, folder, p))

for p in special:                     # 整体布局.pdf 等
    add(p, os.path.join(BOOK, '00-导读与总览', p))

# ---------- 2. ipynb ----------
for p in sorted(glob.glob('*.ipynb')):
    m = re.match(r'LA_(\d\d)_(\d\d)_(\d\d)\.ipynb$', p)
    if not m:
        print('  !! 无法解析的 notebook:', p)
        continue
    ch = m.group(1)
    add(p, os.path.join(NB, CH_NAME[ch], p))

# ---------- 3. 数据 ----------
for p in sorted(glob.glob('*.pkl')):
    add(p, os.path.join(NB, '12-数据矩阵-PCA-协方差', p))

# ---------- 输出 ----------
plan = [{'src': s, 'dst': d.replace('\\', '/')} for s, d in moves]
io.open('_moveplan.json', 'w', encoding='utf-8').write(
    json.dumps(plan, ensure_ascii=False, indent=1))

print('计划移动 %d 个文件' % len(plan))
print('留原地的文件:', [f for f in os.listdir('.')
                     if os.path.isfile(f) and not f.startswith('_')
                     and not f.endswith(('.pdf', '.ipynb', '.pkl'))])

if '--apply' not in sys.argv:
    sys.exit(0)

ok = fail = 0
for item in plan:
    src, dst = item['src'], item['dst']
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    r = subprocess.run(['git', 'mv', '-f', src, dst],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode == 0:
        ok += 1
    else:
        try:
            os.replace(src, dst)
            ok += 1
        except Exception as e:
            fail += 1
            print('  失败:', src, '->', dst, r.stderr.strip()[:120], e)
print('完成: 成功 %d, 失败 %d' % (ok, fail))
