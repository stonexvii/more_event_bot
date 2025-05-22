from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import config
from .fsm_states import AnyMessage
from keyboards import *

any_router = Router()


@any_router.channel_post()
async def any_post(message: Message):
    print(message.chat.id)
    # print(message.from_user.id)


@any_router.message()
async def any_message(message: Message, bot: Bot, state: FSMContext):
    await state.set_state(AnyMessage.catch)
    # for key, item in dict(message).items():
    #     if item:
    #         print(key, item)
    await state.update_data(**dict(message))
    if message.video:
        await bot.send_video(
            chat_id=config.ADMIN_TG_ID,
            video=message.video.file_id,
            caption=message.caption,
            caption_entities=message.caption_entities,
            protect_content=True,
            reply_markup=ikb_confirm(message.from_user.id),
        )
    elif message.photo:
        await bot.send_photo(
            chat_id=config.ADMIN_TG_ID,
            photo=message.photo[-1].file_id,
            caption=message.caption,
            caption_entities=message.caption_entities,
            protect_content=True,
            reply_markup=ikb_confirm(message.from_user.id),
        )
    elif message.text:
        await bot.send_message(
            chat_id=config.ADMIN_TG_ID,
            text=message.text,
            entities=message.entities,
            protect_content=True,
            reply_markup=ikb_confirm(message.from_user.id),
        )
    else:
        await message.answer(
            text='Данное сообщение нельзя переслать',
        )
    await bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id,
    )
