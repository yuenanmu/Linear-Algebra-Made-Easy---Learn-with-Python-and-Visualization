import io, json

d = json.load(io.open('_pdfinfo.json', encoding='utf-8'))
n = 0
for i in d:
    if i.get('kind') == 'OTHER' or not i['file'].startswith('LA_'):
        continue
    prefix = 'PPT_' if i.get('kind') == 'ppt' else ''
    full = 'LA_%s_%s_%s%s.pdf' % (i['ch'], i['sec'], prefix, i['name'])
    assert full == i['file'], (full, i['file'])
    i['name'] = full
    n += 1
io.open('_pdfinfo.json', 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1))
print('fixed', n, 'entries')
