import sys

def add(num1, num2):
    add= num1 + num2
    return add

num1 = float(sys.argv[1])
opr = sys.argv[2]
num2 = float(sys.argv[3])

if opr == "add":
    output = add(num1, num2)
    print("The Addition of two numbers: ", output)