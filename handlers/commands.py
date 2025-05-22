from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject

import config
from messages import BotMessage, MessagePath

command_router = Router()


@command_router.message(Command('start'))
async def command_start(message: Message):
    msg = BotMessage(MessagePath.START).text
    await message.answer(
        text=msg if msg else 'None',
    )


@command_router.message(Command('rules'))
async def command_rules(message: Message):
    msg = BotMessage(MessagePath.RULES).text
    await message.answer(
        text=msg if msg else 'None',
    )


@command_router.message(Command('help'))
async def command_help(message: Message):
    msg = BotMessage(MessagePath.HELP).text
    await message.answer(
        text=msg if msg else 'None',
    )


@command_router.message(Command('set'), F.from_user.id == config.ADMIN_TG_ID)
async def command_set(message: Message, command: CommandObject):
    path, text = command.args.split('\n', 1)
    if path == 'start':
        path = MessagePath.START
    elif path == 'rules':
        path = MessagePath.RULES
    elif path == 'help':
        path = MessagePath.HELP
    BotMessage.write_file(path, text)
    await message.answer(
        text=f'{path.name} изменен!'
    )
