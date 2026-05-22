from calculator import add, subract, multiply, divide
from calculator import minNumber, evenNumber, temperatureCtoF, temperatureFtoC
from calculator import squareArea, trianguleArea, elipseArea
from calculator import cmToM, mToCm, lToMl, mlToL, realToDolar, dolarToReal
from calculator import salary
from calculator import auth

def test_divide():
    assert divide(8,0) == print("it's not possible to divide by 0")

def test_multiply():
    assert multiply(2,4) == 8

def test_subtract():
    assert subract(10,5) == 5

def test_minNumber():
    assert minNumber(5,7) == 5

def test_evenNumber():
    assert evenNumber(5) == False

def test_celsius():
    assert temperatureCtoF(25) == 77.0

def test_fahrenheit():
    assert temperatureFtoC(68) == 20.0

def test_squareArea():
    assert squareArea(4) == 16

def test_trianguleArea():
    assert trianguleArea(5, 2) == 10

def test_elipseArea():
    assert elipseArea(4, 2) == 25.12

def test_cmToM():
    assert cmToM(200) == 2

def test_mToCm():
    assert mToCm(1) == 100

def test_lToMl():
    assert lToMl(5) == 5000

def test_mlToL():
    assert mlToL(1000) == 1

def test_realToDolar():
    assert realToDolar(100) == 20.00

def test_dolarToReal():
    assert dolarToReal(100) == 500.00

def test_salary():
    assert salary(10, 300) == 2670.00

def test_loginValido():
    assert auth("thaiis", 123) == "login!"

def test_usuarioInvalido():
    assert auth("thais", 123) == "usuário inválido!"

def test_senhaInvalida():
    assert auth("thaiis", 124) == "senha inválida!"

def test_loginInvalido():
    assert auth("thaiss", 223) == "tudo inválido!"