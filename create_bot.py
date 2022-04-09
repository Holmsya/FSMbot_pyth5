from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage    # позволяет хранить данные в ОЗУ

API_TOKEN = '5191483081:AAHFy4leaeuA_wWEP0HdKgs7smimsE6oYLA'

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
