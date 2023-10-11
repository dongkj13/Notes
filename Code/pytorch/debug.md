```python
if torch.distributed.get_rank() != 0:
    import sys
    sys.stdin.close()
    print(f"rank: {torch.distributed.get_rank()} stdin close")
    
    while True:
        pass
else:
    import pdb;pdb.set_trace()
```

