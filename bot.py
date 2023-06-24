from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config
import asyncio


async def main():

    api: Config = load_config('.env.txt')
    bot: Bot = Bot(api.tg_token.token)
    dp: Dispatcher = Dispatcher()


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)




if __name__ == '__main__':
    asyncio.run(main())