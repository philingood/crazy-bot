from g4f.client import Client
from config import OPENAI_SYSTEM_MESSAGE


SYSTEMMSG = OPENAI_SYSTEM_MESSAGE
 

def ask_gpt(client=Client()):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": SYSTEMMSG},
                  {"role": "user", "content": "Hello"}]
    )
    return response.choices[0].message.content