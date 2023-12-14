import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from aiogram import F
from aiogram.filters import Command
import asyncio
import asyncpg

from core.handlers.contacts import get_deletecontact, get_viewcontacts, get_addcontact, gotname, gottag, gotinfo, gotdeletedname
from core.handlers.starts import get_start, get_help, get_register
from core.middleware.contacts import RequestSession
from core.utils.databaseconnector import Request
from core.utils.statesform import StatqForm

#TAKENTOKEN = "6702120663:AAHmT9ZuSA-mluoTmAUWNiXgnQpvv__LaWc"
BOTNAME = '@cringycheckersbot'
dp = Dispatcher()
bot = Bot(token = os.getenv("takentoken"))
async def start():
    pool_connect = await asyncpg.create_pool(user = 'postgres', password = 'pavapepe', database = 'contacts',
                                             host = '127.0.0.1', port = 5432, command_timeout = 60)
    dp.update.middleware.register(RequestSession(pool_connect))
    dp.message.register(gotname, StatqForm.GETNAME)
    dp.message.register(gottag, StatqForm.GETTAG)
    dp.message.register(gotinfo, StatqForm.GETINFO)
    dp.message.register(gotdeletedname, StatqForm.DELETENAME)
    dp.message.register(get_start, F.text == 'start')
    dp.message.register(get_start, Command(commands = ['start']))
    dp.message.register(get_help, F.text == 'help')
    dp.message.register(get_help, Command(commands=['help']))
    dp.message.register(get_register, Command(commands=['register']))
    dp.message.register(get_addcontact, Command(commands=['addcontact']))
    dp.message.register(get_viewcontacts, Command(commands=['viewcontacts']))
    dp.message.register(get_deletecontact, Command(commands=['deletecontact']))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
