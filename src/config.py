import logging
import os

from dotenv import load_dotenv

# import argparse
# from sys import exception

load_dotenv()

# parser = argparse.ArgumentParser(description="Настройки бота")
# parser.add_argument(
#     "--log-level",
#     default="INFO",
#     choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
#     help="Уровень логирования (по умолчанию: INFO)",
# )
try:
    args = parser.parse_args()
    log_level = getattr(logging, args.log_level.upper(), logging.INFO)
except NameError:
    args = None
    log_level = logging.INFO

logging.basicConfig(
    level=log_level, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

TEST = int(os.getenv("TEST", 0))
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_TOKEN_TEST = os.getenv("BOT_TOKEN_TEST")
ADMIN_ID = os.getenv("ADMIN_ID")
PAY_TOKEN = os.getenv("PAY_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_SYSTEM_MESSAGE = os.getenv("OPENAI_SYSTEM_MESSAGE")
DATABASE_FILE = os.getenv("DATABASE_FILE")

TEST_MODE = False

if not DATABASE_FILE:
    logger.error("Error while reading config: DATABASE_FILE is missing")

if BOT_TOKEN_TEST:
    logger.info("Running in test mode")
    BOT_TOKEN = BOT_TOKEN_TEST
    if TEST == 1:
        TEST_MODE = True
elif not BOT_TOKEN:
    raise ValueError("Error while reading config: BOT_TOKEN is missing")

if not ADMIN_ID:
    logging.warning("Admin ID not found. Bot will work w/o admin rights.")
if not OPENAI_API_KEY:
    logging.warning("OpenAI API key not found. AI will not work.")
