from aiogram import Router, F
from aiogram.types import Message
from openai import AsyncOpenAI
import config

router = Router()

client = AsyncOpenAI(api_key=config.OPENAI_API_KEY)
OPENAI_SYSTEM_MESSAGE = config.OPENAI_SYSTEM_MESSAGE


async def ask_gpt(question):
    response = await client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": OPENAI_SYSTEM_MESSAGE
            },
            {
                "role": "user",
                "content": question
            }
        ],
        model="gpt-3.5-turbo",
        max_tokens=100,
        temperature=0.7
    )
    return response.choices[0].message.content


@router.message(F.text)
async def message_with_text(message: Message):
    response = await ask_gpt(message.text)
    await message.reply(response)


@router.message(F.sticker)
async def message_with_sticker(message: Message):
    await message.answer("Это стикер!")


@router.message(F.animation)
async def message_with_gif(message: Message):
    await message.answer("Это GIF!")
