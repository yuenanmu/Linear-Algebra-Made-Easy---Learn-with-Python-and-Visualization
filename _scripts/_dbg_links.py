# -*- coding: utf-8 -*-
import io, os, re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.join(ROOT, '..'))

files = []
for dirpath, dirnames, filenames in os.walk('.'):
    dirnames[:] = [d for d in dirnames if d not in ('.git', '.obsidian', '__pycache__')]
    for fn in filenames:
        files.append(os.path.relpath(os.path.join(dirpath, fn), '.').replace('\\', '/'))

by_path = set(files)
by_name = {}
for p in files:
    by_name.setdefault(os.path.basename(p), []).append(p)
by_stem = {}
for p in files:
    if p.lower().endswith('.md'):
        by_stem.setdefault(os.path.splitext(os.path.basename(p))[0], []).append(p)

print('索引文件数:', len(files))
print('示例 PDF 条目:', [p for p in files if p.endswith('.pdf')][:3])
print('by_name 里含"什么是向量"的键:',
      [k for k in by_name if '什么是向量' in k][:6])


def resolve(t):
    if t in by_path:
        return True, 'path'
    if t + '.md' in by_path:
        return True, 'path+.md'
    b = os.path.basename(t)
    if b in by_name:
        return True, 'basename'
    if b + '.md' in by_name:
        return True, 'basename+.md'
    stem = os.path.splitext(b)[0]
    if stem in by_stem:
        return True, 'stem'
    return False, ''


LINK = re.compile(r'\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]')
md_files = ['线性代数不难·导读.md'] + sorted(
    os.path.join('导读', f) for f in os.listdir('导读') if f.endswith('.md'))

total = ok = 0
broken = {}
for mf in md_files:
    text = io.open(mf, encoding='utf-8').read()
    for raw in LINK.findall(text):
        t = raw.strip()
        if not t or t.startswith('http'):
            continue
        total += 1
        good, how = resolve(t)
        if good:
            ok += 1
        else:
            broken.setdefault(t, []).append(mf)

print('链接总数: %d 可解析: %d 异常: %d' % (total, ok, total - ok))
for t, where in sorted(broken.items())[:25]:
    print('  x [[%s]] : %s' % (t, ', '.join(sorted(set(where))[:1])))
