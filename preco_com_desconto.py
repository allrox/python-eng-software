# Função para aplicar descontos condicionais por quantidade
def valor_total():

    itens = eval(input("Qual a quantidade de itens comprados? "))

    # Declaração de constantes APENAS PARA ESTUDO!
    PRECO = 10
    DESCONTO_10 = .9
    DESCONTO_20 = .8

    if itens <= 10:
        total = PRECO * itens
    elif itens <= 20:
        total = (PRECO * itens) * DESCONTO_10
    else:
        total = (PRECO * itens) * DESCONTO_20

    print(f"Total da compra: R${round(total,2)}")


# Calculando o valor total através da função
valor_total()
