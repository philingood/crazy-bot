from aiogram import Router, F
from aiogram.types import Message
from ask_gpt import ask_g4f

router = Router()


@router.message(F.text)
async def message_with_text(message: Message):
    response = ask_g4f(message.text)
    await message.reply(response)


@router.message(F.sticker)
async def message_with_sticker(message: Message):
    await message.answer("Это стикер!")


@router.message(F.animation)
async def message_with_gif(message: Message):
    await message.answer("Это GIF!")
