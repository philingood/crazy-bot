import logging
import os

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

TEST = int(os.getenv("TEST", 0))
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_TOKEN_TEST = os.getenv("BOT_TOKEN_TEST")
ADMIN_ID = os.getenv("ADMIN_ID")
PAY_TOKEN = os.getenv("PAY_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_SYSTEM_MESSAGE = os.getenv("OPENAI_SYSTEM_MESSAGE")

TEST_MODE = False

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
    OPENAI_API_KEY = None
    OPENAI_SYSTEM_MESSAGE = None
