import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

class ManageMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command()
    async def test(self, ctx):
        '''
        Hàm test() kiểm tra xem bot có đang hoạt động hay không
        Input: bối cảnh thực hiện câu lệnh (ctx)
        Output: None
        '''
        await ctx.send(f"{ctx.message.author} used the test!")
        await ctx.send("Bot is working")

    @commands.command() # Clear 'number' of message(s)
    async def clear(self, ctx, number: int = commands.parameter(default=5)):
        '''
        Hàm clear() để xóa một số lượng tin nhắn trong lịch sử chat.
        Input: Bối cảnh thực hiện câu lệnh (ctx), số lượng tin nhắn muốn xóa
        Output: None
        '''
        await ctx.channel.purge(limit=number+1)
        await ctx.send(f"Removed {number} most recent message(s)")

# For making extension
async def setup(bot):
    '''
    Hàm setup() dùng để thêm lệnh Quản lý tin nhắn
    Input: Đối tượng bot
    Output: None
    '''
    await bot.add_cog(ManageMessages(bot))