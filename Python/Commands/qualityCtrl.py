import os
import yagmail
from dotenv import load_dotenv



def configure():
    load_dotenv()

load_dotenv()

#TODO Tirar dependencia do Yagmail.
#TODO Adicionar envio do Feedback para banco de dados.
async def suggestion(ctx):
    SUBJECT = "Sugestão de Melhoria - " + str(ctx.author)
    TEXT= str(ctx.content)

    yag = yagmail.SMTP(os.getenv("emailSender"), os.getenv("emailPassword"))
    yag.send(os.getenv("emailReciever"), SUBJECT, TEXT)

async def bug(ctx):
    SUBJECT = "Bug reportado - " + str(ctx.author)
    TEXT= str(ctx.content)

    yag = yagmail.SMTP(os.getenv("emailSender"), os.getenv("emailPassword"))
    yag.send(os.getenv("emailReciever"), SUBJECT, TEXT)

async def feature(ctx):
    SUBJECT = "Sugestão de Feature - " + str(ctx.author)
    TEXT= str(ctx.content)

    yag = yagmail.SMTP(os.getenv("emailSender"), os.getenv("emailPassword"))
    yag.send(os.getenv("emailReciever"), SUBJECT, TEXT)