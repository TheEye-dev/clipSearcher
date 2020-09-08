import sys
import webbrowser
from time import *
from colorama import Fore
from os import system, name

def downloadAnimate() :
    animation = ["%10[■□□□□□□□□□]","%20[■■□□□□□□□□]", "%30[■■■□□□□□□□]", "%40[■■■■□□□□□□]", "%50[■■■■■□□□□□]", "%60[■■■■■■□□□□]", "%70[■■■■■■■□□□]", "%80[■■■■■■■■□□]", "%90[■■■■■■■■■□]", "%100[■■■■■■■■■■]"]

    for i in range(len(animation)):
        sleep(0.9)
        sys.stdout.write("\r\t" + Fore.RED + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")

def clear() :

    ## for windows
    if name == 'nt' :
        clearWindows = system('cls')

    ## for mac and linux(here os.name is 'posix')
    else :
        clearLinuxMac = system('clear')


def rerunProgram() :
    print(Fore.LIGHTCYAN_EX + "\n\n=================")
    print(Fore.LIGHTCYAN_EX + "1 = Yes : 0 = No")
    userChoose = int(input(Fore.CYAN + "Re-Run The Program (1/0) : "))
    if userChoose == 1 :
        sleep(2.5)
        clear()
        searchForClips()

    elif userChoose == 0 :
        print(Fore.YELLOW + "\n[#] See You Soon")
        sleep(1.0)
        quit()

    else :
        print(Fore.LIGHTMAGENTA_EX + "\n[!] Choose Correctly")
        sleep(1.0)
        clear()
        rerunProgram()


def searchForClips() :
    print(Fore.LIGHTGREEN_EX + """
   =======[ $$ Clip Channels $$ ]=======
--------------------------------------------
| [1] Netflix           [2] 20th Century   |
|------------------------------------------|
| [3] IGnoxboek3g       [4] Thorny Rose    |
|------------------------------------------|
|             [5] LionsGate                |
--------------------------------------------
""")
    userChannelChoice = input(Fore.LIGHTGREEN_EX + "\t\nChoose Channel : ")
    userCharacterChoice = input(Fore.LIGHTGREEN_EX + "Choose Character : ")

    if userChannelChoice == '1' :
        sleep(1.0)
        clear()

        print(Fore.LIGHTRED_EX + "[+] Channel : Netflix")
        print(Fore.LIGHTRED_EX + "[+] Character : ", userCharacterChoice)

        print("\n     Searching For Result ..")
        sleep(0.2)
        downloadAnimate()
        sleep(1.0)

        webbrowser.open_new("https://www.youtube.com/c/Netflix/search?query=" + userCharacterChoice)

        rerunProgram()

    elif userChannelChoice == '2' :
        sleep(1.0)
        clear()

        print(Fore.LIGHTRED_EX + "[+] Channel : 20th Century Studio")
        print(Fore.LIGHTRED_EX + "[+] Character : ", userCharacterChoice)

        print("\n     Searching For Result ..")
        sleep(0.2)
        downloadAnimate()
        sleep(1.0)

        webbrowser.open_new("https://www.youtube.com/c/20thCenturyStudios/search?query=" + userCharacterChoice)

        rerunProgram()

    elif userChannelChoice == '3' :
        sleep(1.0)
        clear()

        print(Fore.LIGHTRED_EX + "[+] Channel : IGnoxboek3g Channel")
        print(Fore.LIGHTRED_EX + "[+] Character : ", userCharacterChoice)

        print("\n     Searching For Result ..")
        sleep(0.2)
        downloadAnimate()
        sleep(1.0)

        webbrowser.open_new("https://www.youtube.com/channel/UCovlJRl7OeQAiIOGeHTC9qw/search?query=" + userCharacterChoice)

        rerunProgram()

    elif userChannelChoice == '4' :
        sleep(1.0)
        clear()

        print(Fore.LIGHTRED_EX + "[+] Channel : Thorny Rose Channel")
        print(Fore.LIGHTRED_EX + "[+] Character : ", userCharacterChoice)

        print("\n     Searching For Result ..")
        sleep(0.2)
        downloadAnimate()
        sleep(1.0)

        webbrowser.open_new("https://www.youtube.com/c/ThornyRose13/search?query=" + userCharacterChoice)

        rerunProgram()

    elif userChannelChoice == '5' :
        sleep(1.0)
        clear()

        print(Fore.LIGHTRED_EX + "[+] Channel : LionsGate Movies")
        print(Fore.LIGHTRED_EX + "[+] Character : ", userCharacterChoice)

        print("\n     Searching For Result ..")
        sleep(0.2)
        downloadAnimate()
        sleep(1.0)

        webbrowser.open_new("https://www.youtube.com/c/LionsgateMovies/search?query=" + userCharacterChoice)

        rerunProgram()

    else :
        print(Fore.RED + "\n\t\t[ Choose Correctly ]")
        sleep(1.5)
        clear()
        searchForClips()

searchForClips()
rerunProgram()