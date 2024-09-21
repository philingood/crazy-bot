import config
from aiogram import Bot, Dispatcher
from handlers import base_commands, payments, simple_answers

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

dp.include_routers(base_commands.router, payments.router, simple_answers.router)
