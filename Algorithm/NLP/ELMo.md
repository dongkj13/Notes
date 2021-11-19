## ELMo（Embeddings from Language Models）
[Deep contextualized word representations](https://arxiv.org/pdf/1802.05365.pdf)
[翻译：Deep contextualized word representations](https://www.jianshu.com/p/4a59135bf71d)

> ELMo是一个深度带上下文的词表征模型（deep contextualized word representation），能同时建模（1）单词使用的复杂特征（例如，语法和语义）；（2）这些特征在上下文中会有何变化（如歧义等）。这些词向量从深度双向语言模型（biLM）的隐层状态中衍生出来，biLM是在大规模的语料上面Pretrain的。它们可以灵活轻松地加入到现有的模型中，并且能在很多NLP任务中显著提升现有的表现，比如问答、文本蕴含和情感分析等。

![](https://i.stack.imgur.com/fpiNA.png)


## 参考

- [ELMo原理解析及简单上手使用](https://zhuanlan.zhihu.com/p/51679783)
- [[论文笔记]ELMo](https://zhuanlan.zhihu.com/p/37684922)
- [ELMo解读（论文 + PyTorch源码）](https://blog.csdn.net/Magical_Bubble/article/details/89160032)
- [文本分类实战（九）—— ELMO 预训练模型](https://www.cnblogs.com/jiangxinyang/p/10235054.html)

