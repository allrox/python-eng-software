from linha_separadora import linha_separadora

# Comportamento da soma de listas
x = ['10', '11', '12']
y = ['20', '21', '22']
z = ['30', '31', '32']

# Soma de arrays
r = x + y + z
print(f"Array x: {x}, Array Y: {y}, Array z: {z}")
print(f"Resultado da soma de arrays: {r}")

linha_separadora("-")

# Comportamento da multiplicação de listas
a = ['5']
print(f"Array A original: {a}")
print(f"Array A multiplicada por 5: {a * 5}")

linha_separadora("-")

# Troca de conteúdo entre variáveis
lampada_1 = "queimada"
lampada_2 = "nova"

# Estado original
print(f"Estado original  ->  Lâmpada 1: {lampada_1}, Lâmpada 2: {lampada_2}")

troca = lampada_1
lampada_1 = lampada_2
lampada_2 = troca

# Novo estado
print(f"Novo estado      ->  Lâmpada 1: {lampada_1}, Lâmpada 2: {lampada_2}")
