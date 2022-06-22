import csv
import re 
regex = '[A-Za-z0-9._]+@[a-z0-9]+\.[a-z.]'

def validar_nome(nome):
    arquivo = open('banco_de_bandas.csv', 'r')
    lista = list(csv.reader(arquivo, delimiter=';', lineterminator='\n'))

    nome_existente = False
    for musico in lista:
        if musico[0] == nome:
            nome_existente = True

    arquivo.close()
    
    if nome_existente:
        return 'Nome já cadastrado, digite novamente!'


def validar_email(email, validar_existente):
    arquivo = open('banco_de_bandas.csv', 'r')
    lista = list(csv.reader(arquivo, delimiter=';', lineterminator='\n'))

    email_existente = False
    if validar_existente:
        for musico in lista:
            if musico[1]==email:
                email_existente = True

    arquivo.close()
    
    if not re.search(regex,email):
        return 'E-mail inválido, digite novamente!'
    elif email_existente:
        return 'E-mail já cadastrado, digite novamente!'
        

def incluir_musicos():

    erro_nome = not None
    while erro_nome is not None:
        nome = str(input('Digite o nome do músico: '))
        erro_nome = validar_nome(nome.title())
        if erro_nome is not None:
            print(erro_nome)

    erro_email = not None
    while erro_email is not None:
        e_mail = str(input('Digite o email: '))
        erro_email = validar_email(e_mail.lower(), True)
        if erro_email is not None:
            print(erro_email) 
        
    genero_musical = input('Digite os gêneros musicais separados por vírgula: ')
    instrumentos = input('Digite os instrumentos separados por vírgula: ')

    musico = [[nome.title(), e_mail.lower(), genero_musical.title(), instrumentos.title()]]
    
    arquivo = open('banco_de_bandas.csv', 'a')
    dados = csv.writer(arquivo, delimiter=';', lineterminator='\n')
    dados.writerows(musico)
    arquivo.close()

def busca_exata(parametros_busca):
    arquivo = open('banco_de_bandas.csv', 'r')
    lista = list(csv.reader(arquivo, delimiter=';', lineterminator='\n'))

    lista_exata = lista[:]

    for musico in lista:
        remover_musico = False
        for indice in range(2):
            if parametros_busca[indice] != '' and musico[indice].lower()!=parametros_busca[indice].lower():
                remover_musico = True

        for indice in range(2,4):
            list_parametro_musico = musico[indice].replace(' ','').split(',')
            for parametro_musico in list_parametro_musico:
                if parametros_busca[indice] != '' and parametro_musico.lower()!=parametros_busca[indice].lower():
                    remover_musico = True

        if remover_musico:
            lista_exata.remove(musico)
    
    arquivo.close()

    return lista_exata

def busca_geral(parametros_busca):
    arquivo = open('banco_de_bandas.csv', 'r')
    lista = list(csv.reader(arquivo, delimiter=';', lineterminator='\n'))

    lista_geral = lista[:]

    for musico in lista:
        remover_musico = True
        for indice in range(2):
            if parametros_busca[indice] != '' and parametros_busca[indice].lower() in musico[indice].lower():
                remover_musico = False

        for indice in range(2,4):
            list_parametro_musico = musico[indice].replace(' ','').split(',')
            for parametro_musico in list_parametro_musico:
                if parametros_busca[indice] != '' and parametros_busca[indice].lower() in parametro_musico.lower():
                    remover_musico = False

        if remover_musico:
            lista_geral.remove(musico)
    
    arquivo.close()

    return lista_geral

def imprimir_lista_musicos(lista_musicos):
    if len(lista_musicos) > 0:
        for musico in lista_musicos:
            print('-'*33)
            parametros = ['Nome', 'E-mail', 'Gênero Musical', 'Instrumento']
            [print('{}: {}'.format(parametro, musico[indice])) for indice, parametro in enumerate(parametros)]
    else:
        print('-'*33)
        print('Nenhum músico foi encontrado!')

def validar_parametros_busca(lista_parametros):
    parametros_validos = False
    
    for parametro in lista_parametros:
        if parametro != '':
            parametros_validos = True
    
    return parametros_validos

def buscar_musico():
    tipo_busca = int(input('Digite 1 para realizar uma busca exata ou 2 para realizar uma busca geral: '))
    while not (tipo_busca == 1 or tipo_busca == 2):
        print('Tipo de busca inválido!')
        tipo_busca = int(input('Digite 1 para realizar uma busca exata ou 2 para realizar uma busca geral: '))

    parametros = ['Nome', 'E-mail', 'Gênero Musical', 'Instrumento']
    parametros_busca = [input('Digite o {} que deseja utilizar em sua busca, ou deixe em branco: '.format(parametro)) for parametro in parametros]
    while not validar_parametros_busca(parametros_busca):
        print('Insira ao menos um parâmetro')
        parametros_busca = [input('Digite o {} que deseja utilizar em sua busca, ou deixe em branco: '.format(parametro)) for parametro in parametros]

    if tipo_busca == 1:
        imprimir_lista_musicos(busca_exata(parametros_busca))
    else:
        imprimir_lista_musicos(busca_geral(parametros_busca))

