from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
import util
import pickle
from tqdm import tqdm
from collections import Counter

word_count = Counter()
it = util.DataIter()

"""with tqdm(total=util.DataIter.ITEM_COUNT) as pbar:
    for o in it:
        word_list = jieba.cut(o['content'])
        word_count.update(word_list)
        pbar.update(1)"""

with open('./asset/wc.pkl', 'rb') as f:
    word_count = pickle.load(f)
print(word_count)

del_key = []
for k in word_count.keys():
    if len(k)<2:
        del_key.append(k)

for k in del_key:
    del word_count[k]

# 创建词云对象（设置中文字体）
wordcloud = WordCloud(width=800, height=400,
    font_path="C:\\Windows\\Fonts\\simhei.ttf",  # 需要设置中文字体路径
    background_color='white'
).generate_from_frequencies(word_count)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.savefig('asset/cloud.png', dpi=500)