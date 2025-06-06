import asyncio
import menu
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.client.session.aiohttp import AiohttpSession
session = AiohttpSession(proxy="http://proxy.server:3128")
from handlers import router as handlers_router
load_dotenv()

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(handlers_router)




async def main() -> None:
    # bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    bot = Bot(token=TOKEN, session=session)
    await menu.set_bot_menu(bot)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())