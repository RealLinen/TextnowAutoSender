import pytextnow ; import http; import threading; import os
from essential_generators import DocumentGenerator ; from datetime import datetime, timezone, timedelta ; from flask import Flask
#=======================================#
def setInterval(func , time, *arguments):
    e = threading.Event()
    while not e.wait(time):
        func(*arguments)
#=======================================#
textnowUsername = "<textnowusername>"
textnowsid_cookie = "<textnowsidcookie>"
textnowcsrf_cookie = "<textnowcsrf_cookie>"
#=======================================#
Generator = DocumentGenerator()
Format = format
webServer = Flask(__name__)

ESTTime = datetime.now(timezone(timedelta(hours=-4), 'EST'))
client = pytextnow.Client(textnowUsername, sid_cookie=textnowsid_cookie, csrf_cookie=textnowcsrf_cookie)
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
