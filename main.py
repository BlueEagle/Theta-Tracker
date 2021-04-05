#!/usr/bin/env python3
import os, yaml

DEBUG_MODE = True
running = True

def dprint(text):
    if DEBUG_MODE:
        print(text)


def isSetup():
    fileExists = os.path.isfile(".tdata.yml")
    if fileExists:
        dprint("Theta coin data found.")
    else:
        dprint("No coin data found.")
    return fileExists

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def greeter():
    if not isSetup():
        # Begin set up sequence
    else:
        # Greet the user

while(running):
    # Clear the screen
    clear()

    # Print appropriate text to greet the user

    # Wait for input from the user to begin another phase of the menu