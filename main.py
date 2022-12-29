
from pytube import YouTube
from pathlib import Path

import time
import os
import sys

payload = """     _ __       ,----.          ,-.-.      _,---.   ,---.             ___   
  .-`.' ,`.  ,-.--` , \,-..-.-./  \==\ .-`.' ,  \ .--.'  \     .-._ .'=.'\  
 /==/, -   \|==|-  _.-`|, \=/\=|- |==|/==/_  _.-' \==\-/\ \   /==/ \|==|  | 
|==| _ .=. ||==|   `.-.|- |/ |/ , /==/==/-  '..-. /==/-|_\ |  |==|,|  / - | 
|==| , '=',/==/_ ,    / \, ,     _|==|==|_ ,    / \==\,   - \ |==|  \/  , | 
|==|-  '..'|==|    .-'  | -  -  , |==|==|   .--'  /==/ -   ,| |==|- ,   _ | 
|==|,  |   |==|_  ,`-._  \  ,  - /==/|==|-  |    /==/-  /\ - \|==| _ /\   | 
/==/ - |   /==/ ,     /  |-  /\ /==/ /==/   \    \==\ _.\=\.-'/==/  / / , / 
`--`---'   `--`-----``   `--`  `--`  `--`---'     `--`        `--`./  `--`               """

class font_colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


default = """
.----------.---------------------------.
| Commands |        Utility            |
:----------+---------------------------:
| help     | shows all of the commands |
'----------'---------------------------'\n\n\n"""


help = ("""\n\n..........................................
: Commands :           Utility           :
:..........:.............................:
: download :  Downloads a youtube video  :
:..........:.............................:\n\n
""")
def typingPrint(text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.007)
print(font_colors.OKBLUE + payload)
print(font_colors.OKGREEN + default + font_colors.FAIL)


while True:
    command= input('')
    if command == "help":
        print(help)
    if command == "download":
        typingPrint("\nEnter youtube link ( with https:// ):\n")
        link = input('\n')
        try:
                trying=  YouTube(link)
        except:
                if os ==  "nt" : os.system('cls')
                else: os.system('clear')
                typingPrint(f'{ font_colors.WARNING } /!\ This video does not exist or is not available now.{font_colors.FAIL}\n\n')
                time.sleep(2)
                continue
        typingPrint(f'\n{font_colors.BOLD}In what folder do you want to proceed to the download ? ( {font_colors.WARNING}make sure to write the exact name of you folder, else video will automatically be downloaded in your "Download" folder{font_colors.ENDC} )')
        directory = input('\n\n')
        if directory == "":
                directory = "Downloads"
            
           
                
        dir = str(os.path.join(Path.cwd())+ f'\{directory}')
        video = trying.streams.get_highest_resolution()
        typingPrint(f"\nYour video :{font_colors.HEADER} {trying.title}{font_colors.OKCYAN}, is downloading right now in highest quality !\n")
        video.download(dir)
        print(f"\nSuccessfuly downloaded the video into the {dir} folder.\n {Fore.LIGHTRED_EX}")
        time.sleep(2)
        clear()
        print(Fore.CYAN+ payload)
        print(Fore.GREEN + default +Fore.LIGHTRED_EX)
    
