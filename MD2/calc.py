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


def parbaudit_ievadi(ievade):
    
    def check_float(arg):
        if arg.isnumeric():
            return float(arg)
        else:
            exit()
        

    if ievade == '+':
        skaitlis_1 = input("Ievadīt pirmo vērtību summēšanai:")
        skaitlis_1 = check_float( skaitlis_1 )
        skaitlis_2 = input("Ievadīt otro vērtību summēšanai:")
        skaitlis_2 = check_float( skaitlis_2 )
        print("rezultāts: ", summa(skaitlis_1,skaitlis_2))
    elif ievade == '-':
        skaitlis_1 = input("Ievadīt pirmo vērtību atņemšanai:")
        skaitlis_1 = check_float( skaitlis_1 )
        skaitlis_2 = input("Ievadīt otro vērtību atņemšanai:")
        skaitlis_2 = check_float( skaitlis_2 )
        print("rezultāts: ", atnemsana(skaitlis_1,skaitlis_2))
    elif ievade == '*':
        skaitlis_1 = input("Ievadīt pirmo vērtību multiplicēšanai:")
        skaitlis_1 = check_float( skaitlis_1 )
        skaitlis_2 = input("Ievadīt otro vērtību multiplicēšanai:")
        skaitlis_2 = check_float( skaitlis_2 )
        print("rezultāts: ", multiplikacija(skaitlis_1,skaitlis_2))
    elif ievade == '/':
        skaitlis_1 = input("Ievadīt pirmo vērtību dalīšanai:")
        skaitlis_1 = check_float( skaitlis_1 )
        skaitlis_2 = input("Ievadīt otro vērtību dalīšanai:")
        skaitlis_2 = check_float( skaitlis_2 )
        print("rezultāts: ", dalisana(skaitlis_1,skaitlis_2)) 
    elif ievade == 'eksp':
        skaitlis_1 = input("Ievadīt bāzes vērtību eksponentai:")
        skaitlis_1 = check_float( skaitlis_1 )
        skaitlis_2 = input("Ievadīt pakāpes vērtību eksponentai:")
        skaitlis_2 = check_float( skaitlis_2 )
        print("rezultāts: ", eksponenta(skaitlis_1,skaitlis_2)) 
    else:
        print("operācija nav atrasta. Izvēlēties  [+ , - , * , / , eksp  ]")
        exit()

if __name__ == "__main__":
    print("Testē funkciju: ", __name__)
    assert summa(1,2) == 3
    assert atnemsana(3,1) == 2
    assert multiplikacija(1,2) == 2
    assert dalisana(2,2) == 1
    assert eksponenta(2,2) == 4