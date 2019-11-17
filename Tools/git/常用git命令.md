## 新建代码库

```bash
# 创建版本库
$ git init

# 本地创建远程仓库
$ git init --bare
```

## [配置](./git config.md)

## 增加/删除文件

```bash
# 添加指定文件到暂存区
$ git add [file1] [file2] ...

# 添加指定目录到暂存区，包括子目录
$ git add [dir]

# 添加当前目录的所有文件到暂存区
$ git add .

# 停止追踪指定文件，但该文件会保留在工作区；文件从tracked状态变成untracked状态，相当于add的逆操作
$ git rm --cached [file]

# 直接将文件从文件夹中删除
$ git rm -f [file1]

# 改名文件，并且将这个改名放入暂存区，相当于mv之后在git add
$ git mv [file-original] [file-renamed]
```

## 代码提交

```bash
# 提交暂存区到仓库区
$ git commit -m [message]

# 提交工作区自上次commit之后的变化，直接到仓库区
$ git commit -am [message]

# 提交时显示所有diff信息
$ git commit -v

# 使用一次新的commit，替代上一次提交
# 如果代码没有任何新变化，则用来改写上一次commit的提交信息
$ git commit --amend -m [message]

# 使用一次新的commit，替代上一次提交，并且不修改上次commit的提交信息。
# git rebase -i 是在已经commit之后，合并两个甚至若干个commit。
# git commit --amend 是在未commit之前，直接合并到之前的commit。
$ git commit --amend --no-edit
```

## 分支

TODO

## [标签](./git tag.md)

## 查看信息

```bash
# 显示某次提交的元数据和内容变化或文件
$ git show [--name-only] [commit]

# 显示所有提交过的用户，按提交次数排序
$ git shortlog -sn

# 显示指定文件是什么人在什么时间修改过
$ git blame [file]

# 显示今天你写了多少行代码，三种不同方式的显示
$ git diff --stat '@{1 day ago}'
$ git diff --numstat '@{1 day ago}'
$ git diff --shortstat '@{1 day ago}'
```

[@{}参考](https://git-scm.com/docs/gitrevisions#Documentation/gitrevisions.txt-emem)

## 远程同步

TODO

## [撤销](./git reset.md)

```bash
# 恢复暂存区的指定文件到工作区
$ git checkout [file]

# 恢复某个commit的指定文件到暂存区和工作区
$ git checkout [commit] [file]

# 恢复暂存区的所有文件到工作区
$ git checkout .

# 暂时将未提交的变化移除，稍后再移入
$ git stash
$ git stash pop
```

## 参考

- [常用 Git 命令清单](http://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html)
- [git官网](https://git-scm.com/)
- [git-简易指南](http://www.bootcss.com/p/git-guide/)
- [Pro git](http://iissnan.com/progit/)
- [windows下实现Git在局域网使用](https://www.cnblogs.com/hujunzheng/p/4970411.html)