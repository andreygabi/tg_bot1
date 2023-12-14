from aiogram import Bot, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
import asyncio
import asyncpg

from core.utils.databaseconnector import Request
from core.utils.statesform import StatqForm

async def get_addcontact(message: Message, bot: Bot, request: Request, state: FSMContext):
    await message.answer(f'input contact`s name')
    await state.set_state(StatqForm.GETNAME)


async def gotname(message: Message, state: FSMContext):
    await message.answer(f'input contact`s tag')
    await state.update_data(name = message.text)
    await state.set_state(StatqForm.GETTAG)


async def gottag(message: Message, state: FSMContext):
    await message.answer(f'input contact`s info')
    await state.update_data(tag = message.text)
    await state.set_state(StatqForm.GETINFO)


async def gotinfo(message: Message, state: FSMContext, request: Request):
    await message.answer(f'done!!')
    await state.update_data(info = message.text)
    context_data = await state.get_data()
    name = context_data.get('name')
    tag = context_data.get('tag')
    info = context_data.get('info')
    await request.add_user(message.from_user.id, name, tag, info)
    await state.clear()


async def get_deletecontact(message: Message, bot: Bot, state: FSMContext):
    #DELETE FROM contacts_data_table WHERE (user_id = 1322264290) AND (contact_tag = '1234')
    await message.answer(f'input deleted one`s tag')
    await state.set_state(StatqForm.DELETENAME)


async def gotdeletedname(message: Message, state: FSMContext, request: Request):
    await message.answer(f'done!!!')
    await state.update_data(tag=message.text)
    context_data = await state.get_data()
    tag = context_data.get('tag')
    await request.delete_contact(message.from_user.id, tag)
    await state.clear()


async def get_viewcontacts(message: Message, bot: Bot, request: Request):
    user_id = message.from_user.id
    types = request.view_contacts(user_id)
    await message.answer(types)
