from aiogram import Bot, Dispatcher
from aiogram.types import Message
from core.utils.databaseconnector import Request

async def com_start(message: Message, bot: Bot, request: Request):
    await message.answer(f'hello :)')

async def com_help(message: Message, bot: Bot):
    await message.answer(f'plz tap on (kinda) blue Menu button on ur keyboard')

async def com_register(message: Message, bot: Bot, request: Request):
    await request.reg_user_id(message.from_user.id)
    await message.answer(f'u have been registered')
