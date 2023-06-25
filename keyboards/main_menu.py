from aiogram.types import BotCommand
from aiogram import Bot
from lexicon.lexicon import LEXICON_COMMANDS

async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='/beginning', description=LEXICON_COMMANDS['/beginning']),
        BotCommand(command='/continue', description=LEXICON_COMMANDS['/continue']),
        BotCommand(command='/bookmarks', description=LEXICON_COMMANDS['/bookmarks']),
        BotCommand(command='/help', description=LEXICON_COMMANDS['/help'])
    ]

    await bot.set_my_commands(main_menu_commands)