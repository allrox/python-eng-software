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

linha_separadora(".")


# Função para indicar o número ímpar
def par_ou_impar(x):
    if (x % 2) != 0:
        print(f"O número {x} é ímpar.")
    else:
        print(f"O número {x} é par.")


# Avaliando um número através da função
par_ou_impar(100)


linha_separadora(".")


# Função para avaliar a média de um aluno
def avaliar_media(x):
    if x < 5:
        print(f"A média {x} indica que o aluno está reprovado.")
    elif x < 7:
        print(f"A média {x} indica que o aluno está em recuperação.")
    else:
        print(f"A média {x} indica que o aluno está aprovado.")


# Avaliando a média através da função
avaliar_media(6.4)
