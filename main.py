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




tracemalloc.start()

client = discord.Client()

        
client = commands.Bot(command_prefix='&')
client.remove_command('help')



players = {}

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
  	msg = '**Slow Down Bru**, it will work again in {:.2f}s'.format(error.retry_after)
    await ctx.send(msg)




@client.command()
async def play(ctx, url : str, channel):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

 



@client.command(aliases = ["av"])
async def avatar(ctx,  user : discord.Member = None):
  em = discord.Embed(title = ctx.author )
  em.set_image(url = ctx.author.avatar_url)
  if user is None:
    await ctx.send(embed=em)
  else:
    em = discord.Embed(title = user )
    em.set_image(url = user.avatar_url)
    await ctx.send(embed=em)

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
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


@client.command(aliases = ["ct"])
async def cointoss(ctx):
  responses = ["yes" , "no"]
  await ctx.send(random.choice(responses))







@client.command() 
async def add(ctx,a:int,b:int): 
    await ctx.send(f"{a} + {b} = {a+b}") #Adds A and B

@client.command(aliases = ["sub"]) 
async def subtract(ctx,a:int,b:int): 
    await ctx.send(f"{a} - {b} = {a-b}") #Subtracts A and B

@client.command(aliases = ["mult"]) 
async def multiply(ctx,a:int,b:int): 
    await ctx.send(f"{a} * {b} = {a*b}") #Multplies A and B

@client.command(aliases = ["div"]) 
async def divide(ctx,a:int,b:int): 
    await ctx.send(f"{a} / {b} = {a/b}") #Divides A and B



@client.command()
async def say(ctx, *, text):
    message = ctx.message
    await message.delete()

    await ctx.send(f"{text}")
  


@client.command(help="Play with &rps [your choice]")
async def rps(ctx):
    rpsGame = ['rock', 'paper', 'scissors']
    await ctx.send(f"Rock, paper, or scissors? Choose wisely...")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

    user_choice = (await client.wait_for('message', check=check)).content

    comp_choice = random.choice(rpsGame)
    if user_choice == 'rock':
        if comp_choice == 'rock':
            await ctx.send(f'Well, that was weird. We tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Nice try, but I won that time!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw, you beat me. It won't happen again!\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'paper':
        if comp_choice == 'rock':
            await ctx.send(f'Ae man you actually beat me\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Oh, wacky. We just tied. I call a rematch!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Get good when!!\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            await ctx.send(f'HAHA!! I JUST CRUSHED YOU!! I rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Bruh. >: |\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Oh well, we tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}")


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('&help'))
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      client.load_extension(f'cogs.{filename[:-3]}')
  print('{0.user} ready perfectly'.format(client))


@client.command(aliases = ["restart"])
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





@client.command()
@commands.cooldown(1,15,commands.BucketType.user)
async def help(ctx, user : discord.Member = None, *, message=None):
    if user is None:
      message = message or "ask iloveass2 for doubtsttebayo"
      await ctx.send("NO")
      await ctx.author.send("Jk, Here")
      await ctx.author.send('''```py
      **List of commands in DatteBot** :



     Ping = To see if bot is on or not
     8ball = Fun 8ball game that gives random asnwers to the questions you ask.
     Rps = Play a duel of rock, paper, scissors with DatteBot.
     add = adds two numbers, ex: add 5 6.
     subtract = subtracts two numbers, ex subtract 6 5.
     multiply = multiplies two numbers, ex: multiply 5 6.
     divide = divides two numbers, ex: divide 5 6.
     avatar = alias = av, gets the avatar of the user mentioned alongside with command, ex: avatar @DatteBot.
     say = says what you tell the bot to say, ex: say dattebayo.
     
     
     **IMAGE Commands**
     
     search = searches images, this command only shows normal images i.e. excludes nsfw/explicit content (alias = image)
     
     nsfw = also searches images, but this one does not exclude anything all nsfw or normal images are shown (alias = NSFW)

     **Mention commands** 

     mention = pings anyone you want as many times as you want ( upto 9 doe), usage &mention @person_you_wanna_mantion 'number of times you wanna mention'


     pippai = pings gippai multiple times, usage &pippai 'number of times you wanna ping.'

     hellye = pings nubyea multiple times, usage &hellye 'number of times you wanna ping.'

     ganju = pings gantant multiplr times, usage &ganju 'number of times you wanna ping.'

     rax = you know it already by now.


     
**MUSIC COMMANDS** =
     

     play = usage: you must be in a voice channel to play music, &play "url of music video" "Name of VC you're in"


    pause = pauses the music, &pause

    stop = stops the music, &stop

    leave = leaves the voice channel, if its not playing new music then use leave and then try to play again, must be in the vc to make it leave, &leave

    resume = resumes the music, &resume``` 



     ''')
      await ctx.author.send(message)
    else:
      message = message or "ask iloveass2 for doubtsttebayo"
      await ctx.send("NO")
      await user.send("Jk, Here")
      await user.send('''```py
      **List of commands in DatteBot** :



     Ping = To see if bot is on or not
     8ball = Fun 8ball game that gives random asnwers to the questions you ask.
     Rps = Play a duel of rock, paper, scissors with DatteBot.
     add = adds two numbers, ex: add 5 6.
     subtract = subtracts two numbers, ex subtract 6 5.
     multiply = multiplies two numbers, ex: multiply 5 6.
     divide = divides two numbers, ex: divide 5 6.
     avatar = alias = av, gets the avatar of the user mentioned alongside with command, ex: avatar @DatteBot.
     say = says what you tell the bot to say, ex: say dattebayo.


     **Mention commands** 
     
     pippai = pings gippai multiple times, usage &pippai 'number of times you wanna ping.'

     hellye = pings nubyea multiple times, usage &hellye 'number of times you wanna ping.'

     ganju = pings gantant multiplr times, usage &ganju 'number of times you wanna ping.'

     rax = you know it already by now.


     
**MUSIC COMMANDS** =
     

     play = usage: you must be in a voice channel to play music, &play "url of music video" "Name of VC you're in"


    pause = pauses the music, &pause

    stop = stops the music, &stop

    leave = leaves the voice channel, if its not playing new music then use leave and then try to play again, must be in the vc to make it leave, &leave

    resume = resumes the music, &resume``` 



     ''')
    await user.send(message)
    
      

from keep_alive import keep_alive

keep_alive()
client.run(os.getenv('TOKEN'))
