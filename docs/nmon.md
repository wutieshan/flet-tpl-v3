# nmon


## 参数
```shell
1. -f: 监控结果以文件形式输出, 默认文件名为`<hostname>_YYYYMMMDD_HHMM.nmon`, 必须作为第一个参数来关闭交互式模式, 默认情况下, -f 会设置 -s300 -c288
2. -F: 作用同-f, 区别在于可以自定义输出文件名
3. -t: 显示资源占用较高的进程
4. -s: 采样频率, 单位毫秒
5. -c: 采样次数
6. -m: 指定结果输出的目录


# 示例
nmon -ft -s500 -c120 -m ~/nmon/result
```
