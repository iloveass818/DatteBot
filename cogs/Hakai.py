import discord
from discord.ext import commands
import asyncio

class Hakai(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  
  @commands.command(aliases = ["hakai"])
  async def Hakai(self, ctx, amount, arg:str=None):
    if ctx.author.id == 416909560129781770:
      await ctx.message.delete()
      await ctx.channel.purge(limit=int(amount))
      message_to_delete = await ctx.send(f'{amount} message(s) have been dattebayoed')
      await asyncio.sleep(2)
      await message_to_delete.delete()
   
   
    else:
      message_to_delete = await ctx.send("Only ess kum use dis")
      await asyncio.sleep(2)
      await message_to_delete.delete()
  
  


def setup(client):
  client.add_cog(Hakai(client))