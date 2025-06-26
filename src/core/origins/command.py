import discord

from clientConfig import client
from core.origins.service import slash_search, embed_origin

origins = ['Acólito', 'Amigo dos Animais', 'Amnésico', 'Aristocrata', 'Artesão', 'Artista', 'Assistente de Laboratório', 'Batedor', 'Capanga', 'Charlatão', 'Circense', 'Criminoso', 'Curandeiro', 'Eremita', 'Escravo', 'Estudioso', 'Fazendeiro', 'Forasteiro', 'Gladiador', 'Guarda', 'Herdeiro', 'Herói Camponês', 'Marujo', 'Mateiro', 'Membro de Guilda', 'Mercador', 'Minerador', 'Nômade', 'Pivete', 'Refugiado', 'Seguidor', 'Selvagem', 'Soldado', 'Taverneiro', 'Trabalhador', 'Bacharel', 'Boticário', 'Caçador de Ratos', 'Cão de Briga', 'Carcereiro', 'Carpinteiro de Guilda', 'Catador da Catástrofe', 'Chef Hynne', 'Cirurgião-Barbeiro', 'Citadino Abastado', 'Cocheiro', 'Construtor', 'Contrabandista', 'Coureiro', 'Escriba', 'Espião', 'Ferreiro Militar', 'Freira', 'Goradista', 'Insciente', 'Interrogador', 'Ladrão de Túmulos', 'Menestrel', 'Mensageiro', 'Náufrago', 'Padeiro', 'Pedinte', 'Pescador', 'Servo', 'Suporte de Tropas', 'Agricultor Sambur - Regional(Sambúrdia)', 'Amazona de Hippion - Regional(Deheon, Namalkah)', 'Amoque Púrpura - Regional(Ermos Púrpuras)', 'Anão de Armas - Regional(Doherimm)', 'Andarilho Ubaneri - Regional(Ubani)', 'Aprendiz de Dragoeiro - Regional(Sckharshantallas)', 'Aprendiz de Drogadora - Regional(Galrasia)', "Aristocrata Dai'zenshi - Regional(Tamu-ra)", 'Armeiro Armado - Regional(Zakharov)', 'Aspirante a herói - Regional(Deheon)', 'Assistente Forense - Regional(Salistick)', 'Bandoleiro da Fortaleza - Regional(Khalifor)', 'Barão Arruinado - Regional(Trebuck)', 'Catador da Cidade Velha - Regional(Nova Malpetrim)', 'Cativo das Fadas - Regional(Pondsmânia)', 'Competidor do Circuito - Regional(Trebuck)', 'Cosmopolita - Regional(Valkaria)', 'Cria da Favela - Regional(Valkaria)', 'Criado pelas Voracis - Regional(Galrasia)', 'De Outro Mundo - Regional(Éter Divino)', 'Descendente colleniano - Regional(Ahlen)', 'Desertor da Supremacia - Regional(Supremacia)']
async def autocomplete_origin(ctx: discord.AutocompleteContext):
    return [origin for origin in origins]

@client.slash_command(
    name = "origins",
    description = "Informa beneficios e itens da origem selecionada.",
    guild_ids = [474008663174938637,783489084848209940,873471117514403840,1252699400334217389,1354173016157982850,563153398392684554,1380775370856595537]
)
async def slash_origins(ctx,
    origem: str = discord.Option(str, "Pick a color!", autocomplete=autocomplete_origin)                 
):
    
    id = await slash_search(ctx, origem)
    embed = await embed_origin(id)
    await ctx.respond(embed = embed)