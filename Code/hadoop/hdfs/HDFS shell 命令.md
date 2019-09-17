## ls
```sh
hadoop fs -ls [-d] [-h] [-R] [<path> ...]
```
如果是文件，则按照如下格式返回文件信息：\
文件名 <副本数> 文件大小 修改日期 修改时间 权限 用户ID 组ID \
如果是目录，则返回它直接子文件的一个列表，就像在Unix中一样。目录返回列表的信息如下：\
目录名 <dir> 修改日期 修改时间 权限 用户ID 组ID 

| para |                         discription                          |
| :--: | :----------------------------------------------------------: |
|  -d  |            Directories are listed as plain files.            |
|  -h  | Formats the sizes of files in a human-readable fashion rather than a number of bytes. |
|  -R  |               列出hdfs文件系统所有的目录和文件               |

## mkdir
```sh
hadoop fs -mkdir [-p] <path> ...
```
接受路径指定的uri作为参数，创建这些目录。其行为类似于Unix的mkdir -p，它会创建路径中的各级父目录。

## mv
```sh
hadoop fs -mv <src> ... <dst>
```
将文件从源路径移动到目标路径。这个命令允许有多个源路径，此时目标路径必须是一个目录。不允许在不同的文件系统间移动文件。

## rm
```sh
hadoop fs -rm [-f] [-r|-R] [-skipTrash] <src> ...
```
删除指定的文件。

|    para    |                         discription                          |
| :--------: | :----------------------------------------------------------: |
| -skipTrash | option bypasses trash, if enabled, and immediately deletes <src> |
|     -f     | If the file does not exist, do not display a diagnostic message or modify the exit status to reflect an error. |
|   -[rR]    |               Recursively deletes directories                |


## cp
```sh
hadoop fs -cp [-f] [-p | -p[topax]] <src> ... <dst>
```
将文件从源路径复制到目标路径。这个命令允许有多个源路径，此时目标路径必须是一个目录。


## get
```sh
hadoop fs -get [-p] [-ignoreCrc] [-crc] <hdfs file> <local file>
```
复制文件到本地文件系统。可用-ignorecrc选项复制CRC校验失败的文件。使用-crc选项复制文件以及CRC信息。

| para |                         discription                          |
| :--: | :----------------------------------------------------------: |
|  -p  | preserves access and modification times, ownership and the mode. |


## put
```sh
hadoop fs -put [-f] [-p] <local file> <hdfs file>
```
从本地文件系统中复制单个或多个源路径到目标文件系统。也支持从标准输入中读取输入写入目标文件系统。

| para |                         discription                          |
| :--: | :----------------------------------------------------------: |
|  -p  | preserves access and modification times, ownership and the mode. |
|  -f  |       overwrites the destination if it already exists.       |


## cat
```sh
hadoop fs -cat [-ignoreCrc] <src> ...
hadoop fs -cat  hdfs文件路径 > 本地路径   ##从hdfs上下载文件到本地
hadoop fs -cat /user/* | head -100
hadoop fs -cat /user/* | tail -5
```
将路径指定文件的内容输出到stdout。


## du
```sh
hadoop fs -du [-s] [-h] <path> ...
```
显示目录中所有文件的大小，或者当只指定一个文件时，显示此文件的大小。

|   para    |                         discription                          |
| :-------: | :----------------------------------------------------------: |
|    -du    |                         以字节为单位                         |
|  -du -h   | 以合适的作为单位，第一个数是本文件大小，第二个数所有副本的大小=本文件大小*副本数 |
|  -du -s   |          显示文件夹下所有文件大小总和，以字节为单位          |
| -du -s -h |         显示文件夹下所有文件大小总和，以合适的为单位         |

## getmerge
```sh
hadoop fs -getmerge <hdfs dir> <local file>
```
将hdfs指定目录下所有文件排序后合并到local指定的文件中，文件不存在时会自动创建，文件存在时会覆盖里面的内容

## touchz
```sh
hadoop fs -touchz /user/data.txt 
```
在hdfs指定目录下创建空白文件


## help
```sh
hadoop fs -help **
```
查询帮助

## 参考

- [hadoop HDFS常用文件操作命令](https://segmentfault.com/a/1190000002672666)
- [Hadoop Shell命令 官网](https://hadoop.apache.org/docs/r1.0.4/cn/hdfs_shell.html)