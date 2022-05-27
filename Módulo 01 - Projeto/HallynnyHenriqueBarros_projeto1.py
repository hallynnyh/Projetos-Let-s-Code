import json
import os.path
import sys


def obter_dados():
    
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados


def listar_categorias(dados):
    
    lista_categorias = []
    for i in range(len(dados)):
        if dados[i]["categoria"] not in lista_categorias:
            lista_categorias.append(dados[i]["categoria"])
    lista_categorias.sort()
    return lista_categorias


def listar_por_categoria(dados, categoria):
    
    produtos_por_categorias = []
    for i in range(len(dados)):
        if dados[i]["categoria"] == categoria:
            produtos_por_categorias.append(dados[i])
    return produtos_por_categorias


def produto_mais_caro(dados, categoria):
    
    produto_caro = listar_por_categoria(dados, categoria)
    caro = sorted(produto_caro, key=lambda k: float(k['preco']), reverse=True)
    return caro[0]


def produto_mais_barato(dados, categoria):
   
    produto_barato = listar_por_categoria(dados, categoria)
    barato = sorted(produto_barato, key=lambda k: float(k['preco']))
    return barato[0]


def top_10_caros(dados):
   
    produtos_ordenados_decrescente = sorted(
        dados, key=lambda k: float(k['preco']), reverse=True)
    mais_caros = []
    for i in range(10):
        mais_caros.append(produtos_ordenados_decrescente[i])
    return mais_caros


def top_10_baratos(dados):
    
    produtos_ordenados_crescente = sorted(
        dados, key=lambda k: float(k['preco']))
    mais_baratos = []
    for i in range(10):
        mais_baratos.append(produtos_ordenados_crescente[i])
    return mais_baratos

def validar_categoria (texto, dados):
    
    lista_categorias = listar_categorias(dados)
    categoria = input(texto)
    while categoria not in lista_categorias and categoria != "0":
        categoria = input("Categoria inválida! Digite novamente ou digite 0 para retornar ao menu principal: ")
    return categoria
            

def menu(dados):
    
    opcao = int (input("\n Loja Hallynny Henrique | Seja bem-vindo! \n ---------------------------------------- \n1. Listar categorias \n2. Listar produtos de uma categoria \n3. Produto mais caro por categoria \n4. Produto mais barato por categoria \n5. Top 10 produtos mais caros  \n6. Top 10 produtos mais baratos  \n0. Sair \n ---------------------------------------- \n Digite o número correspondente a opção desejada: "))
    while opcao != 0:
        if opcao == 1:
            lista_categorias=listar_categorias(dados)
            print("")
            for i in range(len(lista_categorias)):
                print(lista_categorias[i])
        elif opcao == 2:
            categoria = validar_categoria ("Para visualizar os produtos de uma categoria, digite a categoria desejada: ", dados)
            if categoria != "0":
                produtos_categoria = listar_por_categoria(dados, categoria)
                for i in range(len(produtos_categoria)):
                    print(produtos_categoria[i])
        elif opcao == 3:
            categoria_mais_caro = validar_categoria ("Para visualizar o produto mais caro de uma categoria, digite a categoria desejada: ", dados)
            if categoria_mais_caro != "0":
                print ("\nO produto mais caro da categoria", categoria_mais_caro, "é: \n", produto_mais_caro(dados, categoria_mais_caro))
        elif opcao == 4:
            categoria_mais_barato = validar_categoria ("Para visualizar o produto mais barato de uma categoria, digite a categoria desejada: ", dados)
            if categoria_mais_barato != "0":
                print ("\nO produto mais barato da categoria", categoria_mais_barato, "é: \n",  produto_mais_barato(dados, categoria_mais_barato))
        elif opcao == 5:
            mais_caros = top_10_caros(dados)
            print("\n Estes são os 10 produtos mais caros:\n")
            for i in range(len(mais_caros)):
                print(mais_caros[i])
        elif opcao == 6:
            mais_baratos = top_10_baratos(dados)
            print("\nEstes são os 10 produtos mais baratos:\n")
            for i in range(len(mais_baratos)):
                print(mais_baratos[i])
        else:
            print("\nOpção inválida! Digite novamente de acordo com o menu informado: \n")
        opcao = int (input("\n Loja Hallynny Henrique | Seja bem-vindo! \n ---------------------------------------- \n1. Listar categorias \n2. Listar produtos de uma categoria \n3. Produto mais caro por categoria \n4. Produto mais barato por categoria \n5. Top 10 produtos mais caros  \n6. Top 10 produtos mais baratos  \n0. Sair \n ---------------------------------------- \n Digite o número correspondente a opção desejada: "))




# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)
print("\nObrigada por escolher a Loja Hallynny Henrique. Volte sempre!\n")