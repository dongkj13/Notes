|    func     |                             desc                             |
| :---------: | :----------------------------------------------------------: |
| namedtuple  | factory function for creating tuple subclasses with named fields |
|    deque    | list-like container with fast appends and pops on either end |
|  ChainMap   | dict-like class for creating a single view of multiple mappings |
|   Counter   |         dict subclass for counting hashable objects          |
| OrderedDict |  dict subclass that remembers the order entries were added   |
| defaultdict | dict subclass that calls a factory function to supply missing values |
|  UserDict   | wrapper around dictionary objects for easier dict subclassing |
|  UserList   |   wrapper around list objects for easier list subclassing    |
| UserString  | wrapper around string objects for easier string subclassing  |

## namedtuple
使用 **`namedtuple(typename, field_names)`** 命名tuple中的元素来使程序更具可读性，即以类的方式访问元素变量。

实际上就是创建一个名为typename的类（继承tuple），具有field_names等属性变量，同时简化类里的相关变量和函数，节省空间。
```python
>>> from collections import namedtuple
>>> City = namedtuple('City', ['name', 'country', 'population', 'coordinates'])
>>> tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
>>> tokyo
City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
>>> tokyo.population
36.933
>>> tokyo.coordinates
(35.689722, 139.691667)
>>> tokyo[1]
'JP'
>>> tokyo_info_dict = tokyo._asdict()   # 转换成字典
>>> tokyo_info_dict
dict(name:'Tokyo', country:'JP', population:36.933, coordinates:(35.689722, 139.691667))
```

## defaultdict
defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值

```python
dict1 = defaultdict(int)            # 默认值为0
dict2 = defaultdict(set)            # 默认值为set()
dict3 = defaultdict(str)            # 默认值为空字符串
dict4 = defaultdict(list)           # 默认值为[]
dict5 = defaultdict(dict)           # 默认值为{}
def gen_default():
    return {
        "name":"",
        "nums":0
    }
dict6 = defaultdict(gen_default)    ## 默认值为自定义dict
```

## deque
双端队列，相比list多了appendleft, extendleft, popleft操作，即从队列左端进行操作

## Counter
Counter用来统计相关元素的出现次数，**利用堆的方式解决top k问题**
```python
>>> from collections import Counter
>>> ct = Counter('abracadabra')
>>> ct
Counter({'a': 5, 'r': 2, 'b': 2, 'd': 1, 'c': 1})
>>> ct.update('aaaaazzz')
>>> ct
Counter({'a': 10, 'z': 3, 'r': 2, 'b': 2, 'd': 1, 'c': 1})
>>> ct.most_common(2)
[('a', 10), ('z', 3)]
>>> ct.elements()
<itertools.chain object at 0x7fbaad4b44e0>
```

## OrderedDict
继承自dict，维护加入dict时的顺序，相比dict多了popitem, move_to_end操作
```python
from collections import OrderedDict

user_dict = OrderedDict()
user_dict["b"] = "bobby1"
user_dict["a"] = "bobby2"
user_dict["c"] = "bobby3"
print(user_dict)
# OrderedDict([("b", "bobby1"), ("a", "bobby2"), ("c", "bobby3")])
print(user_dict.popitem())      # 移除最后一个元素
# ("c", "bobby3")
user_dict.move_to_end("b")      # 将key移到最后
print(user_dict)
# OrderedDict([("a", "bobby2"), ("c", "bobby3"), ("b", "bobby1")])
```

## ChainMap

##### 使用ChainMap可以将多个字典串联起来，当做一个字典来处理

```python
user_dict1 = {"a": "xiaohong", "b": "xiaohua"}
user_dict2 = {"c": "xiaopang", "d": "xiaoming"}
new_dict = ChainMap(user_dict1, user_dict2)
print(new_dict)
# ChainMap({'a': 'xiaohong', 'b': 'xiaohua'}, {'c': 'xiaopang', 'd': 'xiaoming'})
```

##### 可以直接访问串联起来的数据

```python
print(new_dict["c"])
# xiaopang
```

##### 当不同的字典具有相同的主键的时候，在遍历串联之后的数据时，会只能遍历到之前的

```python
user_dict1 = {"a": "xiaohong", "b": "xiaohua"}
user_dict2 = {"b": "xiaopang", "d": "xiaoming"}
new_dict = ChainMap(user_dict1, user_dict2)
for key, value in new_dict.items():
    print(key, value)
# d xiaoming
# b xiaohua
# a xiaohong
```

##### 可以动态添加新的dict
```python
new_dict.new_child(new_dict)
```

##### maps 方法会将串联起来的字典以列表的形式展示

```python
print(new_dict.maps)
# [{'a': 'xiaohong', 'b': 'xiaohua'}, {'c': 'xiaopang', 'd': 'xiaoming'}]
```

##### ChainMap 并不是对源数据的拷贝，而是 指向源数据
```python
new_dict.maps[0]["a"] = "pangzi"
print(new_dict)
# ChainMap({'a': 'pangzi', 'b': 'xiaohua'}, {'c': 'xiaopang', 'd': 'xiaoming'})
```

## Iterator 迭代器对象
```python
class myIterator(Iterator):
    def __init__(self, **args):
    
    def next(self):
        if self.index == len(self.xx):
            raise StopIteration
        ## do you things
        self.index += 1
        return xxx
```

## Iterable 可迭代对象
```python
class myIterable(Iterable):
    def __init__(self, **args):
    
    def __iter__(self):
        return myIterator()
```


## 参考

- [collections官网](https://docs.python.org/3.7/library/collections.html)