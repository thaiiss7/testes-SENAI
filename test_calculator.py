from calculator import add, subract, multiply, divide
from calculator import minNumber, evenNumber, temperatureCtoF, temperatureFtoC

# def test_divide():
#     assert divide(8,0) == print("it's not possible to divide by 0")

# def test_multiply():
#     assert multiply(2,4) == 8

# def test_subtract():
#     assert subract(10,5) == 5

def test_minNumber():
    assert minNumber(5,7) == 5

def test_evenNumber():
    assert evenNumber(5) == False

def test_celsius():
    assert temperatureCtoF(25) == 77.0

# def test_fahrenheit():
#     assert temperatureCtoF(68) == 20.0