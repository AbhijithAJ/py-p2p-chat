import eel,socket
from threading import *

HOST = input("enter ip address or press enter to take default (127.0.0.1)").strip() or "127.0.0.1"
PORT = input("enter port number or press enter to take default (5000) :").strip().isnumeric() or 5000 

# Set web files folder
eel.init('web')
def send_to_java(data):    # send to js
    eel.serverResponse_js(data)
def alertraise_js(data):
    eel.alertfrmserver_js(data)

data_to_send =[]

@eel.expose                         # Expose this function to Javascript
def clientInput_py(data):
    print(data)
    data_to_send.append(data)
    try:
        for data in range(len(data_to_send)):
            x = data_to_send.pop(0)
            s.send(x.encode())                        
    except:
        data_to_send.insert(0,x)
        print("no connection")

def start_eel():
    eel.start('chat_client.html', size=(1000, 600))    # Start

try:        
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    t = Thread(target = start_eel,args=())
    t.start()
except Exception as n:
    print(n)
    input()

while 1:
    try:
        msg=s.recv(1024).decode()
        send_to_java(msg)
    except Exception as n:
        print(n)
        input()