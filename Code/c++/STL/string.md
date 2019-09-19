## 初始化
```c++
#include <string>
string s1;                  //初始化字符串，空字符串
string s2 = s1;             //拷贝初始化，深拷贝字符串
string s3 = "I am Yasuo";   //直接初始化，s3存了字符串
string s4(10, 'a');         //s4存的字符串是aaaaaaaaaa
string s5(s4);              //拷贝初始化，深拷贝字符串
string s6("I am Ali");      //直接初始化
string s7 = string(6, 'c'); //拷贝初始化，cccccc
```


## 常用函数
### [截取子串](http://www.cplusplus.com/reference/string/string/substr/)
```c++
s.substr(pos, n)    //截取s中从pos开始（包括0）的n个字符的子串，并返回
s.substr(pos)       //截取s中从从pos开始（包括0）到末尾的所有字符的子串，并返回
```

### 替换子串
```c++
s.replace(pos, n, s1)   //用s1替换s中从pos开始（包括0）的n个字符的子串
```

### 查找子串
```c++
s.find(s1)              //查找s中第一次出现s1的位置，并返回（包括0）
s.rfind(s1)             //查找s中最后次出现s1的位置，并返回（包括0）
s.find_first_of(s1)     //查找在s1中任意一个字符在s中第一次出现的位置，并返回（包括0）
s.find_last_of(s1)      //查找在s1中任意一个字符在s中最后一次出现的位置，并返回（包括0）
s.fin_first_not_of(s1)  //查找s中第一个不属于s1中的字符的位置，并返回（包括0）
s.fin_last_not_of(s1)   //查找s中最后一个不属于s1中的字符的位置，并返回（包括0）
```

### [删除函数](http://www.cplusplus.com/reference/string/string/erase/)
```c++
s.erase(pos, n);    //删除从pos开始的n个字符，比如erase(0,1)就是删除第一个字符
s.erase(position);  //删除position处的一个字符(position是个string类型的迭代器)，比如s.erase(s.begin())就是删除第一个字符
s.erase(first,last);//删除从first到last之间的字符（first和last都是迭代器），比如s.erase(s.end()-3, s.end())就是删除最后3个字符
```

### 扩展函数
```c++
string str;
string str2="Writing ";
string str3="print 10 and then 5 more";

str.append(str2);                       // "Writing "
str.append(str3,6,3);                   // "10 "
str.append("dots are cool",5);          // "dots "
str.append("here: ");                   // "here: "
str.append(10u,'.');                    // ".........."
str.append(str3.begin()+8,str3.end());  // " and then 5 more"
str.append<int>(5,0x2E);                // "....."

cout << str << '\n';               
//Writing 10 dots here: .......... and then 5 more.....
```


## 和int互相转换
```c++
int num = stoi(str);            //string转int
string str = to_string(num);    //int转string
```
[stoi](http://www.cplusplus.com/reference/string/stoi/): string to int

## ASCII码互换
```c++
string a = string(1, 0 + 'a');      //'a'
int i = a - 'a';                    //0
```

## split实现
```c++
// path = "/a/../../b/../c//.//";
for(int i = 0; i<path.length(); i++)
    path[i] = (path[i] == '/' ? ' ' : path[i]);
stringstream istr(path);
string str;
while (istr>>str)
    // do something with str
    cout<<str<<endl;
}
```