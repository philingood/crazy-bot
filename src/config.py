from dotenv import load_dotenv
import os

load_dotenv()

try:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    PAY_TOKEN = os.getenv('PAY_TOKEN')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    ADMIN_ID = os.getenv('ADMIN_ID')
    SYSTEM_MESSAGE = os.getenv('SYSTEM_MESSAGE')

except (TypeError, ValueError) as ex:
    print("Error while reading config:", ex)
