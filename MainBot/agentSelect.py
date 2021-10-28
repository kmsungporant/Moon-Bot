import nextcord
import random
import time
from nextcord import embeds
from nextcord.ext import commands, tasks


class agentSelect(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Agent', 'Val', 'val'])
    @commands.cooldown(1,10,commands.BucketType.user)
    async def agent(self, ctx):
        if (ctx.channel.id == 609958852166680586):
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
            await ctx.send(f"Your agent is: **{random.choice(responses)}**")
        else:
            msg = await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")
            time.sleep(1)
            await msg.delete()

def setup(client):
    client.add_cog(agentSelect(client))