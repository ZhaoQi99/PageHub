FROM python:3.12

RUN sed -i 's@deb.debian.org@mirrors.tuna.tsinghua.edu.cn@g' /etc/apt/sources.list.d/debian.sources
RUN apt update
RUN apt install vim tree -y

WORKDIR /app
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN playwright install
RUN playwright install-deps

ADD . .
RUN pip install .

EXPOSE 8001
CMD ["/bin/bash", "-c", "pagesaver init;pagesaver server"]