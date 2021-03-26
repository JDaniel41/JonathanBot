import discord
from discord.ext import commands
from cogs.Greetings import Greetings
from cogs.SwearJar import SwearJar
from cogs.RandomFacts import RandomFacts
import os

TOKEN = os.environ["DISCORD_TOKEN"]

bot = commands.Bot(command_prefix='!')

bot.add_cog(Greetings(bot))
bot.add_cog(SwearJar(bot))
bot.add_cog(RandomFacts(bot))

@bot.event
async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')
        game = discord.Game("The Game of Life")
        await bot.change_presence(activity=game)


print("BOT IS STARTING!")
bot.run(TOKEN)
