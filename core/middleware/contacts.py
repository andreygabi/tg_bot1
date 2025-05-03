from typing import Callable, Awaitable, Dict, Any
import asyncpg

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from core.utils.databaseconnector import Request

class RequestSession:
    def __init__(self, connector: asyncpg.pool.Pool):
        super().__init__()
        self.connector = connector

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, any]], Awaitable],
            event: TelegramObject,
            data: Dict[str, any],
    ) -> Any:
        async with self.connector.acquire() as connect:
            data["request"] = Request(connect)
            return await handler(event, data)
