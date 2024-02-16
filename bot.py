import asyncio
import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from handlers import base_commands, simple_answers, payments

load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

PAY_TOKEN = os.getenv('PAY_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


async def main():
    logging.basicConfig(level=logging.INFO)

    # dp.include_routers(base_commands.router, payments.router)
    dp.include_routers(base_commands.router, payments.router, simple_answers.router)

    await bot.delete_webhook(drop_pending_updates=False)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
