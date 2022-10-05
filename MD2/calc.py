#!/usr/bin/env python3

def summa(arg1, arg2):
    return arg1 + arg2
    
def atnemsana(arg1, arg2):
    return arg1 - arg2

def multiplikacija(arg1, arg2):
    return arg1 * arg2

def dalisana(arg1, arg2):
    return arg1 / arg2

def eksponenta(arg1, arg2):
    return arg1 ** arg2


if __name__ == "__main__":
    print("Testē funkciju: ", __name__)
    assert summa(1,2) == 3
    assert atnemsana(3,1) == 2
    assert multiplikacija(1,2) == 2
    assert dalisana(2,2) == 1
    assert eksponenta(2,2) == 4