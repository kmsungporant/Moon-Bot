import nextcord
import random
import json
import time
import aiohttp
from nextcord.ext import commands, tasks
from io import BytesIO
from nextcord.ext.commands import has_permissions, MissingPermissions
import asyncio as asyncio


with open("config.json", "r") as read_file:
    data = json.load(read_file)

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
    


    @commands.command(pass_context = True, aliases=['Poll'])
    @commands.cooldown(1,20,commands.BucketType.user)
    async def poll(self, ctx, question, *options: str):
        if (ctx.channel.id == 609958852166680586 or ctx.channel.id == 890412538460766208):
            if len(options) <= 1:
                await ctx.send('You need more than one option to make a poll!')
            elif len(options) > 10:
                await ctx.send('You cannot make a poll for more than 10 things!')
            else:
                if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
                    reactions = ['✅', '❌']
                else:
                    reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']
                description = []
                for x, option in enumerate(options):
                    description += '\n {} {}'.format(reactions[x], option)
                embed = nextcord.Embed(title=question, description=''.join(description))
                react_message = await ctx.send(embed=embed)
                for reaction in reactions[:len(options)]:
                    await react_message.add_reaction(reaction)
                self.client.poll_dict[react_message.id] = {
                    'options': options,
                    'reactions': reactions,
                    'author': ctx.author.id
                }
                self.client.poll_dict[react_message.id]['timer'] = tasks.LoopEntry(self.check_poll, 60, react_message.id)
                self.client.poll_dict[react_message.id]['timer'].start()
        else:
            await ctx.send("You can't use this in this channel. Use it in **#Bot-Commands**.")

    @commands.command(pass_context = True, aliases=['Steal', 'Stealemoji', 'StealEmoji'])
    @commands.has_permissions(manage_emojis_and_stickers = True)
    async def stealEmoji(self, ctx, url:str, *, name):
        guild = ctx.guild
        async with aiohttp.ClientSession() as ses:
            async with ses.get(url) as r:
                try:
                    imgOrGif = BytesIO(await r.read())
                    bValue = imgOrGif.getvalue()
                    if r.status in range(200, 299):
                        emoji = await guild.create_custom_emoji(image=bValue, name=name)
                        await ctx.send(f"Emoji created! {emoji}")
                        await ses.close()
                    else:
                        await ctx.send("Invalid URL")
                
                except nextcord.HTTPException:
                    await ctx.send("File is too large.")

    


def setup(client):
    client.add_cog(util(client))