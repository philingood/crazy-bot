from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from config import logger, DB_FILE

from db.db import DataBase
from db.model import Inbound, User

router = Router()


@router.message(Command("status"))
async def cmd_status(message: Message):
    if DB_FILE:
        user_id = message.chat.id
        logger.info(user_id)
        db = DataBase(DB_FILE)
        inbound = Inbound(db.get_client_by_tgid(user_id)[0])
        client = User(inbound.settings["clients"][0])
        logger.info("Client status recived")

        await message.answer(f"{client}")
    else:
        await message.answer("Error: No connection to database")
