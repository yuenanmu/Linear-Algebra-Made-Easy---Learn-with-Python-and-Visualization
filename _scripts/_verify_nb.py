# -*- coding: utf-8 -*-
"""只读校验：把 notebook 的代码单元格抽取出来执行，检查代码是否能跑通。
不修改原文件；画图使用 Agg 后端（不弹窗）。
用法: python _verify_nb.py <notebook 路径> [更多路径...]
"""
import io, json, os, sys, traceback

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402


def run(path):
    path = os.path.abspath(path)
    d = json.load(io.open(path, encoding='utf-8'))
    cells = []
    for i, c in enumerate(d['cells']):
        if c['cell_type'] != 'code':
            continue
        code = ''.join(c['source'])
        if not code.strip():
            continue
        code = '\n'.join(l for l in code.split('\n')
                         if not l.lstrip().startswith(('%', '!')))
        cells.append((i, code))

    g = {'__name__': '__main__', 'plt': plt}
    old = os.getcwd()
    os.chdir(os.path.dirname(path))     # 让 read_pickle 等相对路径生效
    ok = 0
    try:
        for i, code in cells:
            try:
                exec(compile(code, '<cell %d>' % i, 'exec'), g)
                ok += 1
            except Exception:
                print('  [FAIL] cell %d in %s' % (i, os.path.basename(path)))
                traceback.print_exc(limit=2)
                return False, '%d/%d cells ok' % (ok, len(cells))
            plt.close('all')
    finally:
        os.chdir(old)
    return True, '%d cells ok' % ok


if __name__ == '__main__':
    total_ok = 0
    for p in sys.argv[1:]:
        base = os.path.basename(p)
        try:
            good, msg = run(p)
        except Exception as e:
            good, msg = False, 'open failed: %s' % e
        print(('  PASS ' if good else '  FAIL ') + base + '  ' + msg)
        total_ok += 1 if good else 0
    print('== %d/%d notebooks 可跑通 ==' % (total_ok, len(sys.argv) - 1))
