# 定时任务


## 基本语法
```shell
# 查看当前用户的定时任务
crontab -l

# 编辑定时任务
crontab -e

# 删除定时任务
crontab -r
```


## 时间格式
```shell
# 时间由5各字段组成, 分别表示: 分钟 小时 日期 月份 星期
# 例如:
# 每天凌晨2点执行一次command
0 2 * * * command
# 每隔5分钟执行一次command
*/5 * * * * command


# 特殊符号
# 1. 匹配任意值: *
# 2. 枚举: ,
# 3. 指定范围: -
# 4. 间隔: /
```