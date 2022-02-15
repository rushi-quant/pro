FROM python:3.9.10
RUN apt update -y
RUN apt install vim -y
RUN git clone https://github.com/rushi-quant/pro.git /rushiquant
WORKDIR /rushiquant
RUN python -m pip install --upgrade pip
RUN pip3 install -r docs/requirements.txt
