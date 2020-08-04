## Input

```python
import pandas as pd
data = pd.read_csv("input.csv", sep=',', header='infer', names=names, index_col=0)
```

| 参数      | 说明                                                         |
| --------- | ------------------------------------------------------------ |
| sep       | 字符串，分割符，默认值为","                                  |
| header    | 数据开始前的列名所占用的行数，缺省值"infer"将第一行视作列名，如果names参数有值，且header=0将使用names参数作为列名。如果header=None，默认0-N为列名，所有数据为表格内容 |
| names     | 新的列名数组                                                 |
| index_col | 如果index=0，指定第0列为索引                                 |

## Output

```python
data.to_csv("output.csv", sep=',')
```

| 参数     | 说明                        |
| :------- | --------------------------- |
| sep      | 字符串，分割符，默认值为"," |
| columns  | list，需要输出的列名        |
| header   | 是否输出header，默认True    |
| index    | 是否输出index，默认True     |
| quoting  | 是否带""，默认False         |
| encoding | 编码格式，默认为utf-8       |


##  参考

- [pandas.read_csv学习笔记](https://blog.csdn.net/zjyklwg/article/details/79556545)
- [pandas input](https://pandas.pydata.org/pandas-docs/stable/reference/io.html)
- [pandas output](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#serialization-io-conversion)

