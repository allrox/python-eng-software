from linha_separadora import linha_separadora


# Teste para exibir números divisíveis por um número x
numero = int(input("De que número você deseja começar? "))
divisor = int(input("Informe o divisor (do qual serão identificados os múltiplos): "))
limite = int(input("Informe o número limite: "))
contador = 0

# Laço que avalia se o número é divisível sem resto
while numero <= limite:
    if numero % divisor == 0:
        print(numero, end=" ")
        contador += 1
    else:
        pass
    numero += 1

# Exibição dos resultados
print("")
print(f"Foram listados {contador} números na faixa.")

linha_separadora("-")

# Estudo para troca de valores dos índices de uma array
times = ["Flamengo", "Vasco", "Botafogo"]

# Array na ordem original
print(times)

# Troca do conteúdo dos índices 0 e 2
# Movendo Botafogo para o início da lista
temp = times[0]
times[0] = times[2]
times[2] = temp

# Array na nova ordem
print(times)
