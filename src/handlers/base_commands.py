from random import randint

import config
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, InlineKeyboardButton, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import logger
from docker import from_env

try:
    docker_client = from_env()
except Exception as e:
    logger.error(f"Error while connecting to docker: {e}")

router = Router()

ADMIN_ID: str = str(config.ADMIN_ID)


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.reply(
        "Привет!\nИспользуй эти команды для общения с ботом:\n/help - справка\n/pay - оплата тарифа\n/status - статус подписки\n/random"
    )


@router.message(Command("help"))
async def cmd_help(message: Message):
    registered_users = ["6872483557"]
    CHAT_ID = str(message.chat.id)
    if CHAT_ID == ADMIN_ID:
        await message.reply(
            "Привет, админ!\nВот список доступных команд:\n/help - справка\n/pay - оплата тарифа\n/status - статус подписки\n/service_status - статус сервисов\n/random - генерация случайного числа"
        )
    elif CHAT_ID in registered_users:
        await message.reply(
            "Привет!\nИспользуй эти команды для общения с ботом:\n/help - справка\n/pay - оплата тарифа\n/status - статус подписки\n/service_status - статус сервисов\n/random - генерация случайного числа"
        )
    else:
        await message.reply("Зарегистрируйтесь прежде чем использовать бота")


@router.message(Command("random"))
async def cmd_random(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.as_markup(),
    )


@router.callback_query(F.data == "random_value")
async def send_random_value(callback: CallbackQuery):
    await callback.message.answer(str(randint(1, 10)))
    await callback.answer()


@router.message(Command("service_status"))
async def cmd_service_status(message: Message):
    containers = docker_client.containers.list()
    status_message = "Статус контейнеров:\n"
    for container in containers:
        status_message += f"{container.name}: {container.status}\n"
    await message.reply(status_message)
