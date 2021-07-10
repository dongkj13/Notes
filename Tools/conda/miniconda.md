## Miniconda简介

Miniconda是一款小巧的python环境管理工具，安装包大约只有50M多点，其安装程序中包含conda软件包管理器和Python。一旦安装了Miniconda，就可以使用conda命令安装任何其他软件工具包并创建环境等。


## Miniconda安装

1、下载最新版 miniconda：

```sh
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

2、在bash中安装：

```sh
sh Miniconda3-latest-Linux-x86_64.sh
```

3、手动生效环境变量，或添加conda初始化到.bashrc / .zshrc文件

```bash


# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/data08/home/dongkaijie.572/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/data08/home/dongkaijie.572/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/data08/home/dongkaijie.572/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/data08/home/dongkaijie.572/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

