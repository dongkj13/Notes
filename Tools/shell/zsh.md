

## 安装zsh

查看系统当前使用的shell

```bash
$ echo $SHELL 
/bin/bash
```

查看系统是否安装了zsh

```bash
$ cat /etc/shells 
/bin/bash
/bin/csh
/bin/ksh
/bin/sh
/bin/tcsh
/bin/zsh
```

安装zsh

```bash
$ brew install zsh zsh-completions
```

切换shell为zsh

```ruby
$ chsh -s /bin/zsh
Changing shell for root.
Shell changed.
```

重启服务器，可使用`reboot`

## 安装oh-my-zsh

```bash
git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
```

## 配置主题

```sh
# Oh-My-Zsh 的默认配置文件在：~/.zshrc。编辑～/.zshrc 修改主题，这里我用的是 ys 主题，更多主体看[这里](https://github.com/robbyrussell/oh-my-zsh/wiki/Themes)，直接修改即可，无需下载
ZSH_THEME="ys"
# !!!! 重启终端后有效 或 使用 source ~/.zshrc 更新配置

# 题外话，不太想显示主机名，所以直接干掉主机名
# 编辑 ~/.oh-my-zsh/themes/ys.zsh-theme，最后面改成这样
PROMPT="
%{$terminfo[bold]$fg[blue]%}#%{$reset_color%} \
%(#,%{$bg[yellow]%}%{$fg[black]%}%n%{$reset_color%},%{$fg[cyan]%}%n) \
%{$fg[white]%}in \
%{$terminfo[bold]$fg[yellow]%}%~%{$reset_color%}\
${hg_info}\
${git_info}\
 \
%{$fg[white]%}[%*] $exit_code
%{$terminfo[bold]$fg[red]%}$ %{$reset_color%}"
```

## 插件推荐

#### autojump

```shell
git clone git://github.com/joelthelion/autojump.git $ZSH_CUSTOM/plugins/autojump
cd $ZSH_CUSTOM/plugins/autojump
./install.py
vim ~/.zshrc
# 在文件里找到plugins，添加
plugins=(autojump)
# 在文件末尾添加
[[ -s ~/.autojump/etc/profile.d/autojump.sh ]] && . ~/.autojump/etc/profile.d/autojump.sh
source ~/.zshrc
```

#### zsh-autosuggestion

```shell
git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
```

#### zsh-syntax-highlighting

```shell
git clone git://github.com/zsh-users/zsh-syntax-highlighting $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
```

## 参考

[oh-my-zsh让终端好用到飞起~](https://juejin.im/post/5d773da76fb9a06aff5e9a99)

[oh-my-zsh,让你的终端从未这么爽过](https://www.jianshu.com/p/d194d29e488c)

[yxy zshrc配置](https://github.com/xy24/dotfiles/blob/master/osx/zshrc)

