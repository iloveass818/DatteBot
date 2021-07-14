import discord
from discord.ext import commands


class Calculations(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, a: int, b: int):
        await ctx.send(f"{a} + {b} = {a+b}")  #Adds A and B

    @commands.command(aliases=["sub"])
    async def subtract(self, ctx, a: int, b: int):
        await ctx.send(f"{a} - {b} = {a-b}")  #Subtracts A and B

    @commands.command(aliases=["mult"])
    async def multiply(self, ctx, a: int, b: int):
        await ctx.send(f"{a} * {b} = {a*b}")  #Multplies A and B

    @commands.command(aliases=["div"])
    async def divide(self, ctx, a: int, b: int):
        await ctx.send(f"{a} / {b} = {a/b}")  #Divides A and B


def setup(client):
    client.add_cog(Calculations(client))
