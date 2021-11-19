在NLP任务中，神经网络模型的训练和预测都需要借助词表来对句子进行表示。传统构造词表的方法，是先对各个句子进行分词，然后再统计并选出频数最高的前N个词组成词表。通常训练集中包含了大量的词汇，以英语为例，总的单词数量在17万到100万左右。出于计算效率的考虑，通常N的选取无法包含训练集中的所有词。因而，这种方法构造的词表存在着如下的问题：

- 实际应用中，模型预测的词汇是开放的，对于未在词表中出现的词(Out Of Vocabulary, OOV)，模型将无法处理及生成；
- 词表中的低频词/稀疏词在模型训练过程中无法得到充分训练，进而模型不能充分理解这些词的语义；
- 一个单词因为不同的形态会产生不同的词，如由"look"衍生出的"looks", "looking", "looked"，显然这些词具有相近的意思，但是在词表中这些词会被当作不同的词处理，一方面增加了训练冗余，另一方面也造成了大词汇量问题。

一种解决思路是使用字符粒度来表示词表，虽然能够解决OOV问题，但单词被拆分成字符后，一方面丢失了词的语义信息，另一方面，模型输入会变得很长，这使得模型的训练更加复杂难以收敛。

针对上述问题，Subword(子词)模型方法横空出世。它的划分粒度介于词与字符之间，比如可以将”looking”划分为”look”和”ing”两个子词，而划分出来的"look"，”ing”又能够用来构造其它词，如"look"和"ed"子词可组成单词"looked"，因而Subword方法能够大大降低词典的大小，同时对相近词能更好地处理。

目前有三种主流的Subword算法，它们分别是：Byte Pair Encoding (BPE)，WordPiece和Unigram Language Model。

## Byte Pair Encoding (BPE)

[Neural machine translation of rare words with subword units](https://arxiv.org/pdf/1508.07909.pdf)

https://github.com/rsennrich/subword-nmt

## WordPiece



## Unigram Language Model (ULM)



## 参考

- [NLP三大Subword模型详解：BPE、WordPiece、ULM](https://zhuanlan.zhihu.com/p/198964217)
- [深入理解NLP Subword算法：BPE、WordPiece、ULM](https://zhuanlan.zhihu.com/p/86965595)

