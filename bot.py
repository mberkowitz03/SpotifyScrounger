# bot.py
import os
import random
from dotenv import load_dotenv


from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='join', help='Joins voice channel of sender')
async def join(ctx):
    if ctx.voice_client is None:
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await ctx.message.add_reaction('👋')
            await channel.connect()
        else:
            await ctx.send("You have to be in a voice channel to invite me!")
    else:
        await ctx.send("I'm already in a voice channel, Sorry!")

@bot.command(name='leave', help='Leaves the current voice channel')
async def leave(ctx):
    if ctx.voice_client and ctx.author.voice:
        await ctx.voice_client.disconnect()
        await ctx.message.add_reaction('👋')
    else:
        await ctx.send('I\'m not in a voice channel at the moment!')

bot.run(TOKEN)