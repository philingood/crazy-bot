import logging

import config
from aiogram import Bot, Dispatcher
from handlers import base_commands, payments, simple_answers

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

dp.include_routers(base_commands.router, payments.router, simple_answers.router)
