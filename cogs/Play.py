from discord.ext import commands
import DiscordUtils
from youtube_dl import YoutubeDL
from discord import FFmpegPCMAudio
from discord.utils import get

music = DiscordUtils.Music()

class Play(commands.Cog):
    '''
    Lớp Play chứa các hàm liên quan đến phát media, ví dụ như video youtube.
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, url):
        '''
        Hàm play()
        Input: Nhận input là bối cảnh thực hiện câu lệnh (ctx) và url đến video muốn phát
        Output: None
        '''
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if not voice.is_playing():
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
            URL = info['url']
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            await ctx.send('Bot is playing')

# For making extension
async def setup(bot):
    '''
    Hàm setup() dùng để thêm lệnh Play
    Input: Đối tượng bot
    Output: None
    '''
    await bot.add_cog(Play(bot))