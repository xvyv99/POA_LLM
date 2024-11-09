import util

res = util.ResultIter()
pd = {}
id = {}

for l in res:
    if 'polarity' not in l:
        continue
    if l['polarity'] in pd:
        pd[l['polarity']] += 1
    else:
        pd[l['polarity']] = 1

    if 'intensity' not in l:
        continue
    if l['intensity'] in pd:
        id[l['intensity']] += 1
    else:
        id[l['intensity']] = 1
print(pd)
print(id)