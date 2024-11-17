import matplotlib.pyplot as plt
import util

res = util.ResultIter('modify.log')
sc = util.SubCounter()

for x in res:
    sc.add(x)

yp = []
yn = []
ym = []

y0 = []

timeline = sorted(sc.count)[45:]
for t in timeline:
    p = sc.count[t][0]
    n = sc.count[t][2]
    m = sc.count[t][1]
    pp = p/(p+n) if p+n!=0 else 0
    ym.append(m)
    yn.append(n)
    yp.append(p)
    y0.append(p-n)

plt.rcParams['font.sans-serif'] = ['SimHei']

plt.plot(timeline, yp, label='正面')
plt.plot(timeline, ym, label='中性')
plt.plot(timeline, yn, label='负面')
plt.xticks(rotation=15)
plt.legend()
plt.savefig("asset/trend0.svg")

plt.close()
plt.plot(timeline, y0)
plt.savefig("asset/trend1.svg")
