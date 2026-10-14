# -*- coding: utf-8 -*-
"""校验 导读/ 与根 README 里的所有 [[wikilink]] 是否能解析到真实文件。
用法（在仓库任意位置）：python _scripts/_validate_links.py
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))   # _scripts/
os.chdir(HERE)

# 建立索引：所有可被链接的文件的相对仓库根路径
files = []
for dirpath, dirnames, filenames in os.walk('..'):
    dirnames[:] = [d for d in dirnames
                   if d not in ('.git', '.obsidian', '__pycache__')]
    for fn in filenames:
        p = os.path.relpath(os.path.join(dirpath, fn), HERE).replace('\\', '/')
        if p.startswith('../'):
            p = p[3:]
        files.append(p)

by_path = set(files)
by_name = {}
for p in files:
    by_name.setdefault(os.path.basename(p), []).append(p)
by_stem = {}
for p in files:
    if p.lower().endswith('.md'):
        by_stem.setdefault(os.path.splitext(os.path.basename(p))[0], []).append(p)


def resolve(t):
    if t in by_path:
        return True
    if t + '.md' in by_path:
        return True
    b = os.path.basename(t)
    if b in by_name or b + '.md' in by_name:
        return True
    if os.path.splitext(b)[0] in by_stem:
        return True
    return False


LINK = re.compile(r'\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]')
md_files = ['../线性代数不难·导读.md'] + sorted(
    os.path.join('..', '导读', f) for f in os.listdir(os.path.join('..', '导读'))
    if f.endswith('.md'))

total = ok = 0
broken = {}
for mf in md_files:
    text = io.open(mf, encoding='utf-8').read()
    for raw in LINK.findall(text):
        t = raw.strip()
        if not t or t.startswith('http'):
            continue
        total += 1
        if resolve(t):
            ok += 1
        else:
            broken.setdefault(t, []).append(os.path.basename(mf))

out = ['索引文件数: %d' % len(files),
       '链接总数: %d 可解析: %d 异常: %d' % (total, ok, total - ok)]
for t, where in sorted(broken.items()):
    out.append('  x [[%s]] : %s' % (t, ', '.join(sorted(set(where))[:2])))
out.append('全部链接有效 OK' if not broken else '存在无效链接，见上')
io.open(os.path.join(HERE, '_linkcheck.txt'), 'w', encoding='utf-8').write(
    '\n'.join(out))
print('\n'.join(out))
sys.exit(0 if not broken else 1)
