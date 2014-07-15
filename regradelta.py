import random

def regradelta(matrizTreino):
    ## posicao 0 tem o teta e de 1 a 10 os Wi ##
    w = [-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5]
    ## intesidade do deslocamento eh de 0.1 ##
    mi = 0.1
    ## guarda a somatoria dos erros, deve comecar com valor diferente de 0 para entrar no while ##
    et = 1
    ## variavel que guarda a quantidade de vezes que o programa iterou ##
    iteractions = 0
    ## criterio de parada eh enqnt o erro nao for 0 ou enqnt nao chegar a 10k iteracoes ##
    while ((et != 0) and (iteractions < 10000)):
        ## seta o somatorio dos erros para 0 a cada comeco de iteracao ##
        et = 0
        ## mistura os exemplos que serao usados para aprender ##
        random.shuffle(matrizTreino)
        ## percorre os exemplos ##
        for teste in matrizTreino:
            ## calcula o valor de Y para o vetor w e o teste atual ##
            y = calcula(w,teste)
            ## calcula o erro deste exemplo ##
            erro = y - teste[0]
            ## percorre o vetor de W e de teta ##
            for i in range(len(w)):                      
                if (i==0):
                    ## calcula o teta usando a formula passada em sala ##
                    w[i] += mi * erro                    
                else :
                    ## calcula os W's usando a formula passada em sala ##
                    w[i] -= mi * erro * teste[i]
            ## faz o somatorio modular dos erros ##
            et += abs(erro)
            ## aumenta o valor da interacao ##
            iteractions += 1
    ## ao final, retorna o vetor de pesos sinapticos usado ##
    return w                                             


## calcula (somatorio de Wi Xi) - teta, se for maior que zero retorna 1, caso contrario 0 ##
def calcula(w,teste):
    x= - w[0]
    for i in range(1,len(w)):
        x += w[i] * teste[i]
    if x > 0:
        return 1
    return 0

## primeira posicao fala se eh peixe ou nao e a restante sao os xi ##
matrixtr= [                         
    [1, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 1 ],        # bass
    [1, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 1 ],        # carp
#[1, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 1 ],        # catfish, sera usado para teste
#[1, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 1 ],        # chub, sera usado para teste
    [1, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 1 ],        # dogfish
    [1, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 1 ],        # haddock
    [1, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 1 ],        # herring
    [1, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 1 ],        # pike
    [1, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 1 ],        # piranha
    [1, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 1 ],        # seahorse
    [1, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 1 ],        # sole
    [1, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 1 ],        # stingray
    [1, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 1 ],        # tuna
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 0 ],        # aardvark
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # antelope
#[0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 0 ],        # bear, sera usado para teste
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # boar
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # buffalo
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # calf
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 0 ],        # cavy
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # cheetah
    [0, 1 , 1 , 0 , 1 , 0 , 0 , 1 , 1 , 0 , 1 ],        # chicken
    [0, 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],        # clam
    [0, 0 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ],        # crab
    [0, 0 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ],        # crayfish
