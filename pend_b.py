import math
import matplotlib.pyplot as plt

## variaveis globais definidas pelo professor ##
M=4
m=1
g=9.81
l=0.7
PI=3.14159

ml=m*l
MMm=M+m


## funcao enviada pelo professor ##
## recebe um vetor contendo ##
## 1: angulo ##
## 2: posicao no eixo X ##
## 3: velocidade angular ##
## 4: velocidade no eixo X ##
## a forca que sera aplicada ao carrinho ##
## e pra quanto tempo depois desse ser calculada a situacao do carrinho e do pendulo ##
def RK4_pend(V,force,dt):

	h=dt/2	
	A=[]
	B=[]
	C=[]
	D=[]
	Vn=[0,0,0,0]
	f=force

	a0=V[0]
	x0=V[1]
	w0=V[2]
	v0=V[3]

	a=a0
	x=x0
	w=w0
	v=v0
	senA=math.sin(a)
	cosA=math.cos(a)
	dw0=(f+MMm*g*senA/cosA-ml*w*w*senA) / (MMm*l/cosA-ml*cosA)
	dv0=(f+ml*dw0*cosA-ml*w*w*senA) / MMm
	
	A=[w]
	A.append(v)
	A.append(dw0)
	A.append(dv0)

	a=a0+h*A[0]/2.
	x=x0+h*A[1]/2.
	w=w0+h*A[2]/2.
	v=v0+h*A[3]/2.
	senA=math.sin(a)
	cosA=math.cos(a)

	B=[w]
	B.append(v)
	dw=(f+MMm*g*senA/cosA-ml*w*w*senA) / (MMm*l/cosA-ml*cosA)
	B.append(dw)
	dv=(f+ml*dw*cosA-ml*w*w*senA) / MMm
	B.append(dv)

	a=a0+h*B[0]/2.
	x=x0+h*B[1]/2.
	w=w0+h*B[2]/2.
	v=v0+h*B[3]/2.
	senA=math.sin(a)
	cosA=math.cos(a)

	C=[w]
	C.append(v)
	dw=(f+MMm*g*senA/cosA-ml*w*w*senA) / (MMm*l/cosA-ml*cosA)
	C.append(dw)
	dv=(f+ml*dw*cosA-ml*w*w*senA) / MMm
	C.append(dv)

	a=a0+h*C[0]
	x=x0+h*C[1]
	w=w0+h*C[2]
	v=v0+h*C[3]
	senA=math.sin(a)
	cosA=math.cos(a)

	D=[a]
	D.append(x)
	dw=(f+MMm*g*senA/cosA-ml*w*w*senA) / (MMm*l/cosA-ml*cosA)
	D.append(dw)
	dv=(f+ml*dw*cosA-ml*w*w*senA) / MMm
	D.append(dv)

	for i in range(4):
		Vn[i] = V[i] + (h/6.0)*(A[i]+2.0*B[i]+2.0*C[i]+D[i]) 
	return Vn

## recebe um angulo e determina seu grau de pertinencia para o grupo 1 (caindo esquerda) ##

def fuzzifica_angulo_grupo1(angulo):

        if(angulo < -0.87):
                return 1
        else:
                subida = ((-0.35)-angulo)/((-0.35)-(-0.87))
                if(subida>0):
                        return subida
                else:
                        return 0

## recebe uma velocidade angular e determina seu grau de pertinencia para o grupo 1 (muito rapido esquerda) ##

def fuzzifica_velang_grupo1(velang):

        if(velang < -2):
                return 1
        else:
                subida = ((-1)-velang)/((-1)-(-2))
                if(subida>0):
                        return subida
                else:
                        return 0

## recebe um angulo e determina seu grau de pertinencia para o grupo 5 (caindo direita) ##
                
def fuzzifica_angulo_grupo5(angulo):

        if(angulo > 0.87):
                return 1
        else:
                subida = (angulo-0.35)/(0.87-0.35)
                if(subida>0):
                        return subida
                else:
                        return 0

## recebe uma velocidade angular e determina seu grau de pertinencia para o grupo 5 (muito rapido direita) ##

def fuzzifica_velang_grupo5(velang):

        if(velang > 2):
                return 1
        else:
                subida = (velang-1)/(2-1)
                if(subida>0):
                        return subida
                else:
                        return 0

