from operator import itemgetter

def menu():
    print("0 - Sair")
    print("1 - Carregar arquivo")
    print("2 - Listar arquivo")
    print("3 - Criar uma lista com os 5 times que que mais vitórias tiveram.")
    print("4 - Informar o campeão e o total de pontos de cada ano.")
    print("5 - Informar o time que mais gols fez a cada ano")
    print("6 - Informar o time que foi campeão tendo o menor valor em jogadores")
    print("7 - Informar qual time foi mais vezes rebaixado")
    print("8 - Informar a média de idade dos times a cada ano")
    print("9 - Informar o time que mais gols sofre por ano")
    print("10 - Escolha um time e mostre sua melhor e pior classificação")
    print("11 - Pontuação das equipes por ano")
    print("12 - Informe o time que mais valor teve em seus atletas ao longo do tempo")
    print("13 - Digite o time para ver o ano em que teve mais jogadores")

def carregar(arq, mat):
    arquivo = open(arq, "r")
    for linha in arquivo:
        linha = linha.replace("\n", "")
        linha = linha.replace(",", ".")
        dados = linha.split(";")
        mat.append(dados)

    arquivo.close()

def verificarNome(name, mat):
    existe = False
    for i in range(len(mat)):
        if name.lower() == mat[i][2].lower():
            existe = True
    return existe

def listarMatriz(mat):
    for i in range(len(mat)):
        print(mat[i])

def listarMaisVitorias(mat):
    dic = {}
    for i in range(1, (len(mat))):
        if mat[i][2] in dic:
            dic[mat[i][2]] = dic[mat[i][2]] + int(mat[i][3])
        else:
            dic[mat[i][2]] = int(mat[i][3])
    maisV = (sorted(dic.items(), key=itemgetter(1)))
    listaOrdenada = []
    for k in range(-1, -6, -1):
        listaOrdenada.append(maisV[k])
    return listaOrdenada

def informarCampeaoPontos(mat):
    dic = {}
    for i in range(1, len(mat)):
        if mat[i][0] in dic:
            if int(mat[i][1]) == 1:
                dic[mat[i][0]] =  mat[i][2], ((int(mat[i][3])*3) + (int(mat[i][5])*1))
        else:
            dic[mat[i][0]] = mat[i][1]
    return dic

def informarTimeMaisGolsAno(mat):
    matriz = []
    for i in range(1, (len(mat))):
        lista = []
        if len(matriz) == 0:
            lista.append(mat[i][0])
            matriz.append(lista)
        else:
            if mat[i][0] != mat[i - 1][0]:
                lista.append(mat[i][0])
                matriz.append(lista)

    for ano in range(len(matriz)):
        nomeMaior = " "
        maior = 0
        for i in range(1, (len(mat))):
            if int(mat[i][0]) == int(matriz[ano][0]):
                if int(mat[i][6]) > int(maior):
                    maior = mat[i][6]
                    nomeMaior = mat[i][2]
        matriz[ano].append(nomeMaior)

    return matriz

def informarTimeMenorValorCampeao(mat):
    menor = 999999999
    nomeMenor = ""
    for i in range(len(mat)):
        if mat[i][1] == "1":
            if int(mat[i][12]) < menor:
                menor = int(mat[i][12])
                nomeMenor = mat[i][2]
    return nomeMenor

def informarNomeMaisRebaixado(mat):
    dic = {}
    for i in range(1, (len(mat))):
        if int(mat[i][1]) > 16:
            if mat[i][2] in dic:
                dic[mat[i][2]] = dic[mat[i][2]] + 1
            else:
                dic[mat[i][2]] = 1
    maisRebaixado = []
    nroRebaixado = 0
    for j in dic.keys():
        if dic[j] > nroRebaixado or dic[j] == nroRebaixado :
            nroRebaixado = dic[j]
            maisRebaixado.append(j)
    return maisRebaixado

def mediaTimesAno(mat):
    matriz = []
    for i in range(1, (len(mat))):
        lista = []
        if len(matriz) == 0:
            lista.append(mat[i][0])
            matriz.append(lista)
        else:
            if mat[i][0] != mat[i - 1][0]:
                lista.append(mat[i][0])
                matriz.append(lista)

    for ano in range(len(matriz)):
        idadeSoma = 0
        contador = 0
        for i in range(1, (len(mat))):
            if int(mat[i][0]) == int(matriz[ano][0]):
                    idadeSoma = float(mat[i][10]) + idadeSoma
                    contador = contador + 1
        mediaIdade = idadeSoma/contador
        matriz[ano].append(round(mediaIdade,2))

    return matriz

