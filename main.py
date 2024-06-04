from aiogram import Bot, Dispatcher, executor, types
from config import TELEGRAM_API
from keyboards.key_in import key1, key2, key3, key4


bot = Bot(token=TELEGRAM_API)
dp = Dispatcher(bot)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для того, чтобы загрузить бота'),
    ]
    await bot.set_my_commands(commands)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Нажми кнопку, чтобы перейти на виды военных самолётов и танков', reply_markup=key1())


@dp.callback_query_handler(lambda c: c.data == 'go_to_2')
async def go_to_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты перешёл на вторую клавиатуру', reply_markup=key2())


@dp.callback_query_handler(lambda c: c.data == 'go_to_3')
async def go_to_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты перешёл на третью клавиатуру', reply_markup=key3())


@dp.callback_query_handler(lambda c: c.data == 'go_to_4')
async def go_to_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты перешёл на четвёртую клавиатуру', reply_markup=key4())


@dp.callback_query_handler(lambda c: c.data == 'go_to_1')
async def go_to_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты перешёл на первую клавиатуру', reply_markup=key1())


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
