import io, json
plan = json.load(io.open('_moveplan.json', encoding='utf-8'))
srcs = set(p['src'] for p in plan)
import glob
allf = [f for f in glob.glob('*.pdf') + glob.glob('*.ipynb') + glob.glob('*.pkl')]
missing = [f for f in allf if f not in srcs]
lines = ['plan=%d  total=%d  missing=%d' % (len(plan), len(allf), len(missing)), '']
lines += ['MISSING: ' + f for f in missing]
lines.append('')
from collections import Counter
lines.append(str(Counter(p['dst'].split('/')[1] + '/' + p['dst'].split('/')[2] for p in plan)))
io.open('_check.txt', 'w', encoding='utf-8').write('\n'.join(lines))
print('ok')
