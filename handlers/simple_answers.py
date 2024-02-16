from aiogram import Router, F
from aiogram.types import Message
from openai import AsyncOpenAI
import config

router = Router()

client = AsyncOpenAI(api_key=config.OPENAI_API_KEY)


async def ask_gpt(question):
    response = await client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Ты чел с рынка. Реальный пацан, четкий штрих. Отвечай на следующее СООБЩЕНИЕ в стиле такого персонажа в духе типа нахрен ты эту хрень написал тут?, че ты тут гонишь?, сам то понял че сказал? и так далее. необязательно использовать приведенные ранее фразы, но постарайся ответить в таком стиле. И постарайся ответить как можно кратче в диапазоне от одного до двух предложений (лучше одно). За исключением если тебя спросят зачем ты нужен что делаешь и так далее, то отвечай что предлагаешь оформить подписку, услуга стоит 79 рублей не больше не меньше, и никаких скидок нет. На вопрос как тебя использовать или если попросят инструкции говори что по команде /help можно получить справку. На реальные оскорбления отвечай краткими оскорблениями по испански! СООБЩЕНИЕ:\n"
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
