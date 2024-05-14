from discord.ext import commands

class ServerManager(commands.Cog):
    '''
    Lớp ServerManager chứa những lệnh liên quan đến quản lý server.
    '''
    def __init__(self, bot):
        '''
        Hàm thiết lập của lớp
        Input: self, Đối tượng bot
        Ouput: None
        '''
        self.bot = bot

    @commands.command()
    async def crtext(self, ctx, str):
        '''
        Phương thức ServerManager.crtext() tạo 1 text channel mới.
        Input: bối cảnh thực hiện câu lệnh (ctx), chuỗi kí tự
        Output: None
        '''
        await ctx.message.guild.create_text_channel(str)
        await ctx.send(f"Created new text channel {str}")

    @commands.command()
    async def crvoice(self, ctx, str):
        '''
        Phương thức ServerManager.crvoice() tạo 1 voice channel mới.
        Input: bối cảnh thực hiện câu lệnh (ctx), chuỗi kí tự
        Output: None
        '''
        await ctx.message.guild.create_voice_channel(str)
        await ctx.send(f"Created new voice channel {str}")
    

async def setup(bot):
    '''
    Hàm setup() dùng để thêm nhóm lệnh General
    Input: Đối tượng bot
    Output: None
    '''
    await bot.add_cog(ServerManager(bot))