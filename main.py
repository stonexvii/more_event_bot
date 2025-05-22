from aiogram import Bot, Dispatcher
from aiogram.types import Message

import asyncio

import config
import misc
from handlers import routers


async def start_bot():
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    dp.startup.register(misc.on_start)
    dp.shutdown.register(misc.on_shutdown)
    dp.include_routers(*routers)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        pass
