import discord
from clientConfig import client
from core.help.service import embed_help_command

@client.slash_command(
    name = "help",
    description = "Comando de ajuda do bot",
)
async def help(ctx):
    embedMessage = embed_help_command(client)
    return await ctx.respond(embed = embedMessage)