﻿print('=======================================================')
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
print('================ QUESTÃO 2 =============================')
print('Ex 3A: Uso o Comando While.')
print('Contar Valores de 0 até 200, São Múltiplos de 7.')
print('')

Contar=0; i=0
while i<200:
    if i%7==0:
        Contar=Contar+1
    i=i+1
print('Múltiplos de 7 São:', Contar)
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
    print('----------- Fim da Questao2!!    -----------------------')
t = input("Digite 2 Segundos: ") 
print('========================================================')
countdown(int(t)) 
print('========================================================')
