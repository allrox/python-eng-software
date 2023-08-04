from linha_separadora import linha_separadora


def estimate():
    frequency = eval(input("Informe a frequência por semana: "))
    formats = eval(input("Informe quantas formatos serão criados por publicação: "))
    difficulty = eval(input("Informe um grau de complexidade de 1 (baixo), 2 (médio) ou 3 (alto): "))
    base_pricing = 120

    total_publications = (frequency * formats) * 4.5
    difficulty_tax = (difficulty / 10) + 1

    your_estimate = total_publications * difficulty_tax * base_pricing
    linha_separadora("-")
    print(f"O seu orçamento para {total_publications} posts ao mês é igual a R${round(your_estimate)}.")
    print(f"O preço médio por publicação é R${round(your_estimate/total_publications)}")


estimate()
