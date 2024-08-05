import asyncio
import discord
from discord.ext import commands, tasks
import random
import logging
import config


intents = discord.Intents.all()
intents.message_content = True
intents.members = True
intents.guilds = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

@bot.command(name='sync', description='Owner only')
async def sync(ctx):
    await bot.tree.sync()
    logging.info('Command tree synced.')

@bot.event
async def on_ready():
    update_status.start()
    logging.info(f'We are logged in as {bot.user.name}')
    await bot.load_extension("cogs.ErrorHandeling")
    await bot.load_extension("cogs.General")


@tasks.loop(minutes=5)
async def update_status():
    for guild in bot.guilds:
        total_members = guild.member_count
        status1 = f"{total_members} Members"
        await bot.change_presence(activity=discord.Game(name=status1))
        await asyncio.sleep(180)  # Waits 3 minutes
        status2 = f"I am a tutorial bot by maxiroe"
        await bot.change_presence(activity=discord.Game(name=status2))
        await asyncio.sleep(180)  # Waits 3 minutes



bot.run(config.TOKEN)
