import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode

from user_handler import user_router


async def start_up(token) -> None:
    bot = Bot(token=token, parse_mode=ParseMode.HTML)

    dp = Dispatcher()
    dp.include_routers(user_router)

    print('Bot is ready to work!')
    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_up('TOKENHERE'))
