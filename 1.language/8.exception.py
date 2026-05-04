## with
import time
from contextlib import contextmanager

@contextmanager
def timer(name="Operation"):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"{name} took {elapsed:.4f} seconds")

# 使用
with timer("Database query"):
    # 模拟耗时操作
    time.sleep(0.5)
    # 即使这里发生异常，也会打印耗时