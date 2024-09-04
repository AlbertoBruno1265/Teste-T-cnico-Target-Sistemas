# Declaração da função recursiva que verifica se o número digitado faz parte da sequência de Fibonacci
def faz_parte_da_fibonnaci(valor_a_ser_verificado, atual=0, proximo=1):

    # Caso base da função recursiva
    if atual >= valor_a_ser_verificado:

        # Retorno de um valor booleano para saber se o número pertence a sequência de Fibonacci
        return atual == valor_a_ser_verificado

    else:

        # Chamada recursiva da função
        return faz_parte_da_fibonnaci(valor_a_ser_verificado, proximo, atual + proximo)

# Variável que armazena número digitado pelo usuário
valor_digitado = int(input("Digite um número inteiro: "))

# Chamada da função recursiva que verifica se o número digitado pelo usuário é igaual ao último número calculado da sequência de Fibonnaci
if faz_parte_da_fibonnaci(valor_digitado):
    print("O número que você digitou pertence a sequência de Fibonacci!")
else:
    print("O número que você digitou não pertence a sequência de Fibonacci!")

