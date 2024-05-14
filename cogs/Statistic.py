from discord.ext import commands
from table2ascii import table2ascii as t2a, PresetStyle

class Statistic(commands.Cog):
    '''
    Lớp Statistic chứa các hàm liên quan đến thống kê, ví dụ như thống kê số lượng tin nhắn.
    '''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def sta(self, ctx):
        '''
        Hàm sta()
        Input: Hàm sta nhận input là context chỉ bối cảnh sử dụng lệnh của người dùng.
        (context là 1 đối tượng trong thư viện Discord)
        Output: Bảng thống kê số lượng tin nhắn gửi bởi người dùng
        '''
        response = await ctx.send('Caculatiing...')
        table = []
        async for mess in ctx.channel.history(limit=100):
            if not mess.author.bot:
                if len(table) == 0:
                    table.append([mess.author, mess.author.name, 1])
                    continue

                for i in range(len(table)):
                    if mess.author == table[i][0]:
                        table[i][2] += 1
                        break

                    if i == len(table) - 1:
                        table.append([mess.author, mess.author.name, 1])

        table.sort(key=lambda x: x[2], reverse=True)
        
        title = 'MEMBER CONTRIBUTION TABLE\n'
        i = 0
        ranked = table.copy()
        for i in range (len(table)):
            table[i].insert(0, i+1)

        statistic = t2a(
            header=["Rank", "ID", "Name", "Number of messages"],
            body = ranked,
            style=PresetStyle.thin_compact
        )
        
        await response.edit(content = title)
        await ctx.send(f"```\n{statistic}\n```")

        return statistic
    
# For making extension
async def setup(bot):
    '''
    Hàm setup() dùng để thêm lệnh Statistic
    Input: Đối tượng bot
    Output: None
    '''
    await bot.add_cog(Statistic(bot))