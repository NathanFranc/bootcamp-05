import csv

# Função para ler o arquivo CSV
def ler_csv(nome_arquivo):
    print(f"Lendo o arquivo {nome_arquivo}...")
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)  # Lê como dicionário
        dados = list(leitor)
    print(f"{len(dados)} registros lidos.")
    return dados

# Função para processar os dados em um dicionário, agrupando por categoria
def processar_dados(dados):
    categorias = {}
    for item in dados:
        categoria = item['Categoria']  # A chave 'Categoria' corresponde ao nome da coluna
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(item)
    print(f"{len(categorias)} categorias encontradas.")
    return categorias

# Função para calcular o total de vendas por categoria
def calcular_vendas_categoria(dados):
    vendas_por_categoria = {}
    for categoria, items in dados.items():
        total_vendas = sum(float(item['Quantidade']) * float(item['Venda']) for item in items)  # Calcula as vendas
        vendas_por_categoria[categoria] = total_vendas
    return vendas_por_categoria

# Função principal para integrar as funções anteriores
def main():
    nome_arquivo = 'vendas.csv'  # Substitua pelo caminho correto do seu arquivo CSV
    dados_brutos = ler_csv(nome_arquivo)  # Lê os dados do arquivo CSV
    dados_processados = processar_dados(dados_brutos)  # Processa os dados para agrupar por categoria
    vendas_por_categoria = calcular_vendas_categoria(dados_processados)  # Calcula as vendas por categoria

    # Exibindo os resultados
    print("Vendas por Categoria:")
    for categoria, total_vendas in vendas_por_categoria.items():
        print(f"Categoria: {categoria}, Total de Vendas: R${total_vendas:.2f}")

# Chama o fluxo principal
if __name__ == '_main_':
    main()