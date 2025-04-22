import asyncio
import menu
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from handlers import router as handlers_router
load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(handlers_router)




# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await menu.set_bot_menu(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())