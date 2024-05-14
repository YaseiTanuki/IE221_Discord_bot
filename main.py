import os
from dotenv import load_dotenv
import discord
from discord.ext import commands


# Using .env file
load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$ ", intents=intents)

# Print when bot is ready
@bot.event
async def on_ready():
    '''
    Hàm on_ready() thực hiện những hoạt động cần thiết khi lần đầu khởi chạy bot.
    Input: None
    Output: None
    '''
    await bot.load_extension('cogs.General')
    await bot.load_extension('cogs.ServerManager')
    await bot.load_extension('cogs.MessageManager')
    await bot.load_extension('cogs.MemberManager')
    await bot.load_extension('cogs.Statistic')
    await bot.load_extension('cogs.Media')
    await bot.load_extension('cogs.Game')
    print("Bot is now ready")

# Start bot (must be the last function to call)
bot.run(os.getenv('DISCORD_APP_TOKEN'))