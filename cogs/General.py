from discord.ext import commands

class General(commands.Cog):
    '''
    Lớp General chứa những lệnh chung của bot (những lệnh dùng cho nhiều mục đích)
    '''
    def __init__(self, bot):
        '''
        Hàm thiết lập của lớp
        Input: self, Đối tượng bot
        Ouput: None
        '''
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        '''
        Hàm test() kiểm tra xem bot có đang hoạt động hay không
        Input: bối cảnh thực hiện câu lệnh (ctx)
        Output: None
        '''
        await ctx.send(f"{ctx.message.author} used the test!")
        await ctx.send("Bot is working")
    
    @commands.command()
    async def join(self, ctx):
        '''
        Hàm join() để bot có thể vào voice channel.
        Input: Bối cảnh thực hiện câu lệnh (ctx)
        Output: None
        '''
        await ctx.author.voice.channel.connect()

    @commands.command()
    async def leave(self, ctx):
        '''
        Hàm leave() để bot rời khỏi voice channel.
        Input: Bối cảnh thực hiện câu lệnh (ctx)
        Output: None
        '''
        await ctx.voice_client.disconnect()

async def setup(bot):
    '''
    Hàm setup() dùng để thêm nhóm lệnh General
    Input: Đối tượng bot
    Output: None
    '''
    await bot.add_cog(General(bot))