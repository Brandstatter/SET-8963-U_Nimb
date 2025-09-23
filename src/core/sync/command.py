import discord

from clientConfig import client

@client.slash_command(
    name="sync",
    description="Sincroniza os comandos da aplicação. (Apenas Donos)",
    guild_ids=[563153398392684554]    
)
async def sync(ctx):
    AUTHORIZED_IDS = [211612940191793153, 196032561150033921]
    if ctx.author.id not in AUTHORIZED_IDS:
        await ctx.respond("Você não tem permissão para usar este comando!", ephemeral=True)
        return

    await ctx.defer(ephemeral=True) # Responde "pensando..." de forma privada
    try:
        await client.sync_commands()
        print("Comandos sincronizados com sucesso.")
        await ctx.respond("✅ Comandos sincronizados com sucesso!", ephemeral=True)
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")
        await ctx.respond(f"❌ Ocorreu um erro ao sincronizar: {e}", ephemeral=True)