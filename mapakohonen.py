import string
import random

## esta funcao faz a leitura do arquivo do Wine Data Set retornando uma matriz com os valores lidos ##
def creatematriz(nomearq):
    ## cria a matriz a ser retornada ##
    ## a primeira coluna possui a classe original, as 13 seguintes sao os dados ##
    ## e a ultima eh a classe designada pelo algoritmo ##
    matrizretorno = [[0 for e in range(15)] for e in range(178)]
    ## abre o arquivo no modo de leitura ##
    a = open(nomearq,"r")
    ## itera sobre as 178 linhas do arquivo ##
    for i in range(178):
        ## le uma linha e a atribui p/ variavel 'linha' ##
        linha = a.readline()
        ## separa a linha nas virgulas, colocando cada texto separado num vetor de strings ##
        partes = linha.split(",")
        ## itera sobre as 14 partes no qual a linha foi separada, atribuindo cada uma delas p/ a posicao devida na matriz ##
        ## eh bom lembrar que eh necessario converter cada uma dessas 14 partes para float, uma vez que foi pego do arquivo como string ##
        for j in range(14):
            matrizretorno[i][j] = float(partes[j])
    ## retorna a matriz com as posicoes preenchidas ##
    return matrizretorno

#      *(0)
#    *(1) *(2)
#  *(3) *(4) *(5)
## retorna os vizinhos de 'quem' para o grau 'nivel', seguindo a numeracao da "imagem" acima ##
def vizinhos(quem,nivel):
    if(quem==0):
        if(nivel==0):
            return [0]
        if(nivel==1):
            return [1,2]
        if(nivel==2):
            return [3,4,5]
    if(quem==1):
        if(nivel==0):
            return [1]
        if(nivel==1):
            return [0,2,3,4]
        if(nivel==2):
            return [5]
    if(quem==2):
        if(nivel==0):
            return [2]
        if(nivel==1):
            return [0,1,4,5]
        if(nivel==2):
            return [3]
    if(quem==3):
        if(nivel==0):
            return [3]
        if(nivel==1):
            return [1,4]
        if(nivel==2):
            return [0,2,5]
    if(quem==4):
        if(nivel==0):
            return [4]
        if(nivel==1):
            return [1,2,3,5]
        if(nivel==2):
            return [0]
    if(quem==5):
        if(nivel==0):
            return [5]
        if(nivel==1):
            return [2,4]
        if(nivel==2):
            return [0,1,3]

## funcao que define como o eta ira variar##
## neste caso ela esta implementada seguindo o seguinte decaimento geometrico: ##
## a cada 100 iteracoes, o eta sera dividido pela metade ##
def mudaeta(iteracoes,eta):
    novoeta = eta
    if(iteracoes%100==0):
        novoeta = 0.5 * eta
    return novoeta


def mapakohonen(matriztreino):
    ## cria o vetor dos pesos sinapticos com valores randomicos, o numero de linhas eh a quantidade de atributos de entrada do problema ##
    ## e o numero de colunas eh em quantas classes o problema sera clusterizado ##
    w = [[random.random() for e in range(6)] for e in range(13)]
    ## define como os vizinhos serao afetados por alteracoes feitas no ganhador (de certa forma eh a funcao V(x,y)##
    ## o ganhador sera afetado inteiramente, por isso 1 na primeira posicao ##
    ## o primeiro vizinho sera afetado pela metade, por isso 0.5 na segunda posicao ##
    ## e como sugerido pelo professor, apenas o primeiro vizinho sera considerado, portanto 0 na terceira posicao ##
    mudavizinhos = [1,0.5,0]
    ## valor inicial do eta ##
    eta = 0.6
    ## inicializa as iteracoes ##
    iteractions = 0
    ## roda o algoritmo enquanto o numero de iteracoes for menor que mil ##
    while(iteractions<1000):
        ## mistura a ordem que as entradas serao apresentadas ##
        random.shuffle(matriztreino)
        ## pra cada entrada roda o proximo bloco ##
        for treino in matriztreino:
            ## seta o menor D(j) como sendo infinito, desta forma qualquer um dos D(j) ganharao dele ##
            menor = float("inf")
            ## seta a posicao do menor D(j) como sendo uma posicao invalida ##
            menorposit = -1
            ## faz para cada uma das 6 classes do algoritmo o proximo bloco ##
            for j in range(6):
                ## inicializa a distancia euclidiana ##
                somatorio = 0
                ## faz o calculo da distancia euclidiana para os 13 atributos ##
                ## esse calculo eh feito fazendo o somatorio da diferenca de cada entrada e do peso sinaptico correspondente e elevando ao quadrado##
                for i in range(13):
                    somatorio += (w[i][j] - treino[i+1]) ** 2
                ## caso esta distancia euclidiana seja menor que a menor distancia euclidiana anterior ##
                ## esta ditancia euclidiana passara a ser a menor e a sua posicao sera salva ##
                if(somatorio<menor):
                    menor = somatorio
                    menorposit = j

            # A partir daqui, faremos a atualizacao #

            ## salva qual foi o neuronio selecionado para esta entrada na posicao adequada da matriz original (conforme descricao da confeccao da matriz)##
            treino[14] = menorposit + 1
            ## itera sobre os 3 graus de vizinhanca existentes para este problema ##
            for viz in range(3):
                ## pega os vizinhos de grau 'viz'(0,1,2) da posicao vencedora ##
                mudar = vizinhos(menorposit,viz)
                ## itera sobre os vizinhos ##
                for r in range(len(mudar)):
                    ## altera o peso sinaptico de cada entrada de cada vizinho de acordo com o previsto no pseudocodigo ##
                    for i in range(13):
                        w[i][mudar[r]] += mudavizinhos[viz] * eta * (treino[i+1] - w[i][mudar[r]])
        ## incrementa a variavel iteracoes ##
        iteractions+= 1
        ## faz a alteracao no eta ##
        eta = mudaeta(iteractions,eta)
    ## retorna a matriz de pesos sinapticos ##
    return w

## funcao que fala quantos elementos das classes originais ha em cada classe criada pelo algoritmo ##  
def resultados(matriz):
    for i in range(3):
        primeira = 0
        segunda = 0
        terceira = 0
        quarta = 0
        quinta = 0
        sexta = 0
        for teste in matriz:
            if(teste[0]==i+1):
                if(teste[14]==1):
                    primeira+=1
                if(teste[14]==2):
                    segunda+=1
                if(teste[14]==3):
                    terceira+=1
                if(teste[14]==4):
                    quarta+=1
                if(teste[14]==5):
                    quinta+=1
                if(teste[14]==6):
                    sexta += 1
        print("Classe ",i+1,":")
        print("1: ",primeira)
        print("2: ",segunda)
        print("3: ",terceira)
        print("4: ",quarta)
        print("5: ",quinta)
        print("6: ",sexta)

## cria a matriz ##
mat = creatematriz("winedatasetdados.txt")
## executa o algoritmo para a matriz criada ##
w = mapakohonen(mat)
## chama a funcao 'resultados' para a matriz alterada pelo algoritmo de mapa de kohonen ##
resultados(mat)

