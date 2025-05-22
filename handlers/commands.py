from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

import text

command_router = Router()


@command_router.message(Command('start'))
async def command_start(message: Message):
    await message.answer(
        text=text.message_start,
    )


@command_router.message(Command('rules'))
async def command_rules(message: Message):
    await message.answer(
        text=text.message_rules,
    )


@command_router.message(Command('help'))
async def command_help(message: Message):
    await message.answer(
        text=text.message_help,
    )
