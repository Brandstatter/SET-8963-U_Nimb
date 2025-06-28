import discord
from clientConfig import client

@client.slash_command(
    name = "help",
    description = "Comando de ajuda do bot",
)
async def help(ctx):
    for command in client.all_commands:
        print(command)
    