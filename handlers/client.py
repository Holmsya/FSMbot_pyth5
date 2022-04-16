from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from keyboards import kb_main, kb_cancel, kb_other


class FSMClient(StatesGroup):
    photo = State()
    name = State()
    description = State()


async def send_welcome(message: types.Message):
    await message.reply("Hello!", reply_markup=kb_main)


async def function_keyboard(message: types.Message):
    await message.reply('Func', reply_markup=kb_other)


async def remove_keyboard(message: types.Message):
    await message.reply('Keyboard removed', reply_markup=ReplyKeyboardRemove())


async def upload(message: types.Message):
    await FSMClient.photo.set()
    await message.reply("Upload photo", reply_markup=kb_cancel)


async def upload_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMClient.next()
    await message.reply("Insert name")


async def insert_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMClient.next()
    await message.reply("Insert description")


async def insert_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        await message.answer(str(data), reply_markup=kb_main)
    await state.finish()


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK", reply_markup=kb_main)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(function_keyboard, Text(equals='Other', ignore_case=True))
    dp.register_message_handler(remove_keyboard, Text(equals='Remove keyboard', ignore_case=True))
    dp.register_message_handler(upload, commands=['upload'], state=None)
    dp.register_message_handler(upload_photo, content_types=['photo'], state=FSMClient.photo)
    dp.register_message_handler(cancel, commands=['cancel'], state='*')
    dp.register_message_handler(cancel, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(insert_name, state=FSMClient.name)
    dp.register_message_handler(insert_description, state=FSMClient.description)

