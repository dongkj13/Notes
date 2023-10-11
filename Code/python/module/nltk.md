[toc]

## 简介



## 提词干 Stemmers

在英语中，一个单词常常是另一个单词的“变种”，如：happy=>happiness，这里happy叫做happiness的词干（stem）。在信息检索系统中，我们常常做的一件事，就是在Term规范化过程中，提取词干（stemming），即除去英文单词分词变换形式的结尾。

### Porter Stemmer

应用最为广泛的、中等复杂程度的、基于后缀剥离的词干提取算法是波特词干算法，也叫波特词干器（Porter Stemmer）。

```python
from nltk.stem.porter import *
stemmer = PorterStemmer()
plurals = ['caresses', 'flies', 'dies', 'mules', 'denied','died', 'agreed', 'owned', 'humbled', 'sized','meeting', 'stating', 'siezing', 'itemization','sensational', 'traditional', 'reference', 'colonizer','plotted']
singles = [stemmer.stem(plural) for plural in plurals]
print(' '.join(singles))

'''
output: caress fli die mule deni die agre own humbl size meet
state siez item sensat tradit refer colon plot
'''
```

### Snowball Stemmer

雪球词干算法，支持多种语言

```python
>>> from nltk.stem.snowball import SnowballStemmer
>>> SnowballStemmer.languages
(u'arabic', u'danish', u'dutch', u'english', u'finnish', u'french', u'german', u'hungarian', u'italian', u'norwegian', u'porter', u'portuguese', u'romanian', u'russian', u'spanish', u'swedish')
```

以英语为例：

```python
>>> stemmer = SnowballStemmer("english")
>>> print(stemmer.stem("running"))
run
```

可以设置忽略停用词：

```python
>>> stemmer2 = SnowballStemmer("english", ignore_stopwords=True)
>>> print(stemmer.stem("having"))
have
>>> print(stemmer2.stem("having"))
having
```

一般来说，SnowballStemmer("english")要比PorterStemmer()更准确。

```python
>>> print(SnowballStemmer("english").stem("generously"))
generous
>>> print(SnowballStemmer("porter").stem("generously"))
gener
```

也可以通过以下方式直接使用英语提词干。

```python
>>> stemmer3 = nltk.stem.snowball.EnglishStemmer()
>>> print(stemmer3.stem("generously"))
```

### Lancaster Stemmer

也是一种词干提取器，直接看代码吧。

```python
>>> from nltk.stem.lancaster import LancasterStemmer
>>> lancaster_stemmer = LancasterStemmer()
>>> lancaster_stemmer.stem(‘maximum’)
'maxim'
>>> lancaster_stemmer.stem(‘presumably’)
'presum'
>>> lancaster_stemmer.stem(‘multiply’)
'multiply'
>>> lancaster_stemmer.stem(‘provision’)
u'provid'
>>> lancaster_stemmer.stem(‘owed’)
'ow'
```

### 对比

```python
words = ['table', 'probably', 'wolves', 'playing',
         'is', 'dog', 'the', 'beaches', 'grounded',
         'dreamt', 'envision']
# 在名词和动词中，除了与数和时态有关的成分以外的核心成分。
# 词干并不一定是合法的单词
pt_stemmer = nltk.stem.porter.PorterStemmer()  # 波特词干提取器
lc_stemmer = nltk.stem.lancaster.LancasterStemmer()   # 兰卡斯词干提取器
sb_stemmer = nltk.stem.snowball.SnowballStemmer("english")# 思诺博词干提取器
for word in words:
    pt_stem = pt_stemmer.stem(word)
    lc_stem = lc_stemmer.stem(word)
    sb_stem = sb_stemmer.stem(word)
    print("%8s %8s %8s %8s" % (word,pt_stem,lc_stem,sb_stem))
```

```
              pt       lc       sb
   table     tabl     tabl     tabl
probably  probabl     prob  probabl
  wolves     wolv     wolv     wolv
 playing     play     play     play
      is       is       is       is
     dog      dog      dog      dog
     the      the      the      the
 beaches    beach    beach    beach
grounded   ground   ground   ground
  dreamt   dreamt   dreamt   dreamt
envision    envis    envid    envis
```

### 词型还原器

```python
# 词型还原：复数名词->单数名词 ；分词->动词原型
# 单词原型一定是合法的单词
lemmatizer = nltk.stem.WordNetLemmatizer()
for word in words:
    # 将名词还原为单数形式
    n_lemma = lemmatizer.lemmatize(word, pos='n')
    # 将动词还原为原型形式
    v_lemma = lemmatizer.lemmatize(word, pos='v')
    print('%8s %8s %8s' % (word, n_lemma, v_lemma))
```

```
   table    table    table
probably probably probably
  wolves     wolf   wolves
 playing  playing     play
      is       is       be
     dog      dog      dog
     the      the      the
 beaches    beach    beach
grounded grounded   ground
  dreamt   dreamt    dream
envision envision envision
```

## 参考

- [NLTK中的Stemmers](https://www.cnblogs.com/Patrick-L/p/12251747.html)
- [02 NLTK 分句、分词、词干提取、词型还原](https://www.cnblogs.com/wodexk/p/10292947.html)

