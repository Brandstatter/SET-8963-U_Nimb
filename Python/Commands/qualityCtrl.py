import os
import yagmail
from dotenv import load_dotenv


def configure():
    load_dotenv()

load_dotenv()

#TODO Tirar dependencia do Yagmail.
#TODO Adicionar envio do Feedback para banco de dados.
async def suggestion(ctx):
    subject = "Sugestão de Melhoria - " + str(ctx.author)
    text= str(ctx.content)

    yag = yagmail.SMTP(os.getenv("emailSender"), os.getenv("emailPassword"))
    yag.send(os.getenv("emailReciever"), subject, text)

async def bug(ctx):
    subject = "Bug reportado - " + str(ctx.author)
    text = str(ctx.content)

    yag = yagmail.SMTP(os.getenv("emailSender"), os.getenv("emailPassword"))
    yag.send(os.getenv("emailReciever"), subject, text)

async def feature(ctx):
    subject = "Sugestão de Feature - " + str(ctx.author)
    text= str(ctx.content)

    yag = yagmail.SMTP(os.getenv("emailSender"), os.getenv("emailPassword"))
    yag.send(os.getenv("emailReciever"), subject, text)