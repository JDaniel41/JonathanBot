from discord.ext import commands
from cogs.Greetings import Greetings
from cogs.SwearJar import SwearJar
import os

TOKEN = os.environ["DISCORD_TOKEN"]

bot = commands.Bot(command_prefix='!')

bot.add_cog(Greetings(bot))
bot.add_cog(SwearJar(bot))

@bot.event
async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')

print("BOT IS STARTING!")
bot.run(TOKEN)
