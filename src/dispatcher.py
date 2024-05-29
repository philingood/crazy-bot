import logging
from aiogram import Bot, Dispatcher
from handlers import base_commands, simple_answers, payments
import config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# if not config.BOT_TOKEN:
#     exit("No token provided")

# bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

# dp.include_routers(base_commands.router, payments.router)
dp.include_routers(base_commands.router, payments.router, simple_answers.router)
