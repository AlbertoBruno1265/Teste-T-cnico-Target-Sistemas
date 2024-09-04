
# Variável que armazena string digitada pelo usuário
string_digitada = str(input("Digite uma frase: "))

# Variável que irá armazenar a string invertida
string_invertida = ""

# Variável que armazena a quantidade de caracteres presentes na string digitada pelo usuário
tamanho_string_digitada = len(string_digitada)

# Laço que itera a partir do último índice da string até o primeiro
for i in range(tamanho_string_digitada-1, -1, -1):

    # Variável "string_invertida" concatena caracteres da variável "string_digitada"
    string_invertida += string_digitada[i]

# Exibição do resultado
print("Sua frase invertida é:")
print(string_invertida)