import os
import yagmail
from dotenv import load_dotenv

def configure():
    load_dotenv()

load_dotenv()

async def sugestion(ctx):
    print(str(ctx.message.author))
    print(str(ctx.message.content))
    SUBJECT = "Sugestão de Feature - " + str(ctx.message.author)
    TEXT= str(ctx.message.content)

    yag = yagmail.SMTP(os.getenv("emailSender"), os.getenv("emailPassword"))
    yag.send(os.getenv("emailReciever"), SUBJECT, TEXT)
