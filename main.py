import discord
import os
import requests
import json
from keep_alive import keep_alive

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "\n - " + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('{0.user} is alive!'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content == ('quote'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content == ('quote help'):
    await message.channel.send('**Commands**\n`quote` - get a random quote\n`quote help` - bot information')

keep_alive()
client.run(os.getenv('TOKEN'))
