from discord.ext import commands

bot = commands.Bot(command_prefix='?')
token = 'NzA2Mzk2MDk1NTA4NTEyNzY4.Xq5pSA.B0EvxUeEI2_PknRs-5RsPO93PSo'

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    print("Fired up and ready to go~")

@bot.command()
async def crab(ctx, arg):
    await ctx.send("{} is gone".format(arg))

bot.run(token)