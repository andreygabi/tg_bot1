from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
import asyncio
from core.handlers.starts import com_start, com_help, com_register
from aiogram.filters import Command
from aiogram import F
from core.middleware.contacts import RequestSession
import asyncpg
from core.utils.databaseconnector import Request
from core.handlers.contacts import com_deletecontact, com_viewcontacts, com_addcontact, gotname, gottag, gotinfo, gotdeletedname
from core.utils.statesform import StatqForm

TAKENTOKEN = "6702120663:AAHmT9ZuSA-mluoTmAUWNiXgnQpvv__LaWc"
BOTNAME = '@cringycheckersbot'
dp = Dispatcher()
bot = Bot(token = TAKENTOKEN)
async def start():
    pool_connect = await asyncpg.create_pool(user = 'postgres', password = 'pavapepe', database = 'contacts',
                                             host = '127.0.0.1', port = 5432, command_timeout = 60)
    dp.update.middleware.register(RequestSession(pool_connect))
    dp.message.register(gotname, StatqForm.GETNAME)
    dp.message.register(gottag, StatqForm.GETTAG)
    dp.message.register(gotinfo, StatqForm.GETINFO)
    dp.message.register(gotdeletedname, StatqForm.DELETENAME)
    dp.message.register(com_start, F.text == 'start')
    dp.message.register(com_start, Command(commands = ['start']))
    dp.message.register(com_help, F.text == 'help')
    dp.message.register(com_help, Command(commands=['help']))
    dp.message.register(com_register, Command(commands=['register']))
    dp.message.register(com_addcontact, Command(commands=['addcontact']))
    dp.message.register(com_viewcontacts, Command(commands=['viewcontacts']))
    dp.message.register(com_deletecontact, Command(commands=['deletecontact']))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
