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
    await bot.load_extension('cogs.ManageMember')
    await bot.load_extension('cogs.Statistic')
    await bot.load_extension('cogs.Play')
    print("Bot is now ready")

@bot.command()
async def join(ctx):
    await ctx.author.voice.channel.connect()

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

# Start bot (must be the last function to call)
bot.run(os.getenv('DISCORD_APP_TOKEN'))