from typing import List
from discord.ext import commands
import discord

class TicTacToeButton(discord.ui.Button['TicTacToe']):
    '''
    Lớp TicTacToeButton để tạo ra nút có thể tương tác cho trò chơi TicTacToe   
    '''
    def __init__(self, x: int, y: int):
        '''
        Hàm thiết lập của lớp
        Input: self, số nguyên x, số nguyên y
        Ouput: None
        '''
        super().__init__(style=discord.ButtonStyle.secondary, label='\u200b', row=y)
        self.x = x
        self.y = y

    async def callback(self, interaction: discord.Interaction):
        '''
        Hàm callback() để thay đổi view mỗi khi có tương tác của người dùng
        Input: tương tác của người dùng
        Output: None
        '''
        assert self.view is not None
        view: TicTacToe = self.view
        state = view.board[self.y][self.x]
        if state in (view.X, view.O):
            return

        if view.current_player == view.X:
            self.style = discord.ButtonStyle.danger
            self.label = 'X'
            self.disabled = True
            view.board[self.y][self.x] = view.X
            view.current_player = view.O
            content = "It is now O's turn"
        else:
            self.style = discord.ButtonStyle.success
            self.label = 'O'
            self.disabled = True
            view.board[self.y][self.x] = view.O
            view.current_player = view.X
            content = "It is now X's turn"

        winner = view.check_board_winner()
        if winner is not None:
            if winner == view.X:
                content = 'X won!'
            elif winner == view.O:
                content = 'O won!'
            else:
                content = "It's a tie!"

            for child in view.children:
                child.disabled = True

            view.stop()

        await interaction.response.edit_message(content=content, view=view)

class TicTacToe(discord.ui.View):
    '''
    Lớp TicTacToe là để tạo ra đối tượng bàn cờ 3x3.
    '''
    children: List[TicTacToeButton]
    X = -1
    O = 1
    Tie = 2

    def __init__(self):
        '''
        Hàm thiết lập của lớp
        Input: self
        Ouput: None
        '''
        super().__init__()
        self.current_player = self.X
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        for x in range(3):
            for y in range(3):
                self.add_item(TicTacToeButton(x, y))

    def check_board_winner(self):
        '''
        Hàm check_board_winner để kiểm tra đã có người chiến thắng hay chưa.
        Input: Self
        Output: -1 nếu X thắng, 1 nếu 0 thắng, 2 nếu hòa, None nếu chưa có kết quả.
        '''
        for across in self.board:
            value = sum(across)
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        for line in range(3):
            value = self.board[0][line] + self.board[1][line] + self.board[2][line]
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        diag = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        if all(i != 0 for row in self.board for i in row):
            return self.Tie

        return None
    
class Game(commands.Cog):
    '''
    Lớp Game chứa những lệnh (command) liên quan đến chơi trò chơi
    '''
    def __init__(self, bot):
        '''
        Hàm thiết lập của lớp
        Input: self, Đối tượng bot
        Ouput: None
        '''
        self.bot = bot
        
    @commands.command()
    async def tic(self, ctx):
        '''
        Phương thức Game.tic() để gửi giao diện trò chơi tic tac toe.
        Input: self, bối cảnh thực hiện câu lệnh (ctx)
        Output: None
        '''
        await ctx.send(view=TicTacToe())

# For making extension
async def setup(bot):
    await bot.add_cog(Game(bot))
