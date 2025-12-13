import asyncio
from aiogram import Bot, Dispatcher
from config import *

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())