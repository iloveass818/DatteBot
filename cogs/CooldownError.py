import discord
from discord.ext import commands

class Error(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = '**Slow Down Bru**, it will work again in {:.2f}s'.format(error.retry_after)
            await ctx.send(msg)

  
  


def setup(client):
    client.add_cog(Error(client))