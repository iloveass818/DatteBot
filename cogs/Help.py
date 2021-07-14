import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    @commands.command()
    @commands.cooldown(1,15,commands.BucketType.user)
    async def help(self, ctx, user : discord.Member = None, *, message=None):
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
  


def setup(client):
  client.add_cog(Help(client))