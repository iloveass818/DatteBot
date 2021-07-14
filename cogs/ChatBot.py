import discord
import aiohttp
import os
import json
from discord.ext import commands

class ChatBot(commands.Cog):
  def __init__(self, client):
    self.client = client
  
    
  @commands.Cog.listener()
  async def on_message(self, msg):
    if  msg.author == self.client.user:
      return
      
    if msg.channel.id == 864776000066813982:
      params = {'server': "primary" , 'message':msg.content , 'master': "iloveass2#8380", 'bot': "DatteBot"}
      headers = {"x-api-key":os.getenv('Ai_key')}
      async with aiohttp.ClientSession() as session:
        async with session.get('https://api.pgamerx.com/v4/ai', params=params,headers=headers) as resp:
          text = await resp.json()
          data = text[0]['message']
          await msg.channel.send(data)
          print (resp.text)
    
    else:
      pass


def setup(client):
  client.add_cog(ChatBot(client))