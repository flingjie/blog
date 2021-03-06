Title: Configure Emacs for clojure
Date: 2014-03-29 10:39:00
Category: emacs

1.**使用环境**：
ubuntu12.04 + emacs24 + leiningen2.3.4

2.**配置emacs**   
  a.添加package地址，在`~/.emacs.d/init.el`中加入：   

``` elisp
(require 'package)
(add-to-list 'package-archives
             '("marmalade" . "http://marmalade-repo.org/packages/"))
(package-initialize)
```
    
  b.安装相关插件，在`~/.emacs.d/init.el`中加入：

``` elisp
(defvar my-packages '(starter-kit
                      starter-kit-lisp
                      starter-kit-bindings
                      starter-kit-eshell
                      clojure-mode
                      clojure-test-mode
                      cider))

(dolist (p my-packages)
  (when (not (package-installed-p p))
    (package-install p)))
```

3.**编辑相关操作**   
a.文件、窗口操作

``` text
C-x C-f    打开文件
C-x C-s    保存文件
C-x b      切换buffer
C-x k      关闭当前buffer
C-x o      切换到下一buffer
C-x 0      隐藏当前buffer
C-x 1      隐藏其他buffer
C-x 2      垂直分割窗口
C-x 3      水平分割窗口
```

b.移动操作

```
C-a    移动到行头
C-e    移动到行尾
C-n    移动到下一行
C-p    移动到上一行
C-b    向后移动一个字符
C-f    向前移动一个字符
M-f    向前移动一个单词
M-b    向后移动一个单词
C-v    向下翻页
M-v    向上翻页
M-<    移动到buffer开头
M->    移动到buffer末尾
C-M-f  移动到后一个括号
C-M-f  移动到前一个括号
```

c.编辑操作

```
C-d        删除一个字符
M-d        删除一个单词
C-k        删除一行
C-w        删除选中区域
M-w        复制选中区域
C-y        粘帖
C-j        换行

C-M-Space  选中光标所在的S表达式
C-M-t      交换连个S表达式位置
M-1 (      在当前S表达式外添加一对括号
M-s        删除当前S表达式外的一对括号
M-r        删除当前S表达式外的一对括号(包括内容)
C-)        将后面的括号向后移动一个元素
           (a b (c d) e f) -> (a b (c d e) f)
C-}        将后面的括号向前移动一个元素
           (a b (c d) e f) -> (a b (c) d e f)
C-(        将前面的括号向前移动一个元素
C-{        将前面的括号向后移动一个元素
C-M-q      代码对齐

```

d.帮助操作

```
C-h b    查看当前的key绑定
C-h m    查看当前的编辑模式
C-h a    查找一个关键词的相关帮助
C-h k    查看一个key的绑定
```

4.**编译相关操作**

```
C-c M-j    cider-jack-in,启动nREPL
C-c C-e    执行s表达式
C-c C-r    执行当前选中区
C-c C-z    运行lisp进程
```

5.**宏操作**

```
C-x (   ;;开始录制宏
...     ;;输入操作
C-x )   ;;结束录制
C-x e   ;;执行宏
```