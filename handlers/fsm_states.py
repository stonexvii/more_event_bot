from aiogram.fsm.state import State, StatesGroup


class AnyMessage(StatesGroup):
    catch = State()
    confirm = State()
