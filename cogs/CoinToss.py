import discord
from discord.ext import commands
import random

class CoinToss(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    @commands.command(aliases = ["ct"])
    async def cointoss(self, ctx):
        responses = ["yes" , "no"]
        await ctx.send(random.choice(responses))
  
  


def setup(client):
    client.add_cog(CoinToss(client))