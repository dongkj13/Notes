[toc]
# random

## 整数

### random.randint(a,b)

随机生成[a,b]范围内一个整数。

### random.randrange(a,b,step)

不指定step，随机生成[a,b)范围内一个整数。
指定step，step作为步长会进一步限制[a,b)的范围，比如randrange(0,11,2)意即生成[0,11)范围内的随机偶数。
不指定a，则默认从0开始。

## 分布

### random.random()

随机生成一个[0,1)之间的浮点数。

### random.uniform(a,b)

随机生成一个[a,b]范围内的浮点数。

## 序列

### random.choice(seq)

从非空序列中随机选取一个数据并带回，该序列可以是list、tuple、str、set。
如果序列为空，则弹出**IndexError**错误。

### random.choices(population,weights=None,*,cum_weights=None,k=1)
Python3.6版本新增。

- population：集群。
- weights：相对权重。
- cum_weights：累加权重。
- k：选取次数。

作用：从集群中随机选取k次数据，返回一个列表，可以设置权重。
注意每次选取都不会影响原序列，每一次选取都是基于原序列。（重复抽样）

### random.sample(population,k)

从集群population中选取k个元素，返回一个列表，集群可以是list、tuple、str、set。

与random.choices()的区别：choices是有放回抽样，sample是不放回抽样。故random.sample()的k值不能超出集群的元素个数。

### random.shuffle(lst)

随机打乱序列lst的顺序并**重新排序**，注意它**无返回值**，另外lst只能是一个可变序列，且只支持有下标的序列，因此它也不适用于set。