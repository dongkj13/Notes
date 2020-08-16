## 示例

```python
import getopt
import sys

opts,args = getopt.getopt(sys.argv[1:],'-h-f:-v',['help','filename=','version'])

fiename = ""

for opt_name, opt_value in opts:
    if opt_name in ('-h','--help'):
        print("[*] Help info")
        exit()
    if opt_name in ('-v','--version'):
        print("[*] Version is 0.01 ")
        exit()
    if opt_name in ('-f','--filename'):
        fiename = opt_value
        print("[*] Filename is ",fileName)
        # do something
        exit()
```

## 参考


- [官网](https://docs.python.org/3.1/library/getopt.html)
- [Python命令行:getopt模块详解](https://www.jianshu.com/p/a877e5b46b2d)

