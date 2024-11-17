import util

res = util.ResultIter('modify.log')
pd = util.Counter()
id = util.Counter()
td = util.timeCounter()

for l in res:
    if 'polarity' in l:
        pd.add(l['polarity'])

    if 'intensity' in l:
        id.add(l['intensity'])

    if 'time' in l:
        td.add(util.tranformDate(l['time']))

print(pd.count)
print(id.count)
print(sorted(td.count.keys()))
print(res.cur_index_)