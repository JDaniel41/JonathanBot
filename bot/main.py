from discord.ext import commands
from cogs import Greetings
import os

TOKEN = os.environ["DISCORD_TOKEN"]

bot = commands.Bot(command_prefix='!')

bot.add_cog(Greetings(bot))

@bot.event
async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')

bot.run(TOKEN)
