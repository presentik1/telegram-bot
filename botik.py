import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging

# 🔑 Твой токен
TOKEN = "8444453713:AAHI14Mrbo7g6Bu2mlaF4JTDym_RB3rfN0s"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/info")
async def send_info_buttons(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="❓ Часто задаваемые вопросы", url="https://telegra.ph/CHasto-zadavaemye-voprosy-11-11-11")],
        [InlineKeyboardButton(text="🌐 Наш сайт", url="https://parikpro-34.clients.site/")],
        [InlineKeyboardButton(text="📸 Instagram", url="https://www.instagram.com/parikpro_34?igsh=b2NvNzI1bnhodGUz&utm_source=qr")],
        [InlineKeyboardButton(text="💬 Написать нам в WhatsApp", url="https://wa.me/79377152051")],
        [InlineKeyboardButton(text="🎵 TikTok", url="https://vm.tiktok.com/ZSjHT6guj/")],
        [InlineKeyboardButton(text="▶️ YouTube", url="https://www.youtube.com/@parikpro_34")],
        [InlineKeyboardButton(text="💙 Vk", url="https://vk.com/parikpro_34")],
        [InlineKeyboardButton(text="✉️ Написать нам в Телеграм", url="t.me/tatiana_parikpro_34")]
    ])

    await message.reply("👇 Выберите нужный раздел:", reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