def maisSofreGolsAno(mat):
    matriz = []
    for i in range(1, (len(mat))):
        lista = []
        if len(matriz) == 0:
            lista.append(mat[i][0])
            matriz.append(lista)
        else:
            if mat[i][0] != mat[i - 1][0]:
                lista.append(mat[i][0])
                matriz.append(lista)

    for ano in range(len(matriz)):
        nomeMaisGolsSofridos = " "
        golsSofridos = 0
        for i in range(1, (len(mat))):
            if int(mat[i][0]) == int(matriz[ano][0]):
                if int(mat[i][7]) > int(golsSofridos):
                    golsSofridos = mat[i][7]
                    nomeMaisGolsSofridos = mat[i][2]
        matriz[ano].append(nomeMaisGolsSofridos)

    return matriz

def pesquisarTime(name, mat):
    melhorPosicao = 999
    piorPosicao = 0
    listaAnoPior = []
    listaAnoMelhor = []
    for i in range(len(mat)):
        if name.lower() == mat[i][2].lower():
            if int(mat[i][1]) > piorPosicao:
                piorPosicao = int(mat[i][1])
    for j in range(len(mat)):
        if name.lower() == mat[j][2].lower():
            if int(mat[j][1]) < melhorPosicao:
                melhorPosicao = int(mat[j][1])

    for k in range(len(mat)):
        if name.lower() == mat[k][2].lower() and int(mat[k][1]) == melhorPosicao:
            listaAnoMelhor.append(mat[k][0])

    for p in range(len(mat)):
        if name.lower() == mat[p][2].lower() and int(mat[p][1]) == piorPosicao:
            listaAnoPior.append(mat[p][0])

    return melhorPosicao, piorPosicao, listaAnoMelhor, listaAnoPior


def verificarTimeExiste(mat, name):
    existe = False
    for i in range(len(mat)):
        if mat[i][0] == name:
            existe = True
    return existe


def encontrarMaiorAno(matUm, matDois):
    for i in range(len(matUm)):
        anoMaior = 0
        for j in range(1,(len(matDois))):
            if matUm[i][0] == matDois[j][2]:
                if int(matDois[j][0]) > anoMaior:
                    anoMaior = int(matDois[j][0])
        matUm.append(anoMaior)
    return matUm

def verificarPontuação(mat):
    matriz = []
    for i in range(1, (len(mat))):
        lista = []
        if len(matriz) == 0:
            lista.append(mat[i][0])
            matriz.append(lista)
        else:
            if mat[i][0] != mat[i - 1][0]:
                lista.append(mat[i][0])
                matriz.append(lista)

    for k in range(len(matriz)):
        for l in range(1, (len(mat))):
            tupla = ()
            pontuacao = 0
            lista = []
            if matriz[k][0] == mat[l][0]:
                if int(mat[l][8]) > 0:
                    pontuacao = (int(mat[l][3]) * 10) + (int(mat[l][5]) * 6) + (int(mat[l][8]) * 1)
                    tupla = (mat[l][2] + " - Pontuação: " + str(pontuacao))
                    lista.append(tupla)
                else:
                    pontuacao = (int(mat[l][3]) * 10) + (int(mat[l][5]) * 6)
                    tupla = (mat[l][2] + " - Pontuação: " + str(pontuacao))
                    lista.append(tupla)
            if len(tupla) != 0:
                matriz[k].append(lista)


    return matriz

def verificarMaisValorizado(mat):
    matriz = []
    for i in range(1, (len(mat))):
        lista = []
        if len(matriz) == 0:
            lista.append(mat[i][2])
            lista.append(mat[i][0])
            matriz.append(lista)
        else:
            nome = mat[i][2]
            existe = verificarTimeExiste(matriz, nome)
            if existe == False:
                lista.append(nome)
                lista.append(mat[i][0])
                matriz.append(lista)

    for k in range(len(matriz)):
        anoMenor = 9999
        for l in range(1, (len(mat))):
            if matriz[k][0] == mat[l][2]:
                if int(mat[l][0]) < anoMenor:
                    anoMenor = int(mat[l][0])
        matriz[k].append(anoMenor)

    for name in range(len(matriz)):
        numeroUm = 0
        numeroDois = 0
        valorDif = 0
        for u in range(1,(len(mat))):
            if matriz[name][0] == mat[u][2]:
                if int(matriz[name][1]) == int(mat[u][0]):
                    numeroUm = int(mat[u][12])
        for o in range(1, (len(mat))):
            if matriz[name][0] == mat[o][2]:
                if int(matriz[name][2]) == int(mat[o][0]):
                    numeroDois = int(mat[o][12])
        valorDif = numeroUm - numeroDois
        matriz[name].append(valorDif)

    maiorValorização = 0
    nomeValorização = ""
    for valor in range(len(matriz)):
        if matriz[valor][3] > maiorValorização:
            maiorValorização = matriz[valor][3]
            nomeValorização = matriz[valor][0]

    return nomeValorização


