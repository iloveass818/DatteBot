import discord
from discord.ext import commands

class Purge(commands.Cog):
  def __init__(self, client):
    self.client = client
    
    
  @commands.command()
  @commands.has_role('People With Perms')
  async def purge(self, ctx, amount, arg:str=None):
    await ctx.message.delete()
    await ctx.channel.purge(limit=int(amount))
    message_to_delete = await ctx.send(f'{amount} message(s) have been dattebayoed')
    await asyncio.sleep(2)
    await message_to_delete.delete()
  
  


def setup(client):
  client.add_cog(Purge(client))