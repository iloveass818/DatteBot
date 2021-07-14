import discord
from discord.ext import commands
import random

class Ball(commands.Cog):
    def __init__(self, client):
        self.client = client
    


    @commands.command(aliases=['8b', "8ball"])
    async def _8ball(self, ctx, *, question):
        responses = [
                    "It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Dattebayo r hapand to be is the.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Yes I am.",
                    "Your Mom.",
                    "Error 404 not found.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        await ctx.send(random.choice(responses))


    

  
  


def setup(client):
    client.add_cog(Ball(client))