def multy(a,b):
    return a * b

def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def dev(a,b):
    return a / b

def calculator(a,b,op):
    if op == "*":
        result = multy(a,b)
        print("the result is", result)
    if op == "-":
        result = substract(a,b)
        print("the result is", result)
    if op == "+":
        result = add(a,b)
        print("the result is", result)
    if op == "/":
        result = dev(a,b)
        print("the result is", result)


while True:
    chouce1 = int(input("entre the first number: "))
    chouce2 = int(input("entre the secend number: "))
    op = input("entre an operation: ")
    calculator(chouce1,chouce2,op)