## recebe um angulo e determina seu grau de pertinencia para o grupo 4 (pequeno direita) ##

def fuzzifica_angulo_grupo4(angulo):

        subida = (angulo - 0) / (0.35 - 0)
        descida = (0.7 - angulo) / (0.7 - 0.35)

        if(subida < descida):
                if(subida > 0):
                        return subida
                else:
                        return 0
        else:
                if(descida > 0):
                        return descida
                else:
                        return 0

## recebe uma velocidade angular e determina seu grau de pertinencia para o grupo 4 (rapido direita) ##

def fuzzifica_velang_grupo4(velang):

        subida = (velang - 0) / (1 - 0)
        descida = (2 - velang) / (2 - 1)

        if(subida < descida):
                if(subida > 0):
                        return subida
                else:
                        return 0
        else:
                if(descida > 0):
                        return descida
                else:
                        return 0

## recebe um angulo e determina seu grau de pertinencia para o grupo 2 (pequeno esquerda) ##

def fuzzifica_angulo_grupo2(angulo):

        subida = (0 - angulo) / (0 - (-0.35))
        descida = (angulo - (-0.7)) / ((-0.35) - (-0.7))

        if(subida < descida):
                if(subida > 0):
                        return subida
                else:
                        return 0
        else:
                if(descida > 0):
                        return descida
                else:
                        return 0

## recebe uma velocidade angular e determina seu grau de pertinencia para o grupo 2 (rapido esquerda) ##

def fuzzifica_velang_grupo2(velang):

        subida = (0 - velang) / (0 - (-1))
        descida = (velang - (-2)) / ((-1) - (-2))

        if(subida < descida):
                if(subida > 0):
                        return subida
                else:
                        return 0
        else:
                if(descida > 0):
                        return descida
                else:
                        return 0

## recebe um angulo e determina seu grau de pertinencia para o grupo 3 (OK) ##

def fuzzifica_angulo_grupo3(angulo):

        subida = (0.35 - angulo) / (0.35 - 0)
        descida = (angulo - (-0.35)) / (0 - (-0.35))

        if(subida < descida):
                if(subida > 0):
                        return subida
                else:
                        return 0
        else:
                if(descida > 0):
                        return descida
                else:
                        return 0
                
## recebe uma velocidade angular e determina seu grau de pertinencia para o grupo 3 (devagar) ##

def fuzzifica_velang_grupo3(velang):

        subida = (0.1 - velang) / (0.1 - 0)
        descida = (velang - (-0.1)) / (0 - (-0.1))

        if(subida < descida):
                if(subida > 0):
                        return subida
                else:
                        return 0
        else:
                if(descida > 0):
                        return descida
                else:
                        return 0

## recebe o grau de pertinencia de um angulo e de uma velocidade, ve qual o menor e ##
## retorna a area gerada por este grau de pertinencia no grupo 4 de forca (weak direita)##

def defuzzifica_for_grupo4 (grau1,grau2):

        if(grau1>grau2):
                grau=grau2
        else:
                grau=grau1

        x1 = (grau - 0) / (1.0/10) 

        x2 = (grau - 2) / ((-1.0)/10)

        area = ((20 + (x2 - x1)) * grau) / 2

        return area

## recebe o grau de pertinencia de um angulo e de uma velocidade, ve qual o menor e ##
## retorna a area gerada por este grau de pertinencia no grupo 3 de forca (weak esquerda)##

def defuzzifica_for_grupo3 (grau1,grau2):

        if(grau1>grau2):
                grau=grau2
        else:
                grau=grau1

        x1 = (grau - 0) / (1.0/10) 

        x2 = (grau - 2) / ((-1.0)/10)

        area = ((20 + (x2 - x1)) * grau) / 2

        return area

## recebe o grau de pertinencia de um angulo e de uma velocidade, ve qual o menor e ##
## retorna a area gerada por este grau de pertinencia no grupo 5 de forca (strong direita)##

def defuzzifica_for_grupo5 (grau1,grau2):

        if(grau1>grau2):
                grau=grau2
        else:
                grau=grau1

        x1 = (grau + 0.6667) / (1.0/30) 

        x2 = (grau - 2.6667) / ((-1.0)/30)

        area = ((60 + (x2 - x1)) * grau) / 2

        return area

