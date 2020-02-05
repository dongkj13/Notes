# 1 基本命令

## 1.1 环境管理

### 查看当前的conda版本

```shell
$ conda --version
```

### 常看当前所有的环境：

```shell
$ conda env list 
$ conda info -e

# conda environments:
#
base                  *  /Users/dongkaijie/opt/anaconda3
deeplearning             /Users/dongkaijie/opt/anaconda3/envs/deeplearning
python27                 /Users/dongkaijie/opt/anaconda3/envs/python27
```

\* 表示当前所在环境

### 创建新的Python环境

```shell 
$ conda create -n python27 python=2.7
$ conda create -n deeplearning python=3.7 numpy matplotlib pandas jupyter
```

### 切换环境

```shell
$ source activate env_name
```

### 退出环境

```shell
$ deactivate env_name
```

### 移除环境

```shell
$ conda remove -n env_name --all
```

## 1.2 包管理

| 命令                 | 意义                  |
| -------------------- | --------------------- |
| `conda list`         | 查看当前环境的包      |
| `conda list -n xxx`  | 查看指定xxx环境下的包 |
| `conda search xxx`   | 查找包                |
| `conda update xxx`   | 更新包                |
| `conda update --all` | 更新所有库            |
|`conda install xxx`|安装包|
|`conda install -n env_name xxx`|指定安装的环境|
|`conda remove xxx`|卸载包|

# 参考

[Mac安装 anaconda及其基本命令](https://blog.csdn.net/qq_31573519/article/details/82845515)