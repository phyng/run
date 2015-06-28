# my
My python cli toolkit.

## 这是什么
如果经常写一些 Python 小程序，然后在终端中运行，但是分散在各个文件中太不方便了，所以需要一个统一的管理工具。

## 结构和用法

~~~text
.
├── bin
│   ├── cli1.py
│   ├── cli2.py
│   └── my.py
~~~

只需要添加一次 `sudo ln -s /path/to/bin/my.py /usr/bin/my`，之后就能愉快的通过 my 调用程序了：

~~~sh
# my cli1 会自动映射到 cli1.py 的 main() 函数
$ my cli1
# 后面的 args1 args2 会自动以 *args 传入 main(*args)
$ my cli2 argv1 argv2
~~~

~~~python
# cli2.py 示例
def main(*args):
    print args.join(' ')

# run
$ my cli2 hello world
~~~

## TODO

  * [ ] `my admin list/add/edit/remove/show`
