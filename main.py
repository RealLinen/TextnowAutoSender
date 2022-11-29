import pytextnow ; import http; import threading; import os
from essential_generators import DocumentGenerator ; from datetime import datetime, timezone, timedelta ; from flask import Flask
#=======================================#
def setInterval(func , time, *arguments):
    e = threading.Event()
    while not e.wait(time):
        func(*arguments)
#=======================================#
Generator = DocumentGenerator()
Format = format
webServer = Flask(__name__)

ESTTime = datetime.now(timezone(timedelta(hours=-4), 'EST'))
client = pytextnow.Client("dev.vecio", sid_cookie="s%3AsQz3eA4g0Bl01148v7juoGha6ud2ZePQ.WrI737vlQXniH5NgjkmDcvtEkiO9VyAthY0Da3kpJXQ", csrf_cookie="s%3AF8t427RI11KaeuGYRSfUUBYq.7HNkqQudB77TNv2II7LLJOAO9u7vOf1sg3wCapqK7q4")
#=======================================#
def send_message(number = "2028735033", message = False, toSend = True):
    client.send_sms("2028735033", (message or Generator.sentence()))
    print("< Textnow > | Sent message '"+message+"' | To '"+number+"'")
    return "true"
def Intv1():
    send_message("2028735033", Generator.sentence())
    send_message("2028735033", "================= | From: "+Generator.name()+"at: "+Generator.email()+" | =================")
#=======================================#
print("!<>[ Textnow Bot ]: Status = Enabled<>!")
send_message("2028735033", "< Loaded "+(ESTTime.strftime('%Y-%m-%d %H:%M:%S'))+" > | Hello how are you doing today?")
send_message("2028735033", "================= | From: "+Generator.name()+"at: "+Generator.email()+" | =================")
setInterval(Intv1, 7200)