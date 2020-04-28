## 简介

Google 的 gflags 是一套命令行参数处理的开源库。比 getopt 更方便，更功能强大，从 C++的库更好的支持 C++（如 C++的 string 类型）。 

## 定义Flag

```c++
#include <iostream>
#include <gflags/gflags.h>
static bool ValidatePort(const char* flagname, gflags::int32 value)
{
    if (value > 0 && value < 32768)
    {
        return true;
    }
    return false;
}

DEFINE_int32(port, 8080, "What port to listen on");
DEFINE_validator(port, &ValidatePort);
DEFINE_bool(debug, false, "Turn on the debug mode");
```

支持的类型有：

- `DEFINE_bool`: boolean
- `DEFINE_int32`: 32-bit integer
- `DEFINE_int64`: 64-bit integer
- `DEFINE_uint64`: unsigned 64-bit integer
- `DEFINE_double`: double
- `DEFINE_string`: C++ string

没有列表之类的复杂类型，这样保证了库的设计的简单。

`DEFINE` 宏有三个参数：flag名、默认值、描述使用方法的帮助。帮助会在执行 `--help` flag时显示。

可以在任何源文件中定义flag，但是每个只能定义一次。如果需要在多处使用，那么在一个文件中 `DEFINE` ，在其他文件中 `DECLARE` 。比较好的方法是在 .cc 文件中 `DEFINE` ，在 .h 文件中 `DECLARE` ，这样包含头文件即可使用flag了。

在库中定义flag很好用，但是也有些问题。比如一个库可能没有flag的合适的默认值。解决办法是可以使用flag验证器在没有有效flag值的时候给出提示。

注意： `DEFINE_foo` 和 `DECLARE_foo` 是全局命名空间的。

## 使用Flag

```c++
int main(int argc, char *argv[])
{
    gflags::ParseCommandLineFlags(&argc, &argv, true);
    std::cout << "port = " << FLAGS_port << std::endl;
    std::cout << "debug = " << std::boolalpha << FLAGS_debug << std::endl;
    return 0;
}
```

定义的flag可以像正常的变量一样使用，只需在前面加上 `FLAGS_` 前缀。如前面例子中定义了 `FLAGS_port` 和 `FLAGS_debug` 两个变量。

最后，还需要解析命令行。通常把它放在 `main()` 的开始处，传入的 `argc` 和 `argv` 参数可能被修改。

最后一个参数如果为true， `ParseCommandLineFlags` 会从 `argv` 删除flag，修改 `argc` ，最后只剩下命令行参数。

相反如果为false， `argc` 不会修改， `argv` 会被重新排列，flag在前，参数在后， `ParseCommandLineFlags` 会返回 `argv` 中第一个命令行参数的位置，即最后一个flag的后一个位置。

根据命令行的解析，修改 `FLAGS_*` 变量。

## 参考

- [GFlags使用文档](http://www.yeolar.com/note/2014/12/14/gflags/)
- [使用 Google gflags 解析命令行参数](http://senlinzhan.github.io/2017/10/07/gflags/)

