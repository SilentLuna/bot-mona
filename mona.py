import os

import discord

import asyncio

from discord.ext import commands

bot = commands.Bot(command_prefix='!')

game = discord.Game("You must be tired.")

@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    await bot.change_presence(status=discord.Status.online, activity=game)

bot.run(token)
