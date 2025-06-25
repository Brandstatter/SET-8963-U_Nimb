import discord
from clientConfig import client
from core.dice.service import roll_dice, range_roll

@client.slash_command(
    name = "dados",
    description = "Rolagem de dados.",
    guild_ids = [474008663174938637,783489084848209940,873471117514403840,1252699400334217389,1354173016157982850,563153398392684554,1380775370856595537]
)
async def slash_dice(
    ctx,
    quantidade: int = discord.Option(int, description="Quantidade"),
    dados: int = discord.Option(int ,description="Dados"),
    bonus: int = discord.Option(int, description="Bônus (opcional)")
):
    print(quantidade)
    print(dados)
    print(bonus)
    await ctx.respond(embed = await roll_dice(ctx, dados, quantidade, bonus))