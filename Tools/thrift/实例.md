### 定义thirft文件

```thrift
namespace py HelloWorld

struct Student {
    1: string name;
    2: i32 age;
}

service HelloWorld {
    i32 birth_year(1:Student stu),
    string say(1:string msg)
}

```

### 自动生成代码

用定义好的thrift文件生成我们需要的目标语言的源码，会在./gen-py/HelloWorld/下生成5个文件。

```sh
thrift --gen py HelloWord.thrift
```

<p align="center">
  <img src=".\..\..\Image\thrift\thrift_demo_file.png">
</p>
定义的结构体、枚举类型、异常类型等数据类型会在ttypes.py中实现，

```python
class Student:
  """
  Attributes:
   - name
   - age
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.I32, 'age', None, None, ), # 2
  )

  def __init__(self, name=None, age=None,):
    self.name = name
    self.age = age
```

定义的服务类型会在HelloWorld.py中实现

```python
class Iface:
  def birth_year(self, stu):
    """
    Parameters:
     - stu
    """
    pass

  def say(self, msg):
    """
    Parameters:
     - msg
    """
    pass
```

### 生成server端代码

```python
#!/usr/bin/env python

import socket
import sys
sys.path.append('./gen-py')

from HelloWorld import HelloWorld
from HelloWorld.ttypes import *		# 引入HelloWorld.thrift中定义的结构体等数据类型

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class HelloWorldHandler:
    def birth_year(self, stu):
        print "name: ", stu.name
        print "age: ", stu.age
        print "birth_year: ", 2020 - stu.age
        return 2020 - stu.age

    def say(self, msg):
        ret = "Received: " + msg
        print ret
        return ret
```

### 启动服务

```python
handler = HelloWorldHandler()

processor = HelloWorld.Processor(handler)

transport = TSocket.TServerSocket("localhost", 9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print "Starting thrift server in python..."
server.serve()
print "done!"
```

### 客户端发送请求

```python
#!/usr/bin/env python

import sys
sys.path.append('./gen-py')

from HelloWorld import HelloWorld
from HelloWorld.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = HelloWorld.Client(protocol)
    transport.open()

    stu = Student('Jim', 20)

    print "client - birth_year"
    print "server - ", client.birth_year(stu)

    print "client - say"
    msg = client.say("Hello!")
    print "server - " + msg

    transport.close()
except Thrift.TException, ex:
    print "%s" % (ex.message)
```

## 参考

- [Thrift_demo](https://github.com/dongkj13/Thrift_demo)

