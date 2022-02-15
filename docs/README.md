## 环境搭建
```
注意：centos8以上系统
```
### 进入root账号
- #### 如果是新的服务器，先进入服务器，然后设置root的密码
```
sudo passwd
```
回车
```
输入两次密即可，注意，输入密码的时候，是看不见密码的
```
- #### 如果是已有服务器
```
su
```
回车
```
输入root密码即可进入
```
### docker搭建
- #### 安装
```
curl -sSL https://get.daocloud.io/docker | sh
```
```
# 或使用国内镜像
curl -sSL https://get.daocloud.io/docker | sh
# 或用yum安装
```
- #### 查看版本
```
docker version
```
```
[root@VM-4-2-centos ~]# docker version
Client: Docker Engine - Community
 Version:           20.10.12
 API version:       1.41
 Go version:        go1.16.12
 Git commit:        e91ed57
 Built:             Mon Dec 13 11:45:22 2021
 OS/Arch:           linux/amd64
 Context:           default
 Experimental:      true

Server: Docker Engine - Community
 Engine:
  Version:          20.10.12
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.16.12
  Git commit:       459d0df
  Built:            Mon Dec 13 11:43:44 2021
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.4.12
  GitCommit:        7b11cfaabd73bb80907dd23182b9347b4245eb5d
 runc:
  Version:          1.0.2
  GitCommit:        v1.0.2-0-g52b36a2
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
[root@VM-4-2-centos ~]# 
```
- #### 启动docker
```
systemctl start docker
```
```
docker ps
```
```
[root@VM-8-15-centos ~]# docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
### rabbitmq服务器搭建
- #### 下载镜像
```
docker pull rabbitmq:management
```
- #### 启动rabbit
```
docker run -d --name rabbit -p 15672:15672 -p 5672:5672 rabbitmq:management
```
- #### 进入rabbit服务器
```
docker exec -it rabbit /bin/bash
```
```
[root@VM-8-15-centos ~]# docker exec -it rabbit /bin/bash
root@603ed0490de4:/# 
```
- #### 添加test用户
```
rabbitmqctl add_user test 123456
```
- #### 设置用户标
```
rabbitmqctl set_user_tags test administrator
```
- #### 设置用户权限
```
rabbitmqctl set_permissions -p / test ".*" ".*" ".*"
```
- #### 查看当前用户
```
rabbitmqctl list_users
```
```
root@603ed0490de4:/# rabbitmqctl list_users
Listing users ...
user    tags
test    [administrator]
guest   [administrator]
```
- #### 退出rabbit服务器
```
exit
```
- #### 如果要把rabbit服务器对外使用，则需要在服务器对应的安全组里面开放 5672 端口

================================================

### mongodb服务器搭建
- #### 下载镜像
```
docker pull mongo:latest
```
- #### 启动mongodb
```
docker run -itd --name mongo -p 27017:27017 mongo --auth
```
- #### 进入mongodb服务器
```
docker exec -it mongo mongo admin
use admin
# 创建一个名为test，密码为 123456 的用户。
db.createUser({ user:'test',pwd:'123456',roles:[ { role:'userAdminAnyDatabase', db: 'admin'},"readWriteAnyDatabase"]});
# 添加成功如下显示
Successfully added user: {
        "user" : "test",
        "roles" : [
                {
                        "role" : "userAdminAnyDatabase",
                        "db" : "admin"
                },
                "readWriteAnyDatabase"
        ]
}
# 尝试使用上面创建的用户信息进行连接。
db.auth('test', '123456')
DBQuery.shellBatchSize = 300
# 查看数据据
show dbs
# 显示如下
admin   0.000GB
config  0.000GB
local   0.000GB
```
- #### 退出mongodb服务器
```
exit
```
- #### 如果要把mongodb服务器对外使用，则需要在服务器对应的安全组里面开放 27017 端口

================================================
### 策略服务器搭建
- #### 下载镜像
```
docker pull rsyuan/quant
```
- #### 启动策略服务器
```
docker run -itd --name rsquant --link rabbit --link mongo -p 9999:9999 rsyuan/quant
```
- #### 进入策略服务器
```
docker exec -it rsquant /bin/bash
```
- #### 查看当前时区
```
date -R
# 显示如下
Wed, 26 Jan 2022 07:53:10 +0000
# 与国内时间不一样
# 改为国内时区
tzselect
# 显示如下
 1) Africa
 2) Americas
 3) Antarctica
 4) Asia
 5) Atlantic Ocean
 6) Australia
 7) Europe
 8) Indian Ocean
 9) Pacific Ocean
