from linha_separadora import linha_separadora


# Função para calcular o fatorial n! = n(n-1)
# Método recursivo (O método chama a si mesmo: Linha 12)
def funcao_fatorial(num):

    # Avalia se o número informado é 0 ou 1, valores cujo fatorial é 1
    if num == 0 or num == 1:
        return 1
    # Calcula o fatorial multiplicando o valor de n por (n-1)
    # O laço será finalizado quando num - 1 coincide, eventualmente, com num == 1
    return num * funcao_fatorial(num - 1)


n = 3
print(f"O fatorial do número {n} é: {funcao_fatorial(n)}")

linha_separadora("-")


# Método iterativo (Trabalha através das iterações)
def funcao_fatorial_iterativo(num):
    f = 1

    # Observe que, neste caso, o cálculo usa o range invertido, de 1 até num + 1,
    # encerrando o laço quando num atinge o parâmetro da função.
    # "num + 1" é utilizado pois o FOR não consideraria o último item da lista (exceto).

    for i in range(1, num + 1):
        f = f * i
    return f


n = 4
print(f"O fatorial de {n} é {funcao_fatorial_iterativo(n)}.")

linha_separadora("-")


def fatorial(num):
    fat = 1
    if num == 0 or num == 1:
        return fat
    else:
        for x in range(2, num + 1):
            fat = fat*x
        return fat


n = 5
print(f"O fatorial de {n} é {fatorial(n)}")