#[0, 1 , 1 , 0 , 1 , 0 , 0 , 1 , 1 , 0 , 1 ],        # crow, sera usado para teste
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # deer
#[0, 0 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 1 ],        # dolphin, sera usado para teste
    [0, 1 , 1 , 0 , 1 , 0 , 0 , 1 , 1 , 0 , 1 ],        # dove
    [0, 1 , 1 , 0 , 1 , 1 , 0 , 1 , 1 , 0 , 1 ],        # duck
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # elephant
    [0, 1 , 1 , 0 , 1 , 0 , 0 , 1 , 1 , 0 , 1 ],        # flamingo
    [0, 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ],        # flea
    [0, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 ],        # frog
    [0, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 ],        # frog
    [0, 0 , 0 , 1 , 1 , 0 , 1 , 1 , 1 , 0 , 1 ],        # fruitbat
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # giraffe
#[0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 0 ],        # girl, sera usado para teste
    [0, 0 , 1 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 ],        # gnat
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # goat
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 0 ],        # gorilla
    [0, 1 , 1 , 0 , 1 , 1 , 0 , 1 , 1 , 0 , 1 ],        # gull
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # hamster
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # hare
    [0, 1 , 1 , 0 , 1 , 0 , 0 , 1 , 1 , 0 , 1 ],        # hawk
    [0, 0 , 1 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 ],        # honeybee
    [0, 0 , 1 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 ],        # housefly
    [0, 1 , 1 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 1 ],        # kiwi
    [0, 0 , 1 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 ],        # ladybird
    [0, 1 , 1 , 0 , 1 , 0 , 0 , 1 , 1 , 0 , 1 ],        # lark
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # leopard
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # lion
#[0, 0 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ],        # lobster, sera usado para teste
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # lynx
    [0, 0 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 0 , 1 ],        # mink
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # mole
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # mongoose
#[0, 0 , 1 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 ],        # moth, sera usado para teste
    [0, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 1 ],        # newt
    [0, 0 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ],        # octopus
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # opossum
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # oryx
    [0, 1 , 1 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 1 ],        # ostrich
    [0, 1 , 1 , 0 , 1 , 0 , 0 , 1 , 1 , 0 , 1 ],        # parakeet
    [0, 1 , 1 , 0 , 0 , 1 , 0 , 1 , 1 , 0 , 1 ],        # penguin
    [0, 1 , 1 , 0 , 1 , 0 , 0 , 1 , 1 , 0 , 1 ],        # pheasant
    [0, 0 , 1 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # pitviper
    [0, 0 , 1 , 1 , 0 , 1 , 0 , 1 , 1 , 0 , 1 ],        # platypus
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # polecat
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # pony
    [0, 0 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 1 ],        # porpoise
#[0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # puma, sera usado para teste
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # pussycat
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # raccoon
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # reindeer
    [0, 1 , 1 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 1 ],        # rhea
    [0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 1 ],        # scorpion
    [0, 0 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 ],        # seal
#[0, 0 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 1 ],        # sealion, sera usado para teste
    [0, 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 1 ],        # seasnake
    [0, 0 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ],        # seawasp
    [0, 1 , 1 , 0 , 1 , 1 , 0 , 1 , 1 , 0 , 1 ],        # skimmer
    [0, 1 , 1 , 0 , 1 , 1 , 0 , 1 , 1 , 0 , 1 ],        # skua
    [0, 0 , 1 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # slowworm
    [0, 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ],        # slug
    [0, 1 , 1 , 0 , 1 , 0 , 0 , 1 , 1 , 0 , 1 ],        # sparrow
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # squirrel
    [0, 0 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ],        # starfish
    [0, 1 , 1 , 0 , 1 , 1 , 0 , 1 , 1 , 0 , 1 ],        # swan
    [0, 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ],        # termite
#[0, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 ],        # toad, sera usado para teste
    [0, 0 , 1 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 1 ],        # tortoise
    [0, 0 , 1 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # tuatara
    [0, 0 , 0 , 1 , 1 , 0 , 1 , 1 , 1 , 0 , 1 ],        # vampire
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # vole
    [0, 1 , 1 , 0 , 1 , 0 , 0 , 1 , 1 , 0 , 1 ],        # vulture
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # wallaby
    [0, 0 , 1 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 ],        # wasp
    [0, 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 ],        # wolf
    [0, 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ],        # worm
    [0, 1 , 1 , 0 , 1 , 0 , 0 , 1 , 1 , 0 , 1 ]]        # wren
    
w = regradelta(matrixtr)
## colocar a entrada para qual voce deseja testar ##
teste = [0, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 ]
if (calcula(w,teste)==1) :
    print('Eh peixe')
else :
    print('Nao eh peixe')
