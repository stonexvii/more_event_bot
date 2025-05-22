from .commands import command_router
from .any_message import any_router
from .callback import callback_router

routers = [
    callback_router,
    command_router,
    any_router,
]

__all__ = [
    'routers',
]
