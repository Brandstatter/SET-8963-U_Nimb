import discord

# async def embed_help():
#     help = discord.Embed(
#         title = "Comandos de Prefixo (T)",
#         description= """
#         **Te** ou **Tmagia** + **nome da magia** - Retorna informações sobre a magia. \n
#         **Tl** ou **Trandom** - Retorna uma magia aleatoria.\n
#         **Tcond** + **nome da condição** - Retorna informações sobre a condição. \n
#         **Tr**, **Traças** ou **Traces** - Selecione uma raça para receber as habilidades racias melhoras de atributos da raça selecionada.\n
#         **TD** ou **Tdice** + **Numero de dados** + **Valor dos dados** + **Bonus** - Rola dados de acordo com parametros passados.\n
#         **Tf** ou **report** - Comando para reportar um bug, sugerir melhoria ou uma nova feature para o bot.\n
#         """
#     )
#     return help

def embed_help_command(client: discord.Bot):
    embedCommands = discord.Embed(
        title="Comandos do bot",
        description="Slash commands configurados no bot",
        color=discord.Color.random(),
        footer=discord.EmbedFooter(
            text="v1.0.0"
        )
    )

    embedCommands.add_field(name="\u200b", value="\u200b", inline=False)

    for command in client.application_commands:
        embedCommands.add_field(
            name=command.name,
            value=command.description,
            inline=False
        )
    
    embedCommands.add_field(name="\u200b", value="\u200b", inline=False)
    return embedCommands