from telebot import types

def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
    btn1 = types.KeyboardButton('Add link')
    btn2 = types.KeyboardButton('Remove link')
    btn3 = types.KeyboardButton('Test menu')
    markup.add(btn1, btn2, btn3)
    return markup