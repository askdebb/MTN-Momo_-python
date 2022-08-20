import numpy as np

def mtn_MOMO_Registered_user(splitter):
    index_size_counter = 0
    regUser = []
    regUser.append(splitter)
    index_size_counter+1
        
def mtn_MOMO_Registered_user_pin(pin_number):
    index_size = 10
    regUserPin = []
    for i in range(index_size):
        regUserPin.append(pin_number)
    return regUserPin

def no_int_begins(registeredUser):
    splitter =[registeredUser]
    bugger = [char for char in splitter[0]]
    bug = input(bugger[0])
    
    size_splitter_carries = len(bugger)
    for i in range(size_splitter_carries):
        if bugger[0] == '0 - 9':
            print("started with a number")
        else:
            return splitter