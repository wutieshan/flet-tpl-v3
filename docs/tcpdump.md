# tcpdump


## Introduction
```shell
# tcpdump是一个linux命令行工具, 用于抓取网络数据包


# 帮助
tcpdump -h


# 过滤端口
sudo tcpdump port 80
sudo tcpdump src port 80
sudo tcpdump dst port 80


# 过滤网段
sudo tcpdump net 192.168
sudo tcpdump src net 192.168
sudo tcpdump dst net 192.168


# 过滤host
sudo tcpdump host 192.168.1.100
sudo tcpdump src host 192.168.1.100
sudo tcpdump dst host 192.168.1.100


# 过滤协议
sudo tcpdump arp
sudo tcpdump ip
sudo tcpdump tcp
sudo tcpdump udp
sudo tcpdump icmp


# 过滤网口
sudo tcpdump -i any
sudo tcpdump -i eth0


# 协议header过滤
# protocal[a:b]
tcp[10:15]


# 逻辑运算符
and: &&
or: ||
not: !


# 比较运算符
>
<
=
!=
>=
<=


## 参数说明
-i: 指定网卡接口
-w: 保存数据包到文件
-n: 不解析域名, 防止DNS循环
-s: 指定抓取的数据包的大小; 默认64K
-c: 设定捕获包的数量
-w: 保存数据包到文件; xxx.pcap
-C: 分割文件大小; 如 -C 10M


## 解析pcap文件
tcpdump -n -r xxx.pcap
```


## pcap
### pcap格式概述
```shell
# pcap是一种通用的数据流格式
# pcap文件可以分为3部分: global header, packet header, packet data


# global header
# 固定长度为24bytes, 记录了pcap文件的一些基本信息
1. magic: 4bytes: 用于识别文件开头和文件大小端模式
    \xa1\xb2\xc3\xd4: big-endian
    \xd4\xc3\xb2\xa1: little-endian
2. major: 2bytes: uint16: pcap文件的主版本号
3. minor: 2bytes: uint6: pcap文件的次版本号
4. thiszone: 4bytes: int32: 当前时区偏移量
5. sigfigs: 4bytes: uint32: 时间戳的精度
6. snaplen: 4bytes: uint32: 最大抓取数据包长度


# packet header
# 固定长度为16bytes, 记录了每个数据包的一些基本信息
1. seconds: 4bytes: uint32: unix时间戳以秒为单位的整数部分
2. microseconds: 4bytes: uint32: unix时间戳以秒为单位的小数部分
3. caplen: 4bytes: uint32: 抓取到的数据帧的长度, packet data的长度
4. len: 4bytes: uint32: 实际数据帧的长度, 一般不大于caplen, 多数情况下和caplen相等


# packet data
# 紧跟在packet header之后, 长度为caplen
```


### pcap格式解析
```python

```


## 过滤
```shell
# 1. 根据IP地址
ip.addr == xxx
ip.src == xxx
ip.dst == xxx


# 2. 根据端口号
tcp.port == xxx
udp.port == xxx
tcp.srcport == xxx
tcp.dstport == xxx


# 3. 根据协议
tcp
udp
icmp
http
dns


# 4. 端到端通信
# 显示特定tcp流的所有数据包
tcp.stream eq xx


# 5. 根据时间
frame.time == xxx


# 6. 根据请求或响应
http.request.method == "POST"
http.request.uri == "/login"
http.request.uri.query == xxx
http.response.code == 404
http.host contains xxx


# 7. DNS查询
dns.qry.name == xxx
dns.qry.type contains xxx


# 8. ICMP类型
icmp.type == xxx


# 9. TCP标志
tcp.flags.syn == 1
tcp.flags.ack == 1
tcp.flags.fin == 1


# 10. 协议字段
eth.addr == xxx
tcp.seq == xxx
```