

import discord
import os
from stayin_alive import stayin_alive

stayin_alive()

TOKEN = os.environ['DISCORD_BOT_SECRET']

client = discord.Client()

greetings = ['hello','hi','hii','hiii','hewwo','greetings']

@client.event
async def on_ready():
  print('i did it! ^.^')
  print(client.user)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if 'uwu' in message.content.lower():
    if any(greeting in message.content.lower() for greeting in greetings):
      await message.channel.send('hewwo! ^.^')
    await message.channel.send('uwu')
  if 'owo' in message.content.lower():
    if any(greeting in message.content.lower() for greeting in greetings):
      await message.channel.send('hewwo! ^.^')
    await message.channel.send('owo')
  if any(greeting == message.content.lower() for greeting in greetings):
    await message.channel.send('hewwo! ^.^')
        


client.run(TOKEN)