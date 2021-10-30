import nextcord
import random
import time
import json
from random import choice
from nextcord import embeds
from nextcord.ext import commands, tasks


class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Agent', 'Val', 'val'])
    @commands.cooldown(1,10,commands.BucketType.user)
    async def agent(self, ctx):
        if (ctx.channel.id == 609958852166680586 or ctx.channel.id == 890412538460766208):
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
            msg = await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")
            time.sleep(1)
            await msg.delete()

    @commands.command(aliases=['Gun', 'gun', 'Gunselect'])
    @commands.cooldown(1,10,commands.BucketType.user)
    async def gunselect(self, ctx):
        if (ctx.channel.id == 609958852166680586 or ctx.channel.id == 890412538460766208):
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
            msg = await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")
            time.sleep(1)
            await msg.delete()

    

    @commands.command(aliases=['cf', 'Coinflip', 'CoinFlip', 'Cf', 'CF'])
    @commands.cooldown(1,10,commands.BucketType.user)
    async def coinflip(self, ctx):
        if (ctx.channel.id == 609958852166680586 or ctx.channel.id == 890412538460766208):

            determine_flip = [1, 0]
            if random.choice(determine_flip) == 1:
                embed = nextcord.Embed(title="Coinflip", description=f"{ctx.author.mention} Flipped coin, we got **Heads**!")
                await ctx.send(embed=embed)

            else:
                embed = nextcord.Embed(title="Coinflip", description=f"{ctx.author.mention} Flipped coin, we got **Tails**!")
                await ctx.send(embed=embed)
        else:
            msg = await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")
            time.sleep(1)
            await msg.delete()

def setup(client):
    client.add_cog(fun(client))