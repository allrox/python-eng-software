from linha_separadora import linha_separadora


# Avaliando uma array para somar números pares
lista = [10, 2, 5, 7, 6, 3, 10, 8, 2, 1, 7, 3, 13, 31, 75, 98, 67, 33, 28]


# Laço que busca e soma números pares da array
def soma_pares(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f"A soma dos números pares da lista é {soma}.")


# Avaliando um array para somar e listar múltiplos de um número x
def encontra_multiplos(lista):
    multiplos = []
    soma = 0
    divisor = 4
    for i in lista:
        if i % divisor == 0:
            soma += i
            multiplos.insert(i, i)
    print(f"A soma dos múltiplos de {divisor} é {soma}.")
    print(f"Os múltiplos de {divisor} encontrados na lista foram {multiplos}")


print(f"Lista utilizada no estudo {lista}")
soma_pares(lista)

linha_separadora("-")

encontra_multiplos(lista)
