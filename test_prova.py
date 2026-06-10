from prova import classificar_produto, verficar_estoque
from prova import calcular_frete, conceito, calcular_desconto
from prova import classificacao_filme, nivel_combustivel
from prova import classe_ipv4

#  questao 1:
def test_product1():
    assert classificar_produto(10) == "Econômico"

def test_product2():
    assert classificar_produto(50) == "Intermediário"

def test_product3():
    assert classificar_produto(199) == "Intermediário"

def test_product4():
    assert classificar_produto(200) == "Premium"

def test_product5():
    assert classificar_produto(-5) == "Invalid"

#  questao 2:
def test_estoque1():
    assert verficar_estoque(0) == "Sem Estoque"

def test_estoque2():
    assert verficar_estoque(5) == "Estoque Baixo"

def test_estoque3():
    assert verficar_estoque(10) == "Estoque Baixo"

def test_estoque4():
    assert verficar_estoque(20) == "Estoque Normal"

def test_estoque5():
    assert verficar_estoque(-1) == "Invalid"

#  questao 3
def test_frete1():
    assert calcular_frete(0.5) == 15

def test_frete2():
    assert calcular_frete(1) == 15

def test_frete3():
    assert calcular_frete(3) == 30

def test_frete4():
    assert calcular_frete(5) == 30

def test_frete5():
    assert calcular_frete(10) == 50

#  questao 4
def test_conceito1():
    assert conceito(2) == "D"

def test_conceito2():
    assert conceito(5) == "C"

def test_conceito3():
    assert conceito(7) == "B"

def test_conceito4():
    assert conceito(9.5) == "A"

def test_conceito5():
    assert conceito(0) == "D"

#  questao 5
def test_desconto1():
    assert calcular_desconto(80) == 0

def test_desconto2():
    assert calcular_desconto(100) == 0

def test_desconto3():
    assert calcular_desconto(250) == 10

def test_desconto4():
    assert calcular_desconto(500) == 10

def test_desconto5():
    assert calcular_desconto(800) == 20

# questao 6
def test_filme1():
    assert classificacao_filme(7) == "Livre"

def test_filme2():
    assert classificacao_filme(10) == "10 Anos"

def test_filme3():
    assert classificacao_filme(14) == "14 anos"

def test_filme4():
    assert classificacao_filme(19) == "18 Anos"

def test_filme5():
    assert classificacao_filme(-5) == "Invalid"

# questao 7
def test_nivel1():
    assert nivel_combustivel(1) == "Reserva"

def test_nivel2():
    assert nivel_combustivel(10) == "Reserva"

def test_nivel3():
    assert nivel_combustivel(12) == "Médio"

def test_nivel4():
    assert nivel_combustivel(50) == "Médio"

def test_nivel5():
    assert nivel_combustivel(70) == "Cheio"

# questao 8
def test_ip1():
    assert classe_ipv4(10) == "A"

def test_ip2():
    assert classe_ipv4(172) == "B"

def test_ip3():
    assert classe_ipv4(192) == "C"

def test_ip4():
    assert classe_ipv4(230) == "D"

def test_ip5():
    assert classe_ipv4(250) == "E"