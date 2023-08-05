# Função para encontrar o termo N da sequência Fibonacci
# A sequência Fibonacci é iniciada por 1, 1, e a partir do terceiro termo,
# cada termo será resultante da soma dos dois que o antecedem.
# É um caso de recursividade. Repare que a função chama a si mesma na linha 9.
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        # A soma dos dois termos anteriores é realizada até atingir
        # o número N informado, ou o enésimo item da sequência Fibonacci
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(31))
