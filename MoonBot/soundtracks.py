import nextcord
import random
import json
import config
import asyncio as asyncio
from itertools import cycle
from nextcord.ext import commands, tasks
from nextcord.player import FFmpegAudio, FFmpegPCMAudio


class soundtracks(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['Beach'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def beach(self, ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/soundTracks/Beach.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)

                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send(f"You can't use this in this channel. Use it in <#{config.BOT_COMMAND_CHANNEL_ID}>.")
            await asyncio.sleep(2)
            await msg.delete()

    @commands.command(pass_context=True, aliases=['Alan'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def alan(self, ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/soundTracks/alan.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)

                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send(f"You can't use this in this channel. Use it in <#{config.BOT_COMMAND_CHANNEL_ID}>.")
            await asyncio.sleep(2)
            await msg.delete()

    @commands.command(pass_context=True, aliases=['chris'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def Chris(self, ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/soundTracks/Christian.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)

                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send(f"You can't use this in this channel. Use it in <#{config.BOT_COMMAND_CHANNEL_ID}>.")
            await asyncio.sleep(2)
            await msg.delete()

    @commands.command(pass_context=True, aliases=['chris2'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def Chris2(self, ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/soundTracks/Chris2.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)

                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send(f"You can't use this in this channel. Use it in <#{config.BOT_COMMAND_CHANNEL_ID}>.")
            await asyncio.sleep(2)
            await msg.delete()

    @commands.command(pass_context=True, aliases=['jeff2'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def Jeff2(self, ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/soundTracks/Jeff2.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)

                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send(f"You can't use this in this channel. Use it in <#{config.BOT_COMMAND_CHANNEL_ID}>.")
            await asyncio.sleep(2)
            await msg.delete()

    @commands.command(pass_context=True, aliases=['Teddy'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def teddy(self, ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/soundTracks/Teddy.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)

                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send(f"You can't use this in this channel. Use it in <#{config.BOT_COMMAND_CHANNEL_ID}>.")
            await asyncio.sleep(2)
            await msg.delete()

    @commands.command(pass_context=True, aliases=['jeff'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def Jeff(self, ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/soundTracks/Jeff.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)

                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send(f"You can't use this in this channel. Use it in <#{config.BOT_COMMAND_CHANNEL_ID}>.")
            await asyncio.sleep(2)
            await msg.delete()

    @commands.command(pass_context=True, aliases=['stef'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def Stef(self, ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/soundTracks/STEF.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)

                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send(f"You can't use this in this channel. Use it in <#{config.BOT_COMMAND_CHANNEL_ID}>.")
            await asyncio.sleep(2)
            await msg.delete()

    @commands.command(pass_context=True, aliases=['om', 'OM'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def Om(self, ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/soundTracks/om.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)

                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send(f"You can't use this in this channel. Use it in <#{config.BOT_COMMAND_CHANNEL_ID}>.")
            await asyncio.sleep(2)
            await msg.delete()

    @commands.command(pass_context=True, aliases=['dan'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def Dan(self, ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/soundTracks/DanBruh.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)

                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send(f"You can't use this in this channel. Use it in <#{config.BOT_COMMAND_CHANNEL_ID}>.")
            await asyncio.sleep(2)
            await msg.delete()

    @commands.command(pass_context=True, aliases=['depot'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def Depot(self, ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            channel = ctx.message.author.voice.channel
            voice = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/soundTracks/depot.mp3')
            if (ctx.author.voice):
                if voice is None:
                    voice = await channel.connect()
                elif voice.channel != channel:
                    voice.move_to(channel)

                player = voice.play(source)
            else:
                await ctx.send("You are not in a voice channel! ")
        else:
            msg = await ctx.send(f"You can't use this in this channel. Use it in <#{config.BOT_COMMAND_CHANNEL_ID}>.")
            await asyncio.sleep(2)
            await msg.delete()


def setup(client):
    client.add_cog(soundtracks(client))
