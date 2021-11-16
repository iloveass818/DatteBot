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
      
    if msg.channel.id == 843820294803947561:
        params = {'server': "main" , 'message': msg.content , 'bot_master': "iloveass2#8380", 'bot_name': "DatteBot", 'bot_gender': "male", 'bot_birth_date': "23rd April 2021", 'bot_company':"Ess Kum pvt. Ltd. ™®©✓✓✓"} 
        headers = {'Authorization':os.getenv('Ai_key') }
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.pgamerx.com/v5/ai', params=params,headers=headers) as resp:
                text = await resp.json()
                await msg.channel.send(text[0]['response'])
    
    else:
      pass


def setup(client):
  client.add_cog(ChatBot(client))