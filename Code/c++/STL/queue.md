> c++队列模板类的定义在<queue>头文件中,queue 模板类需要两个模板参数，一个是元素类型，一个容器类型，元素类型是必要的，容器类型是可选的，默认为deque类型。

## 定义queue
```c++
#include <queue>
queue<int> q1;
queue<double> q2;
```
## 基本函数
|   函数    |         描述         |
| :-------: | :------------------: |
| `push()`  |  在队尾添加一个元素  |
|  `pop()`  |     删除队首元素     |
| `front()` |  返回队首元素的引用  |
| `back()`  |  返回队尾元素的引用  |
| `size()`  | 返回队列中元素的个数 |
| `empty()` |   判断队列是否为空   |

## 示例代码
```c++
#include <iostream>
#include <queue>
using namespace std;
int main()
{
    int e, n, m;
    queue<int> q1;
    for (int i=0; i<10; i++)
       q1.push(i);          // 在队尾添加一个元素
    if (!q1.empty())        // 判断队列是否为空
        cout<<"队列不空";
    n = q1.size();          // 返回队列中元素个数
    cout<<n<<endl;
    m = q1.back();          // 返回队尾元素
    cout<<m<<endl;
    for(int j = 0; j<n; j++){
       e = q1.front();      // 返回队首元素
       cout<<e<<" ";
       q1.pop();            // 弹出队首元素
    }
    cout<<endl;
    if (q1.empty())
        cout<<"队列不空";
}
```