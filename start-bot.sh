#!/bin/sh

cd /root/
git clone https://github.com/philingood/crazy-vpn-bot.git
cd crazy-vpn-bot/
rm -rf .git/
docker compose up --build