import asyncio
from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


async def main():
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())