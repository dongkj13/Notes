# ESIM

[Enhanced LSTM for Natural Language Inference](https://arxiv.org/abs/1609.06038)

主要改进：

1. 精细的设计序列式的推断结构。
2. 考虑局部推断和全局推断。

作者主要是用句子间的注意力机制，来实现局部的推断，进一步实现全局的推断。

ESIM一共包含四部分，Input Encoding、Local Inference Modeling、 Inference Composition、Prediction。

![img](https://raw.githubusercontent.com/terrifyzhao/terrifyzhao.github.io/master/assets/img/2019-05-20-%E6%96%87%E6%9C%AC%E5%8C%B9%E9%85%8D%E6%A8%A1%E5%9E%8B%E4%B9%8BESIM/pic1.jpg)

## 参考

[文本匹配模型之ESIM](https://terrifyzhao.github.io/2019/05/20/%E6%96%87%E6%9C%AC%E5%8C%B9%E9%85%8D%E6%A8%A1%E5%9E%8B%E4%B9%8BESIM.html)

[ESIM笔记](https://tianhongzxy.github.io/2020/05/04/ESIM%E7%AC%94%E8%AE%B0/)

[短文本匹配的利器-ESIM（含代码详解）](https://zhuanlan.zhihu.com/p/47580077) 

https://github.com/pengshuang/Text-Similarity/blob/master/models/ESIM.py