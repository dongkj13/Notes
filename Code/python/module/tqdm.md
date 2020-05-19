tqdm 是一个快速，可扩展的Python进度条，可以在 Python 长循环中添加一个进度提示信息用法，用户只需要封装任意的迭代器`tqdm(iterator)`。

tqdm(list)方法可以传入任意一种list。trange(i) 是 tqdm(range(i)) 的简单写法。

```python
import time
# 方法1
from tqdm import tqdm  
for i in tqdm(range(100)):  
    time.sleep(0.01)
    
# 方法2
from tqdm import trange
for i in trange(100):
    time.sleep(0.01) 
```

结果：

```
 0%|          | 0/100 [00:00<?, ?it/s]
 11%|█         | 11/100 [00:00<00:00, 100.00it/s]
 22%|██▏       | 22/100 [00:00<00:00, 100.00it/s]
 32%|███▏      | 32/100 [00:00<00:00, 100.00it/s]
 43%|████▎     | 43/100 [00:00<00:00, 100.00it/s]
 54%|█████▍    | 54/100 [00:00<00:00, 100.00it/s]
 64%|██████▍   | 64/100 [00:00<00:00, 99.11it/s] 
 74%|███████▍  | 74/100 [00:00<00:00, 99.37it/s]
 85%|████████▌ | 85/100 [00:00<00:00, 99.56it/s]
 95%|█████████▌| 95/100 [00:00<00:00, 99.69it/s]
100%|██████████| 100/100 [00:01<00:00, 99.70it/s]
```

也可以为进度条设置描述：

```python
import time
from tqdm import tqdm

pbar = tqdm(["a", "b", "c", "d"])  
for char in pbar:  
    # 设置描述
    pbar.set_description("Processing %s" % char)
    time.sleep(1)
```

结果：

```ruby
0%|          | 0/4 [00:00<?, ?it/s]
Processing a:  25%|██▌       | 1/4 [00:01<00:03,  1.00it/s]
Processing b:  50%|█████     | 2/4 [00:02<00:02,  1.00it/s]
Processing c:  75%|███████▌  | 3/4 [00:03<00:01,  1.00it/s]
Processing d: 100%|██████████| 4/4 [00:04<00:00,  1.00it/s]
```

## 参考

- [官网](https://pypi.org/project/tqdm/)
- [tqdm](https://www.jianshu.com/p/21cf48be6bf6)

