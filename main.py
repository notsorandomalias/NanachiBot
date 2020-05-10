from discord import File
from discord.ext import commands
from wand.image import Image
from wand.drawing import Drawing
import os

bot = commands.Bot(command_prefix='?')
token = os.environ.get("DISCORD_TOKEN")

def hello(string):
    with Drawing() as draw:
        with Image(filename='src/crabrave.gif') as image:
            draw.font = 'src/impact.ttf'
            draw.font_size = 50
            
            for i in range(len(image.sequence)):
                draw.text(0, 0, string)
                draw(image.sequence[i])

            image.save(filename='test.gif')

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    print("Fired up and ready to go~")

@bot.command()
async def crab(ctx, arg):
    #try:
    hello(arg)
    await ctx.send(file=File('test.gif'))
    os.remove('test.gif')
    #except:
    #    await ctx.send("Error: Failed to send a gif of a crab rave rendered in Unreal Engine 4 in 4k. sad crabs")

@bot.command()
async def p(ctx):
    await ctx.send(file=File('src/peepeepriv.jpg'))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return

    if 'poogers' or 'pooger' in message.content:
        mention = message.author.mention
        response = f"{mention} please shut the fuck up."
        await message.channel.send(response)

bot.run(token)