import discord
from discord.ext import commands

class MemberManager(commands.Cog):
    '''
    Lớp MemberManager chứa các phương thức liên quan đến quản lý thành viên.
    '''
    def __init__(self, bot):
        '''
        Hàm thiết lập của lớp
        Input: self, Đối tượng bot
        Ouput: None
        '''
        self.bot = bot
    
    # Commands for admin
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(seft, ctx, user: discord.Member):
        '''
        Phương thức kick() để mời một người dùng rời khỏi máy chủ.
        Input: Bối cảnh thực hiện câu lệnh (ctx), người dùng cần xóa.
        Output: None
        '''
        if ctx.message.author.top_role > user.top_role:
            await user.kick()
            await ctx.send(f'{user.name} is gone!')
        else:
            await ctx.send("You don't have permission!")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: discord.Member):
        '''
        Hàm ban() để chặn một người dùng khỏi server
        Input: bối cảnh thực hiện câu lệnh (ctx), người dùng cần chặn
        Output: None
        '''
        if ctx.message.author.top_role > user.top_role:
            await user.ban()
            await ctx.send(f'{user.name} is gone and will nerver comeback!')
        else:
            await ctx.send("You don't have permission!")


    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def add(seft, ctx, role: discord.Role, user:  discord.Member):
        '''
        Hàm add() để thêm một role cho một người dùng
        Input: Bối cảnh thực hiện câu lệnh (ctx), tên role, người dùng cần thêm role
        Ouput: None
        '''
        if discord.utils.get(ctx.guild.roles, name = role.name):
            if ctx.message.author.top_role > role:
                await user.add_roles(role)
                await ctx.send(f"{user} is now {role}")
            else:
                await ctx.send("You don't have permission!")
        else:
            await ctx.send("Role not exist!")

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def minus(seft, ctx, role: discord.Role, user: discord.Member):
        '''
        Hàm minus() để bỏ một role cho một người dùng
        Input: Bối cảnh thực hiện câu lệnh (ctx), tên role, người dùng cần bỏ role
        Ouput: None
        '''
        if discord.utils.get(ctx.guild.roles, name = role.name):
            if ctx.message.author.top_role > user.top_role:
                await user.remove_roles(role)
                await ctx.send(f"{user} is no longer a {role}")
            else:
                await ctx.send("You don't have permission!")
        else:
            await ctx.send("Role not exist!")

# For making extension
async def setup(bot):
    '''
    Hàm setup() dùng để thêm nhóm lệnh MemberManager
    Input: Đối tượng bot
    Output: None
    '''
    await bot.add_cog(MemberManager(bot))