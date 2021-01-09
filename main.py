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
    await message.channel.send('**Commands**\n`quote` - get a random quote\n`quote help` - bot information\n`quote daily` - set up or manage daily quotes in a specific channel\n`quote upvote` - if you like the bot, upvote it\n`quote contact` - contact the developer\n`quote ping` - ping the bot, and get back a pong')

  if message.content == ('quote daily'):
    await message.channel.send('Daily quotes are currently under development. When they\'re done, you\'ll be able to pick a channel the the frequency for the quotes to be posted in.')

  if message.content == ('quote contact'):
    await message.channel.send('If you need help with or have questions about the bot, you can join the server for the bot (https://discord.gg/8Vu6X4CH3k) or contact the developer (dt#6595).')

  if message.content == ('quote ping'):
    await message.channel.send('Pong! :ping_pong:')

  if message.content == ('quote upvote'):
    await message.channel.send('If you like the bot, or want to leave a review, you can do so here: https://top.gg/bot/794288033927135302. You can also say `quote contact` to get an invite link to a server dedicated for the bot.')

@client.event
async def on_guild_join(Guild):
  await Guild.system_channel.send('Hello! Thank you for adding me to your server. You can say `quote` to get a random quote, or `quote help` for more commands.')

keep_alive()
client.run(os.getenv('TOKEN'))
