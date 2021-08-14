

import discord
import os
from stayin_alive import stayin_alive

stayin_alive()

TOKEN = os.environ['DISCORD_BOT_SECRET']

client = discord.Client()

greetings = ["hi", "hello", "hey", "helloo", "hellooo", "g morining", "gmorning", "good morning", "morning", "good day", "good afternoon", "good evening", "greetings", "greeting", "good to see you", "its good seeing you", "how are you", "how're you", "how are you doing", "how ya doin'", "how ya doin", "how is everything", "how is everything going", "how's everything going", "how is you", "how's you", "how are things", "how're things", "how is it going", "how's it going", "how's it goin'", "how's it goin", "how is life been treating you", "how's life been treating you", "how have you been", "how've you been", "what is up", "what's up", "what is cracking", "what's cracking", "what is good", "what's good", "what is happening", "what's happening", "what is new", "what's new", "what is neww", "g’day", "howdy", "hewwo"]

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
    
  if any(message.content.lower().startswith(greeting) for greeting in greetings):
    await message.channel.send('hewwo! ^.^')
        

client.run(TOKEN)