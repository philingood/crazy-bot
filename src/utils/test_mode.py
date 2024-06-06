import logging

from aiogram import Bot

import config

logger = logging.getLogger(__name__)


async def notify_admin_test_mode(bot: Bot):
    if config.TEST_MODE:
        if config.ADMIN_ID is None:
            logger.error("ADMIN_ID not set in config.py")
        else:
            ADMIN_ID = int(config.ADMIN_ID)
            await bot.send_message(
                chat_id=ADMIN_ID, text="crazy-bot: Бот запущен в тестовом режиме"
            )
        raise SystemExit(0)
