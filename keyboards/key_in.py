from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def key1():
    keyboard1 = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton('Виды самолётов', callback_data='go_to_2')
    button2 = InlineKeyboardButton('Танки', callback_data='go_to_3')
    button3 = InlineKeyboardButton('Машины', callback_data='go_to_4')
    keyboard1.add(button1, button2, button3)
    return keyboard1


def key2():
    keyboard2 = InlineKeyboardMarkup(row_width=2)
    button4 = InlineKeyboardButton('Вернуться назад', callback_data='go_to_1')
    button5 = InlineKeyboardButton('Истребители', url='https://ru.m.wikipedia.org/wiki/Истребители_(фильм)')
    button6 = InlineKeyboardButton('Истрибители-перехватчики', url='https://ru.wikipedia.org/wiki/Перехватчик')
    button7 = InlineKeyboardButton('Истребители-бомбардировщики', url='https://ru.wikipedia.org/wiki/Истребитель-бомбардировщик')
    button8 = InlineKeyboardButton('Бомбардировщики (ракетоносцы)', url='https://ru.wikipedia.org/wiki/Ту-160')
    button9 = InlineKeyboardButton('Штурмовики', url='https://ru.wikipedia.org/wiki/Штурмовик')
    button10 = InlineKeyboardButton('Разведчики', url='https://ru.wikipedia.org/wiki/Самолёт-разведчик')
    button11 = InlineKeyboardButton('Многоцелевые (предназначенные для решения нескольких задач)', url='https://en.wikipedia.org/wiki/Multirole_combat_aircraft')
    button12 = InlineKeyboardButton('Противолодочные', url='https://ru.wikipedia.org/wiki/Противолодочный_самолёт')
    button13 = InlineKeyboardButton('Военно-транспортные', url='https://en.wikipedia.org/wiki/List_of_military_transport_aircraft')
    keyboard2.add(button4, button5, button6, button7, button8, button9, button10, button11, button12, button13)
    return keyboard2


def key3():
    keyboard3 = InlineKeyboardMarkup(row_width=2)
    button14 = InlineKeyboardButton('Вернуться назад', callback_data='go_to_1')
    button15 = InlineKeyboardButton('Русские танки', url='https://ru.wikipedia.org/wiki/Список_советской_и_российской_серийной_бронетехники')
    keyboard3.add(button14, button15)
    return keyboard3


def key4():
    keyboard4 = InlineKeyboardMarkup(row_width=2)
    button16 = InlineKeyboardButton('Вернуться назад', callback_data='go_to_1')
    button17 = InlineKeyboardButton('Военные русские машины', url='https://вооружение.рф/armaments/boevye-mashiny/')
    keyboard4.add(button16, button17)
    return keyboard4


