FROM python:3.12.1-bookworm

COPY requirements-prod.txt /service/
WORKDIR /service

#RUN sed -i 's@deb.debian.org@mirrors.tuna.tsinghua.edu.cn@g' /etc/apt/sources.list.d/debian.sources
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "Asia/Shanghai" > /etc/timezone
RUN pip install -r requirements.txt
