from discord import File
from discord.ext import commands
import os
import re

bot = commands.Bot(command_prefix='?')
token = os.environ.get("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    print("Fired up and ready to go~")

@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return

    if re.search('(?i)\\bpooger', message.content):
        authormention = message.author.mention
        response = f"{authormention} please shut the fuck up."
        await message.channel.send(response)
    
    await bot.process_commands(message)

@bot.command()
async def crab(ctx):
    await ctx.send(file=File('src/crabrave.gif'))

@bot.command()
async def p(ctx):
    await ctx.send(file=File('src/peepeepriv.jpg'))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)