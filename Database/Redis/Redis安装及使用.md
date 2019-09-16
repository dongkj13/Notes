## Windows
- 下载地址：https://github.com/microsoftarchive/redis/releases
- 下载 Redis-x64-xxx.zip压缩包到 C 盘，解压后，将文件夹重新命名为 redis。
- 将安装目录 `C:\redis` 添加至环境变量
- 启动Redis服务
    - `redis-server.exe` 使用默认配置
    - `redis-server.exe redis.windows.conf`
- 启动Redis客户端
    - `redis-cli.exe -h 127.0.0.1 -p 6379`


## Linux
- 下载地址：https://www.redis.net.cn/download/
```cmd
$ wget http://download.redis.io/releases/redis-2.8.17.tar.gz
$ tar xzf redis-2.8.17.tar.gz
$ cd redis-2.8.17
$ make
```
- 启动Redis服务
    - `./src/redis-server`
- 启动Redis客户端
    - `./src/redis-cli`