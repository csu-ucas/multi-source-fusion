import socket 
import json 
import datetime

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.bind(("localhost", 60000))
skt.listen()

tmprt = -65536
humid = -65536
firdt = False 

while True:
    conn = skt.accept()
    msg = str(conn[0].recv(1024).decode())
    if not msg:
        continue 
    else:
        msg_tup = msg[1:len(msg)-1].split(', ')
        
        print(msg_tup)
        if msg_tup[0] == "'DTH'":
            # print(msg[0])
            # print(msg[1])
            # print(msg[2])
            # print(msg[3])
            tmprt = float(msg_tup[2])
            humid = float(msg_tup[3])
        elif msg_tup[0] == "'FireSuspect'":
            
            firdt = (msg_tup[1] == 'True')
            print(firdt)
        if firdt and (tmprt >= 27):
            print("Fire Detected: %s"%datetime.datetime.now())
        elif (not firdt) and (tmprt >=27):
            print("Suspicious temperature augmentation: %s"%datetime.datetime.now())
        else:
            print("No Fire Detected: %s"%datetime.datetime.now())
            

        # print(msg_tup[0])
        conn[0].shutdown(0)
