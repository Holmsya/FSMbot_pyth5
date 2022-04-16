from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_upload = KeyboardButton('/upload')
button_test1 = KeyboardButton('Remove keyboard')
button_test2 = KeyboardButton('test2')
button_other = KeyboardButton('Other')

button_contact = KeyboardButton('Send contact', request_contact=True)
button_gps = KeyboardButton('Send location', request_location=True)


kb_main = ReplyKeyboardMarkup(resize_keyboard=True)    # создаём объект клавиатуры
# kb_main.add(button_upload).add(button_test1).insert(button_test2)  # собираем клавиатуру из кнопок
kb_main.add(button_upload).row(button_test1, button_test2).add(button_other)

button_cancel = KeyboardButton('cancel')

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(button_cancel)

kb_other = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_other.row(button_contact, button_gps)