def busca_por_email(email):
    arquivo = open('banco_de_bandas.csv', 'r')
    lista = list(csv.reader(arquivo, delimiter=';', lineterminator='\n'))

    indice = None

    for musico in lista:
        if musico[1] == email.lower():
            imprimir_lista_musicos([musico])
            indice = lista.index(musico)
    
    arquivo.close()
    
    return indice


def alterar_musico():
    erro_email = not None
    while erro_email is not None:
        email = input('Selecione o músico para modificar informando o e-mail: ')
        erro_email = validar_email(email, False)

    indice = busca_por_email(email)
    if indice != None:
        genero_musical = input('Digite os gêneros musicais separados por vírgula: ')
        instrumentos = input('Digite os instrumentos separados por vírgula: ')

        arquivo = open('banco_de_bandas.csv', 'r')
        lista = list(csv.reader(arquivo, delimiter=';', lineterminator='\n'))

        lista[indice][2] = genero_musical.title()
        lista[indice][3] = instrumentos.title()

        arquivo = open('banco_de_bandas.csv', 'w')
        dados = csv.writer(arquivo, delimiter=';', lineterminator='\n')
        dados.writerows(lista)

        arquivo.close()
    else:
        print('-'*33)
        print('Músico não encontrado!')

def buscar_por_genero_e_instrumento(genero, instrumento):
    arquivo = open('banco_de_bandas.csv', 'r')
    lista = list(csv.reader(arquivo, delimiter=';', lineterminator='\n'))

    indice = None

    musicos = []

    for musico in lista:
        list_genero_musico = musico[2].replace(' ','').split(',')
        list_instrumento_musico = musico[3].replace(' ','').split(',')
        
        if genero.title() in list_genero_musico and instrumento.title() in list_instrumento_musico:
            musicos.append(musico)            
    
    arquivo.close()
    
    return musicos

def agrupar_musicos(musicos, bandas):
    aux = []
    if len(bandas) > 0:
        for a in bandas:
            for b in musicos[0]:
                if b not in a:
                    novo_a = a[:]
                    novo_a.append(b)
                    aux.append(novo_a)
        bandas = aux[:]
    else:
        for musico in musicos[0]:
            bandas.append([musico])
    musicos.pop(0)

    
    return agrupar_musicos(musicos, bandas) if (len(musicos) > 0) else bandas

def imprimir_bandas(bandas, instrumentos):
    for banda in bandas:
        print('-'*33)
        for indice in range(len(instrumentos)):
            print('{}: {}'.format(instrumentos[indice], banda[indice][1]))

def montar_banda():
    genero = input('Digite o gênero desejado: ')
    while genero == '':
        print('Gênero inválido!')
        genero = input('Digite o gênero desejado: ')
    
    quantidade_membros = int(input('Digite a quantidade de músicos desejada: '))
    while quantidade_membros < 1:
        print('Quantidade inválida')
        quantidade_membros = int(input('Digite a quantidade de músicos desejada: '))
    
    lista_instrumentos = list([input('Intrumento {}: '.format(indice+1)) for indice in range(quantidade_membros)])
    
    # lista_musicos = list([buscar_por_genero_e_instrumento(genero, instrumento)] for instrumento in lista_intrumentos)

    lista_musicos = []
    for instrumento in lista_instrumentos:
        lista_musicos.append(buscar_por_genero_e_instrumento(genero, instrumento))

    bandas = agrupar_musicos(lista_musicos,[])
    imprimir_bandas(bandas, lista_instrumentos)
        

def menu():
    opcao = int (input('\n Bandas on-line | Seja bem-vindo! \n'+ '-'*33 +'\n1. Cadastras músicos \n2. Buscar músicos \n3. Modificar músicos \n4. Montar bandas \n0. Sair \n '+ '-'*33 + ' \nDigite o número correspondente a opção desejada: '))
    while opcao != 0:
        if opcao == 1:
            incluir_musicos()
        elif opcao == 2:
            buscar_musico()
        elif opcao == 3:
            alterar_musico()
        elif opcao == 4:
            montar_banda()
        opcao = int (input('\n Bandas on-line | Seja bem-vindo! \n'+ '-'*33 +'\n1. Cadastras músicos \n2. Buscar músicos \n3. Modificar músicos \n4. Montar bandas \n0. Sair \n '+ '-'*33 + ' \nDigite o número correspondente a opção desejada: '))


try:
    arquivo = open('banco_de_bandas.csv', 'r')
except FileNotFoundError:
    tabela = [['nome', 'e_mail', 'genero_musical', 'instrumentos']]
    arquivo = open('banco_de_bandas.csv', 'w')
    dados = csv.writer(arquivo, delimiter=';', lineterminator='\n')
    dados.writerows(tabela)
arquivo.close()

menu()