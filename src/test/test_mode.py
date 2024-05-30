from aiogram import Bot
from utils.docker_util import stop_docker_container
import config


async def notify_admin_test_mode(bot: Bot):
    if config.TEST_MODE:
        ADMIN_ID = int(config.ADMIN_ID)
        await bot.send_message(chat_id=ADMIN_ID, text="Бот запущен в тестовом режиме")
        # await stop_docker_container()
