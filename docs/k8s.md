# k8s


## 1. 集群信息


## 2. 资源管理
```shell
# 1. 获取资源列表
kubectl get <resource_t> [-n <namespace>]
kubectl get pods -n s6023


# 2. 获取资源详细信息
kubectl describe <resource_t> <resource_name> [-n <namespace>]
kubectl describe pod xxxxxxxxxxx -n s6023


# 3. 创建资源


# 4. 删除资源


# 5. 编辑资源
```


## 3. 应用程序管理


## 4. 日志和调试
```shell
# 1. 查看日志
kubectl logs <pod_name> [-n <namespace>]
kubectl logs <pod_name> [-n <namespace>] [-c <container_name>]  # 如果一个pod下有多个容器


# 2. 查看实时日志
kubectl logs -f <pod_name> [-n <namespace>]


# 3. 进入容器
kubectl exec -it <pod_name> [-n <namespace>] -- /bin/bash
```


## 5. 配置和服务发现


## 6. 其它常用命令
```shell
# 1. 查看节点信息
kubectl get nodes


# 2. 查看命名空间
kubectl get namespaces
```