import discord
import random
import os
from discord.ext import commands
from googleapiclient.discovery import build

class images(commands.Cog):
  def __init__(self, client):
    self.client = client
    
    
  @commands.command(aliases = ["search"])
  async def image(self, ctx, *, search):
    ran=random.randint(0,9)
    resource=build("customsearch", "v1", developerKey=os.getenv('image_api')).cse()
    result = resource.list(q=f"{search}", cx="fc5c521f5aa6967d3",safe="high", searchType="image").execute()
    url = result["items"][ran]["link"]
    embed1 = discord.Embed(title=f"Here is the image you requested for ({search.title()})")
    embed1.set_image(url=url)
    await ctx.send(embed=embed1)




  @commands.command(aliases = ["nsfw", "n", "N"])
  async def NSFW(self, ctx, *, search):
    if ctx.channel.is_nsfw():
      ran=random.randint(0,9)
      resource=build("customsearch", "v1", developerKey=os.getenv('image_api')).cse()
      result=resource.list(q=f"{search}", cx="707a314bf5400d87b",searchType="image").execute()
      url = result["items"][ran]["link"]
      embed1 = discord.Embed(title=f"Here is the image you requested for {search.title()})")
      embed1.set_image(url=url)
      await ctx.send(embed=embed1, delete_after = 60)
      await ctx.message.delete()
    else:
      await ctx.send("You need to use this command in a nsfw channel!")
  
  


def setup(client):
  client.add_cog(images(client))