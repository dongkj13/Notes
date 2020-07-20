## 简介

Levenshtein是一个快速计算字符间编辑距离和相似度的扩展包。

## 安装

```sh
pip install python-Levenshtein
```

## 用法

### 汉明距离

要求str1和str2必须长度一致。是描述两个等长字串之间**对应**位置上**不同**字符的个数。

```python
Levenshtein.hamming('abc', 'cba')		# 结果为2
Levenshtein.hamming('abc', 'cam')		# 结果为3
```

### 编辑距离

也称Levenshtein距离，是描述由一个字串转化成另一个字串最少的操作次数，在其中的操作包括插入、删除、替换。算法实现：动态规划，可参考[编辑距离算法实现](https://blog.csdn.net/asty9000/article/details/81384650)。

```python
Levenshtein.distance('abc', 'ac')		# 结果为1，插入一次
Levenshtein.distance('kitten', 'sitting')		# 结果为3，k替换成s，e替换成i，插入g
```

### 莱文斯坦比

计算公式  r = (sum - ldist) / sum, 其中sum是指str1 和 str2 字串的长度总和，ldist是**类编辑距离**。
**注意**：这里的类编辑距离不是2中所说的编辑距离，2中三种操作中每个操作+1，而在此处，删除、插入依然+1，但是替换+2。这样设计的目的：ratio('a', 'c')，sum=2，按2中计算为（2-1）/2 = 0.5，'a'，'c'没有重合，显然不合算，但是替换操作+2，就可以解决这个问题。

```python
Levenshtein.ratio(str1, str2)
```

### Jaro距离

```python
Levenshtein.jaro(s1, s2)
```

两个给定字符串S1和S2的Jaro Distance为：

![img](https://files.jb51.net/file_images/article/201611/20161128113042931.png?20161028113051)

其中的m为s1, s2匹配的字符数，t是换位的数目。

两个分别来自S1和S2的字符如果相距不超过

![img](https://files.jb51.net/file_images/article/201611/20161128113147012.png?20161028113154)

时，我们就认为这两个字符串是匹配的；而这些相互匹配的字符则决定了换位的数目t，简单来说就是不同顺序的匹配字符的数目的一半即为换位的数目t。举例来说，MARTHA与MARHTA的字符都是匹配的，但是这些匹配的字符中，T和H要换位才能把MARTHA变为MARHTA,那么T和H就是不同的顺序的匹配字符，`t=2/2=1`。

两个字符串的Jaro Distance即为：

![img](https://files.jb51.net/file_images/article/201611/20161128113221330.png?20161028113229)

### Jaro–Winkler距离

```python
Levenshtein.jaro_winkler(s1, s2)
```

计算Jaro–Winkler距离，而Jaro-Winkler则给予了起始部分就相同的字符串更高的分数，他定义了一个前缀p，给予两个字符串，如果前缀部分有长度为ι的部分相同，则Jaro-Winkler Distance为：

![img](https://files.jb51.net/file_images/article/201611/20161128113305143.png?20161028113312)

dj是两个字符串的Jaro Distance，l是前缀的相同的长度，但是规定最大为4，p则是调整分数的常数，规定不能超过25，不然可能出现dw大于1的情况，Winkler将这个常数定义为0.1。

## 参考

- [官网](https://pypi.org/project/python-Levenshtein/)
- [Python文本相似性计算之编辑距离详解](https://www.jb51.net/article/98449.htm)
- [Levenshtein全部函数](http://www.coli.uni-saarland.de/courses/LT1/2011/slides/Python-Levenshtein.html#Levenshtein-inverse)
- [Jaro–Winkler distance](http://en.wikipedia.org/wiki/Jaro–Winkler_distance)

