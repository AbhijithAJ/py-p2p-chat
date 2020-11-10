import socket,eel
from threading import *
import time

# get the hostname
host = input("enter ip address or press enter to take default (127.0.0.1)").strip() or "127.0.0.1"
port = input("enter port number or press enter to take default (5000) :").strip().isnumeric() or 5000  # initiate port no above 1024
# Set web files folder
eel.init('web')

def send_to_js(data):               # send to js
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
            conn.send(x.encode())    
            time.sleep(0.01)                             
    except:
        alertraise_js("not connected to client")
        data_to_send.insert(0,x)
        print("no connection")

def start_eel():
    eel.start('chat_server.html', size=(1000, 600),port=8001)    # Start

try:
    t = Thread(target = start_eel,args=())
    t.start()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))  # bind host address and port together

    s.listen(1)
    conn, address = s.accept()  # accept new connection
except Exception as n:
    print(n)
    input()

print("Connection from: " + str(address))
alertraise_js("connected to"+str(address))
while True:
   # receive data stream. it won't accept data packet greater than 1024 bytes
    try:
        data = conn.recv(1024).decode()
        send_to_js(data)
        if data:
            print("from connected user: " + str(data))
    except:
        alertraise_js("connection terminated by client. plz restart application")