import io
import discord
from discord.ext import commands
from PIL import Image
from classes.chess.piece.chess_manager import Manager

manager = Manager()

class Test(commands.Cog):
  def __init__(self, bot):
    self.msg = 'wasa'
    
  @commands.command()
  async def sum(self, ctx, *args: int):
    sum = 0
    for k in args:
      sum += k
    await ctx.send(sum)
  
  @commands.command()
  async def dm(self, ctx, *message: str):
    author = ctx.author
    if author.dm_channel is None:
      await author.create_dm()
    msg =''
    for s in message:
      msg += ' ' + s
    if msg == '':
      msg = 'Empty'
    await author.dm_channel.send(msg)
  
  @commands.command()
  async def img(self, ctx):
    board = Image.open('./assets/chess/boards/board01.png')
    board = board.convert('RGBA')
    
    hbb = Image.open('./assets/chess/pieces/HBB.png')
    hbb = hbb.convert('RGBA').resize((hbb.width//2, hbb.height//2))
    board.paste(hbb, (62, 62+80*5-hbb.height-20), hbb)
    buffer = io.BytesIO()
    board.save(buffer, format='PNG')
    buffer.seek(0)
    
    file = discord.File(buffer, filename='board.png')
    embed = discord.Embed(title='Tablero')
    embed.set_image(url='attachment://board.png')
    await ctx.send(embed=embed, file=file)
  
  @commands.command()
  async def show(self, ctx):
    img = manager.to_image()
    
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    file = discord.File(buffer, filename='game.png')
  
    embed = discord.Embed(title='Game')
    embed.set_image(url='attachment://game.png')
    await ctx.send(embed=embed, file=file)
    
  @commands.command()
  async def move(self, ctx, *args: str):
    xyi = args[0]
    xyf = args[1]
    
    prev_pos = (ord(xyi[0])-97, int(xyi[1])-1)
    post_pos = (ord(xyf[0])-97, int(xyf[1])-1)
    await ctx.send(f'{prev_pos}{post_pos}')
    
    move = manager.move(prev_pos, post_pos)
    
    if move:
      img = manager.to_image()
      
      buffer = io.BytesIO()
      img.save(buffer, format='PNG')
      buffer.seek(0)
      file = discord.File(buffer, filename='game.png')
    
      embed = discord.Embed(title='Game')
      embed.set_image(url='attachment://game.png')
      await ctx.send(embed=embed, file=file)
    
    await ctx.send('Se ha movido' if move else 'No')

def setup(bot):
  bot.add_cog(Test(bot))