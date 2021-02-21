import discord
import os
import requests
import json
import random

sad_words = ['Sad', 'sad', 'Angry', 'angry', 'Depressed', 'depressed', 'Unhappy', 'unhappy', 'Hate', 'hate', 'Bored', 'bored', 'boring', 'Miserable', 'miserable', 
            'bitter', 'glum', 'gloomy', 'dejected', 'sorry', 'melancholy', 'Melancholy', 'upset', 'Upset', 'weeping', 'frustration', 'Frustration', 'frustrated', 'down']
encouraging_phrase = ['Hang in there!', 'You are doing great buddy!', 'Cheer up!', 'You are awesome!', 'Keep on trying!', 'You are getting better every day!', 
                     'You are really giving your best!', 'You really inspire me mate! Keep going strong!', 'I have every bit of confidence in your abilities!',]

client = discord.Client()

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = json.loads(response.text)
    quote = data[0]['q'] + " -" + data[0]['a']
    return quote

@client.event
async def on_ready():
    print("We have logged in as {}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    if any(word in message.content for word in sad_words):
        await message.channel.send(random.choice(encouraging_phrase))
        
client.run(os.environ.get('TOKEN'))