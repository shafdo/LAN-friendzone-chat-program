import socket
from termcolor import cprint,colored
import threading
import sys
import platform
import os
import time




if platform.system() == "Windows":
	clear = lambda:os.system("cls")

if platform.system() == "Linux":
	clear = lambda:os.system("clear")



cprint("[!] Enter your Profile name: ","green",end="")
name = input()



s = socket.socket()
s.bind(("",80))
# cprint('Waiting For Connection','white','on_green',["blink"])
cprint('Waiting For Connection',"blue")

s.listen(5)

session,addr = s.accept()
cprint("[*] Incomming Connection","white","on_green")
time.sleep(2)
clear()


cprint("Connection Established\n","white","on_cyan",["blink"])
cprint("Chat Program Activated ! Profile name %s\n"%(name),"white","on_yellow",["bold"])
cprint('[NOTE] Type "Bye" or "Exit" to quit Chat Program\n',"green")

session.send(name.encode())
partner = session.recv(1024).decode("utf-8")
outing = partner+" ---> Bye"

cprint("Emoji's You Like","white")
print("""
	
	😀 😁 😂 🤣 😃 😄 😅 😆 😉 😊 😋 😎 😍 😘 🥰 😗
	😙 😚 ☺️ 🙂 🤗 🥴 🤩 🤔 🤨 😐 😑 😶 🙄 😏 😣 😥 
	😮 🤐 😯 😪 😫 😴 😌 😛 😜 😝 😒 🤭 🥵 🥶 😳 🤪 
	😵 😡 😠 🤬 😷 🤒 🤕 🤢 🤮 🤧 😇 🤠 🤡 🥳 😓 😔 
	🥴 🤪 😕 🙃 🤑 😲 ☹️ 🙁 😖 😞 😟 😤 😢 😭 😦 😧 
	😨 😩 🤯 😬 😰 😱 🥳 😵 😈 👹 👺 💀 👻 👽 🤖 💩 

""")


def sending():
	try:
		while True:
			#sending
			msg = input()

			if msg == "Exit" or msg == "exit" or msg == "bye" or msg  == "Bye":
				msg = name+" ---> Bye"
				session.send(msg.encode())
				cprint("\nConnection Closed","white","on_red",["blink"])
				break
			msg = "[+] "+name+" --> "+msg
			session.send(msg.encode())
			msg = ''

		session.close()
		sys.exit()

	except:
		sys.exit()


def receving():
	try:
		while True:
			#recving
			text = session.recv(1024).decode("utf-8")
			if outing ==  text:
				print(text)
				cprint("\nConnection Closed","white","on_red",["blink"])
				break

			cprint(text,"magenta")

		session.close()
		sys.exit()

	except:
		sys.exit()







t1 = threading.Thread(target=sending)
t2 = threading.Thread(target=receving)

t1.start()
t2.start()

