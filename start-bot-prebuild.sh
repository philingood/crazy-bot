#!/bin/sh

mkdir crazy-vpn-bot && cd crazy-vpn-bot

vim .env

docker pull philingood/crazy-vpn-bot
docker run -d --restart always philingood/crazy-vpn-bot
