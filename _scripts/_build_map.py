import json, io
from collections import defaultdict

info = json.load(io.open('_pdfinfo.json', encoding='utf-8'))
nb = json.load(io.open('_nbtitles.json', encoding='utf-8'))

zh, en = {}, {}
ppt = defaultdict(lambda: [None, None])
for i in info:
    if i.get('kind') == 'body':
        key = (i['ch'], i['sec'])
        (zh if i['lang'] == 'zh' else en)[key] = i['name']
    elif i.get('kind') == 'ppt':
        key = (i['ch'], i['sec'])
        ppt[key][0 if i['lang'] == 'zh' else 1] = i['name']

nbs = defaultdict(list)
for n in nb:
    parts = n['file'].split('_')
    nbs[(parts[1], parts[2])].append((n['file'], n['title']))

lines = []
for ch in sorted(set(k[0] for k in zh)):
    lines.append('=' * 78)
    lines.append('第 %d 章  (章节ID %s)' % (int(ch), ch))
    for s in sorted(set(k[1] for k in zh if k[0] == ch)):
        k = (ch, s)
        lines.append('  [%s-%s] 中: %s' % (ch, s, zh[k]))
        lines.append('           英: %s' % en.get(k, '-'))
        lines.append('           PPT中/英: %s | %s' % (ppt[k][0], ppt[k][1]))
        if nbs.get(k):
            for f, t in nbs[k]:
                lines.append('           NB %s : %s' % (f, t))
        else:
            lines.append('           NB 无')
    lines.append('')

io.open('_map.txt', 'w', encoding='utf-8').write('\n'.join(lines))
print('written lines:', len(lines))
