import discord
import os
import subprocess
import random as rd
from stayin_alive import stayin_alive

stayin_alive()

TOKEN = os.environ['DISCORD_BOT_SECRET']

intents = discord.Intents(message_content=True, messages=True, typing=True)
client = discord.Client(intents=intents)

greetings = [
    "hi", "hii", "hiii", "hello", "hey", "helloo", "hellooo", "g morining",
    "gmorning", "good morning", "morning", "good day", "good afternoon",
    "good evening", "greetings", "greeting", "good to see you",
    "its good seeing you", "how are you", "how're you", "how are you doing",
    "how ya doin'", "how ya doin", "how is everything",
    "how is everything going", "how's everything going", "how is you",
    "how's you", "how are things", "how're things", "how is it going",
    "how's it going", "how's it goin'", "how's it goin",
    "how is life been treating you", "how's life been treating you",
    "how have you been", "how've you been", "what is up", "what's up",
    "what is cracking", "what's cracking", "what is good", "what's good",
    "what is happening", "what's happening", "what is new", "what's new",
    "what is neww", "g’day", "howdy", "hewwo", "konnichiwa"
]

greeting_resp = [
  'hewwo! ^.^', 'hiiii :3', 'hewwo senpai (✿◠‿◠)'
]

laughs = [
    "lol", "lolz", "lul", "lmao", "lmaoo", "kek", "kekw", "huah", "haha",
    "hahaha", "hahahaha", "hehe", "h u a h", "l m a o", "l o l", "lmfao"
]

laugh_resp = ['HUAH HUAH HUAH :3']

nyas = ['nya', 'n y a']

nya_resp = ['nyaaaa ≧◉◡◉≦']


@client.event
async def on_ready():
    print('i did it! ^.^')
    print(client.user)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any(message.content.lower().startswith(greeting)
           for greeting in greetings):
        await message.channel.send(rd.choice(greeting_resp))

    if any(laugh in message.content.lower() for laugh in laughs):
        await message.channel.send('HUAH HUAH HUAH :3')

    if 'uwu' in message.content.lower():
        await message.channel.send('uwu')

    if any(nya in message.content.lower() for nya in nyas):
        await message.channel.send('nyaaaa ≧◉◡◉≦')

    if 'owo' in message.content.lower():
        await message.channel.send('owo')


try:
    client.run(TOKEN)
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    #os.system("kill -9 $(lsof -t -i:\"8080\"")
    #os.system("python restarter.py")
    #os.system('kill 1')
    subprocess.Popen("kill -9 $(lsof -t -i:\"8080\"".split(), stdout=subprocess.PIPE)
    subprocess.Popen("python restarter.py".split(), stdout=subprocess.PIPE)
    subprocess.Popen("kill 1".split(), stdout=subprocess.PIPE)
