#!/bin/sh

mkdir crazy-bot && cd crazy-bot

vim .env

docker pull philingood/crazy-bot

docker run \
    --name crazy-bot \
    --env-file .env \
    --restart=always \
    -d \
    philingood/crazy-bot
