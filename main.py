from discord.ext import commands

bot = commands.Bot(command_prefix='?')
token_file = open('token.txt', 'r')
token = token_file.readline()
token_file.close()

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    print("Fired up and ready to go~")

@bot.command()
async def crab(ctx, arg):
    await ctx.send("{} is gone".format(arg))

bot.run(token)