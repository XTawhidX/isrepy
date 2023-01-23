import os
import discord
from discord.ext import commands
from keep_alive import keep_alive
from discord.ext.commands import Bot

intents = discord.Intents.all()

bot = commands.Bot(intents=discord.Intents.all(),
                   command_prefix="!",
                   description='The Best Bot For the Best User!')


@bot.event
async def on_ready():
  print('Autoreact ready...')


@bot.event
async def on_message(message):
  # Channel IDs for the channels where the bot should add reactions
  channel_ids = [
    952294553078104125, 952289028978393118, 952294613819981846,
    952293983118315641, 952296775966945371, 952294832745897984
  ]

  if message.channel.id in channel_ids:
    await message.add_reaction("<:verify:919867240881487882>")
    await message.add_reaction("<:Rainbow_Heart:951077755108343808>")
    await message.add_reaction("<:VOXCGifEmojileri41:951077674120527892>")
    await message.add_reaction("<:Is: 909520183939461243>")
    await message.add_reaction("<:heart_:930165098939576371>")


keep_alive()
bot.run("")
