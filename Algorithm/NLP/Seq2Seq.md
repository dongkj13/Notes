[Encoder-Decoder 和 Seq2Seq](https://easyai.tech/ai-definition/encoder-decoder-seq2seq/)
> **Encoder-Decoder** 模型主要是 NLP 领域里的概念。它并不特指某种具体的算法，而是一类算法的统称。Encoder-Decoder 算是一个通用的框架，在这个框架下可以使用不同的算法来解决不同的任务。
>
> 1. 不论输入和输出的长度是什么，中间的「向量 c」 长度都是固定的（当输入信息太长时，会丢失掉一些信息）
> 2. 根据不同的任务可以选择不同的编码器和解码器（可以是一个 RNN，但通常是其变种 LSTM 或者 GRU ）

> **Seq2Seq**（是 Sequence-to-sequence 的缩写），就如字面意思，输入一个序列，输出另一个序列。这种结构最重要的地方在于输入序列和输出序列的长度是可变的。

> **「Seq2Seq」和「Encoder-Decoder」的关系**
>
> Seq2Seq（强调目的）不特指具体方法，满足「输入序列、输出序列」的目的，都可以统称为 Seq2Seq 模型。
>
> 而 Seq2Seq 使用的具体方法基本都属于Encoder-Decoder 模型（强调方法）的范畴。
>
> 总结一下的话：
>
> - Seq2Seq 属于 Encoder-Decoder 的大范畴
> - Seq2Seq 更强调目的，Encoder-Decoder 更强调方法

1. [Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation](https://arxiv.org/pdf/1406.1078.pdf)
   [翻译：Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation](https://blog.csdn.net/u010555997/article/details/76474533)

> 较早提出Encoder-Decoder这种结构，由两个神经网络（RNN）组成。一个RNN将一个符号序列（sequence of symbols）编码成一个固定长度的向量表示，另一个则将这个表示解码成另一个符号序列。该模型的编码器和解码器被联合训练（jointly trained），以最大化给定源序列的目标序列的条件概率（conditional probability）。

2. [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/pdf/1409.3215.pdf)
   [翻译：Sequence to Sequence Learning with Neural Networks](https://www.yanxishe.com/blogDetail/11165)
> 使用4层LSTM网络将输入序列映射到一个固定维度的向量，然后使用另一个深层LSTM从向量中解码目标序列。同时将源句子顺序颠倒后再输入 Encoder 中，比如源句子为“A B C”，那么输入 Encoder 的顺序为 “C B A”，经过这样的处理后，取得了很大的提升，而且这样的处理使得模型能够很好地处理长句子。

![](https://tva1.sinaimg.cn/large/007S8ZIlly1gipbj7qd26j30ng07caaa.jpg)

3. [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/pdf/1409.0473.pdf)
   [翻译：Neural Machine Translation by Jointly Learning to Align and Translate](https://www.yiyibooks.cn/yiyibooks/Neural_Machine_Translation_by_Jointly_Learning_to_Align_and_Translate/index.html)
> 在Encoder-Decoder的基础上提出了注意力机制。新架构包括一个双向RNN作为编码器和一个在解码翻译期间模拟搜索源语句（编码器输出的加权和）的解码器。

![](https://tva1.sinaimg.cn/large/007S8ZIlly1gipbi6sqqnj30ro0de3z2.jpg)



## 其他参考

- [seq2seq学习笔记](https://blog.csdn.net/Jerr__y/article/details/53749693)
- [完全图解RNN、RNN变体、Seq2Seq、Attention机制](https://zhuanlan.zhihu.com/p/28054589)