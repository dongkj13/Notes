Python的hashlib提供了常见的摘要算法，如SHA1，SHA224，SHA256，SHA384，SHA512，MD5算法等等。

什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

摘要算法就是通过摘要函数`f()`对任意长度的数据`data`计算出固定长度的摘要`digest`。摘要函数是一个单向函数，计算`f(data)`很容易，但通过`digest`反推`data`却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同，因此摘要算法能指出数据是否被篡改过。

```python
import hashlib

md5 = hashlib.md5()
# 方式1
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()
# 方式2
md5.update('how to use md5 in ')
md5.update('python hashlib?')
print md5.hexdigest()
# 方式3
print hashlib.md5('how to use md5 in python hashlib?').hexdigest()
```

每种摘要算法的位数（字节），位数越多，算法越安全，不过算法越慢。

```python
from hashlib import md5, sha1, sha224, sha256, sha384, sha512
print md5().digest_size     # 16
print sha1().digest_size    # 20
print sha224().digest_size  # 28
print sha256().digest_size  # 32
print sha384().digest_size  # 48
print sha512().digest_size  # 64
```

## 参考

- [hashlib-廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/897692888725344/923057313018752)

