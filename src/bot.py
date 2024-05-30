import asyncio
from dispatcher import dp, bot
import test.test_mode as tm


async def main():
    await bot.delete_webhook(drop_pending_updates=False)
    await tm.notify_admin_test_mode(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
