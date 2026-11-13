
import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

movies = {
    "1001": "🎬 Kino: Namuna film 1",
    "1002": "🎬 Kino: Namuna film 2",
}

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🍿 Xush kelibsiz!\n\n"
        "Kino kodini yuboring va filmingizni toping."
    )

@dp.message(F.text)
async def find_movie(message: Message):
    code = message.text.strip()

    if code in movies:
        await message.answer(movies[code])
    else:
        await message.answer(
            "❌ Bunday kod topilmadi. "
            "Kino kodini tekshirib qayta yuboring."
        )

async def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN kiritilmagan!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
