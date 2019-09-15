|       方法       |                    说明                     |
| :--------------: | :-----------------------------------------: |
|     os.mkdir     |                  创建目录                   |
|   os.makedirs    |                递归创建目录                 |
|     os.rmdir     | 删除空目录，删除有内容的目录见shutil.rmtree |
|     os.chdir     |              改变当前工作目录               |
|    os.rename     |                   重命名                    |
|    os.remove     |                  删除文件                   |
|    os.getcwd     |              获取当前工作路径               |
|    os.listdir    |             列出指定目录的文件              |
|     os.walk      |                  遍历目录                   |
|   os.path.join   |              连接目录与文件名               |
|  os.path.split   |              分割文件名与目录               |
| os.path.abspath  |                获取绝对路径                 |
| os.path.dirname  |                  获取路径                   |
| os.path.basename |            获取文件名或文件夹名             |
| os.path.splitext |             分离文件名与扩展名              |
|  os.path.isfile  |        判断给出的路径是否是一个文件         |
|  os.path.isdir   |        判断给出的路径是否是一个目录         |
|  os.path.exists  |                  是否存在                   |


后文的例子以下面的目录结构为参考，工作目录为 /Users/ethan/coding/python。

Users/ethan\
└── coding\
&emsp;&emsp;  └── python\
&emsp;&emsp;&emsp;&emsp;&ensp;├── hello.py    - 文件\
&emsp;&emsp;&emsp;&emsp;&ensp;└── web         - 目录

## os.path.abspath：获取文件或目录的绝对路径
```cmd
$ pwd
/Users/ethan/coding/python
$ python
>>> import os                          # 记得导入 os 模块
>>> os.path.abspath('hello.py')
'/Users/ethan/coding/python/hello.py'
>>> os.path.abspath('web')
'/Users/ethan/coding/python/web'
>>> os.path.abspath('.')                # 当前目录的绝对路径
'/Users/ethan/coding/python'
```

## os.path.dirname：获取文件或文件夹的路径
```cmd
>>> os.path.dirname('/Users/ethan/coding/python/hello.py')
'/Users/ethan/coding/python'
>>> os.path.dirname('/Users/ethan/coding/python/')
'/Users/ethan/coding/python'
>>> os.path.dirname('/Users/ethan/coding/python')
'/Users/ethan/coding'
```


## os.path.basename：获取文件名或文件夹名
```cmd
>>> os.path.basename('/Users/ethan/coding/python/hello.py')
'hello.py'
>>> os.path.basename('/Users/ethan/coding/python/')
''
>>> os.path.basename('/Users/ethan/coding/python')
'python'
```


## os.path.splitext：分离文件名与扩展名
```cmd
>>> os.path.splitext('/Users/ethan/coding/python/hello.py')
('/Users/ethan/coding/python/hello', '.py')
>>> os.path.splitext('/Users/ethan/coding/python')
('/Users/ethan/coding/python', '')
>>> os.path.splitext('/Users/ethan/coding/python/')
('/Users/ethan/coding/python/', '')
```


## os.path.split：分离目录与文件名
```cmd
>>> os.path.split('/Users/ethan/coding/python/hello.py')
('/Users/ethan/coding/python', 'hello.py')
>>> os.path.split('/Users/ethan/coding/python/')
('/Users/ethan/coding/python', '')
>>> os.path.split('/Users/ethan/coding/python')
('/Users/ethan/coding', 'python')
```

## os.path.isfile/os.path.isdir
```cmd
>>> os.path.isfile('/Users/ethan/coding/python/hello.py')
True
>>> os.path.isdir('/Users/ethan/coding/python/')
True
>>> os.path.isdir('/Users/ethan/coding/python')
True
>>> os.path.isdir('/Users/ethan/coding/python/hello.py')
False
```

## os.walk
os.walk 是遍历目录常用的模块，它返回一个包含 3 个元素的元祖：(dirpath, dirnames, filenames)。dirpath 是以 string 字符串形式返回该目录下所有的绝对路径；dirnames 是以列表 list 形式返回每一个绝对路径下的文件夹名字；filesnames 是以列表 list 形式返回该路径下所有文件名字。
```cmd
>>> for root, dirs, files in os.walk('/Users/ethan/coding'):
...     print root
...     print dirs
...     print files
...
/Users/ethan/coding
['python']
[]
/Users/ethan/coding/python
['web2']
['hello.py']
/Users/ethan/coding/python/web2
[]
[]
```

## 参考

- [os官方文档](https://docs.python.org/3/library/os.html)
- [os.path官方文档](https://docs.python.org/3/library/os.path.html)
- [os 模块](http://funhacks.net/explore-python/File-Directory/os.html)
- [Python OS 文件/目录方法](http://www.runoob.com/python/os-file-methods.html)