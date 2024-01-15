from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from states import StartState
from builders import profile
from secret_key import secret_key

user_router = Router()


@user_router.message(F.text == "Отмена")
async def cancel_handler(msg: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await msg.answer(text='Действие отменено!',
                     reply_markup=ReplyKeyboardRemove())


@user_router.message(CommandStart())
async def get_secretkey(msg: Message, state: FSMContext):
    await state.set_state(StartState.waiting_for_key)
    await msg.answer(text='Привет! Пришли секретный ключ для авторизации.',
                     reply_markup=profile('Отмена'))


@user_router.message(StartState.waiting_for_key)
async def get_secretkey(msg: Message, state: FSMContext):
    if msg.text == secret_key:
        await msg.answer(text='Авторизация прошла успешно! \nТеперь вы можете пользоваться ботом.',
                         reply_markup=ReplyKeyboardRemove())
    else:
        await msg.answer(text='Неправильный секретный ключ! Попробуйте ещё раз.')


@user_router.message(F.text == "Отмена")
async def cancel_handler(msg: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await msg.answer(text='Действие отменено!',
                     reply_markup=ReplyKeyboardRemove())
