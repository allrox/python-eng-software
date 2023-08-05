# Função para criar lista com x elementos e incremento y
def cria_lista(itens, intervalo):
    lista = []
    for i in range(itens):
        i += intervalo
        lista.append(i)
    return lista

