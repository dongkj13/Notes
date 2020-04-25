## Bisect - 数组二分查找算法

这个模块对有序列表提供了支持，使得他们可以在插入新数据仍然保持有序。对于长列表，如果其包含元素的比较操作十分昂贵的话，这可以是对更常见方法的改进。这个模块叫做 bisect因为其使用了基本的二分（bisection）算法。

## 函数

### bisect.bisect_left(a, x, lo=0, hi=len(a))

在 a 中找到 x 合适的插入点以维持有序。参数 lo 和 hi 可以被用于确定需要考虑的子集；默认情况下整个列表都会被使用。如果 x 已经在 a 里存在，那么插入点会在已存在元素之前（也就是左边）。

### bisect.bisect_right(a, x, lo=0, hi=len(a))

别名 `bisect.bisect()`

类似于 `bisect_left()`，但是返回的插入点是 a 中已存在元素 x 的右侧。

### bisect.insort_left(a, x, lo=0, hi=len(a))

将 x 插入到一个有序序列 a 里，并维持其有序。如果 a 有序的话，这相当于 `a.insert(bisect.bisect_left(a, x, lo, hi), x)`。要注意搜索是 O(log n) 的，插入却是 O(n) 的。

### bisect.insort_right(a, x, lo=0, hi=len(a))

别名`bisect.insort()`

类似于 `insort_left()`，但是把 x 插入到 a 中已存在元素 x 的右侧。

## 示例

```python
import bisect

values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('New  Pos  Contents')
print('---  ---  --------')

l = []
for i in values:
    position = bisect.bisect(l, i)    # 显示将会插入的位置, 并未实际插入
    bisect.insort(l, i)   # 实际插入并维护一个有序数组
    print('{:3}  {:3}'.format(i, position), l)
    
# output
# New  Pos  Contents
# ---  ---  --------
#  14    0 [14]
#  85    1 [14, 85]
#  77    1 [14, 77, 85]
#  26    1 [14, 26, 77, 85]
#  50    2 [14, 26, 50, 77, 85]
#  45    2 [14, 26, 45, 50, 77, 85]
#  66    4 [14, 26, 45, 50, 66, 77, 85]
#  79    6 [14, 26, 45, 50, 66, 77, 79, 85]
#  10    0 [10, 14, 26, 45, 50, 66, 77, 79, 85]
#   3    0 [3, 10, 14, 26, 45, 50, 66, 77, 79, 85]
#  84    9 [3, 10, 14, 26, 45, 50, 66, 77, 79, 84, 85]
#  77    8 [3, 10, 14, 26, 45, 50, 66, 77, 77, 79, 84, 85]
#   1    0 [1, 3, 10, 14, 26, 45, 50, 66, 77, 77, 79, 84, 85]

```

## 参考

- [维护有序数组的模块bisect]([https://ofooo.github.io/wiki/python/%E5%BA%93/%E7%BB%B4%E6%8A%A4%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E7%9A%84%E6%A8%A1%E5%9D%97bisect/](https://ofooo.github.io/wiki/python/库/维护有序数组的模块bisect/))
- [bisect官网](https://docs.python.org/zh-cn/3/library/bisect.html#module-bisect)
- [bisect源码](https://github.com/python/cpython/blob/3.8/Lib/bisect.py)

