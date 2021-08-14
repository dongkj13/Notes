[`glob`](https://docs.python.org/zh-cn/3/library/glob.html#module-glob) 模块可根据 Unix 终端所用规则找出所有匹配特定模式的路径名，**但会按不确定的顺序返回结果**。 

## 基本用法：

### `glob.glob(pathname)`

返回所有匹配的文件路径列表。它只有一个参数`pathname`，定义了文件路径匹配规则，这里可以是绝对路径，也可以是相对路径。

```python
import glob

file_names = glob.glob('~/workspace/*.txt')
file_names = sorted(file_names)
```

### `glob.iglob(pathname)`

获取一个可编历对象，使用它可以逐个获取匹配的文件路径名。与`glob.glob()`的区别是：`glob.glob`同时获取所有的匹配路径，而`glob.iglob`一次只获取一个匹配路径。

```python
import glob

file_names = glob.iglob('~/workspace/*.txt')
for fn in file_names:
    print(fn)
```

### 通配符：

- 通配符-星号`*`：星号`*`匹配一个文件名段中的0个或多个字符
- 单配符-问号`?`：问号`?`会匹配文件名中该位置的单个字符。
- 字符区间-`[a-z]`：使用字符区间`[a-z]`，可以匹配多个字符中的一个字符。

## 参考

- [官网](https://docs.python.org/zh-cn/3/library/glob.html#module-glob)
- [[Python] glob 模块（查找文件路径）](https://www.jianshu.com/p/542e55b29324)

