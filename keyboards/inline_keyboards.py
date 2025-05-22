from aiogram.utils.keyboard import InlineKeyboardBuilder

from collections import namedtuple

from .callback_data import PostRequest

Button = namedtuple('Button', ['text', 'button', 'reason'])


def ikb_confirm(user_tg_id: int):
    keyboard = InlineKeyboardBuilder()
    buttons = [
        Button('✅ Опубликовать', 'accept', 'accept'),
        Button('❌ Персональные данные', 'cancel', 'personal'),
        Button('❌ Название компании', 'cancel', 'company'),
        Button('❌ Религия, нация, политика', 'cancel', 'religion'),
        Button('❌ Уголовные дела', 'cancel', 'crime'),
        Button('❌ Реклама', 'cancel', 'advertising'),
        Button('❌ Иные причины', 'cancel', 'other'),

    ]
    for button in buttons:
        keyboard.button(
            text=button.text,
            callback_data=PostRequest(
                button=button.button,
                reason=button.reason,
                author_id=user_tg_id,
            )
        )
        keyboard.adjust(1)
    return keyboard.as_markup()
