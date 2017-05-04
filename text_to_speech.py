import os, time

def robot(text):
    os.system("espeak ' " + text + " ' ")


while True:
    talk = input('>>> ')
    robot(' ' + talk)
