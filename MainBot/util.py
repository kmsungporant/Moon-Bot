import nextcord
import random
from nextcord.ext import commands, tasks
from nextcord.ext.commands import has_permissions, MissingPermissions
import asyncio as asyncio

class util(commands.Cog):
    def __init__(self,client):
        self.client = client

    
    @commands.command(aliases=['Clear'])
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
    
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permissions to do that!")
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if not member.id == self.client.user.id:
            return

        elif before.channel is None:
            voice = after.channel.guild.voice_client
            time = 0
            while True:
                await asyncio.sleep(1)
                time = time + 1
                if voice.is_playing() and not voice.is_paused():
                    time = 0
                if time == 30:
                    await voice.disconnect()
                if not voice.is_connected():
                    break

    


    


def setup(client):
    client.add_cog(util(client))