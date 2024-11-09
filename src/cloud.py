from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
import util
import pickle
from tqdm import tqdm
from collections import Counter

word_count = Counter()
it = util.DataIter()

with tqdm(total=util.DataIter.ITEM_COUNT) as pbar:
    for o in it:
        word_list = jieba.cut(o['content'])
        word_count.update(word_list)
        pbar.update(1)

with open('./asset/wc.pkl', 'wb') as f:
    pickle.dump(word_count, f)

# 创建词云对象（设置中文字体）
wordcloud = WordCloud(width=800, height=400,
    font_path="C:\\Windows\\Fonts\\simhei.ttf",  # 需要设置中文字体路径
    background_color='white'
).generate_from_frequencies(word_count)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()