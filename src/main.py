from discord import File
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont, ImageSequence
from io import BytesIO

bot = commands.Bot(command_prefix='?')
with open('token.txt', 'r') as token_file:
    token = token_file.readline()

'''
def crabwrite(file):
    #impact = ImageFont.truetype('impact.ttf', 32)
    frames = []

    for frame in ImageSequence.Iterator(file):
        cr = ImageDraw.Draw(frame)
        cr.text((0, 1000), "Hello World", align='center')
        del cr

        b = BytesIO()
        frame.save(b, format='GIF')
        frame = Image.open(b)

        frames.append(frame)
    
    frames[0].save('out.gif', save_all=True, append_images=frames[1:])
'''

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    print("Fired up and ready to go~")

@bot.command()
async def crab(ctx):
    try:
        await ctx.send(file=File("srcmedia/crabrave.gif"))
    except:
        await ctx.send("Error: Failed to send a gif of a crab rave rendered in Unreal Engine 4 in 4k. sad crabs")

@bot.command()
async def p(ctx):
    await ctx.send(file=File('peepeepriv.jpg'))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)