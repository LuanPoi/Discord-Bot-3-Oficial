import discord
import yaml

_config = yaml.safe_load(open('..\config.yaml', 'r'))

oficialSovietico = discord.Client()

@oficialSovietico.event
async def on_ready():
    print('We have logged in as {0.user}'.format(oficialSovietico))

@oficialSovietico.event
async def on_message(message):
    if message.author == oficialSovietico.user:
        return

    if message.content.startswith('$hw'):
        await message.channel.send('Hello World!')

    if (message.author.id == ((_config['guardaSovietico'])['id'])) & (message.content.endswith("à vista!")):
        await message.channel.send('Abram os portões!')

    if (message.author.id == ((_config['guardaSovietico'])['id'])) & (message.content.startswith('Ele não trouxe vodka!')):
        await message.channel.send('Fechem os portões!')

    if (message.author.id == ((_config['guardaSovietico'])['id'])) & (message.content.startswith('Ele trouxe vodka!')):
        await message.channel.send('Abram os portões! Rápido!')

oficialSovietico.run(_config['discordBotKey'])
