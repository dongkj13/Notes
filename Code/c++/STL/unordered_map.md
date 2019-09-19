## 定义
```c++
#include <unordered_map>
unordered_map<int, int> map1;
unordered_map<string, int> map2;
unordered_map<int, unordered_map<int, int>> map3;   //相当于二维数组
```

## 成员函数
|    函数     |                   描述                   |
| :---------: | :--------------------------------------: |
| `umap[key]` |            访问key对应的元素             |
| `insert()`  |                 插入元素                 |
|  `erase()`  |                 删除元素                 |
|  `clear()`  |                 清空内容                 |
|  `find()`   | 查找元素，没找到：返回unordered_map::end |
|  `count()`  |  查找元素的个数，存在返回1，不存在返回0  |
|  `size()`   |             返回有效元素个数             |
|  `empty()`  |               判断是否为空               |


## 遍历map
```c++
for(unordered_map<int, int>::iterator it = m.begin(); it != m.end(); it++)
    cout<<it->first<<it->second<<endl;
```

## unordered_map和map

- `unordered_map`存储机制是哈希表，，即`unordered_map`内部元素是无序的。

- `map`是红黑树，`map`中的元素是按照二叉搜索树存储，进行中序遍历会得到有序遍历。
- 成员函数基本一致