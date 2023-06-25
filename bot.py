from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config
import asyncio
import logging
from handlers import other_handlers, user_handlers
from keyboards.main_menu import set_main_menu

# Инициализируем логгер
logger = logging.getLogger(__name__)


async def main():


    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')


    api: Config = load_config('.env.txt')
    bot: Bot = Bot(api.tg_token.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()


    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)


    await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)




if __name__ == '__main__':
    asyncio.run(main())