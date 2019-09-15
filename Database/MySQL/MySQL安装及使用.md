- [MySQL官方下载地址](https://dev.mysql.com/downloads/installer/)
- [MySQL安装教程](https://blog.csdn.net/qq_33144861/article/details/80267462)
- 将安装目录 `C:\Program Files\MySQL\MySQL Server 8.0\bin` 添加至环境变量
- 启动和关闭mysql服务
    - [**用管理员身份来运行cmd程序**](https://blog.csdn.net/qq_35830949/article/details/79537590)
    - `net start [mysql_name]`  确认是正确的mysql服务名
    - `net stop [mysql_name]`
- 登录数据库
```sh
--mysql [–h主机名或者IP地址]  –u用户名  –p密码 [默认初始进入数据库]
mysql -hlocalhost -uroot -p23452345     # 登录本机默认数据库
```

