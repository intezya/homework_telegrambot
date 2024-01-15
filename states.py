from aiogram.fsm.state import StatesGroup, State


class StartState(StatesGroup):
    waiting_for_key = State()
