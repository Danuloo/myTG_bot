from aiogram import Bot, Dispatcher, types
import asyncio
from mail_bot import check_mail

TOKEN = "8654515457:AAHEXRE-wCsNQl8L6w-uO9qrywz0dudhvUE"
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def get_id(message: types.Message):
    await message.answer("Бот ще працює")

async def check_mail_loop():  # ✅ визначена ДО main()
    while True:
        try:
            results = check_mail()
            for subject in results:
                await bot.send_message(
                    chat_id=509811253,
                    text=f"📢 Модульний контоль\n{subject}"
                )
        except Exception as e:
            print(f"Помилка: {e}")

        await asyncio.sleep(60)

async def main():
    asyncio.create_task(check_mail_loop())  # ✅ тепер функція вже існує
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
