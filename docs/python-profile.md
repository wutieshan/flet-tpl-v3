# python性能分析


## 方案
```python
# 1. 使用time.perf_counter()计时
# 2. 使用timeit()测量小段代码的执行时间
# 3. 使用resource模块(unix)获取进程的内存使用情况
# 4. 使用psutil三方模块(跨平台)监控cpu和内存
# 5. 使用memory_profiler逐行分析内存使用
# 6. 使用cprofile分析函数调用次数和耗时  ==>  可以结合可视化工具(如snakeviz)
# 7. 使用line_profiler逐行分析
# 8. 
```