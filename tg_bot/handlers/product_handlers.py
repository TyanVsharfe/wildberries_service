import json

import requests
from aiogram.enums import parse_mode, ParseMode
from aiogram.filters import Command, CommandObject
from aiogram import types


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
        response = requests.get(f"http://localhost:8000/api/products/{product_id}")
        if response.status_code != 200 or response.text is None:
            return await message.answer(
                f"Ошибка: база данных пуста или соединение с ней потеряно {response.status_code}")
        else:
            json_response = json.loads(response.text)
            await message.answer(f"```json\n{json.dumps(json_response, indent=4, ensure_ascii=False)} \n```", parse_mode=ParseMode.MARKDOWN)


async def cmd_get_all_products(message: types.Message, command: CommandObject):
    response = requests.get("http://localhost:8000/api/products/all")
    if response.status_code != 200 or response.text is None:
        return await message.answer(f"Ошибка: база данных пуста или соединение с ней потеряно {response.status_code}")
    else:
        await message.answer(response.text)


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
        response = requests.post(f"http://localhost:8000/api/products/{product_id}")
        if response.status_code != 200 or response.text is None:
            return await message.answer(
                f"Ошибка: база данных пуста или соединение с ней потеряно {response.status_code}")
        else:
            json_response = json.loads(response.text)
            await message.answer(f"Товар добавлен"
                                 f"```json\n{json.dumps(json_response, indent=4, ensure_ascii=False)} \n```", parse_mode=ParseMode.MARKDOWN)


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
        response = requests.delete(f"http://localhost:8000/api/products/{product_id}")
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
        response = requests.put(f"http://localhost:8000/api/products/{product_id}")
        if response.status_code != 200 or response.text is None:
            return await message.answer(
                f"Ошибка: база данных пуста или соединение с ней потеряно {response.status_code}")
        else:
            json_response = json.loads(response.text)
            await message.answer(f"Товар обновлен\n "
                                 f"```json\n{json.dumps(json_response, indent=4, ensure_ascii=False)} \n```", parse_mode=ParseMode.MARKDOWN)