import discord

from discord.ui import View 
from clientConfig import client
from core.quality.service import feature, bug, suggestion

@client.slash_command(
    name = "feedback",
    description = "Comando para sugerir melhorias, novas features ou reportar bugs no bot.",
)
async def slash_feedback(ctx, 
    feedback_option : str = discord.Option(str, choices = ["Feature", "Bug", "Sugestão"])
    ):
    original_author = ctx.author
    if feedback_option == "Feature":
        await ctx.respond("Por favor escreva qual a feature você gostaria que fosse adicionado no Magic Madness. Não esqueça de descrever oque a feature deve realizar.")
        msg = await client.wait_for("message")
        if original_author == msg.author:
            await feature(msg)
    elif feedback_option == "Bug":
        await ctx.respond("Por favor informe qual o comando que o bug se encontra e descreva oque está acontecendo.")
        msg = await client.wait_for("message")
        if original_author == msg.author:
            await bug(msg)
    else:
        await ctx.respond("Por favor informe o comando e como podemos melhorar a sua experiencia.")
        msg = await client.wait_for("message")
        if original_author == msg.author:
            await suggestion(msg)