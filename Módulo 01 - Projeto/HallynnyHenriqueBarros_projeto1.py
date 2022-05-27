import json
import os.path
import sys


def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados


def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.
    '''
    ...

    lista_categorias = []
    for i in range(len(dados)):
        if dados[i]["categoria"] not in lista_categorias:
            lista_categorias.append(dados[i]["categoria"])
    lista_categorias.sort()
    return lista_categorias


def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    ...
    produtos_por_categorias = []
    for i in range(len(dados)):
        if dados[i]["categoria"] == categoria:
            produtos_por_categorias.append(dados[i])
    return produtos_por_categorias


def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    ...
    produto_caro = listar_por_categoria(dados, categoria)
    caro = sorted(produto_caro, key=lambda k: float(k['preco']), reverse=True)
    return caro[0]


def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    ...
    produto_barato = listar_por_categoria(dados, categoria)
    barato = sorted(produto_barato, key=lambda k: float(k['preco']))
    return barato[0]


def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    ...
    produtos_ordenados_decrescente = sorted(
        dados, key=lambda k: float(k['preco']), reverse=True)
    mais_caros = []
    for i in range(10):
        mais_caros.append(produtos_ordenados_decrescente[i])
    return mais_caros


def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais baratos.
    '''
    ...
    produtos_ordenados_crescente = sorted(
        dados, key=lambda k: float(k['preco']))
    mais_baratos = []
    for i in range(10):
        mais_baratos.append(produtos_ordenados_crescente[i])
    return mais_baratos


def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
    ...

    opcao = int (input("Loja Hallynny Henrique | Seja bem-vindo! \n ---------------------------------------- \n1. Listar categorias \n2. Listar produtos de uma categoria \n3. Produto mais caro por categoria \n4. Produto mais barato por categoria \n5. Top 10 produtos mais caros  \n6. Top 10 produtos mais baratos  \n0. Sair \n ---------------------------------------- \n Digite o número correspondente a opção desejada: "))
    while opcao != 0:
        if opcao == 1:
            lista_categorias=listar_categorias(dados)
            for i in range(len(lista_categorias)):
                print(lista_categorias[i])
        elif opcao == 2:
            categoria = input("Para visualizar os produtos de uma categoria, digite a categoria desejada: ")
            produtos_categoria = listar_por_categoria(dados, categoria)
            for i in range(len(produtos_categoria)):
                print(produtos_categoria[i])
        elif opcao == 3:
            categoria_mais_caro = input("Para visualizar o produto mais caro de uma categoria, digite a categoria desejada: ")
            print (produto_mais_caro(dados, categoria_mais_caro))
        elif opcao == 4:
            categoria_mais_barato = input("Para visualizar o produto mais caro de uma categoria, digite a categoria desejada: ")
            print (produto_mais_barato(dados, categoria_mais_barato))
        elif opcao == 5:
            mais_caros = top_10_caros(dados)
            print("Estes são os 10 produtos mais caros:")
            for i in range(len(mais_caros)):
                print(mais_caros[i])
        elif opcao == 6:
            mais_baratos = top_10_baratos(dados)
            print("Estes são os 10 produtos mais baratos:")
            for i in range(len(mais_baratos)):
                print(mais_baratos[i])
        else:
            print("\nOpção inválida! Digite novamente de acordo com o menu informado: \n")
        opcao = int (input("Loja Hallynny Henrique | Seja bem-vindo! \n ---------------------------------------- \n1. Listar categorias \n2. Listar produtos de uma categoria \n3. Produto mais caro por categoria \n4. Produto mais barato por categoria \n5. Top 10 produtos mais caros  \n6. Top 10 produtos mais baratos  \n0. Sair \n ---------------------------------------- \n Digite o número correspondente a opção desejada: "))




# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)
print("Obrigada por escolher a Loja Hallynny Henrique. Volte sempre!")