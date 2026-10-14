import io, json, sys

def cells(path):
    return json.load(io.open(path, encoding='utf-8'))['cells']

def show(path, idxs, label=''):
    cs = cells(path)
    print('=' * 70)
    print(path, label)
    for i in idxs:
        c = cs[i]
        print('---- cell %d (%s) ----' % (i, c['cell_type']))
        print(''.join(c['source'])[:900])

def magics(path):
    out = []
    for i, c in enumerate(cells(path)):
        if c['cell_type'] != 'code':
            continue
        for line in ''.join(c['source']).split('\n'):
            s = line.strip()
            if s.startswith('%') or s.startswith('!'):
                out.append((i, s))
    return out

TARGETS = [
    '代码/01-向量/LA_01_08_05.ipynb',
    '代码/04-行列式/LA_04_04_01.ipynb',
    '代码/12-数据矩阵-PCA-协方差/LA_12_03_01.ipynb',
    '代码/15-图论-拉普拉斯矩阵/LA_15_04_01.ipynb',
]
for p in TARGETS:
    print('###', p)
    for i, s in magics(p):
        print('   magic cell %d: %s' % (i, s))

show('代码/01-向量/LA_01_08_05.ipynb', [6, 7, 8])
show('代码/04-行列式/LA_04_04_01.ipynb', [7, 8, 9])
show('代码/12-数据矩阵-PCA-协方差/LA_12_03_01.ipynb', [30, 31, 32])
show('代码/15-图论-拉普拉斯矩阵/LA_15_04_01.ipynb', [29, 30, 31])
