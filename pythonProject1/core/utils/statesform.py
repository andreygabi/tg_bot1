from aiogram.fsm.state import StatesGroup, State

class StatqForm(StatesGroup):
    GETNAME = State()
    GETTAG = State()
    GETINFO = State()
    DELETENAME = State()