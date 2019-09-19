> 所谓的deque是”double ended queue”的缩写，双端队列不论在尾部或头部插入元素，都十分迅速。而在中间插入元素则会比较费时，因为必须移动中间其他的元素。双端队列是一种随机访问的数据类型，提供了在序列两端快速插入和删除操作的功能，它可以在需要的时候改变自身大小，完成了标准的C++数据结构中队列的所有功能。 

## 定义deque
```c++
#include <deque>
deque<type> deq;                // 声明一个元素类型为type的双端队列que
deque<type> deq(size);          // 声明一个类型为type、含有size个默认值初始化元素的的双端队列que
deque<type> deq(size, value);   // 声明一个元素类型为type、含有size个value元素的双端队列que
deque<type> deq(mydeque);       // deq是mydeque的一个副本
deque<type> deq(first, last);   // 使用迭代器first、last范围内的元素初始化deq
```
## 基本函数
| 函数           | 描述                           |
| -------------- | ------------------------------ |
| `deq[]`        | 用来访问双向队列中单个的元素。 |
| `push_front()` | 在队首添加一个元素             |
| `push_back()`  | 在队尾添加一个元素             |
| `pop_front()`  | 删除队首元素                   |
| `pop_back()`   | 删除队尾元素                   |
| `front()`      | 返回队首元素                   |
| `back()`       | 返回队尾元素                   |
| `empty()`      | 判断队列是否为空               |
| `size()`       | 返回队列中元素的个数           |

