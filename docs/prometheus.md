# prometheus


## reference
> - [中文文档](https://icloudnative.io/prometheus)
> - [Prometheus官方文档](https://prometheus.io/docs/introduction/overview/)


## PromQL
### cpu使用率
```shell
# 计算思路
# 总时间 - 空闲时间 = 使用时间
100 - avg by (instance)(irate(node_cpu_seconds_total{mode="idle"}[1m])) * 100


# Note: 尽量不要使用!=, 可能某些情况下, 特定mode的cpu占用不会被统计
avg by (instance)(irate(node_cpu_seconds_total{mode!="idle"}[1m])) * 100
```


### 内存使用率
```shell
# 计算思路
# 已用内存 = 总内存 - 空闲内存
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes{instance=$_server} * 100
```


### 网络流量

