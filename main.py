from discord import File
from discord.ext import commands
from wand.image import Image
from wand.drawing import Drawing
import os

bot = commands.Bot(command_prefix='?')
token = os.environ.get("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    print("Fired up and ready to go~")

@bot.command()
async def crab(ctx):
    #try:
    hello()
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

bot.run(token)

def hello():
    with Drawing() as draw:
        with Image(filename='src/crabrave.gif') as image:
            draw.font = 'src/impact.ttf'
            draw.font_size = 50
            
            for i in range(102):
                draw.text(int(image.sequence[i].width / 4), int(image.sequence[i].height / 2), 'Hello, world!')
                draw(image.sequence[i])

            image.save(filename='test.gif')