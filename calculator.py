def add(num1, num2):
    print(f"result: {num1 + num2}")
    return num1 + num2

def multiply(num1, num2):
    print(f"result: {num1 * num2}")
    return num1 * num2

def subract(num1, num2):
    print(f"result: {num1 - num2}")
    return num1 - num2

def divide(num1, num2):
    if(num2 == 0):
        return print("it's not possible to divide by 0")
    else:
        print(f"result: {num1/num2}")
        return (num1/num2)
    
def minNumber(num1, num2):
    if(num1 < num2):
        return num1
    else: 
        return num2
    
def evenNumber(a):
    if(a % 2 == 0):
        return True
    else:
        return False
    
def temperatureCtoF(c):
    return (c * 9/5) + 32

def temperatureFtoC(f):
    return (f - 32) * 5/9

# calculo de areas
def squareArea(l):
    return l * l

def trianguleArea(b, a):
    return b * a

def elipseArea(a, b):
    pi = 3.14
    return pi * a * b

# calculo de conversão
def cmToM(a):
    return a / 100

def mToCm(a):
    return a * 100

def lToMl(a):
    return a * 1000

def mlToL(a):
    return a / 1000

def realToDolar(a):
    return round(a / 5, 2)

def dolarToReal(a):
    return round(a * 5, 2)

# calculo de salario
def salary(v, h):
    bruto = v * h

    if (bruto <= 5000.00):
        inss = bruto * 0.11 
        ir = bruto * 0.00
    else:
        inss = bruto * 0.14
        ir = bruto * 0.05

    return bruto - inss - ir

# autentificação
def auth(u, p):
    user = "thaiis"
    password = 123

    if (user == u and password == p):
        return "login!"
    elif (user != u and password != p):
        return "tudo inválido!"
    elif (user != u):
        return "usuário inválido!"
    elif (password != p):
        return "senha inválida!"