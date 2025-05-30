from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_my_commands(bot):
    commands = [BotCommand(command='start', description='Старт'),
                BotCommand(command='status', description='Статус'),
                BotCommand(command='help', description='Помощь')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
