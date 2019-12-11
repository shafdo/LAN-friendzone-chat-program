import socket
import threading
import sys
from termcolor import cprint,colored
import platform
import os
import time



if platform.system() == "Windows":
	clear = lambda:os.system("cls")

if platform.system() == "Linux":
	clear = lambda:os.system("clear")



cprint("[!] Enter your Profile name: ","green",end="")
name = input()

cprint("[!] Enter your Friend's Local IP: ","green",end="")
hisip = input()


cprint("\n[*] Connecting Hold On","white","on_green")



s = socket.socket()
s.connect((hisip,80))
time.sleep(2)
clear()
cprint("Connection Established\n","white","on_cyan",["blink"])
cprint("Chat Program Activated ! Profile name %s\n"%(name),"white","on_yellow",["bold"])
cprint('[NOTE] Type "Bye" or "Exit" to quit Chat Program\n\n',"green")

partner = s.recv(1024).decode("utf-8")
s.send(name.encode())
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
				s.send(msg.encode())
				cprint("\nConnection Closed","white","on_red",["blink"])
				s.close()
				break


			msg = "[+] "+name+" --> "+msg
			s.send(msg.encode())
			msg = ''

	except:
		sys.exit()


def receving():
	try:
		while True:
			#recving
			text = s.recv(1024).decode("utf-8")
			if outing == text:
				print(text)
				cprint("\nConnection Closed","white","on_red",["blink"])
				s.close()
				break

			cprint(text,"green")

	except:
		sys.exit()


t1 = threading.Thread(target=sending)
t2 = threading.Thread(target=receving)

t1.start()
t2.start()


