
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="0.0.0.0"
port=1234
s.connect((host,port))
#server, addr=s.accept()
key=''

import keyboard

while True:
    if keyboard.is_pressed('a'):
        print("You pressed a arrow")
        key='a'
        s.send(bytes("{}\n".format(key), "utf-8"))
        break
    if keyboard.is_pressed('s'):
        print("You pressed s arrow")
        key = 's'
        s.send(bytes("{}\n".format(key), "utf-8"))
        break
    if keyboard.is_pressed('w'):
        print("You pressed w arrow")
        key = 'w'
        s.send(bytes("{}\n".format(key), "utf-8"))
        break
    if keyboard.is_pressed('d'):
        print("You pressed d arrow")
        key = 'd'
        s.send(bytes("{}\n".format(key), "utf-8"))
        break

# display client address

# send message to the client after
# encoding into binary string


#server.send(key)
#server.close()
#if pyautogui.click()=='left':
   # print("got here")

#if pyautogui.keyDown('left'):
    #print("here")


#print(ord('a'))
s.close()

