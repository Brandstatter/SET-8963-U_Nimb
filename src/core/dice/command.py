import discord
from clientConfig import client
from core.dice.service import roll_dice, range_roll

@client.slash_command(
    name = "dados",
    description = "Rolagem de dados."
)
async def slash_dice(
    ctx,
    quantidade: int = discord.Option(int, description="Quantidade"),
    dados: int = discord.Option(int ,description="Dados"),
    bonus: int = discord.Option(int, description="Bônus (opcional)")
):
    await ctx.respond(embed = await roll_dice(ctx, dados, quantidade, bonus))

@client.slash_command(
    name = "range_roll",
    description = "Escolhe um numero entre range informado pelo jogador.",
)
async def slash_rangeRoll(ctx,
    numero1: int = discord.Option(int), 
    numero2: int = discord.Option(int)
):
    await ctx.respond(embed = await range_roll(ctx, numero1, numero2))