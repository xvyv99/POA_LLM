import util
import json

res = util.ResultIter('res.log.merge')

with open('modify.log', 'a') as f:
    for l in res:
        if ('polarity' not in l) or ('intensity' not in l) or ('time' not in l):
            continue
        
        if l['polarity'] in ('正面','正','正向','积极','积极、赞同、喜欢','积极、赞同'):
            l['polarity'] = '积极'
        elif l['polarity'] in ('中','中立','中性'):
            l['polarity'] = '中立'
        elif l['polarity'] in ('负面','消极','愤怒'):
            l['polarity'] = '消极'
        else:
            continue

        if l['intensity'] in ('高','高度'):
            l['intensity'] = 3
        elif l['intensity'] in ('中','中等','中性','适度','一般'):
            l['intensity'] = 2
        elif l['intensity'] in ('低','稍低','稍轻','轻微','较低','稍有','稍','稍微'):
            l['intensity'] = 1
        else:
            continue

        f.write(json.dumps(l)+'\n')