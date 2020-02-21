### 首先确认是否已经有SSH key 

在`~/.ssh`目录下检查是否存在 `id_rsa.pub` 或 `id_dsa.pub`这两个文件，若不存在则需要创建。

### 创建一个 SSH key 

```sh
ssh-keygen -t rsa -C "your_email@example.com"
```

代码参数含义：

-t 指定密钥类型，默认是 rsa ，可以省略。可以使用：”rsa1”(SSH-1) “rsa”(SSH-2) “dsa”(SSH-2) 
-C 设置注释文字，比如邮箱。
-f 指定密钥文件存储文件名。

以上代码省略了 -f 参数，因此，运行上面那条命令后会让你输入一个文件名，用于保存刚才生成的 SSH key 代码，如：

```sh
Generating public/private rsa key pair.
# Enter file in which to save the key (/c/Users/you/.ssh/id_rsa): [Press enter]
```

当然，你也可以不输入文件名，使用默认文件名（推荐），那么就会生成 id_rsa 和 id_rsa.pub 两个秘钥文件。

接着又会提示你输入两次密码（该密码是你push文件的时候要输入的密码，而不是github管理者的密码），

当然，你也可以不输入密码，直接按回车。那么push的时候就不需要输入密码，直接提交到github上了，如：

```sh
Enter passphrase (empty for no passphrase): 
# Enter same passphrase again:
```

接下来，就会显示如下代码提示，则创建成功。

```sh
Your identification has been saved in /c/Users/you/.ssh/id_rsa.
# Your public key has been saved in /c/Users/you/.ssh/id_rsa.pub.
# The key fingerprint is:
# 01:0f:f4:3b:ca:85:d6:17:a1:7d:f0:68:9d:f0:a2:db your_email@example.com
```

## 添加SSH key到github上或者远端服务器上

将`id_rsa.pub`文件的内容添加到[github ssh key](https://github.com/settings/keys)设置中。

或者将`id_rsa.pub`文件的内容添加到远端服务器的`.ssh/authorized_keys`中，输入以下命令快速添加。

```sh
ssh user@remote 'mkdir -p .ssh && cat >> .ssh/authorized_keys' < ~/.ssh/id_rsa.pub
```

## 参考

- [SSH-keygen用法](https://www.cnblogs.com/yanglang/p/9563496.html)
- [SSH 基本用法](https://zhuanlan.zhihu.com/p/21999778)
- [Linux - 配置SSH免密通信 - “ssh-keygen”的基本用法](https://www.cnblogs.com/shoufeng/p/11022258.html)