10) coord - I want to use geographical coordinates.
11) TZ - I want to specify the time zone using the Posix TZ format.
# 输入4 回车
# 显示如下
Please select a country whose clocks agree with yours.
 1) Afghanistan           18) Israel                35) Palestine
 2) Armenia               19) Japan                 36) Philippines
 3) Azerbaijan            20) Jordan                37) Qatar
 4) Bahrain               21) Kazakhstan            38) Russia
 5) Bangladesh            22) Korea (North)         39) Saudi Arabia
 6) Bhutan                23) Korea (South)         40) Singapore
 7) Brunei                24) Kuwait                41) Sri Lanka
 8) Cambodia              25) Kyrgyzstan            42) Syria
 9) China                 26) Laos                  43) Taiwan
10) Cyprus                27) Lebanon               44) Tajikistan
11) East Timor            28) Macau                 45) Thailand
12) Georgia               29) Malaysia              46) Turkmenistan
13) Hong Kong             30) Mongolia              47) United Arab Emirates
14) India                 31) Myanmar (Burma)       48) Uzbekistan
15) Indonesia             32) Nepal                 49) Vietnam
16) Iran                  33) Oman                  50) Yemen
17) Iraq                  34) Pakistan
# 输入9 回车
# 显示如下
Please select one of the following time zone regions.
1) Beijing Time
2) Xinjiang Time
# 输入1 回车
# 显示如下
The following information has been given:

        China
        Beijing Time

Therefore TZ='Asia/Shanghai' will be used.
Selected time is now:   Wed Jan 26 15:55:54 CST 2022.
Universal Time is now:  Wed Jan 26 07:55:54 UTC 2022.
Is the above information OK?
1) Yes
2) No
# 输入1 回车
# 显示如下
You can make this change permanent for yourself by appending the line
        TZ='Asia/Shanghai'; export TZ
to the file '.profile' in your home directory; then log out and log in again.

Here is that TZ value again, this time on standard output so that you
can use the /usr/bin/tzselect command in shell scripts:
Asia/Shanghai
# 最后
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
y
# 查看当前时间
date
# 与国内时间一样了
```
- #### 启动行情服务器
```
nohup python3 src/market.py config/market.json > /dev/null 2>&1 &
```
- #### 启动策略脚本
```
nohup python3 src/server.py config/server.json 后台账号 后台密码 > /dev/null 2>&1 &
# 例如
nohup python3 src/server.py config/server.json lszjl Zjl120221 > /dev/null 2>&1 &
```
- #### 退出策略服务器
```
exit
```
================================================
### 注意要去安全组开放 9999 端口

================================================

### 更新策略服务器

- #### 进入已购买的服务器
- #### 进入策略服务器
```
docker exec -it rsquant /bin/bash
```
- #### 停止行情服务器
```
pkill -f src/market.py
```
- #### 停止策略脚本
```
pkill -f src/server.py
pkill -f python
```
- #### 退出策略服务器
```
exit
```
- #### 停止正在运行的策略服务器
```
docker stop rsquant
```
- #### 删除已停止的策略服务器
```
docker rm rsquant
```
- #### 删除旧镜像
```
docker rmi rsyuan/quant
```
- #### 拉取最新的策略服务器
```
docker pull rsyuan/quant
```
- #### 启动策略服务器
```
docker run -itd --name rsquant --link rabbit --link mongo -p 9999:9999 rsyuan/quant
```
- #### 进入策略服务器
```
docker exec -it rsquant /bin/bash
```
- #### 启动行情服务器
```
nohup python3 src/market.py config/market.json > /dev/null 2>&1 &
```
- #### 启动策略脚本
```
nohup python3 src/server.py config/server.json 后台账号 后台密码 > /dev/null 2>&1 &
# 例如
nohup python3 src/server.py config/server.json lszjl Zjl120221 > /dev/null 2>&1 &
```
- #### 退出策略服务器
```
exit
```
================================================
### 更新最新代码
```
docker exec rsquant git pull -f origin master
```
================================================
### 检查环境
```
docker ps 
# 显示如下三个进程，则说明环境搭建成功
[root@VM-4-2-centos ~]# docker ps
CONTAINER ID   IMAGE                 COMMAND                  CREATED        STATUS        PORTS                                                                                                                                                 NAMES
934b17a1c8d7   centos                "/bin/bash"              26 hours ago   Up 26 hours                                                                                                                                                         centos
34cd1b740b6c   rabbitmq:management   "docker-entrypoint.s…"   2 days ago     Up 2 days     4369/tcp, 5671/tcp, 0.0.0.0:5672->5672/tcp, :::5672->5672/tcp, 15671/tcp, 15691-15692/tcp, 25672/tcp, 0.0.0.0:15672->15672/tcp, :::15672->15672/tcp   rabbit
15cb5894c4e5   mongo                 "docker-entrypoint.s…"   2 days ago     Up 41 hours   0.0.0.0:27017->27017/tcp, :::27017->27017/tcp                                                                                                         mongo
```