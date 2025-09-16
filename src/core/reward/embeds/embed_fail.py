import discord

def embed_fail():
    embed = discord.Embed(
        title="Sem prêmios",
        description="A aventura não rendeu nenhum tesouro. O grupo de aventureiros volta de mãos vazias.",
        color=discord.Color.red()
    )

    return embed