import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = discord.Client()
bot = commands.Bot(command_prefix='?', description="This is a Helper Bot")
bot.remove_command('help')

@bot.command()
async def ping(ctx):
    await ctx.send('pong, ' + ctx.message.author.mention)

@bot.command()
async def help(ctx):
    await ctx.send("To be added, " + ctx.message.author.mention)
   

@bot.command()
async def ip(ctx):
    await ctx.send('Server:')
    await ctx.send('Java: `play.animalparadise.tk`')
    await ctx.send('Bedrock: `play.bedrock.animalparadise.tk` Port: `25566`')
    

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

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    # print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Animal Paradise'))
    print('Bot is Ready!')


@bot.listen()
async def on_message(message):
    return
    #if " ip " in message.content.lower():
    #    # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
    #    await message.channel.send('Server:')
    #    await message.channel.send('Java: `play.animalparadise.tk`')
    #    await message.channel.send('Bedrock: `play.bedrock.animalparadise.tk` Port: `25566`')
    #    await bot.process_commands(message)

    
bot.run('OTgwNDY3MTI5NDExMzA1NDky.GA-RZr.rGjONbVcUL6Q6eJkcgDboRYWpl85AYC3DrrzEY')
