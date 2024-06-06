from config import OPENAI_API_KEY, OPENAI_SYSTEM_MESSAGE
from g4f.client import Client
from openai import AsyncOpenAI

SYSTEMMSG = str(OPENAI_SYSTEM_MESSAGE)


def ask_g4f(message: str, client=Client()) -> str | None:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEMMSG},
            {"role": "user", "content": message},
        ],
    )
    if response.choices[0].message.content:
        if "sorry," in response.choices[0].message.content:
            return "Мне нечего сказать…"
        else:
            return response.choices[0].message.content
    return "Мне нечего сказать…"


async def ask_gpt(question):
    client = AsyncOpenAI(api_key=OPENAI_API_KEY)
    response = await client.chat.completions.create(
        messages=[
            {"role": "system", "content": SYSTEMMSG},
            {"role": "user", "content": question},
        ],
        model="gpt-3.5-turbo",
        max_tokens=100,
        temperature=0.7,
    )
    return response.choices[0].message.content
