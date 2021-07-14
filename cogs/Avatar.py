import discord
from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    @commands.command(aliases = ["av"])
    async def avatar(self, ctx,  user : discord.Member = None):
        em = discord.Embed(title = ctx.author )
        em.set_image(url = ctx.author.avatar_url)
        if user is None:
            await ctx.send(embed=em)
        else:
            em = discord.Embed(title = user )
            em.set_image(url = user.avatar_url)
            await ctx.send(embed=em)

  
  


def setup(client):
    client.add_cog(Avatar(client))