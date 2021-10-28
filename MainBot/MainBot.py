import nextcord
import random
import time
import json
import music
import util
import fun
import soundtracks
import lastOne
import os
import asyncio as asyncio
from itertools import cycle
from nextcord.ext import commands, tasks


with open("config.json", "r") as read_file:
    data = json.load(read_file)

client = commands.Bot(command_prefix = data["prefix"])

cogs = [music, soundtracks, util, fun, lastOne]

for i in range(len(cogs)):
    cogs[i].setup(client)

client.remove_command("help")
status = cycle(['.help for commands', 'Moon Dogs Offical Bot'])

@client.event
async def on_ready():
    change_status.start()
    print('BOT IS READY!')
    print(f'MinBot is connected in: {len(client.guilds)} servers')

@tasks.loop(seconds=3)
async def change_status():
    await client.change_presence(activity=nextcord.Game(next(status)))




@client.group(invoke_without_command=True)
async def help(ctx):
    if (ctx.channel.id == data["channel_idMoon"], data["channel_idTest"]):
        em = nextcord.Embed(title = "__Commands__", description = "Use .[command] in #Bot-Commands\n")
    
        em.add_field(name = "__SoundTracks__", value = "**Beach** - Om's sheesh at the beach\n**Stef** - Stefan's laugh\n**Teddy** - Jeff praises Teddy\n**Jeff** - Jeff's \"Fix Your Mic\"\n**Jeff2** - Jeff's cry for help\n**Chris** - Christian's nut noise\n**Chris2** - Christian's \"I'm a pillow pet\"\n**Om** - Om's fudge you\n**Dan** - Dan's Bruh\n**Alan** - Alan's jump scare\n")
        em.add_field(name = "__Music__", value = "**Play** - Play youtube videos with .play [url]\n**Pause** - Pauses the youtube video\n**Resume** - Resumes the paused youtube video\n**Stop** - Disconnects the bot completely\n")
        em.add_field(name = "__Fun__", value = "**Agent** - Selects a random agent in Valorant!\n**Gun** - Selects a random gun in Valorant!\n**CoinFlip** - Flips a coin!")
        
        await ctx.send(embed = em)
    else:
        await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")
        

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**Still on cooldown!** Please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    

client.run(data["token"])