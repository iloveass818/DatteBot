import os
import discord, asyncio
import aiohttp
from bs4 import BeautifulSoup
from discord.ext import commands
import random
import youtube_dl
from youtube_dl import YoutubeDL
import tracemalloc
from googleapiclient.discovery import build


client = discord.Client()        
client = commands.Bot(command_prefix='&')
client.remove_command('help')


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('&help'))
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      client.load_extension(f'cogs.{filename[:-3]}')
  print('{0.user} ready perfectly'.format(client))


@client.command(aliases = ["restart", "reload"])
async def reload(ctx):
  if ctx.message.author.id == 416909560129781770:
    reload=discord.Embed(description="Bot is reloaded and is ready perfectly!")
    dele=await ctx.send(embed=reload)
    await ctx.message.delete(delay=2)
    await dele.delete(delay=3)
    for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        client.unload_extension(f'cogs.{filename[:-3]}')
        client.load_extension(f'cogs.{filename[:-3]}')

  else:
    await ctx.send("you really thought i'd let everyone use it?")

          
from keep_alive import keep_alive

keep_alive()

client.run(os.getenv('TOKEN'))
