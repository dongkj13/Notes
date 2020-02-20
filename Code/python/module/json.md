## json

### dumps

dumps只完成了序列化为str
```python
def dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kw):
    """Serialize ``obj`` to a JSON formatted ``str``.
    序列化 “obj” 数据类型 转换为 JSON格式的字符串"""

>>> import json
>>> json.dumps([])    # dumps可以格式化所有的基本数据类型为字符串
'[]'
>>> json.dumps(1)    # 数字
'1'
>>> json.dumps('1')   # 字符串
'"1"'
>>> dict = {"name":"Tom", "age":23}  
>>> json.dumps(dict)     # 字典
'{"name": "Tom", "age": 23}'
```

### dump
dump必须传文件描述符，将序列化的str保存到文件中
```python
def dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kw):
    """Serialize ``obj`` as a JSON formatted stream to ``fp`` (a
    ``.write()``-supporting file-like object).
     我理解为两个动作，一个动作是将”obj“转换为JSON格式的字符串，
     还有一个动作是将字符串写入到文件中，也就是说文件描述符fp是必须要的参数 
    """

a = {"name":"Tom", "age":23}
with open("test.json", "w", encoding='utf-8') as f:
    # indent 超级好用，格式化保存字典，默认为None，小于0为零个空格
    # f.write(json.dumps(a, indent=4))
    json.dump(a,f,indent=4)   # 和上面的效果一样
```

### loads
loads 只完成了反序列化
```python
def loads(s, encoding=None, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
    """将包含str类型的JSON文档反序列化为一个python对象"""
       
       
>>> json.loads('{"name":"Tom", "age":23}')
{'age': 23, 'name': 'Tom'}
```


### load
load 只接收文件描述符，完成了读取文件和反序列化
```python
def load(fp, cls=None, object_hook=None, parse_float=None, parse_int=None,
        parse_constant=None, object_pairs_hook=None, **kw):
    """将一个包含JSON格式数据的可读文件反序列化为一个python对象"""

import json
with open("test.json", "r", encoding='utf-8') as f:
    aa = json.loads(f.read())
    f.seek(0)
    bb = json.load(f)    # 与 json.loads(f.read())
print(aa)
print(bb)

# 输出：
{'name': 'Tom', 'age': 23}
{'name': 'Tom', 'age': 23}

```

## simplejson

在开源代码常看到如下代码：

```
try:
    import simplejson as json
except ImportError:
    import json
```

simplejson和json库的区别，除此之外两者用法基本一致：

1. json是python的标准库，是从python 2.6以后才引入
2. simplejson非python标准库，需要单独安装`pip install simplejson`
3. 一般来说simplejson的转存和载入性能比json高

## 参考

- [json官方文档](https://json.readthedocs.io/en/latest/)
- [simplejson官方文档](https://simplejson.readthedocs.io/en/latest/)

