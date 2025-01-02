# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot=commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
   print(f'{bot.user} has connected to discord!')

@bot.event
async def on_message(message):
   if message.author==bot.user:
      return
   if 'наблюдатель' in message.content.lower():
    await message.channel.send(f'привет {message.author.mention}')
    return
   if message.content.startswith('!'):
      await bot.process_commands(message)
      return
   #await message.channel.send('hey')

@bot.command()
async def ping(ctx):
  await ctx.send('help yourself')

bot.run(TOKEN)