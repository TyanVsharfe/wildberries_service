import asyncio
import logging

import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandObject

from tg_bot.handlers import product_handlers

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6797248824:AAHnYKuwxGGFJ1OB2HYn5sM9vmstiAZXM_4")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Здравствуйте! Чтобы увидеть все доступные команды введите /help")


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await bot.set_my_commands([
        aiogram.types.BotCommand("start", "Начать работу"),
        aiogram.types.BotCommand("help", "it is help command...")
    ])
    await message.answer("Hello!")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    dp.message.register(product_handlers.cmd_get_product, Command("get_product", prefix="!"))
    dp.message.register(product_handlers.cmd_add_product, Command("add_product", prefix="!"))
    dp.message.register(product_handlers.cmd_delete_product, Command("delete_product", prefix="!"))
    dp.message.register(product_handlers.cmd_update_product, Command("update_product", prefix="!"))
    asyncio.run(main())