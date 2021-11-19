## 代码框架

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
from itertools import groupby
from itertools import imap
from operator import itemgetter

def increment_counter(group, counter, amount=1):
    line = 'reporter:counter:%s,%s,%d\n' % (group, counter, amount)
    sys.stderr.write(line)
    sys.stderr.flush()

def do_map():
    for line in sys.stdin:
        try:
            items = line.strip().split('\t')
            if len(items) == 1:
                info = json.loads(items[0])
                query = info.get("query", "")
                print query.lower() + '\t' + items[0] + '\t' + "1"
                increment_counter('map', 'pair')
            elif len(items) == 2:
                print items[0].lower() + '\t' + items[1] + '\t' + "2"
                increment_counter('map', 'rewrite')
            else:
                continue
        except Exception, e:
            print >> sys.stderr, "exception: %s" % e
            continue

def do_red():
    for query, items in groupby(imap(lambda x: x.rstrip('\r\n').split('\t'), sys.stdin), itemgetter(0)):
        try:
            for item in items:
                if item[2] == "2":
                		print json.dumps(item[2])
        except Exception, e:
            print >> sys.stderr, "exception: %s" % e
            continue

if __name__ == '__main__':
    if sys.argv[1] == 'map':
        do_map()
    elif sys.argv[1] == 'red':
        do_red()

```

## 调试命令

```shell
cat input_1 | python task.py map
cat input_1 | python task.py map | python task.py red
cat input_1 input_2 | python task.py map | sort | python task.py red
```

