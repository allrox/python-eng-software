# Função para localizar menor valor na lista
def menor_da_lista(lista):
    minimo = lista[0]
    indice = lista[0]

    # A instrução for varre os índices sem a necessidade de  uma variável incremental
    for elemento in lista:
        if elemento < minimo:
            minimo = elemento

            # Armazena o índice do valor encontrado
            indice = lista.index(elemento)

    print(f"O menor item encontrado na lista foi {minimo}, ocupando o índice {indice}.")


menor_da_lista([9, 12, 3, 4, 5, 6, 32, 7, 76, 12, 74, 90, 2, 114, 357, 43, 36, 25, 784, 54, 60])
