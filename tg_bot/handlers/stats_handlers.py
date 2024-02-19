import json
from io import BytesIO

import requests
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandObject
from aiogram import types
from aiogram.types import FSInputFile


async def cmd_get_product_history(message: types.Message, command: CommandObject):
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
        response = requests.get(f"http://localhost:8000/api/stats/{product_id}/graphics")
        if response.status_code != 200 or response.text is None:
            return await message.answer(
                f"Ошибка: база данных пуста или соединение с ней потеряно {response.status_code}")
        else:
            # Создаем объект BytesIO из байтов изображения
            image_bytes = response.content
            image_io = BytesIO(image_bytes)

            # Сохраняем изображение в файл
            with open('image.png', 'wb') as f:
                f.write(image_io.read())
            img = FSInputFile("image.png")
            await message.answer_photo(photo=img)
            image_io.close()


async def cmd_get_products_category_history(message: types.Message, command: CommandObject):
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
        response = requests.get(f"http://localhost:8000/api/stats/{product_id}/categories/graphics")
        if response.status_code != 200 or response.text is None:
            return await message.answer(
                f"Ошибка: база данных пуста или соединение с ней потеряно {response.status_code}")
        else:
            # Создаем объект BytesIO из байтов изображения
            image_bytes = response.content
            image_io = BytesIO(image_bytes)

            # Сохраняем изображение в файл
            with open('image.png', 'wb') as f:
                f.write(image_io.read())
            img = FSInputFile("image.png")
            await message.answer_photo(photo=img)
            image_io.close()


async def cmd_get_product_min_max(message: types.Message, command: CommandObject):
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
        response = requests.get(f"http://localhost:8000/api/stats/{product_id}/min-max")
        if response.status_code != 200 or response.text is None:
            return await message.answer(
                f"Ошибка: база данных пуста или соединение с ней потеряно {response.status_code}")
        else:
            json_response = json.loads(response.text)
            await message.answer(f"```json\n{json.dumps(json_response, indent=4, ensure_ascii=False)} \n```",
                                 parse_mode=ParseMode.MARKDOWN)


async def cmd_get_products_count(message: types.Message):
    response = requests.get(f"http://localhost:8000/api/stats/count")
    if response.status_code != 200 or response.text is None:
        return await message.answer(
            f"Ошибка: база данных пуста или соединение с ней потеряно {response.status_code}")
    else:
        json_response = json.loads(response.text)
        await message.answer(f"```json\n{json.dumps(json_response, indent=4, ensure_ascii=False)} \n```",
                             parse_mode=ParseMode.MARKDOWN)


async def cmd_get_products_categories_count(message: types.Message):
    response = requests.get(f"http://localhost:8000/api/stats/categories/count")
    if response.status_code != 200 or response.text is None:
        return await message.answer(
            f"Ошибка: база данных пуста или соединение с ней потеряно {response.status_code}")
    else:
        json_response = json.loads(response.text)
        await message.answer(f"```json\n{json.dumps(json_response, indent=4, ensure_ascii=False)} \n```",
                             parse_mode=ParseMode.MARKDOWN)
