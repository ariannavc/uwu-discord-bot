

import discord
import os
from stayin_alive import stayin_alive

stayin_alive()

TOKEN = os.environ['DISCORD_BOT_SECRET']

client = discord.Client()


@client.event
async def on_ready():
  print('i did it! ^.^')
  print(client.user)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if 'uwu' in message.content.lower():
    await message.channel.send('uwu')
  if 'owo' in message.content.lower():
    await message.channel.send('owo')


client.run(TOKEN)