def verificarTimeJogadores(name, mat):
    maiorJogadores = 0
    anoJogadores = 0

    for i in range(len(mat)):
        if mat[i][2].lower() == name.lower():
            if int(mat[i][9]) > int(maiorJogadores):
                maiorJogadores = mat[i][9]
                anoJogadores = int(mat[i][0])

    return anoJogadores

matriz = []
nomeArquivo = "TabelaBrasileirao.csv"
opcao = -1


while opcao != 0:
    menu()
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        carregar(nomeArquivo, matriz)

    elif opcao == 2:
        if len(matriz) == 0:
            print("Dados nao inseridos")
        else:
            listarMatriz(matriz)
            for i in range(len(matriz)):
                print(matriz[i])

    elif opcao == 3:
        if len(matriz) == 0:
            print("Dados nao inseridos")
        else:
            maisvitoriais = listarMaisVitorias(matriz)
            print("Os times que possuem mais vitórias são: {}" .format(maisvitoriais))

    elif opcao == 4:
        if len(matriz) == 0:
            print("Dados nao inseridos")
        else:
            campeaoPontos = informarCampeaoPontos(matriz)
            print("Os campeaos de cada ano e sua quantidade de pontos são: {}" .format(campeaoPontos))

    elif opcao == 5:
        if len(matriz) == 0:
            print("Dados nao inseridos")
        else:
            timeMaisGols = informarTimeMaisGolsAno(matriz)
            print("Time que mais fizeram gols a cada ano: ")
            for i in range(len(timeMaisGols)):
                print(timeMaisGols[i])

    elif opcao == 6:
        if len(matriz) == 0:
            print("Dados nao inseridos")
        else:
            nomeDoMenor = informarTimeMenorValorCampeao(matriz)
            print("O time campeão com menor valor é: {}" .format(nomeDoMenor))

    elif opcao == 7:
        if len(matriz) == 0:
            print("Dados nao inseridos")
        else:
            nomeRebaixado = (informarNomeMaisRebaixado(matriz))
            print("O time que mais foi rebaixado é: {}" .format(nomeRebaixado))


    elif opcao == 8:
        if len(matriz) == 0:
            print("Dados nao inseridos")
        else:
            mediaTimeIdade = mediaTimesAno(matriz)
            print("A media de idade dos times em cada ano é: ")
            for i in range(len(mediaTimeIdade)):
                print((mediaTimeIdade[i]))


    elif opcao == 9:
        if len(matriz) == 0:
            print("Dados nao inseridos")
        else:
            timeMaisSofreuGolsAno = maisSofreGolsAno(matriz)
            print("Time que mais sofreram gols a cada ano: ")
            for i in range(len(timeMaisSofreuGolsAno)):
                print(timeMaisSofreuGolsAno[i])

    elif opcao == 10:
        if len(matriz) == 0:
            print("Dados nao inseridos")
        else:
            nomeTimeMelhorPior = input("Digite o nome do time para pesquisar: ")
            nomeExiste = verificarNome(nomeTimeMelhorPior, matriz)
            if nomeExiste == True:
                melhorPos, piorPos, listaMelhor, listaPior = pesquisarTime(nomeTimeMelhorPior, matriz)
                print("A melhor posição do time " + nomeTimeMelhorPior + " foi: " + str(melhorPos) + "º E aconteceu nos ano(s):" + str(listaMelhor))
                print("A pior posição do time " + nomeTimeMelhorPior + " foi: " + str(piorPos) + "º E aconteceu nos ano(s):" + str(listaPior))
            else:
                print("Nome de time nao existe")

    elif opcao == 11:
        if len(matriz) == 0:
            print("Dados nao inseridos")
        else:
            pontuacaoAnos = verificarPontuação(matriz)
            for i in range(len(pontuacaoAnos)):
                print(pontuacaoAnos[i])

    elif opcao == 12:
        if len(matriz) == 0:
            print("Dados nao inseridos")
        else:
            nomeValor = verificarMaisValorizado(matriz)
            print("O time que mais teve valor em seus atletas ao longo do tempo é: {}" .format(nomeValor))

    elif opcao == 13:
        if len(matriz) == 0:
            print("Dados nao inseridos")
        else:
            nomeTime = input("Digite o nome do time: ")
            anoTimeMaisJogadores = verificarTimeJogadores(nomeTime, matriz)
            print("O ano em que o " + nomeTime + " teve mais jogadores foi: " + str(anoTimeMaisJogadores))
