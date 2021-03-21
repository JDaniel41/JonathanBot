import discord
import discord.ext.commands as commands
import aiohttp

class RandomFacts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='get-random-fact')
    async def say_hi(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://useless-facts.sameerkumar.website/api') as r:
                if r.status == 200:
                    js = await r.json()
                    await ctx.send("Here you go! {}".format(js['data']))
                else:
                    await ctx.send("Sorry. I can't get that right now.")
                    await ctx.send("@RocketGoalie#2163 The API might be down.")
        #await ctx.send("Hi {}! Hope you are having a good day".format(ctx.author))


