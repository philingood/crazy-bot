from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from random import randint

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.reply(
        "Привет!\n Используй эти команды для общения с ботом:\n /help - справка\n /pay - оплата тарифа\n /status - статус подписки\n /random")


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.reply(
        "Привет!\n Используй эти команды для общения с ботом:\n /help - справка\n /pay - оплата тарифа\n /status - статус подписки\n /random")


@router.message(Command("random"))
async def cmd_random(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.as_markup()
    )


@router.callback_query(F.data == "random_value")
async def send_random_value(callback: CallbackQuery):
    await callback.message.answer(str(randint(1, 10)))
    await callback.answer()
