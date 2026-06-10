# questao 1:
def classificar_produto(valor):

    if(valor >= 0 and valor < 50):
        return "Econômico"
    elif(valor < 0):
        return "Invalid"
    elif (valor >= 50 and valor < 200):
        return "Intermediário"
    else:
        return "Premium"
    
#  questao 2
def verficar_estoque(qtd):

    if(qtd == 0):
        return "Sem Estoque"
    elif(qtd < 0):
        return "Invalid"
    elif(qtd > 0 and qtd <= 10):
        return "Estoque Baixo"
    else:
        return "Estoque Normal"
    
#  questao 3
def calcular_frete(peso):

    if(peso < 0):
        return "Invalid"
    elif(peso > 0 and peso <= 1):
        return 15
    elif(peso > 1 and peso <= 5):
        return 30
    elif(peso > 5):
        return 50 
    
# questao 4
def conceito(nota):

    if(nota < 5 and nota >= 0):
        return "D"
    elif(nota >= 5 and nota < 7):
        return "C"
    elif(nota >= 7 and nota < 9):
        return "B"
    elif(nota >= 9 and nota <= 10):
        return "A"
    else:
        return "Invalid"
    
# questao 5
def calcular_desconto(compra):

    if(compra <= 100):
        return 0
    elif(compra > 100 and compra <= 500):
        return 10
    else:
        return 20
    
# questao 6
def classificacao_filme(idade):

    if(idade < 0):
        return "Invalid"
    elif(idade > 0 and idade < 10):
        return "Livre"
    elif(idade >= 10 and idade < 14):
        return "10 Anos"
    elif(idade >= 14 and idade < 18):
        return "14 anos"
    else:
        return "18 Anos"
    
# questao 7
def nivel_combustivel(percentual):

    if(percentual <= 10):
        return "Reserva"
    elif(percentual > 10 and percentual <= 50):
        return "Médio"
    elif(percentual > 50):
        return "Cheio"
    
# questao 8
def classe_ipv4(ip):

    if(ip > 0 and ip < 127):
        return "A"
    elif(ip > 127 and ip < 192):
        return "B"
    elif(ip > 191 and ip < 224):
        return "C"
    elif(ip > 223 and ip < 240):
        return "D"
    elif(ip > 239 and ip < 256):
        return "E"
    else:
        return "Invalid"