## recebe o grau de pertinencia de um angulo e de uma velocidade, ve qual o menor e ##
## retorna a area gerada por este grau de pertinencia no grupo 2 de forca (strong esquerda)##

def defuzzifica_for_grupo2 (grau1,grau2):

        if(grau1>grau2):
                grau=grau2
        else:
                grau=grau1

        x1 = (grau + 0.6667) / (1.0/30) 

        x2 = (grau - 2.6667) / ((-1.0)/30)

        area = ((60 + (x2 - x1)) * grau) / 2

        return area

## recebe o grau de pertinencia de um angulo e de uma velocidade, ve qual o menor e ##
## retorna a area gerada por este grau de pertinencia no grupo 6 de forca (muito strong direita)##

def defuzzifica_for_grupo6 (grau1,grau2):

        if(grau1>grau2):
                grau=grau2
        else:
                grau=grau1

        x1 = (grau + 4) / (1.0/20) 

        x2 = (grau - 6) / ((-1.0)/20)

        area = ((40 + (x2 - x1)) * grau) / 2

        return area

## recebe o grau de pertinencia de um angulo e de uma velocidade, ve qual o menor e ##
## retorna a area gerada por este grau de pertinencia no grupo 1 de forca (muito strong esquerda)##

def defuzzifica_for_grupo1 (grau1,grau2):

        if(grau1>grau2):
                grau=grau2
        else:
                grau=grau1

        x1 = (grau + 4) / (1.0/20) 

        x2 = (grau - 6) / ((-1.0)/20)

        area = ((40 + (x2 - x1)) * grau) / 2

        return area

