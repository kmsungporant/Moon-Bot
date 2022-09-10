import asyncio as asyncio
from nextcord.ext import commands
from nextcord.player import FFmpegPCMAudio


class soundtracks(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['Beach'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def beach(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        source = FFmpegPCMAudio(
            'soundTracks/Beach.mp3')
        if (ctx.author.voice):
            if voice is None:
                voice = await channel.connect()
            elif voice.channel != channel:
                voice.move_to(channel)
            player = voice.play(source)
            msg = await ctx.send(f"Now playing Beach.mp3")
            await asyncio.sleep(2)
            await msg.delete()
        else:
            await ctx.send("You are not in a voice channel! ")

    @commands.command(pass_context=True, aliases=['Alan'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def alan(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        source = FFmpegPCMAudio(
            'soundTracks/alan.mp3')
        if (ctx.author.voice):
            if voice is None:
                voice = await channel.connect()
            elif voice.channel != channel:
                voice.move_to(channel)
            player = voice.play(source)
            msg = await ctx.send(f"Now playing Alan.mp3")
            await asyncio.sleep(2)
            await msg.delete()
        else:
            await ctx.send("You are not in a voice channel! ")

    @commands.command(pass_context=True, aliases=['chris'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def Chris(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        source = FFmpegPCMAudio(
            'soundTracks/Christian.mp3')
        if (ctx.author.voice):
            if voice is None:
                voice = await channel.connect()
            elif voice.channel != channel:
                voice.move_to(channel)
            player = voice.play(source)
            msg = await ctx.send(f"Now playing chris.mp3")
            await asyncio.sleep(2)
            await msg.delete()
        else:
            await ctx.send("You are not in a voice channel! ")

    @commands.command(pass_context=True, aliases=['chris2'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def Chris2(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        source = FFmpegPCMAudio(
            'soundTracks/Chris2.mp3')
        if (ctx.author.voice):
            if voice is None:
                voice = await channel.connect()
            elif voice.channel != channel:
                voice.move_to(channel)
            player = voice.play(source)
            msg = await ctx.send(f"Now playing chris2.mp3")
            await asyncio.sleep(2)
            await msg.delete()
        else:
            await ctx.send("You are not in a voice channel! ")

    @commands.command(pass_context=True, aliases=['jeff2'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def Jeff2(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        source = FFmpegPCMAudio(
            'soundTracks/Jeff2.mp3')
        if (ctx.author.voice):
            if voice is None:
                voice = await channel.connect()
            elif voice.channel != channel:
                voice.move_to(channel)
            player = voice.play(source)
            msg = await ctx.send(f"Now playing jeff2.mp3")
            await asyncio.sleep(2)
            await msg.delete()
        else:
            await ctx.send("You are not in a voice channel! ")

    @commands.command(pass_context=True, aliases=['Teddy'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def teddy(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        source = FFmpegPCMAudio(
            'soundTracks/Teddy.mp3')
        if (ctx.author.voice):
            if voice is None:
                voice = await channel.connect()
            elif voice.channel != channel:
                voice.move_to(channel)
            player = voice.play(source)
            msg = await ctx.send(f"Now playing Teddy.mp3")
            await asyncio.sleep(2)
            await msg.delete()
        else:
            await ctx.send("You are not in a voice channel! ")

    @commands.command(pass_context=True, aliases=['jeff'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def Jeff(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        source = FFmpegPCMAudio(
            'soundTracks/Jeff.mp3')
        if (ctx.author.voice):
            if voice is None:
                voice = await channel.connect()
            elif voice.channel != channel:
                voice.move_to(channel)
            player = voice.play(source)
            msg = await ctx.send(f"Now playing jeff.mp3")
            await asyncio.sleep(2)
            await msg.delete()
        else:
            await ctx.send("You are not in a voice channel! ")

    @commands.command(pass_context=True, aliases=['stef'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def Stef(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        source = FFmpegPCMAudio(
            'soundTracks/STEF.mp3')
        if (ctx.author.voice):
            if voice is None:
                voice = await channel.connect()
            elif voice.channel != channel:
                voice.move_to(channel)
            player = voice.play(source)
            msg = await ctx.send(f"Now playing stef.mp3")
            await asyncio.sleep(2)
            await msg.delete()
        else:
            await ctx.send("You are not in a voice channel! ")

    @commands.command(pass_context=True, aliases=['om', 'OM'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def Om(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        source = FFmpegPCMAudio(
            'soundTracks/om.mp3')
        if (ctx.author.voice):
            if voice is None:
                voice = await channel.connect()
            elif voice.channel != channel:
                voice.move_to(channel)
            player = voice.play(source)
            msg = await ctx.send(f"Now playing om.mp3")
            await asyncio.sleep(2)
            await msg.delete()
        else:
            await ctx.send("You are not in a voice channel! ")

    @commands.command(pass_context=True, aliases=['dan'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def Dan(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        source = FFmpegPCMAudio(
            'soundTracks/DanBruh.mp3')
        if (ctx.author.voice):
            if voice is None:
                voice = await channel.connect()
            elif voice.channel != channel:
                voice.move_to(channel)
            player = voice.play(source)
            msg = await ctx.send(f"Now playing dan.mp3")
            await asyncio.sleep(2)
            await msg.delete()
        else:
            await ctx.send("You are not in a voice channel! ")

    @commands.command(pass_context=True, aliases=['depot'])
    @commands.cooldown(1, 20, commands.BucketType.default)
    async def Depot(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        source = FFmpegPCMAudio(
            'soundTracks/depot.mp3')
        if (ctx.author.voice):
            if voice is None:
                voice = await channel.connect()
            elif voice.channel != channel:
                voice.move_to(channel)
            player = voice.play(source)
            msg = await ctx.send(f"Now playing depot.mp3")
            await asyncio.sleep(2)
            await msg.delete()
        else:
            await ctx.send("You are not in a voice channel! ")


def setup(client):
    client.add_cog(soundtracks(client))
