from aiogram import Bot, Dispatcher
from aiogram.types import ChatJoinRequest
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_IDS = [int(x) for x in os.getenv("OWNER_IDS").split(",")]

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.chat_join_request()
async def join_request(event: ChatJoinRequest):
    user = event.from_user

    text = (
        f"Новая заявка\n\n"
        f"Имя: {user.full_name}\n"
        f"ID: {user.id}\n"
        f"Username: @{user.username if user.username else 'нет'}"
    )

    for owner_id in OWNER_IDS:
    await bot.send_message(owner_id, text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
