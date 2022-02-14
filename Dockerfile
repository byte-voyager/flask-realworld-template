FROM python:3.8-buster

COPY requirements.txt /service/
WORKDIR /service

RUN printf 'deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free \n\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free \n\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free \n\
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free' > /etc/apt/sources.list

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "Asia/Shanghai" > /etc/timezone \
&& apt-get update
RUN pip install -i 'https://pypi.douban.com/simple' -r requirements.txt