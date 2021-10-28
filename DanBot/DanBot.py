import nextcord
import os

client = nextcord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-hello'):
        await message.channel.send('Hello!')

with open('token.txt') as f:
    TOKEN = f.readline()
client.run(TOKEN)

