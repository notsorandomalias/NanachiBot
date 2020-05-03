from discord import File
from discord.ext import commands

bot = commands.Bot(command_prefix='?')
with open('token.txt', 'r') as token_file:
    token = token_file.readline()

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    print("Fired up and ready to go~")

@bot.command()
async def c(ctx):
    await ctx.send(file=File('crabrave.gif'))

bot.run(token)