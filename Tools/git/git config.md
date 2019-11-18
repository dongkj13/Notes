## 配置文件如何生效

对于 git 来说，配置文件的权重是**仓库>全局>系统**。如果定义的值有冲突，以权重高的层中定义的为准。

1. `.git/config（仓库级）`，只对当前所属仓库有效
2. ``~/.gitconfig文件（全局级）`，对当前用户及所有仓库有效
3. `/etc/gitconfig文件（系统级）`，对系统上所有用户及他们所拥有的仓库都有效

## 查看配置文件

```bash
# 查看当前仓库生效的所有配置
$ git config -l

# 查看仓库级的 config
$ git config --local -l

# 查看全局级的 config
$ git config --global -l

# 查看系统级的 config
$ git config --system -l
```

## 编辑配置文件

```bash
# 编辑整个配置文件
$ git config [--local|--global|--system] -e

# 添加一个配置项，默认是添加在local配置中。注意add后面的section,key,value一项都不能少，否则添加失败。
$ git config [--local|--global|--system] --add section.key value

# 获取一个配置项，默认是获取local配置中内容。
$ git config [--local|--global|--system] --get section.key

# 删除一个配置项，默认是删除local配置中内容
$ git config [--local|--global|--system] --unset section.key
```

## 常用配置项
```git
[alias]
	st = status
    ci = commit 
    cin = commit --amend --no-edit
	co = checkout
	br = branch
	lm = log --no-merges --color --date=format:'%Y-%m-%d %H:%M:%S' --pretty=format:'%C(yellow)%h%Creset - %C(yellow)%d%Cgreen%s %Cred(%cd) %C(bold blue)<%an>%Creset'
    rvm = push origin HEAD:refs/for/master%r=chenjiajun
    cf = config -l
	df = diff
[user]
	name = dongkaijie
	email = dongkaijie@bytedance.com
[core]
    //默认软件路径\Git\usr\bin\notepad2.exe
    notepad2.exe
```