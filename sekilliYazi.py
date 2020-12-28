import os
from pyfiglet import Figlet


def sekilli_yaz(yazi):
    cool_text = Figlet(font="slant")
    os.system("cls")
    os.system('mode con: cols=75 lines=30')
    return str(cool_text.renderText(yazi))


if __name__ == '__main__':
    print(sekilli_yaz(("Tekno_lover")))
