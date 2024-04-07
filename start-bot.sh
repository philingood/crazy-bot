#!/bin/sh

git clone https://github.com/philingood/crazy-bot.git

cd crazy-bot/
rm -rf .git/
vim .env

docker compose up --build -d