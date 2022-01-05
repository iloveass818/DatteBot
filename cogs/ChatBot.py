import discord
import aiohttp
import os
import json
import requests
from discord.ext import commands

def setup(client):
    client.add_cog(ChatBot(client))

class ChatBot(commands.Cog):
    def __init__(self, client):
        self.client = client
  
    @commands.Cog.listener()
    async def on_message(self, msg):
        if  msg.author == self.client.user:
            return
        api_key = os.environ['Ai_key']
        headers = {"authorization":api_key,
        "x-rapidapi-host":"random-stuff-api.p.rapidapi.com",
        "x-rapidapi-key": "633b3310bbmshb06853853f96fcbp1986d1jsnae275e323f14"}

        url = "https://random-stuff-api.p.rapidapi.com/ai"
        params = {"msg":msg.content,
        "bot_name":"DatteBot","bot_gender":"male","bot_master":"iloveass2#8380","bot_age":"8","bot_company":"iloveass2 sons Pvt. Ltd.","bot_location":"India","bot_email":"googlesoftpplezonkart@.com","bot_build":"Public","bot_birth_year":"2021","bot_birth_date":"23rd April, 2021","bot_birth_place":"India","bot_favorite_color":"Blue","bot_favorite_book":"Harry Potter","bot_favorite_band":"Imagine Doggos","bot_favorite_artist":"Eminem","bot_favorite_actress":"Zendaya","bot_favorite_actor":"Ryan reynolds"}

        resp = requests.request("GET", url, headers=headers, params=params)
        text = resp.json()
        await msg.reply(text["AIResponse"])

