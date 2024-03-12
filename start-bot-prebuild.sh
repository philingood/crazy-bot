#!/bin/sh

mkdir crazy-vpn-bot && cd crazy-vpn-bot

vim .env

docker pull philingood/crazy-vpn-bot

docker run \
    --name crazy-vpn-bot \
    --env-file .env \
    --restart=always \
    -d \
    philingood/crazy-vpn-bot

rm .env
cd ..
rm -rf crazy-vpn-bot