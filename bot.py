import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = discord.Client()
bot = commands.Bot(command_prefix='.', description="This is a Helper Bot")
bot.remove_command('help')

@bot.command()
async def ping(ctx):
    await ctx.send('pong, ' + ctx.message.author.mention)

@bot.command()
async def help(ctx):
    await ctx.send("To be added, " + ctx.message.author.mention)
   


    

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    #embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    
    await ctx.send(embed=embed)


# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Glacier Client'))
    print('Bot is Ready!')


@bot.listen()
async def on_message(message):
    return

    
bot.run('OTQ0Nzc3OTM0OTE1Mzk5Njkx.GG7FnP.09BePYF6tn5AYPpkyk8mnHyoGtVxpGSJS-DiGQ')
