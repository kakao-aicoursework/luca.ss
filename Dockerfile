FROM python:3.9.18-bookworm

RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip3 install -r requirements.txt
RUN apt update
RUN apt install nodejs -y
RUN curl -fsSL https://bun.sh/install | bash -s -- bun-v0.6.9

EXPOSE 3000
EXPOSE 8000
# WORKDIR /app/kakaosync-bot
# CMD pc init
# CMD pc run --port 3000 --loglevel debug