## pair

`std::pair` 是一个结构体模板，其可于一个单元存储两个相异对象。pair 是 `std::tuple` 的拥有两个元素的特殊情况。

```c++
#include <iostream>
#include <utility>
#include <string>
using namespace std;

int main()
{
  pair<string, int> a = make_pair("jerry", 25);
  pair<string, int> b("tom", 24);

  cout << a.first << " " << a.second << endl;
  cout << b.first << " " << b.second << endl;
}
```

## tuple

类模板 `std::tuple` 是固定大小的异类值汇集。它是 `std::pair` 的推广。

```c++
#include <iostream>
#include <utility>
#include <string>
using namespace std;

int main()
{
  tuple<string, int, int> a = make_tuple("jerry", 25, 176);
  cout << std::get<0>(a) << ' ' << std::get<1>(a) << ' ' << std::get<2>(a) << endl;
 	
  tuple<string, int, int> b{"tom", 24, 180};
  string name; int age; int height;
  std::tie(name, age, height) = b;
  cout << name << ' ' << age << ' ' << height <<endl;
}
```

## 参考

- [pair](https://zh.cppreference.com/w/cpp/utility/pair)

- [tuple](https://zh.cppreference.com/w/cpp/utility/tuple)

