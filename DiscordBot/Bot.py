import nextcord
import music
import util
import fun
import soundtracks
import config
import asyncio as asyncio
from itertools import cycle
from nextcord.ext import commands, tasks

intents = nextcord.Intents.all()
# intents.reactions = True
# intents.members = True

client = commands.Bot(command_prefix=config.PREFIX, intents=intents)

cogs = [music, soundtracks, util, fun]

for i in range(len(cogs)):
    cogs[i].setup(client)


client.remove_command("help")
status = cycle(['.help for commands', 'Moon Dogs Offical Bot'])


@client.event
async def on_ready():
    change_status.start()
    print('BOT IS READY!')
    print(f'{(config.BOT_NAME)} is connected in: {len(client.guilds)} servers')


@tasks.loop(seconds=3)
async def change_status():
    await client.change_presence(activity=nextcord.Game(next(status)))


@client.group(invoke_without_command=True)
async def help(ctx):

    em = nextcord.Embed(
        title="__Commands__", description="Use .[command] in only #Bot-Commands\n")

    em.add_field(name="__SoundTracks__", value="**Beach** - Om's sheesh at the beach\n**Stef** - Stefan's laugh\n**Teddy** - Jeff praises Teddy\n**Jeff** - Jeff's \"Fix Your Mic\"\n**Jeff2** - Jeff's cry for help\n**Chris** - Christian's nut noise\n**Chris2** - Christian's \"I'm a pillow pet\"\n**Om** - Om's fudge you\n**Dan** - Dan's Bruh\n**Alan** - Alan's jump scare\n")
    em.add_field(
        name="__Music__", value="**Play** - Play youtube videos with __.play [url]__\n**Pause** - Pauses the youtube video\n**Resume** - Resumes the paused youtube video\n**Stop** - Disconnects the bot completely\n")
    em.add_field(
        name="__Fun__", value="**Agent** - Selects a random agent in Valorant!\n**Gun** - Selects a random gun in Valorant!\n**CoinFlip** - Flips a coin!\n**Clutch** - Deafens the pinged user for 45s __.clutch [@name]__ (Hour cooldown)\n**LastOne** - Plays the \"Last one that leave is GAY game\"\n**FirstOne** - Plays the \"First one that leave is GAY game\"")

    await ctx.send(embed=em)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = await ctx.send('**Still on cooldown!** Available in {:.1f}s'.format(error.retry_after))
        await asyncio.sleep(2)
        await msg.delete()


client.run(config.MOON_BOT_TOKEN)
