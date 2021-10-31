import nextcord
import json
import youtube_dl
import config
from nextcord.ext import commands, tasks
import asyncio as asyncio

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Join'])
    async def join(self, ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            if ctx.author.voice is None:
                await ctx.send("You are not in a voice channel!")
            voice_channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await voice_channel.connect()
            else:
                await ctx.voice_client.move_to(voice_channel)
        else:
            await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")

    @commands.command(aliases=['Play', 'p', 'P'])
    async def play(self, ctx, url):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            if ctx.author.voice is None:
                await ctx.send("You are not in a voice channel!")
            voice_channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await voice_channel.connect()
            else:
                await ctx.voice_client.move_to(voice_channel)
            ctx.voice_client.stop()

            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}
            YDL_OPTIONS = {'format':"bestaudio"}
            vc = ctx.voice_client
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download = False)
                url2 = info['formats'][0]['url']
                source = await nextcord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                vc.play(source)
            while not vc.is_done():
                await asyncio.sleep(1)
            vc.stop()
        else:
            await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")

    
    @commands.command(aliases=['Pause'])
    async def pause(self,ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            if (ctx.voice_client):
                await ctx.voice_client.pause()
                await ctx.send("Paused")
            else:
                await ctx.send("I'm not in a voice channel!")
        else:
            await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")
        
    
    @commands.command(aliases=['Resume'])
    async def resume(self,ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            if (ctx.voice_client):
                await ctx.voice_client.resume()
                await ctx.send("Resumed")
            else:
                await ctx.send("I'm not in a voice channel!")
        else:
            await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")

    
    @commands.command(aliases=['Stop', 'leave', 'Leave'])
    async def stop(self, ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            if (ctx.voice_client):
                if (ctx.author.voice):
                    await ctx.voice_client.disconnect()
                else:
                    await ctx.send("You are not in a voice channel!")
            else:
                await ctx.send("I'm not in a voice channel!")
        else:
            await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")

def setup(client):
    client.add_cog(music(client))
