from linha_separadora import linha_separadora


# Função para calcular o fatorial n! = n(n-1)
# Método recursivo
def funcao_fatorial(num):

    # Avalia se o número informado é 0 ou 1, valores cujo fatorial é 1
    if num == 0 or num == 1:
        return 1
    # Calcula o fatorial multiplicando o valor de n por (n-1)
    return num * funcao_fatorial(num - 1)


n = 3
print(f"O fatorial do número {n} é: {funcao_fatorial(n)}")

linha_separadora("-")


# Método iterativo
def funcao_fatorial_iterativo(num):
    f = 1

    # Observe que, neste caso, o cálculo usa o range invertido, de 1 até num + 1,
    # encerrando o laço quando num atinge o parâmetro da função

    for i in range(1, num + 1):
        f = f * i
    return f


print(f"O fatorial é: {funcao_fatorial_iterativo(4)}")
