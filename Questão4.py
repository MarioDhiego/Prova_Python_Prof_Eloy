print('=======================================================')
print('Universidade: UFPA                                   ==')
print('Curso       : Sistemas de Informação                 ==')
print('Disciplina  : Programação I                          ==')
print('Docente     : Eloi Fávero                            ==')
print('Discente    : Mário Diego Rocha Valente              ==')
print('Matrícula   : 202211140042	                     ==')
print('=======================================================')
print('')
print('')

print('=============== 1ª AVALIAÇÃO ==========================')
print('Programação I em Python      ==========================')
print('Prova Tipo Impares           ==========================')
print('=======================================================')
print('')
print('')

print('')
print('')
print('========================================================')
print('=================== QUESTÃO 4 ==========================')
print('Ex 3A: Uso o Comando While.')
print('Ler Dois Valores X e Y.')
print('Escolher o Menor dos Valores')
print('Escolher o Maior dos Valores')
print('Percorrer do Menor até Maior e Contar Múltiplos 13')
print('')

print('--------------------------------------------------------')
X=int(input('Digite o Valor de X:'))
Y=int(input('Digite o Valor de Y:'))
print('--------------------------------------------------------')
print('Os Valores Digitados São:', X, Y)
def Menor(X,Y):
  if X>Y: return Y
  else: return X
def Maior(X,Y):
  if X<Y: return Y
  else: return X
Menor=Menor(X,Y)
Maior=Maior(X,Y)
print('--------------------------------------------------------')
print('O Menor dos Valores entre X e Y é:', Menor)
print('O Maior dos Valores entre X e Y é:', Maior)
print('--------------------------------------------------------')
Multiplo=0
while Menor<=Maior:
  if Menor%13==0 :
    Multiplo+=1
    Menor+=1
  else:
    Menor+=1
print('Multiplos de 13 São:', Multiplo)
print('========================================================')
print('')
print('')



print('========================================================')
import time 
def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    print('')
    print('----------- Fim da Questao4!!    -----------------------')
t = input("Digite 2 Segundos: ") 
print('========================================================')
countdown(int(t)) 
print('========================================================')