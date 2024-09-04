
# Instanciação da matriz que irá armazenar os mêses e seus respectivos faturamentos
estados = list()

# Variável que irá armazenar o faturamento total da distribuidoras
total_faturamento = 0

# Abre o arquivo .CSV e armazena suas linhas em uma lista chamada "linhas"
with open("ex004.csv") as arquivo:
    linhas = arquivo.readlines()

# Itera sobre cada uma das linhas do arquivo a partir da segunda linha para ignorar o cabeçalho
for linha in linhas[1:]:

    # Divide a linah pelo caracter separador ";"
    linha = linha.split(";")

    # Adiciona o estado e o faturamento na matriz "estados"
    estados.append([linha[0], float(linha[1])])

    # Adiciona o faturamento mensal do estado ao faturamento total da distribuidora
    total_faturamento += float(linha[1])

# Exibição do resultado em forma de tabela
# Exibição do cabeçalho da tabela
print("ESTADO\tFATURAMENTO\tPORCENTAGEM")
for estado in estados:
    # Calcule da porcentagem com arredondamento na segunda casa decimal
    porcentagem = round(estado[1]/total_faturamento*100, 2)

    # Exibição dos dados da tabela
    print(f"{estado[0]}\t{estado[1]}\t{porcentagem}%")
    