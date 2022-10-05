import calc
import sys

def check_float(arg):
    if arg.isnumeric():
        return float(arg)
    else:
        exit()
        

num1 = sys.argv[1]
oper = sys.argv[2]
num2 = sys.argv[3]

num1 = check_float(num1)
num2 = check_float(num2)

if oper == '+':
        print("rezultāts: ", calc.summa(num1, num2))
elif oper == '-':
        print("rezultāts: ", calc.atnemsana(num1, num2))
elif oper == '*':
        print("rezultāts: ", calc.multiplikacija(num1, num2))
elif oper == '/':
        print("rezultāts: ", calc.dalisana(num1, num2)) 
elif oper == 'eksp':
        print("rezultāts: ", calc.eksponenta(num1, num2)) 
else:
    exit()
