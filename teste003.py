# Importa biblioteca "json" para ser possível ler o arquivo "dados.jason"
import json

# Declaração das variáveis
menor_faturamento_mes = 0
maior_faturamento_mes = 0

dias_com_faturamento = 0
dias_com_faturamento_maior_que_a_media_do_mes = 0

total_faturamento_mes = 0
media_faturamento_mes = 0

# Leitura do arquivo "dados.json"
with open("dados.json", "r") as arquivo:
    faturamento_mes = json.load(arquivo)

# Iteração para calcular o faturamento mensal total da distribuidora
for faturamento in faturamento_mes:

    # Verifica se houve faturamento no dia
    if faturamento["valor"] > 0:
        
        # Adiciona o valor do faturado no dia ao faturamento total do mes
        total_faturamento_mes += faturamento["valor"]

        # Incrementar contador de dias que tiveram faturamento
        dias_com_faturamento += 1

# Cálculo da média dos dias faturados
media_faturamento_mes = total_faturamento_mes / dias_com_faturamento

# Iteração para verifiacar o maior e o menor faturamento
for dia in faturamento_mes:

    # Verifica o primeiro dia com faturamento
    if menor_faturamento_mes == 0 and dia["valor"] > 0.0:
        menor_faturamento_mes = dia["valor"]
        maior_faturamento_mes = dia["valor"]

    # Verifica se houve faturamento no dia
    if dia["valor"] > 0.0:
    
        # Verifica se o valor faturado é maior do que o último maior valor faturado
        if dia["valor"] > maior_faturamento_mes:
            maior_faturamento_mes = dia["valor"]

        # Verifica se o valor faturado é menor do que o último menor valor faturado
        if dia["valor"] < menor_faturamento_mes:
            menor_faturamento_mes = dia["valor"]

        # Verifica se o valor faturado é maior do que a média de faturamento do mÊs
        if dia["valor"] > media_faturamento_mes:
            dias_com_faturamento_maior_que_a_media_do_mes += 1

# Exibição das saídas
print(f"Menor valor faturado no mês: {menor_faturamento_mes}")
print(f"Maior valor faturado no mês: {maior_faturamento_mes}")
print(f"Número de dias com o faturamento maior do que a média do mês: {dias_com_faturamento_maior_que_a_media_do_mes}")