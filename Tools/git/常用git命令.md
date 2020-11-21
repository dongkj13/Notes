## 常见的git命令及用法

<p align="center">
  <img src=".\..\..\Image\git_command\git_command.png">
</p>

- Workspace：工作区
- Index / Stage：暂存区
- Repository：仓库区（或本地仓库）
- Remote：远程仓库

## 新建代码库

```bash
# 创建版本库
$ git init

# 本地创建远程仓库
$ git init --bare
```

## 克隆代码库

```bash
# 获取全部分支内容，整体下载时间较长 & 所占磁盘空间较大
$ git clone <repository> [<directory>]

# 获取指定分支的代码
$ git clone <repository> [--branch/-b] [branch_name]

# 获取最近xx（10条提交记录的）代码，默认是master分支
$ git clone <repository> [--depth 10]
```

## [配置](./config.md)

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

```bash
# 创建分支
$ git branch [branch_name]

# 切换分支
$ git checkout [branch_name]

# 快速创建并切换分支
$ git checkout -b [branch_name]

# 查看本地/远程分支
$ git branch
$ git branch [-r] [--remote]
$ git branch [-a] [--all]

# 删除分支
$ git branch -d [branch_name]

# 合并分支，在主分支指定要合并进来的分支
$ git merge [branch_name]
```

## [标签](./tag.md)

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

## 撤销

```bash
# 恢复暂存区的指定文件到工作区
$ git checkout [file]

# 恢复某个commit的指定文件到暂存区和工作区
$ git checkout [commit] [file]

# 恢复暂存区的所有文件到工作区
$ git checkout .

# 回退到某个版本的Staged状态，可以修改提交信息再次提交
$ git reset --soft head^/commit-id

# 回退到某个版本的Modified状态，可以修改需要提交的文件并再次提交
$ git reset --mixed head^/commit-id

# 彻底回退到某个版本，本地的源码也会变为上一个版本的内容（所有的修改都会被丢弃）
$ git reset --hard head^/commmit-id

# 暂时将未提交的变化移除，稍后再移入
$ git stash
$ git stash pop
$ git stash list
$ git stash push -m "commit message" file1 file2 file3
```

## 清空工作区

```bash
# 是一次clean的演习，告诉你哪些文件会被删除。记住他不会真正的删除文件，只是一个提醒
$ git clean -n

# 删除当前目录下所有没有track过的文件。不会删除.gitignore文件里面指定的文件夹和文件，不管这些文件有没有被track过
$ git clean -f [<path>]

# 删除当前目录下没有被track过的文件和文件夹
$ git clean -df

# 删除当前目录下所有没有track过的文件。不管他是否是.gitignore文件里面指定的文件夹和文件
$ git clean -xf
```

- `git reset --hard`和`git clean -f`是一对好基友。结合使用他们能让你的工作目录完全回退到最近一次commit的时候。
- `git clean`对于刚编译过的项目也非常有用。它能轻易删除掉编译后生成的.o和.exe等文件。这个在打包要发布一个release的时候非常有用。

## 参考

- [常用 Git 命令清单](http://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html)
- [git官网](https://git-scm.com/)
- [git-简易指南](http://www.bootcss.com/p/git-guide/)
- [Pro git](http://iissnan.com/progit/)
- [windows下实现Git在局域网使用](https://www.cnblogs.com/hujunzheng/p/4970411.html)
- [工作流一目了然，看小姐姐用动图展示10大Git命令](https://zhuanlan.zhihu.com/p/132573100)
- [Learn Git Branching](https://learngitbranching.js.org)

