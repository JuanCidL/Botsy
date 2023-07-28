import io
import discord
from discord.ext import commands
from PIL import Image

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
      

def setup(bot):
  bot.add_cog(Test(bot))