from aiogram import Bot, Dispatcher
from aiogram.types import ChatJoinRequest
import asyncio
import os

BOT_TOKEN = os.getenv("8821051264:AAFsqNfdfWJsbydQJon55mmWEKve69h6WDM")
OWNER_ID = int(os.getenv("5010393976"))

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.chat_join_request()
async def join_request(event: ChatJoinRequest):
    user = event.from_user

    text = (
        f"Новая заявка\n\n"
        f"Имя: {user.full_name}\n"
        f"ID: {user.id}\n"
        f"Username: @{user.username}"
    )

    await bot.send_message(OWNER_ID, text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
