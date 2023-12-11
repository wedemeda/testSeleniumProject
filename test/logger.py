import logging
from config import token, users
from tg_log_handler import TelegramBotHandler

file_log = logging.FileHandler('Log.log', encoding='utf-8')
console_out = logging.StreamHandler()
tg_out = TelegramBotHandler(token, users)

logging.basicConfig(handlers=(file_log, console_out, tg_out),
                    encoding='utf-8',
                    format='[%(asctime)s | %(levelname)s]: %(message)s',
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.INFO)

logger = logging.getLogger('my_logger')
