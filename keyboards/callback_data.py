from aiogram.filters.callback_data import CallbackData


class PostRequest(CallbackData, prefix='PR'):
    button: str
    reason: str
    author_id: int
