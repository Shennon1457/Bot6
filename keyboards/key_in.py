from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def key1():
    keyboard1 = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton('Виды самолётов', callback_data='go_to_2')
    button13 = InlineKeyboardButton('Танки', callback_data='go_to_3')
    button17 = InlineKeyboardButton('Машины', callback_data='go_to_4')
    keyboard1.add(button1, button13, button17)
    return keyboard1


def key2():
    keyboard2 = InlineKeyboardMarkup(row_width=2)
    button3 = InlineKeyboardButton('Вернуться назад', callback_data='go_to_1')
    button4 = InlineKeyboardButton('Истребители', url='https://ru.m.wikipedia.org/wiki/Истребители_(фильм)')
    button5 = InlineKeyboardButton('Истрибители-перехватчики', url='https://ru.wikipedia.org/wiki/Перехватчик')
    button6 = InlineKeyboardButton('Истребители-бомбардировщики', url='https://ru.wikipedia.org/wiki/Истребитель-бомбардировщик')
    button7 = InlineKeyboardButton('Бомбардировщики (ракетоносцы)', url='https://ru.wikipedia.org/wiki/Ту-160')
    button8 = InlineKeyboardButton('Штурмовики', url='https://ru.wikipedia.org/wiki/Штурмовик')
    button9 = InlineKeyboardButton('Разведчики', url='https://ru.wikipedia.org/wiki/Самолёт-разведчик')
    button10 = InlineKeyboardButton('Многоцелевые (предназначенные для решения нескольких задач)', url='https://en.wikipedia.org/wiki/Multirole_combat_aircraft')
    button11 = InlineKeyboardButton('Противолодочные', url='https://ru.wikipedia.org/wiki/Противолодочный_самолёт')
    button12 = InlineKeyboardButton('Военно-транспортные', url='https://en.wikipedia.org/wiki/List_of_military_transport_aircraft')
    keyboard2.add(button3, button4, button5, button6, button7, button8, button9, button10, button11, button12)
    return keyboard2


def key3():
    keyboard3 = InlineKeyboardMarkup(row_width=2)
    button23 = InlineKeyboardButton('Вернуться назад', callback_data='go_to_1')
    button14 = InlineKeyboardButton('Русские танки', url='https://ru.wikipedia.org/wiki/Список_советской_и_российской_серийной_бронетехники')
    keyboard3.add(button23, button14)
    return keyboard3


def key4():
    keyboard4 = InlineKeyboardMarkup(row_width=2)
    button15 = InlineKeyboardButton('Вернуться назад', callback_data='go_to_1')
    button16 = InlineKeyboardButton('Военные русские машины', url='https://вооружение.рф/armaments/boevye-mashiny/')
    keyboard4.add(button15, button16)
    return keyboard4


