import discord

from discord.ui import View 
from clientConfig import client
from core.quality.service import feature, bug, suggestion


@client.command(aliases = ['t', 'report'])
async def feedback(ctx):
    #TODO Remove buttons after being clicked
    original_author = ctx.message.author

    await ctx.send("Obrigado por nos ajudar a melhorar o Magic Madness!")
    await ctx.send("Deseja sugerir uma feature nova, reportar um bug ou dar uma sugestão de melhoria?")
    feedback_button = discord.ui.Button(label = "Feedback", style = discord.ButtonStyle.green, custom_id = 'Feedback')
    bug_button = discord.ui.Button(label = "Bug", style = discord.ButtonStyle.red, custom_id = 'Bug')
    feature_button = discord.ui.Button(label = "Feature", style = discord.ButtonStyle.green, custom_id = 'Feature')

    buttons = View()

    async def feature_ideia(self):
        await ctx.send("Por favor escreva qual a feature você gostaria que fosse adicionado no Magic Madness. Não esqueça de descrever oque a feature deve realizar.")
        msg = await client.wait_for("message")
        if original_author == msg.author:
            await feature(msg)

    async def bug_report(self):
        await ctx.send("Por favor informe qual o comando que o bug se encontra e descreva oque está acontecendo.")
        msg = await client.wait_for("message")
        if original_author == msg.author:
            await bug(msg)
    
    async def feedback(self):
        await ctx.send("Por favor informe o comando e como podemos melhorar a sua experiencia.")
        msg = await client.wait_for("message")
        if original_author == msg.author:
            await suggestion(msg)

    feature_button.callback = feature_ideia
    bug_button.callback = bug_report
    feedback_button.callback = feedback

    buttons.add_item(feature_button)
    buttons.add_item(bug_button)
    buttons.add_item(feedback_button)
    await ctx.send(view = buttons)


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