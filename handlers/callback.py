from aiogram import Bot, Router, F
from aiogram.types import CallbackQuery

import config
from keyboards.callback_data import PostRequest

callback_router = Router()


@callback_router.callback_query(PostRequest.filter(F.button == 'accept'))
async def accept_post_message(callback: CallbackQuery, bot: Bot):
    if callback.message.photo:
        await bot.send_photo(
            chat_id=config.CHANNEL_TG_ID,
            photo=callback.message.photo[-1].file_id,
            caption=callback.message.caption,
            caption_entities=callback.message.caption_entities,
            protect_content=True,
        )
    elif callback.message.video:
        await bot.send_video(
            chat_id=config.CHANNEL_TG_ID,
            video=callback.message.video.file_id,
            caption=callback.message.caption,
            caption_entities=callback.message.caption_entities,
            protect_content=True,
        )
    else:
        await bot.send_message(
            chat_id=config.CHANNEL_TG_ID,
            text=callback.message.text,
            entities=callback.message.entities,
            protect_content=True,
        )
    await bot.delete_message(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
    )
    await callback.answer(
        text='Сообщение отправлено в канал!',
    )


@callback_router.callback_query(PostRequest.filter(F.button == 'cancel'))
async def reject_post_message(callback: CallbackQuery, callback_data: PostRequest, bot: Bot):
    msg = 'Ваше сообщение отклонено модератором\nПричина:\n'
    if callback_data.reason == 'personal':
        msg += 'Персональные данные'
    elif callback_data.reason == 'company':
        msg += 'Название компании/организации'
    elif callback_data.reason == 'religion':
        msg += 'Упоминание религии/нации/политики'
    elif callback_data.reason == 'crime':
        msg += 'Уголовная ответственность'
    elif callback_data.reason == 'advertising':
        msg += 'Несанкционированная реклама'
    elif callback_data.reason == 'other':
        msg += 'Не указана'
    await callback.answer(
        text='Сообщения отклонено!',
    )
    await bot.delete_message(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
    )
    await bot.send_message(
        chat_id=callback_data.author_id,
        text=msg,
    )
