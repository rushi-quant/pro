# docker centos8 没有centos8的镜像了

# FROM centos
# RUN yum install vim -y
# RUN yum install python39 -y
# WORKDIR /rushiquant
# COPY . .
# RUN rm -rf .git
# RUN rm -rf venv
# RUN pip3 install -r docs/requirements.txt
# RUN cp -rf /usr/bin/python3 /usr/bin/python
# RUN cp -rf /usr/bin/pip3 /usr/bin/pip

# docker centos7 公开版
# centos7 python3.6.8 没有websockets 10.1版本,只有9.1

# FROM centos:centos7
# RUN yum install vim -y
# RUN yum install python3 -y
# WORKDIR /rushiquant
# COPY . .
# RUN rm -rf .git
# RUN rm -rf venv
# RUN pip3 install -r docs/requirements.txt
# RUN cp -rf /usr/bin/python3 /usr/bin/python
# RUN cp -rf /usr/bin/pip3 /usr/bin/pip

# docker centos7 加密版
# centos7 python3.6.8 没有websockets 10.1版本,只有9.1

FROM centos:centos7
RUN yum install vim -y
RUN yum install python3 -y
RUN yum install git -y
RUN git clone https://github.com/rushi-quant/pro.git /rushiquant
WORKDIR /rushiquant
RUN pip3 install -r docs/requirements.txt

# ubuntu 公开版
# docker python:3.9.10 但是这个包比较大

# FROM python:3.9.10
# RUN apt update -y
# RUN apt install vim -y
# WORKDIR /rushiquant
# COPY . .
# RUN rm -rf .git
# RUN rm -rf venv
# RUN python -m pip install --upgrade pip
# RUN pip3 install -r docs/requirements.txt

# ubuntu 加密版
# 但 python 会[python3] <defunct>，进程删不掉

# FROM python:3.9.10
# RUN apt update -y
# RUN apt install vim -y
# RUN git clone https://github.com/rushi-quant/pro.git /rushiquant
# WORKDIR /rushiquant
# RUN python -m pip install --upgrade pip
# RUN pip3 install -r docs/requirements.txt