def FUZZYCONTROL(V,t):

        ## fuzzifica o angulo e a forca, onde a variavel angG1-angG5 guarda o grau de pertinencia do angulo para cada um de seus grupos ##
        ## e velG1-velG5 faz o mesmo para a velocidade angular ##

        angG1 = fuzzifica_angulo_grupo1(V[0])
        
        angG2 = fuzzifica_angulo_grupo2(V[0])

        angG3 = fuzzifica_angulo_grupo3(V[0])

        angG4 = fuzzifica_angulo_grupo4(V[0])

        angG5 = fuzzifica_angulo_grupo5(V[0])

        velG1 = fuzzifica_velang_grupo1(V[2])
        
        velG2 = fuzzifica_velang_grupo2(V[2])
        
        velG3 = fuzzifica_velang_grupo3(V[2])
        
        velG4 = fuzzifica_velang_grupo4(V[2])
        
        velG5 = fuzzifica_velang_grupo5(V[2])

        ## seta a area resultante da inferencia para 0 em todos os 6 conjuntos de forca ##

        forG1=forG2=forG3=forG4=forG5=forG6=0

        ## faz os testes de inferencia, chamando a funcao de deffuzificacao equivalente quando a inferencia for valida ##
        ## alem disso, testa nao ha um grau de pertinencia maior que ja gerou uma area para aquele conjunto de forca ##

        ## primeira coluna da tabela de regras ##

        if(angG1>0 and velG1 > 0):
                temp = defuzzifica_for_grupo6(angG1,velG1)
                if(temp > forG6):
                        forG6 = temp

        if(angG2>0 and velG1 > 0):
                temp = defuzzifica_for_grupo6(angG2,velG1)
                if(temp > forG6):
                        forG6 = temp

        if(angG3>0 and velG1 > 0):
                temp = defuzzifica_for_grupo5(angG3,velG1)
                if(temp > forG5):
                        forG5 = temp

        if(angG4>0 and velG1 > 0):
                temp = defuzzifica_for_grupo4(angG4,velG1)
                if(temp > forG4):
                        forG4 = temp

        if(angG5>0 and velG1 > 0):
                temp = defuzzifica_for_grupo3(angG5,velG1)
                if(temp > forG3):
                        forG3 = temp

        ## segunda coluna da tabela de regras ##

        if(angG1>0 and velG2 > 0):
                temp = defuzzifica_for_grupo6(angG1,velG2)
                if(temp > forG6):
                        forG6 = temp

        if(angG2>0 and velG2 > 0):
                temp = defuzzifica_for_grupo6(angG2,velG2)
                if(temp > forG6):
                        forG6 = temp

        if(angG3>0 and velG2 > 0):
                temp = defuzzifica_for_grupo4(angG3,velG2)
                if(temp > forG4):
                        forG4 = temp

        if(angG4>0 and velG2 > 0):
                temp = defuzzifica_for_grupo3(angG4,velG2)
                if(temp > forG3):
                        forG3 = temp

        if(angG5>0 and velG2 > 0):
                temp = defuzzifica_for_grupo1(angG5,velG2)
                if(temp > forG1):
                        forG1 = temp

        ## terceira coluna da tabela de regras ##

        if(angG1>0 and velG3 > 0):
                temp = defuzzifica_for_grupo6(angG1,velG3)
                if(temp > forG6):
                        forG6 = temp

        if(angG2>0 and velG3 > 0):
                temp = defuzzifica_for_grupo5(angG2,velG3)
                if(temp > forG5):
                        forG5 = temp

        ## esta coluna tem uma linha a menos, pois qnd for velang DEV e angulo OK nada sera feito ##

        if(angG4>0 and velG3 > 0):
                temp = defuzzifica_for_grupo2(angG4,velG3)
                if(temp > forG2):
                        forG2 = temp

        if(angG5>0 and velG3 > 0):
                temp = defuzzifica_for_grupo1(angG5,velG3)
                if(temp > forG1):
                        forG1 = temp

        ## quarta coluna da tabela de regras ##

        if(angG1>0 and velG4 > 0):
                temp = defuzzifica_for_grupo6(angG1,velG4)
                if(temp > forG6):
                        forG6 = temp

        if(angG2>0 and velG4 > 0):
                temp = defuzzifica_for_grupo4(angG2,velG4)
                if(temp > forG4):
                        forG4 = temp

        if(angG3>0 and velG4 > 0):
                temp = defuzzifica_for_grupo3(angG3,velG4)
                if(temp > forG3):
                        forG3 = temp

        if(angG4>0 and velG4 > 0):
                temp = defuzzifica_for_grupo1(angG4,velG4)
                if(temp > forG1):
                        forG1 = temp

        if(angG5>0 and velG4 > 0):
                temp = defuzzifica_for_grupo1(angG5,velG4)
                if(temp > forG1):
                        forG1 = temp

        ## quinta coluna da tabela de regras ##

        if(angG1>0 and velG5 > 0):
                temp = defuzzifica_for_grupo4(angG1,velG5)
                if(temp > forG4):
                        forG4 = temp

        if(angG2>0 and velG5 > 0):
                temp = defuzzifica_for_grupo4(angG2,velG5)
                if(temp > forG3):
                        forG3 = temp

        if(angG3>0 and velG5 > 0):
                temp = defuzzifica_for_grupo2(angG3,velG5)
                if(temp > forG2):
                        forG2 = temp

        if(angG4>0 and velG5 > 0):
                temp = defuzzifica_for_grupo1(angG4,velG5)
                if(temp > forG1):
                        forG1 = temp

        if(angG5>0 and velG5 > 0):
                temp = defuzzifica_for_grupo1(angG5,velG5)
                if(temp > forG1):
                        forG1 = temp

        ## calculo da centroide das areas dos conjuntos de forca ##

        centroide = (forG1 * (-100) + forG2 * (-50) + forG3 * (-10) + forG4 * 10 + forG5 * 50 + forG6 * 100) / (forG1+forG2+forG3+forG4+forG5+forG6)

        return centroide


## funcao fornecida pelo professor que recebe um tempo pelo qual deve-se tentar equilibrar o pendulo ##
## essa funcao faz a chamada da funcao que ira determinar a forca a ser colocada no carrinho ##

def main(tmax):
        dt=0.01
        samp=10
        count=0
        Vars=[]
        T=[]
        X=[1.05,0,0,0]			# lista com as vars iniciais [ang, pos_X, vel_ang, vel_X]
        t=0.
        while t < tmax :
                aux=[]
                if count == 0:			# amostragem - a variacao da forca se da a cada 0.1s
                        f=FUZZYCONTROL(X,t)	# chama a fcao que retorna a forca de controle

                X=RK4_pend(X,f,dt)	
                count+=1
                if count == samp:
                        count=0
                T.append(t)
                aux=[]
                for i in range(4):
                        aux.append(X[i])
                aux.append(f)
                Vars.append(aux)
                t=t+dt

        ang=plt.plot(T,Vars)
        plt.show()

main(20)
