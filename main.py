import os
from dotenv import load_dotenv
import discord
from discord.ext import commands


# Using .env file
load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="r! ", intents=intents)

# Print when bot is ready
@bot.event
async def on_ready():
    await bot.load_extension('cogs.ManageMessages')
    print("Bot is now ready")

# Start bot (must be the last function to call)
bot.run(os.getenv('DISCORD_APP_TOKEN'))