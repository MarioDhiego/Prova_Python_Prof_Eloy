print('=======================================================')
print('Universidade: UFPA                                   ==')
print('Curso       : Sistemas de Informação                 ==')
print('Disciplina  : Programação I                          ==')
print('Docente     : Eloi Fávero                            ==')
print('Discente    : Mário Diego Rocha Valente              ==')
print('Matrícula   : 202211140042	                    ==')
print('=======================================================')
print('')

print('=============== 1ª AVALIAÇÃO ==========================')
print('Programação I em Python      ==========================')
print('Prova Tipo A                 ==========================')
print('=======================================================')
print('')
print('')

print('=======================================================')
print('================ QUESTÃO 1 ============================')
print('Ex 1A: Ler a Lista de Idades e Calcular a Média')
print('')

print('-------------------------------------------------------')
A= input('(OBS: Digitar Idades Separado p/ Virgulas)\n Qual(s) são as Idades:')
Vetor1 = A.split(',')
Vetor2 = [int(i) for i in Vetor1]
print('-------------------------------------------------------')
print('\n Idades:',Vetor2)
print('-------------------------------------------------------')
Soma=0; Amostra=0
for i in Vetor2: Soma+=i; Amostra+=1
Média = (Soma/Amostra)
print('Idade Média:', Média)
print('=======================================================')
print('')
print('')


print('=======================================================')
print('================ Histograma ===========================')
print('')

import matplotlib.pyplot as plt
plt.title('Histograma das Idades')
plt.xlabel('Idades')
plt.ylabel('Frequência Absoluta')
plt.hist(Vetor2, 5, rwidth=0.9, color='red')
plt.show()
print('=======================================================')
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
    print('----------- Fim da Questao1!!    -----------------------')
t = input("Digite 2 Segundos: ") 
print('========================================================')
countdown(int(t)) 
print('========================================================')