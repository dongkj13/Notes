## Wide&Deep

- [Wide&Deep Learning for Recommender Systems](https://arxiv.org/pdf/1606.07792.pdf)
- [翻译：Wide&Deep Learning for Recommender Systems](https://zhuanlan.zhihu.com/p/111243634)

![](https://tva1.sinaimg.cn/large/008i3skNly1gsd9qb1bazj311m09sdj4.jpg)

### The Wide Componet

Wide部分是一个广义的线性模型，如图1(左)所示。Wide部分的特征集合包括原始输入特征和变换特征。最重要的一种变换方式为叉乘变换（cross-product transformation），具体定义如下：
$$
\phi(x) = \prod^d_{i=1} x_i^{c_ki}  \quad  c_ki\in {0,1}
$$
简单理解cross-product就是在二值化特征的情况下对齐进行”与“操作，这种特征变换方式可以提升广义线性模型的非线性。

### The Deep Component

Deep部分是前向神经网络，如图1(右)所示。对于高维稀疏的类别特征，首先转换为一个低维稠密的实值向量，通常被称为嵌入向量。嵌入向量的维度通常在O(10)到O(100)之间。在模型训练阶段，嵌入向量被随机初始化，并在最小化损失函数时进行训练。这些低维稠密的向量随后在神经网络前馈通路中被输入到隐藏层中。特别地，每个隐藏层进行如下计算：
$$
a^{(l+1)} = f(W^{(l)} a^{(l)} + b^{(l)})
$$
其中，$$l$$是层的序号， $$f$$是激活函数，通常为ReLU。$$a^{(l)}, b^{(l)}, W^{(l)}$$ 分别是$$l$$层的激活、偏差和模型参数。

### Joint Training of Wide & Deep Model

wide部分和deep部分通过将它们的输出对数几率（log odds）加权求和作为预测进行组合，随后这一预测值被输入到log loss中进行联合训练。

需要注意的是，joint training和ensemble主要区别在于：

- 在ensemble中，模型之间是独立训练的，互相并不感知对方的存在，它们预测值在推理阶段结合在一起而不是在训练阶段；而jointly training是同时优化所有参数，在训练阶段就考虑了wide部分和deep部分以及它们之间的加权求和的权重参数。
- 模型的大小也是有区别的，对于ensemble，因为训练是互斥的，每个独立的模型为了达到有效的准确性通常导致模型很大（比如更多的特征和更多转换），这样ensemble才能有效。但是相反，对于jointly training，wide部分仅需要补充deep组件的弱点，通常是一小部分交叉特征的变换，而不是一个整个full-size的wide模型。

Wide&Deep模型的联合训练可利用mini-batch随机优化方法将输出梯度反向传播到wide部分和deep部分实现。在Google的实验中，对于wide部分是通过带L1正则项的ftrl优化，对于deep组件通过AdaGrad优化完成。

对于逻辑回归问题，Wide&Deep模型的预测如下：
$$
P(y=1 | x) = \sigma(W^T_{wide} [x, \phi(x)] + W^T_{deep} a^{(l_f)} + b)
$$

## 参考

- [tensorflow官方示例代码](https://github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/examples/learn/wide_n_deep_tutorial.py)

- [看Google如何实现Wide & Deep模型(1)](https://zhuanlan.zhihu.com/p/47293765)
- [看Google如何实现Wide & Deep模型(2.1)](https://zhuanlan.zhihu.com/p/47965313)
- [看Google如何实现Wide & Deep模型(2.2)](https://zhuanlan.zhihu.com/p/47970601)
- [看Google如何实现Wide & Deep模型(3)](https://zhuanlan.zhihu.com/p/48251812)

