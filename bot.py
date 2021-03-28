import discord
import random
from discord.ext import commands
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get

TOKEN = 'ODIwODc0MTQ1Njk5OTg3NDY2.YE7gnw.AXxIl3tMbacdHRgnBnGBxOcWj6A'

bot = commands.Bot(command_prefix='!')


@bot.command()
async def ping(ctx):
    await ctx.send('{0}'.format(round(bot.latency, 1)))

    
@bot.command()
async def whereis(ctx):
    await ctx.send("<@303607757888684032> where r u?")
    
@bot.command()
async def son(ctx):
    await ctx.send("⢸⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⡷⡄⠀⠀ Are ya winning, son?\n⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⡇⠢⣀\n⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠈⠑⢦⡀\n⢸⠀⠀⠀⠀⢀⠖⠒⠒⠒⢤⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠙⢦⡀\n⢸⠀⠀⣀⢤⣼⣀⡠⠤⠤⠼⠤⡄⠀ ⡇⠀⠀⠀⠀⠀⠀⠀⠙⢄\n⢸⠀⠀⠑⡤⠤⡒⠒⠒⡊⠙⡏⠀⢀ ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠢⡄\n⢸⠀⠀⠀⠇⠀⣀⣀⣀⣀⢀⠧⠟⠁  ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⡇\n⢸⠀⠀⠀⠸⣀⠀⠀⠈⢉⠟⠓⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⢸\n⢸⠀⠀⠀⠀⠈⢱⡖⠋⠁⠀⠀⠀⠀    ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⢸\n⢸⠀⠀⠀⠀⣠⢺⠧⢄⣀⠀⠀⣀⣀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⢸\n⢸⠀⠀⠀⣠⠃⢸⠀⠀⠈⠉⡽⠿⠯⡆⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢸\n⢸⠀⠀⣰⠁⠀⢸⠀⠀⠀⠀⠉⠉⠉⠀ ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⢸\n⢸⠀⠀⠣⠀⠀⢸⢄⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢸\n⢸⠀⠀⠀⠀⠀⢸⠀⢇⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢸\n⢸⠀⠀⠀⠀⠀⡌⠀⠈⡆⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸\n⢸⠀⠀⠀⠀⢠⠃⠀⠀⡇⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸\n⢸⠀⠀⠀⠀⢸⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠷                             ⢸")
    
@bot.command()
async def wasitfunny(ctx):
    await ctx.send("not funny")
        
@bot.command()
async def game(ctx):
  responses = [
            "Valorant",
            "Apex Legends",
            "League of Legends",
            "Rainbow Six Siege",
            "Overwatch",
            "Fortnite XD",
            "Oldest one picks",
            "Youngest one picks",
            "Heaviest picks",
            "Counter Strike Global Offensive"]
  await ctx.send(f'{random.choice(responses)}')
  
@bot.command()
async def whereiscarson(ctx):
    for _ in range(10):
        await ctx.send("<@303607757888684032> where r u?")
        
@bot.command()
async def say(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('clip.mp3')
    player = voice.play(source)

@bot.command()
async def adc(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('clip2.mp3')
    player = voice.play(source)
    
@bot.command()
async def wow(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('clip1.mp3')
    player = voice.play(source)
    
@bot.command()
async def what(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('clip4.mp3')
    player = voice.play(source)
    
@bot.command()
async def whatami(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('clip5.mp3')
    player = voice.play(source)
    
    
bot.run(TOKEN)
