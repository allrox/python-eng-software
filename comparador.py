from linha_separadora import linha_separadora


# Entrada dos valores com o método input
# x = eval(input("Informe um valor para x: "))
# y = eval(input("Informe um valor para y: "))

# Função para indicar maior entre dois números
def comparar(x, y):
    if x == y:
        print(f"Os valores de x e y são iguais ({x})")
    elif x > y:
        print(f"O valor de x ({x}) é maior do que y ({y})")
    else:
        print(f"O valor de y ({y}) é maior do que x ({x})")


# Comparando os números através da função
comparar(8, 89)
comparar(75, 32)

linha_separadora(".")


# Função para indicar o número ímpar
def par_ou_impar(x):

    # Implementando o tratamento de exceções
    while True:
        try:
            x = int(x)
            if (x % 2) != 0:
                print(f"O número {x} é ímpar.")
            else:
                print(f"O número {x} é par.")
            break
        except ValueError:
            print("Erro: Não foi informado um número válido! ")
            break


# Avaliando um número através da função
par_ou_impar(13)
par_ou_impar("n")
par_ou_impar(8)


linha_separadora(".")


# Função para avaliar a média de um aluno
def avaliar_media(x):

    # Tratamento de exceção para formato de entrada
    try:

        # Verifica se a nota média informada está na faixa válida 0 - 10
        if (x >= 0) and (x <= 10):
            if x < 5:
                print(f"A média {x} indica que o aluno está reprovado.")
            elif x < 7:
                print(f"A média {x} indica que o aluno está em recuperação.")
            elif x <= 10:
                print(f"A média {x} indica que o aluno está aprovado.")
        else:
            print(input("Informe uma média entre 0 e 10"))

    # Resposta para a exceção
    except TypeError:
        print("Erro: Entrada de dados incompatível!")


# Avaliando a média através da função
x = 8
avaliar_media(x)
