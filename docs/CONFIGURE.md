### 配置文件
- #### 以行情服务器 config/market.json为例
- #### RabbitMQ服务配置 RABBITMQ
```
host `string` ip地址 默认用了本地rabbit服务器，也可以用远程外网，填上对应的的配置即可
port `int` 端口
username `string` 用户名
password `string` 密码
```
- #### MONGODB服务配置 MONGODB
```
host `string` ip地址 默认用了本地mongodb服务器，也可以用远程外网，填上对应的的配置即可
port `int` 端口
username `string` 用户名
password `string` 密码
```
- #### 行情服务器配置 MARKETS
```
"binance_swap"  键值：币安合约标识
"symbols" 键值：交易对
"name" 键值：具体交易对
"channels" 频道：订阅交易所相关ws数据频道
```