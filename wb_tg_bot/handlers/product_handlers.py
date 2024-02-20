import json
import os

import requests
from aiogram.enums import ParseMode
from aiogram.filters import CommandObject
from aiogram import types
from aiogram.types import FSInputFile

from wb_tg_bot.config import settings


async def cmd_get_product(message: types.Message, command: CommandObject):
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы (id продукта)"
        )
        return
    product_arg = command.args.split()[0]
    product_id = 0
    try:
        product_id = int(product_arg)
    except ValueError:
        return await message.answer("Ошибка: не переданы аргументы или они не в том формате (<product_id:int>)")
    finally:
        response = requests.get(f"{settings.API_SERVER}/api/products/{product_id}")
        if response.status_code != 200 or response.text is None:
            return await message.answer(
                f"Ошибка: база данных пуста или соединение с ней потеряно {response.status_code}")
        else:
            json_response = json.loads(response.text)
            await message.answer(f"```json\n{json.dumps(json_response, indent=4, ensure_ascii=False)} \n```",
                                 parse_mode=ParseMode.MARKDOWN)


async def cmd_get_all_products(message: types.Message):
    response = requests.get(f"{settings.API_SERVER}/api/products/all")
    if response.status_code != 200 or response.text is None:
        return await message.answer(f"Ошибка: база данных пуста или соединение с ней потеряно {response.status_code}")
    else:
        json_response = json.loads(response.text)
        with open("all_db.json", 'w', encoding='utf-8') as f:
            f.write(json.dumps(json_response, indent=4, ensure_ascii=False))
        db = FSInputFile("all_db.json")
        await get_db_file(message, db)
        os.remove("all_db.json")
        await message.answer(f"Некоторые записи из бд, абсолютно все записи в файле выше\n"
                             f"```json\n{json.dumps(json_response[:5], indent=4, ensure_ascii=False)} \n```",
                             parse_mode=ParseMode.MARKDOWN)


async def get_db_file(message: types.Message, db: FSInputFile):
    await message.answer_document(document=db, caption="Файл со всеми записями из базы данных")


async def cmd_add_product(message: types.Message, command: CommandObject):
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы (id продукта)"
        )
        return
    product_arg = command.args.split()[0]
    product_id = 0
    try:
        product_id = int(product_arg)
    except ValueError:
        return await message.answer("Ошибка: не переданы аргументы или они не в том формате (<product_id:int>)")
    finally:
        print(f"{settings.API_SERVER}/api/products/{product_id}")
        response = requests.post(f"{settings.API_SERVER}/api/products/{product_id}")
        if response.status_code != 200 or response.text is None:
            return await message.answer(
                f"Ошибка: база данных пуста или соединение с ней потеряно {response.status_code}")
        else:
            json_response = json.loads(response.text)
            await message.answer(f"Товар добавлен"
                                 f"```json\n{json.dumps(json_response, indent=4, ensure_ascii=False)} \n```",
                                 parse_mode=ParseMode.MARKDOWN)


async def cmd_delete_product(message: types.Message, command: CommandObject):
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы (id продукта)"
        )
        return
    product_arg = command.args.split()[0]
    product_id = 0
    try:
        product_id = int(product_arg)
    except ValueError:
        return await message.answer("Ошибка: не переданы аргументы или они не в том формате (<product_id:int>)")
    finally:
        response = requests.delete(f"{settings.API_SERVER}/api/products/{product_id}")
        if response.status_code != 200 or response.text is None:
            return await message.answer(
                f"Ошибка: база данных пуста или соединение с ней потеряно {response.status_code}")
        else:
            json_response = json.loads(response.text)
            await message.answer("Запись удалена")


async def cmd_update_product(message: types.Message, command: CommandObject):
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы (id продукта)"
        )
        return
    product_arg = command.args.split()[0]
    product_id = 0
    try:
        product_id = int(product_arg)
    except ValueError:
        return await message.answer("Ошибка: не переданы аргументы или они не в том формате (<product_id:int>)")
    finally:
        response = requests.put(f"{settings.API_SERVER}/api/products/{product_id}")
        if response.status_code != 200 or response.text is None:
            return await message.answer(
                f"Ошибка: база данных пуста или соединение с ней потеряно {response.status_code}")
        else:
            json_response = json.loads(response.text)
            await message.answer(f"Товар обновлен\n "
                                 f"```json\n{json.dumps(json_response, indent=4, ensure_ascii=False)} \n```",
                                 parse_mode=ParseMode.MARKDOWN)
