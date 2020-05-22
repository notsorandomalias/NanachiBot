from discord import File
from discord.ext import commands
import os
import re

bot = commands.Bot(command_prefix='?')
token = os.environ.get("DISCORD_TOKEN")

@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return

    result = re.match('\bpooger', message, re.IGNORECASE)

    if result in message.content.lower():
        authormention = message.author.mention
        response = f"{authormention} please shut the fuck up."
        await message.channel.send(response)

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    print("Fired up and ready to go~")

@bot.command()
async def crab(ctx, text:str):
    try:
        await ctx.send(file=File('src/crabrave.gif'))
        os.remove('test.gif')
    except:
        await ctx.send("Error: Failed to send a gif of a crab rave rendered in Unreal Engine 4 in 4k. sad crabs")

@bot.command()
async def p(ctx):
    await ctx.send(file=File('src/peepeepriv.jpg'))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)