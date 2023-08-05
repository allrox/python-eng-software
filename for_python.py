from cria_lista import cria_lista
from linha_separadora import linha_separadora

# Criando uma lista para o estudo através da função cria_lista
lista = cria_lista(1,100,7)


# Função que utiliza a estrutura de repetição
# FOR para somar os itens pares de uma lista
def soma_itens_pares(lista):
    acumulador = 0

    # Para cada ELEMENTO na LISTA
    for elemento in lista:
        if elemento % 2 == 0:
            acumulador = elemento + acumulador
        else:
            continue
    return acumulador


def exibir_pares(lista):
    # Cria lista vazia para receber os elementos pares
    lista_pares=[]

    # Para cada ELEMENTO na LISTA
    for elemento in lista:
        if elemento % 2 == 0:
            #Adiciona o elemento à lista
            lista_pares.append(elemento)
        else:
            continue
    return lista_pares


print(f"Lista original: {lista}")
linha_separadora("-")
print(f"Estes foram os itens pares encontrados na lista {exibir_pares(lista)}")
print(f"A soma dos itens pares da lista é {soma_itens_pares(lista)}.")
