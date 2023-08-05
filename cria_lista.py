# Função para criar lista com x elementos e incremento y
def cria_lista(elemento, fim, intervalo):
    # Definindo a variável lista
    lista = []

    # Preenchendo a lista com um laço while
    while elemento <= fim:
        lista.append(elemento)
        elemento += intervalo

    return lista

