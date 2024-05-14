from discord.ext import commands

class MessageManager(commands.Cog):
    '''
    Lớp MessageManger chứa những phương thức liên quan đến quản lý tin nhắn.
    '''
    def __init__(self, bot):
        '''
        Phương thức thiết lập của lớp
        Input: self, Đối tượng bot
        Ouput: None
        '''
        self.bot = bot

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
    Hàm setup() dùng để thêm lệnh MessageManager
    Input: Đối tượng bot
    Output: None
    '''
    await bot.add_cog(MessageManager(bot))