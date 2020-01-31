##Modules to import##
import os, time

##Use and call to modules##
def robot(text):
    os.system("espeak ' " + text + " ' ")

##Continues The Program By Requestinng a new input infinitly##
while True:
    talk = input('>>> ')
    robot(' ' + talk)
