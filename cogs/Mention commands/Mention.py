import discord
from discord.ext import commands

class Mention(commands.Cog):
  def __init__(self, client):
    self.client = client
    
    
  @commands.command()
  @commands.cooldown(1,30,commands.BucketType.user)
  async def mention(self, ctx ,user : discord.Member, ping : int = None):
    message = user.mention
  
    if ping is None:
      await ctx.send("Enter the number of times you want to mention the user alongside the command")
      return

    if ping > 9:
      await ctx.send("Number needs to be 9 or lesser")
      await ctx.message.delete()
      

    else:
      await ctx.message.delete()
      i = 0
      while i < ping:
        await ctx.send(message)
        i = i + 1

  




  @commands.command()
  @commands.cooldown(1,15,commands.BucketType.user)
  async def pippai(self, ctx , ping : int = None):
    if ping is None:
      await ctx.send("Enter the number of times you want to mention the user alongside the command")
      return
    
    if ping > 9:
          await ctx.send("Number needs to be 9 or lesser.")
          await ctx.message.delete()
    else:
          await ctx.message.delete()
          i = 0
          while i < ping:
            await ctx.send("<@725760263239762041>") #replace with user id 
            i = i + 1





  @commands.command()
  @commands.cooldown(1,15,commands.BucketType.user)
  async def hellye(self, ctx , ping : int = None):

    if ping is None:
      await ctx.send("Enter the number of times you want to mention the user alongside the command")
      return

    if ping > 9:
          await ctx.send("Number needs to be 9 or lesser.")
          await ctx.message.delete()
    else:
          await ctx.message.delete()
          i = 0
          while i < ping:
            await ctx.send("<@503806558023581700>") #replace with user id 
            i = i + 1





  @commands.command()
  @commands.cooldown(1,15,commands.BucketType.user)
  async def rax(self, ctx , ping : int = None):
    if ping is None:
      await ctx.send("Enter the number of times you want to mention the user alongside the command")
      return


    if ping > 9:
          await ctx.send("Number needs to be 9 or lesser.")
          await ctx.message.delete()
    else:
          await ctx.message.delete()
          i = 0
          while i < ping:
            await ctx.send("<@543878863491432611>") #replace with user id 
            i = i + 1



  @commands.command()
  @commands.cooldown(1,15,commands.BucketType.user)
  async def ganju(self, ctx , ping : int = None):
    if ping is None:
      await ctx.send("Enter the number of times you want to mention the user alongside the command")
      return
      
    if ping > 9:
          await ctx.send("Number needs to be 9 or lesser.")
          await ctx.message.delete()
    else:
          await ctx.message.delete()
          i = 0
          while i < ping:
            await ctx.send("<@543249590384721943>") #replace with user id 
            i = i + 1
  
  


def setup(client):
  client.add_cog(Mention(client))