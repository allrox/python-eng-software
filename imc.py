# Função para o cálculo de IMC
def imc():

    # Inputs dos valores para as variáveis peso e altura
    peso = eval(input("Informe o seu peso: "))
    altura = eval(input("Informe a sua altura: "))

    # Cálculo de IMC
    indice = peso / (altura ** 2)

    # Impressão do resultado
    print(f"O IMC do indivíduo é igual a {round(indice)}.")


# Chamada para a função
imc()
