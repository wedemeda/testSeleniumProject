import telebot
from logging import Handler, LogRecord


class TelegramBotHandler(Handler):
    def __init__(self, token: str, chat_id: list):
        super().__init__()
        self.token = token
        self.chat_id = chat_id

    def emit(self, record: LogRecord):
        bot = telebot.TeleBot(self.token)
        for chat_id in self.chat_id:
            bot.send_message(
                chat_id,
                self.format(record))
