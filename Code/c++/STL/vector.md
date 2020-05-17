> 向量（Vector）是一个封装了动态大小数组的顺序容器（Sequence Container）。跟任意其它类型容器一样，它能够存放各种类型的对象。可以简单的认为，向量是一个能够存放任意类型的动态数组。

## 基本函数实现
### 构造函数
```c++
#include <vector>
vector<int> a;                      //创建一个空vector
vector<int> a(10);                  //定义了10个整型元素的向量（尖括号中为元素类型名，它可以是任何合法的数据类型），但没有给出初值，其值是不确定的。
vector<int> a(10,1);                //定义了10个整型元素的向量,且给出每个元素的初值为1
vector<int> a(b);                   //用b向量来创建a向量，整体复制性赋值
vector<int> a(b.begin(),b.begin+3); //定义了a值为b中第0个到第2个（共3个）元素
int b[7]={1,2,3,4,5,9,8};
vector<int> a(b,b+7);               //从数组中获得初值
a = vector<int>(10);
```

### 增加函数
```c++
a.push_back(5);                 //在a的最后一个向量后插入一个元素，其值为5
a.insert(a.begin()+1,5);        //在a的第1个元素（从第0个算起）的位置插入数值5，如a为1,2,3,4，插入元素后为1,5,2,3,4
a.insert(a.begin()+1,3,5);      //在a的第1个元素（从第0个算起）的位置插入3个数，其值都为5
a.insert(a.begin()+1,b+3,b+6);  //b为数组，在a的第1个元素（从第0个算起）的位置插入b的第3个元素到第5个元素（不包括b+6），如b为1,2,3,4,5,9,8，插入元素后为1,4,5,9,2,3,4,5,9,8

//C++11引入的新成员，一般用于直接插入结构体的元素
a.emplace_back(arg1, arg2, ...);//在a的最后后插入一个元素（一般结构体），直接将参数转发到构造函数
a.emplace(a.begin()+1, arg1, arg2, ...);//在a的第一个元素后插入结构体
```

[c++11 emplace_back特性](https://zh.cppreference.com/w/cpp/container/vector/emplace_back)

### 删除函数

```c++
a.clear();                          //清空a中的元素
a.pop_back();                       //删除a向量的最后一个元素
a.erase(a.begin()+1,a.begin()+3);   //删除a中第1个（从第0个算起）到第2个元素，
```

### 遍历函数
```c++
a.front();  //返回a的第一个元素
a.back();   //返回a的最后一个元素
a.begin();  //返回向量头指针，指向第一个元素
a.end();    //返回向量尾指针，指向向量最后一个元素的下一个位置
```

### 判断函数
```c++
a.empty();  //判断a是否为空，空则返回ture,不空则返回false
```

### 大小函数
```c++
a.size();       //返回a中元素的个数；
a.capacity();   //返回a在内存中总共可以容纳的元素个数
a.max_size();   //返回a最大可允许的元素数量值
```
### 其他函数
```c++
a.swap(b);                          //b为向量，将a中的元素和b中的元素进行整体性交换
a.assign(b.begin(), b.begin()+3);   //b为向量，将b的0~2个元素构成的向量赋给a
a.assign(4,2);                      //是a只含4个元素，且每个元素为2
```
## 求最大值、最小值、及索引
```c++
#include<algorithm>
int maxValue = *max_element(v.begin(),v.end()); 
int minValue = *min_element(v.begin(),v.end());
int maxPosition = max_element(v.begin(),v.end()) - v.begin(); 
int minPosition = min_element(v.begin(),v.end()) - v.begin();
```

## 数组反序
```c++
#include<algorithm>
vector<int> v={1,2,3,4,5};
reverse(v.begin(), v.end());    //v的值为5，4，3，2，1
```

