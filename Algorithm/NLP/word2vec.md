## gensim实现

[class gensim.models.word2vec.Word2Vec](https://radimrehurek.com/gensim/models/word2vec.html#gensim.models.word2vec.Word2Vec)

```python
# 提前下载语料库
import nltk
nltk.download('abc')
nltk.download('punkt')

import gensim
from nltk.corpus import abc	# 导入语料库abc

# sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]
sentences = abc.sents()
model = gensim.models.Word2Vec(sentences)
X = list(model.wv.vocab)	# 单词以变量的形式存储
data = model.most_similar('science')	# 查找与science相似的单词
embedding = model.wv['science']	# 输出science的embedding向量
```



## 参考

- [[NLP] 秒懂词向量Word2vec的本质 -- 总结](https://zhuanlan.zhihu.com/p/26306795)
- [word2vec Parameter Learning Explained, Xin Rong](https://arxiv.org/pdf/1411.2738.pdf)
- [翻译自Xin Rong的《word2vec Parameter Learning Explained》](https://zhuanlan.zhihu.com/p/53425736)
- [可视化工具](https://ronxin.github.io/wevi/)
- [Word2Vec详解-公式推导以及代码](https://blog.csdn.net/kejizuiqianfang/article/details/99838249)

  - [word2vec源码解析](https://github.com/Link-Li/Word2Vec_C)
- [《word2vec 中的数学原理详解》](https://blog.csdn.net/itplus/article/details/37969519)
- [word2vec原理(一) CBOW与Skip-Gram模型基础](https://www.cnblogs.com/pinard/p/7160330.html)
- [word2vec原理(二) 基于Hierarchical Softmax的模型](http://www.cnblogs.com/pinard/p/7243513.html)
- [word2vec原理(三) 基于Negative Sampling的模型](http://www.cnblogs.com/pinard/p/7249903.html)

