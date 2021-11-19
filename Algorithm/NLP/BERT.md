[toc]

# BERT（Bidirectional Encoder Representations from Transformers）

## 特殊NLP任务

1. 短文本相似 
2. 文本分类
3. QA机器人
4. 语义标注

![image-20210321164419416](https://tva1.sinaimg.cn/large/008eGmZEly1gormcwrab8j30lu0l778r.jpg)


## 代码

Google-Bert源码：https://github.com/google-research/bert/

[Bert模型tensorflow源码解析（详解transformer encoder数据运算）](https://www.jianshu.com/p/2a3872148766)

[BERT解读（论文 + TensorFlow源码）](https://blog.csdn.net/Magical_Bubble/article/details/89514057)


## 参考
- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/pdf/1810.04805.pdf)
- [翻译：BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://www.cnblogs.com/guoyaohua/p/bert.html)
- [jalammar.github.io/illustrated-bert/](https://blog.csdn.net/qq_41664845/article/details/84787969)

# ALBERT（A Lite BERT）

## 模型改进

### Factorized Embedding Parameterization

在BERT、XLNet中，词表的embedding size(E)和transformer层的hidden size(H)是等同的，所以E=H。但实际上词库的大小一般都很大，这就导致模型参数个数就会变得很大。因此先把one-hot映射到低维空间之后，再映射到hidden layer。这其实类似于做了矩阵的分解。

### Cross-layer parameter sharing

Zhenzhong博士提出每一层的layer可以共享参数，这样一来参数的个数不会以层数的增加而增加。所以最后得出来的模型相比BERT-large小18倍以上。


### Inter-sentence coherence loss

在BERT的训练中提出了next sentence prediction loss, 也就是给定两个sentence segments, 然后让BERT去预测它俩之间的先后顺序，但在ALBERT文章里提出这种是有问题的，其实也说明这种训练方式用处不是很大。 所以他们做出了改进，他们使用的是sentence-order prediction loss (SOP)，其实是基于主题的关联去预测是否两个句子调换了顺序。

## 参考

- [ALBERT: A Lite BERT for Self-supervised Learning of Language Representations](https://arxiv.org/abs/1909.11942)

- [BERT的youxiu变体：ALBERT论文图解介绍](https://zhuanlan.zhihu.com/p/142416395)
- [从BERT, XLNet, RoBERTa到ALBERT](https://zhuanlan.zhihu.com/p/84559048)

