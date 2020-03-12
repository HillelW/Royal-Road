'''functions to simulate the logic gates used inside of a computer that all of 
   our arithmetic functions are ultimately based upon'''

def AND(a, b): 
    if a == 1 and b == 1: 
        return True
    else: 
        return False

def NAND(a, b): 
    if a == 1 and b == 1: 
        return False
    else: 
        return True

def OR(a, b): 
    if a == 1: 
        return True
    elif b == 1: 
        return True
    else: 
        return False

def XOR(a, b): 
    if a != b: 
        return 1
    else: 
        return 0

def NOT(a): 
    if(a == 0): 
        return 1
    elif(a == 1): 
        return 0

def NOR(a, b): 
    if(a == 0) and (b == 0): 
        return 1
    elif(a == 0) and (b == 1): 
        return 0
    elif(a == 1) and (b == 0): 
        return 0
    elif(a == 1) and (b == 1): 
        return 0

def XNOR(a,b): 
    if(a == b): 
        return 1
    else: 
        return 0



