import asyncio
import nextcord
import random
import json
import config
from random import choice
from nextcord import embeds
from nextcord.ext import commands, tasks
from nextcord.player import FFmpegAudio, FFmpegPCMAudio
import asyncio as asyncio


class fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.current_channel = None
        self.last = False
        self.first = False

    @commands.command(aliases=['Agent', 'Val', 'val'])
    @commands.cooldown(1,10,commands.BucketType.user)
    async def agent(self, ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            responses = [
                    'Astra',
                    'Breach',
                    'Brimstone',
                    'Cypher',
                    'Jett',
                    'Kay/O',
                    'Killjoy',
                    'Omen',
                    'Phoenix',
                    'Raze',
                    'Reyna',
                    'Sage',
                    'Skye',
                    'Sova',
                    'Viper',
                    'Yoru']

            embed = nextcord.Embed(title="Agent Select | Moon Bot", description=f"{ctx.author.mention} Your agent is: **{random.choice(responses)}**")
            await ctx.send(embed=embed)
        else:
            msg = await ctx.send(f"You can't use this in this channel. Use it in <#{config.BOT_COMMAND_CHANNEL_ID}>.")
            await asyncio.sleep(1)
            await msg.delete()

    @commands.command(aliases=['Gun', 'gun', 'Gunselect'])
    @commands.cooldown(1,10,commands.BucketType.user)
    async def gunselect(self, ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            responses = [
                    'Classic',
                    'Shorty',
                    'Frenzy',
                    'Ghost',
                    'Sheriff',
                    'Stinger',
                    'Spectre',
                    'Bucky',
                    'Judge',
                    'Bulldog',
                    'Guardian',
                    'Phantom',
                    'Vandal',
                    'Marshal',
                    'Operator',
                    'Ares',
                    'Odin']

            embed = nextcord.Embed(title="Gun Selection", description=f"{ctx.author.mention} Your gun is: **{random.choice(responses)}**")
            await ctx.send(embed=embed)
        else:
            msg = await ctx.send(f"You can't use this in this channel. Use it in <#{config.BOT_COMMAND_CHANNEL_ID}>.")
            await asyncio.sleep(1)
            await msg.delete()

    

    @commands.command(aliases=['cf', 'Coinflip', 'CoinFlip', 'Cf', 'CF'])
    @commands.cooldown(1,10,commands.BucketType.user)
    async def coinflip(self, ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):

            determine_flip = [1, 0]
            if random.choice(determine_flip) == 1:
                embed = nextcord.Embed(title="Coinflip", description=f"{ctx.author.mention} Flipped coin, we got **Heads**!")
                await ctx.send(embed=embed)

            else:
                embed = nextcord.Embed(title="Coinflip", description=f"{ctx.author.mention} Flipped coin, we got **Tails**!")
                await ctx.send(embed=embed)
        else:
            msg = await ctx.send(f"You can't use this in this channel. Use it in <#{config.BOT_COMMAND_CHANNEL_ID}>.")
            await asyncio.sleep(1)
            await msg.delete()
    
                
    @commands.command(aliases=['lastOne', 'last', 'Last'])
    @commands.cooldown(1,600,commands.BucketType.default)
    async def LastOne(self, ctx):
        await ctx.send("Sorry, **'last one is gay'** command is not currently functioning properly. Try again later...")
        # if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
        #     if ctx.author.voice is None:
        #         await ctx.send("You are not in a voice channel! Join a voice channel and try again in 30s")

        #     voice = ctx.author.voice.channel

        #     if ctx.voice_client is None:
        #         await voice.connect()
        #     else:
        #         await ctx.voice_client.move_to(voice)
        #     await ctx.send("The game, Last One is gay, has been **initiated**")
        #     self.last = True
        #     self.current_channel = voice            
        #     voiceplay = ctx.channel.guild.voice_client
        #     source = FFmpegPCMAudio('/home/minsung/DiscordBot/soundTracks/lastOne.mp3') 
        #     player = voiceplay.play(source)
        # else:
        #     await ctx.send(f"You can't use this in this channel. Use it in <#{config.BOT_COMMAND_CHANNEL_ID}>.")
        
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if self.last and before.channel.id == self.current_channel.id:
            if (len(before.channel.members) == 1 and member.id != config.MOON_BOT_ID):
                channel = nextcord.utils.get(member.guild.text_channels, id=config.BOT_COMMAND_CHANNEL_ID)
                await channel.send(f"<@{member.id}> left last, therefore, <@{member.id}> {random.choice(['is gay lol 🦄🌈✨', 'is non heterosexual 🚫👩‍❤️‍👨'])}")
                self.last = False
                
        if self.first and before.channel.id == self.current_channel.id and (not after.channel or after.channel.id != self.current_channel.id):
            if member.id != config.MOON_BOT_ID:
                channel = nextcord.utils.get(member.guild.text_channels, id=config.BOT_COMMAND_CHANNEL_ID)
                await channel.send(f"<@{member.id}> left first, therefore, <@{member.id}> {random.choice(['is gay lol 🦄🌈✨', 'is non heterosexual 🚫👩‍❤️‍👨'])}")
                self.first = False


    @commands.command(aliases=['firstOne', 'first', 'First'])
    @commands.cooldown(1,600,commands.BucketType.default)
    async def FirstOne(self, ctx):
        if (ctx.channel.id == config.BOT_COMMAND_CHANNEL_ID or ctx.channel.id == config.BOT_TESTING_CHANNEL_ID):
            if ctx.author.voice is None:
                await ctx.send("You are not in a voice channel! Join a voice channel and try again in 30s")

            voice = ctx.author.voice.channel

            if ctx.voice_client is None:
                await voice.connect()
            else:
                await ctx.voice_client.move_to(voice)
            await ctx.send("The game, First One is gay, has been **initiated**")
            self.first = True
            self.current_channel = voice            
            voiceplay = ctx.channel.guild.voice_client
            source = FFmpegPCMAudio('/home/minsung/DiscordBot/soundTracks/firstOne.mp3') 
            player = voiceplay.play(source)

        else:
            await ctx.send(f"You can't use this in this channel. Use it in <#{config.BOT_COMMAND_CHANNEL_ID}>.")
    


    

def setup(client):
    client.add_cog(fun(client))