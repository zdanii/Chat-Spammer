import time
import os
import pyautogui


os.system('cls;clear & title d4#9944 ON TOP')
print("""

            ████████╗███████╗██╗  ██╗████████╗                
            ╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝                
               ██║   █████╗   ╚███╔╝    ██║                   
               ██║   ██╔══╝   ██╔██╗    ██║                   
               ██║   ███████╗██╔╝ ██╗   ██║                   
               ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝                   
                                                              
███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                              
                    Made by d4#9944
       PLEASE use this for EDUCATIONAL PURPOSES ONLY!                                                                                                                              

""")

message = input("What Message would you like to spam? ") 
repeats = int(input("How many times would you like to send this message? "))
delay = int(input("How many ms do you want to wait in between each message being sent? "))

isloaded = input("Before your start, please get ready your chat box then, then press ENTER to start your spam")

print ("YOU HAVE 5 SECONDS BEFORE THE SPAM")
time.sleep (5)

for i in range (0,repeats):
    if message !="":
            pyautogui.typewrite(message)
            pyautogui.press("Enter")
    else:
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press ("enter")

    time.sleep(delay/1000)
print("SPAM SUCCESSFUL\n")
