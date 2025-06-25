import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True

activity = discord.Activity(type=discord.ActivityType.listening, name="Prefixo 'T'")
client = commands.Bot(command_prefix = "T", case_insensitive = True, activity = activity, status = discord.Status.online, intents = intents)
