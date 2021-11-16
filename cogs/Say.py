import discord
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    @commands.command()
    async def say(self, ctx, *, text):
        message = ctx.message
        await message.delete()

        await ctx.send(f"{text}")
  
  


def setup(client):
    client.add_cog(Say(client))