import discord
import discord.ext.commands as commands

class SwearJar(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
        self.enabled = False
        self.swears = []
        self.allowed_users = ['RocketGoalie#2163']

        with open('bot/assets/swear.txt', 'r') as input_file:
            for line in input_file:
                self.swears.append(line.replace('\n', ''))
        
        print(self.swears)
            
    
    @commands.command(name='enable')
    async def enable_jar(self, ctx):
        if self.enabled == False:
            await ctx.send("Hi {}! Time to make sure Alex doesn't swear".format(ctx.author))
            print("Jar enabled by {}".format(ctx.author))
            self.enabled = True
        else:
            await ctx.send("The Jar is already enabled!!!")

    @commands.command(name='disable')
    async def disable_jar(self, ctx):
        if ctx.author.name + "#" + ctx.author.discriminator not in self.allowed_users:
            print("{} tried to disable me".format(ctx.author.name + "#" + ctx.author.discriminator))
            print(self.allowed_users)
            await ctx.send("Hi {}! Because of Alex you can't disable me. *dabs*".format(ctx.author))
            return
        

        if self.enabled == True:
            await ctx.send("Hi {}! I'm calling it a night for now. Swear away!".format(ctx.author))
            self.enabled = False
        else:
            await ctx.send("The Jar is already disabled!!!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.enabled == False:
            print("Ignoring Message \"{}\" because jar is disabled.".format(message.content))
            return

        if message.author == self.bot.user:
            print("Ignoring Message sent by self: {}".format(message.content))
            return

        for swear in self.swears:
            if swear in message.content.lower():
                await message.channel.send("NO SWEARING {}!".format(message.author.name))
                break
        
        return