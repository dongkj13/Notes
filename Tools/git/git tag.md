## 查看tag

```bash
# 列出所有tag
$ git tag

# 查看tag信息
$ git show [tag_name]
```

## 添加/删除tag
Git 使用的标签有两种类型：轻量级的（lightweight）和含附注的（annotated）。轻量级标签就像是个不会变化的分支，实际上它就是个指向特定提交对象的引用。而含附注标签，实际上是存储在仓库中的一个独立对象，它有自身的校验和信息，包含着标签的名字，电子邮件地址和日期，以及标签说明，标签本身也允许使用 GNU Privacy Guard (GPG) 来签署或验证。一般我们都建议使用含附注型的标签，以便保留相关信息；当然，如果只是临时性加注标签，或者不需要旁注额外信息，用轻量级标签也没问题。
```bash
# 新建一个轻量级tag在指定commit，默认为当前commit
$ git tag [tag_name] [commit-id]

# 新建一个含附注的tag在指定commit，默认为当前commit
$ git tag -a [tag_name] [commit-id] -m [tag_message]

# 删除本地tag
$ git tag -d [tag_name]

# 删除远程tag
$ git push origin :refs/tags/[tagName]
```

## 提交tag

```bash
# 提交指定tag
$ git push [remote] [tag]

# 提交所有tag
$ git push [remote] --tags
```

## 参考

- [6 Git 基础 - 打标签](https://git-scm.com/book/zh/v1/Git-基础-打标签)

