## sys.argv
**获取命令行参数，返回值是List，第一个元素是程序本身**

```python
## test.py
import sys
print(sys.argv)
```

在命令行中测试`test.py`

```cmd
>>> python test.py
['test.py']
>>> python test.py name age weight 19 20
['test.py', 'name', 'age', 'weight', '19', '20']
```

## sys.path
**返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值**

比如就是我们在python源文件中import引入模块的时候就会在sys.path的目录中查找相应的模块，如果在这里面的目录中没有找到你要倒入的模块则会报错。

返回值是一个list则我们如果想倒入一个自定义模块下面的的包或者是模块则可以使用list的append方法在PYTHONPATH环境变量中增加相应的路径。

## sys.stdout, sys.stdin, sys.stderror

`sys.stdout.write`和`print`都是输出相关的函数，**`print`内部也是调用的`sys.stdout`**，`sys.stdout`默认输出是屏幕。

`print`什么类型都可以输出，但是`sys.stdout.write`只可以输出字符串类型,否则报错。`print`默认是最后换行，但是`sys.stdout.write`默认不换行。

```python
# 通过重定向标准输出到文件，直接用print写入文件
import sys
file = sys.stdout                   # 存储原始的输出对象
sys.stdout = open('1.txt', 'w')     # 重定向所有的写入内容到 1.txt 文件,
print('Citizen_Wang')               # 写入到1.txt文件中，在上一行语句中改变了输出流到文件中
print('Hello World')                # 继续写入到文件中
sys.stdout.close()                  # 其实就是 open 文件之后的关闭
sys.stdout = file                   # 将 print 命令的结果返回给控制台
print('输出信息返回在控制台')       # 该信息会在控制台也显示
```


## 参考
- [sys官方文档翻译](https://blog.csdn.net/qq_38526635/article/details/81739321)
- [python3 sys模块](https://www.jianshu.com/p/985980202ea7)