import nextcord
import random
import time
import json
import asyncio as asyncio
from itertools import cycle
from nextcord.ext import commands, tasks
from nextcord.player import FFmpegAudio, FFmpegPCMAudio

with open("config.json", "r") as read_file:
    data = json.load(read_file)
    
class soundtracks(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @commands.command(pass_context = True, aliases=['Beach'])
    @commands.cooldown(1,20,commands.BucketType.default)
    async def beach(self, ctx):
        if (ctx.channel.id == 609958852166680586 or ctx.channel.id == 890412538460766208):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio("/home/minsung/DiscordBot/MainBot/soundTracks/Beach.mp3")
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)
                
                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")
            time.sleep(1)
            await msg.delete()

    @commands.command(pass_context = True, aliases=['Alan'])
    @commands.cooldown(1,20,commands.BucketType.default)
    async def alan(self, ctx):
        if (ctx.channel.id == 609958852166680586 or ctx.channel.id == 890412538460766208):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/MainBot/soundTracks/alan.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)
                
                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")
            time.sleep(1)
            await msg.delete()
            
    

    @commands.command(pass_context = True, aliases=['chris'])
    @commands.cooldown(1,20,commands.BucketType.default)
    async def Chris(self, ctx):
        if (ctx.channel.id == 609958852166680586 or ctx.channel.id == 890412538460766208):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/MainBot/soundTracks/Christian.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)
                
                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")
            time.sleep(1)
            await msg.delete()

    @commands.command(pass_context = True, aliases=['chris2'])
    @commands.cooldown(1,20,commands.BucketType.default)
    async def Chris2(self, ctx):
        if (ctx.channel.id == 609958852166680586 or ctx.channel.id == 890412538460766208):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/MainBot/soundTracks/Chris2.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)
                
                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")
            time.sleep(1)
            await msg.delete()
    

    @commands.command(pass_context = True, aliases=['jeff2'])
    @commands.cooldown(1,20,commands.BucketType.default)
    async def Jeff2(self, ctx):
        if (ctx.channel.id == 609958852166680586 or ctx.channel.id == 890412538460766208):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/MainBot/soundTracks/Jeff2.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)
                
                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")
            time.sleep(1)
            await msg.delete()
    

    @commands.command(pass_context = True, aliases=['Teddy'])
    @commands.cooldown(1,20,commands.BucketType.default)
    async def teddy(self, ctx):
        if (ctx.channel.id == 609958852166680586 or ctx.channel.id == 890412538460766208):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/MainBot/soundTracks/Teddy.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)
                
                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")
            time.sleep(1)
            await msg.delete()
        
    

    @commands.command(pass_context = True, aliases=['jeff'])
    @commands.cooldown(1,20,commands.BucketType.default)
    async def Jeff(self, ctx):
        if (ctx.channel.id == 609958852166680586 or ctx.channel.id == 890412538460766208):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/MainBot/soundTracks/Jeff.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)
                
                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")
            time.sleep(1)
            await msg.delete()
    

    @commands.command(pass_context = True, aliases=['stef'])
    @commands.cooldown(1,20,commands.BucketType.default)
    async def Stef(self, ctx):
        if (ctx.channel.id == 609958852166680586 or ctx.channel.id == 890412538460766208):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/MainBot/soundTracks/STEF.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)
                
                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")
            time.sleep(1)
            await msg.delete()

    @commands.command(pass_context = True, aliases=['om', 'OM'])
    @commands.cooldown(1,20,commands.BucketType.default)
    async def Om(self, ctx):
        if (ctx.channel.id == 609958852166680586 or ctx.channel.id == 890412538460766208):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/MainBot/soundTracks/om.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)
                
                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")
            time.sleep(1)
            await msg.delete()

    @commands.command(pass_context = True, aliases=['dan'])
    @commands.cooldown(1,20,commands.BucketType.default)
    async def Dan(self, ctx):
        if (ctx.channel.id == 609958852166680586 or ctx.channel.id == 890412538460766208):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/MainBot/soundTracks/DanBruh.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)
                
                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")
            time.sleep(1)
            await msg.delete()

    @commands.command(pass_context = True, aliases=['depot'])
    @commands.cooldown(1,20,commands.BucketType.default)
    async def Depot(self, ctx):
        if (ctx.channel.id == 609958852166680586 or ctx.channel.id == 890412538460766208):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/MainBot/soundTracks/depot.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)
                
                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")
            time.sleep(1)
            await msg.delete()

def setup(client):
    client.add_cog(soundtracks(client))