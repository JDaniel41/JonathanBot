import discord
import discord.ext.commands as commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='say_hello')
    async def say_hit(ctx):
        print("Hi {}! Hope you are having a good day".format(ctx.author))


