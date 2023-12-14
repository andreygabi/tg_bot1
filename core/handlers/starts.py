from aiogram import Bot, Dispatcher
from aiogram.types import Message

from core.utils.databaseconnector import Request

async def get_start(message: Message, bot: Bot, request: Request):
    await message.answer(f'hello :)'
                         f'plz /register'
                         f'thx')


async def get_help(message: Message, bot: Bot):
    await message.answer(f'plz tap on (kinda) blue Menu button on ur keyboard'
                         f'u get some options here'
                         f'wanna add a contact? /addcontact'
                         f'wanna delete some? /deletecontact'
                         f'wanna view them? /viewcontacts')


async def get_register(message: Message, bot: Bot, request: Request):
    await request.reg_user_id(message.from_user.id)
    await message.answer(f'u have been registered')
