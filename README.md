# do-while

making poor life choices for conference talks

[![version](https://img.shields.io/pypi/v/do-while.svg)](https://pypi.org/project/do-while)
[![license](https://img.shields.io/pypi/l/do-while.svg)](https://github.com/amyreese/python-do-while/blob/main/LICENSE)


Install
-------

```shell-session
$ pip install do-while
```


Usage
-----

Do a do-while loop:

```py
from do_while import do, while_

queue = [1, 2, 3]

@do
def loop():
    item = queue.pop()
    print(item)

while_(queue)

# 1
# 2
# 3
```

Do an until loop:

```py
from do_while import until

k = 0

@until(lambda: k > 4)
def loop():
    nonlocal k
    print(k)
    k += 1

# 0
# 1
# 2
# 3
# 4
```


License
-------

do-while is copyright Amethyst Reese, and licensed under the MIT license.
