#!/usr/bin/env python3
import os, yaml

DATA_FILE_NAME = ".tdata.yml"
DEBUG_MODE = True
running = True
theta_amount = None

def dprint(text):
    if DEBUG_MODE:
        print(text)


def isSetup():
    fileExists = os.path.isfile(DATA_FILE_NAME)
    if fileExists:
        dprint("Theta coin data found.")
        with open(DATA_FILE_NAME) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            theta_amount = data['theta_amount']
            dprint(f"Data found in file is as follows:\n{data}")
            dprint(f"Theta_amount data type is: {type(theta_amount)}")
            dprint(f"Theta: {theta_amount}")
    else:
        dprint("No coin data found.")
    return fileExists

def setup():
    print("Welcome to setup!")
    theta_amount = int(input("Please enter how much Theta coin you have: "))
    dprint("Create data file.")
    with open(DATA_FILE_NAME, 'w') as f:
        documents = yaml.dump({'theta_amount': theta_amount}, f)
        dprint(f"File written.\n{documents}")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def user_wait():
    t = input()
    
def greeter():
    if not isSetup():
        #@TODO implement
        # Begin set up sequence
        dprint("Begin the set up")
        setup()
    else:
        #@TODO implement
        # Greet the user
        dprint("Greet the user.")
        print(f"Theta logged: {theta_amount}")
        user_wait()

while(running):
    # Clear the screen
    clear()

    # Print appropriate text to greet the user
    greeter()