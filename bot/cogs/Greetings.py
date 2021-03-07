import discord
import discord.ext.commands as commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='greet')
    async def say_hi(self, ctx):
        await ctx.send("Hi {}! Hope you are having a good day".format(ctx.author))


