from linha_separadora import linha_separadora


def estimate():
    frequencia = eval(input("Informe a frequência por semana: "))
    formatos = eval(input("Informe quantas formatos serão criados por publicação: "))
    dificuldade = eval(input("Informe um grau de complexidade de 1 (baixo), 2 (médio) ou 3 (alto): "))
    velocidade = eval(input("Informe 1 para normal, 2 para aumentada ou 3 para urgente: "))
    preco_base = 120

    total_de_publicacoes = (frequencia * formatos) * 4.5
    multiplicador_dificuldade = (dificuldade / 10) + 1

    if velocidade == 1:
        estimativa = total_de_publicacoes * multiplicador_dificuldade * preco_base
    elif velocidade == 2:
        estimativa = ( total_de_publicacoes * multiplicador_dificuldade * preco_base ) * 1.2
    else:
        estimativa = (total_de_publicacoes * multiplicador_dificuldade * preco_base) * 1.4

    linha_separadora("-")
    print(f"O seu orçamento para {total_de_publicacoes} posts ao mês é igual a R${round(estimativa)}.")
    print(f"O preço médio por publicação é R${round(estimativa/total_de_publicacoes)}")


estimate()
