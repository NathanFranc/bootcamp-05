import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
     
   lista = []
   with open(nome_do_arquivo_csv, mode="r", encoding= 'utf-8') as arquivo:
       leitor = csv.DictReader(arquivo)
       for linha in leitor:
              lista.append(linha)
   return lista



def filtrar_produtos_nao_enttegues(lista: list[dict]) -> list[dict]:
    """
    funcao que filtra produtos onde entrega = true
    """
    lista_com_produtos_filtrado = []
    for produto in lista:
        if produto.get("entregue") == "true":
             lista_com_produtos_filtrado.append(produto)
    return lista_com_produtos_filtrado

csv_lido = ler_csv(path_arquivo)
lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_enttegues(lista_de_produtos)
print(produtos_entregues)


def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> int:
    """
    soma todos os produtos que estao na lista
    """
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
       valor_total += int(produto.get("price"))
    return valor_total

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_enttegues(lista_de_produtos)
valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entregues)
print(valor_dos_produtos_entregues)