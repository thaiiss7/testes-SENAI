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