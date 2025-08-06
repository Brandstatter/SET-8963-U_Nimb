import discord

def embed_fail():
    embed = discord.Embed(
        title="Sem prêmios",
        description="Precisa de descrição",
        color=discord.Color.red()
    )

    return embed