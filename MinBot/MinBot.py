import nextcord
import random
import time
import asyncio as asyncio
from itertools import cycle
from nextcord.ext import commands, tasks
from nextcord.player import FFmpegAudio, FFmpegPCMAudio

client = commands.Bot(command_prefix = '.')
status = cycle(['Jeff Sucks Balls', 'Dan Sucks Balls'])

@client.event
async def on_ready():
    change_status.start()
    print('BOT IS READY!')
    print(f'MinBot is connected in: {len(client.guilds)} servers')

@tasks.loop(seconds=2)
async def change_status():
    await client.change_presence(activity=nextcord.Game(next(status)))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**Still on cooldown!** Please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)

@client.command(pass_context = True, aliases=['Beach'])
@commands.cooldown(1,15,commands.BucketType.user)
async def beach(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Beach.mp3')
        player = voice.play(source)
        time.sleep(8)
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("You aint in a voice channel boy. ")


@client.command(pass_context = True, aliases=['Shee'])
@commands.cooldown(1,15,commands.BucketType.user)
async def shee(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Shee.mp3')
        player = voice.play(source)
        time.sleep(8)
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("You aint in a voice channel boy. ")

@client.command(pass_context = True, aliases=['Teddy'])
@commands.cooldown(1,15,commands.BucketType.user)
async def teddy(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Teddy.mp3')
        player = voice.play(source)
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("You aint in a voice channel boy. ")

@client.command(pass_context = True, aliases=['jeff'])
@commands.cooldown(1,15,commands.BucketType.user)
async def Jeff(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('scream.mp3')
        player = voice.play(source)
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("You aint in a voice channel boy. ")

@client.command(pass_context = True, aliases=['stef'])
@commands.cooldown(1,15,commands.BucketType.user)
async def Stef(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('STEF.mp3')
        player = voice.play(source)
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("You aint in a voice channel boy. ")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("I aint in a voice channel boy.")
        
    


    

        
    


    
    

with open('token.txt') as f:
    TOKEN = f.readline()

client.run(TOKEN)