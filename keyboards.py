from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from static import links


inl_btn1 = InlineKeyboardButton('Медиа', callback_data='inl_btn1')
inl_btn2 = InlineKeyboardButton(
    'Посмотреть код бота',
    url=links['repository']
)
inl_btn3 = InlineKeyboardButton('Фото', callback_data='inl_btn3')
inl_btn4 = InlineKeyboardButton('Войсы', callback_data='inl_btn4')
inl_btn5 = InlineKeyboardButton('Назад', callback_data='inl_btn5')
inl_btn6 = InlineKeyboardButton('Селфи', callback_data='inl_btn6')
inl_btn7 = InlineKeyboardButton('Школьные', callback_data='inl_btn7')
inl_btn8 = InlineKeyboardButton('Про GPT', callback_data='inl_btn8')
inl_btn9 = InlineKeyboardButton('Про SQL', callback_data='inl_btn9')
inl_btn10 = InlineKeyboardButton('Про любовь❤️', callback_data='inl_btn10')
inl_btn11 = InlineKeyboardButton('Назад', callback_data='inl_btn11')

inl_kb = InlineKeyboardMarkup(row_width=1).add(inl_btn1, inl_btn2)
inl_kb2 = InlineKeyboardMarkup(row_width=1).add(inl_btn3, inl_btn4, inl_btn5)
inl_kb3 = InlineKeyboardMarkup(row_width=1).add(inl_btn6, inl_btn7, inl_btn11)
inl_kb4 = InlineKeyboardMarkup(row_width=1).add(inl_btn8, inl_btn9, inl_btn10,
                                                inl_btn11)
