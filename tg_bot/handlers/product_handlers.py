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
    await message.answer(f"Id вашего продукта! {product_id}")


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
    await message.answer(f"Id вашего продукта! {product_id}")


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
    await message.answer(f"Id вашего продукта! {product_id}")


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
    await message.answer(f"Id вашего продукта! {product_id}")