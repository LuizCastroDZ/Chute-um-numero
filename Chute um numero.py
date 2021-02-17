import random

Chute = random.randrange(1, 10)                                         #variavel que recebe um numero aleatorio de 1 a 10 ou mais.

i = 1                                                                   #variavel pra controlar o WHILE.

tent = 3                                                                #variavel que controla as tentativas do usuario.

while i == 1:                                                           #loop do programa que sera interrompido caso o usuario errar 3 vezes.
    
    Tentat = int(input('Digite um numero: '))                           #entrada de dado que o usuario escolherá um numero.
    
    if Chute > Tentat:                                                  #Se o chute for maior que a tentativa do usuario, avisar que foi auto demais.
        print('Chute muito abaixo! Suas tentativas restantes: ',tent)   
        tent += -1                                                      #Tirar 1 numero das tentativas que resta.

    elif Chute < Tentat:                                                #Se o chute for menor que a tentativa do usuario, avisar que foi baixo demais.
        print('Chute muito auto! Suas tentativas restantes: ',tent)
        tent += -1                                                      #Tirar 1 numero das tentativas que resta.

    else:                                                               #Caso o numero que o usuario chutar for igual ao numero do (CHUTE) avisar acerto.
        print('Acertou!')
        i += 1                                                          #Caso o usuario acerto o numero somar 1 a variavel de contro do WHILE.

    if tent == 0:                                                       #Para cada tentativa errada, diminuir um da variavel tentativa.
        i += 1