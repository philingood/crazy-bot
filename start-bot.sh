#!/bin/sh

cd /root/
git clone https://github.com/philingood/crazy-vpn-bot.git

cd crazy-vpn-bot/
rm -rf .git/
vim .env

docker compose up --build -d