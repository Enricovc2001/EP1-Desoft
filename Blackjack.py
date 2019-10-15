#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 14:43:54 2019

@author: enricocosta
"""
import random


score = open('carteira.txt','r')
score_jogador=[float(score.readline())]
#print(score.readline())
score.close()
aposta=input('Quanto vc quer apostar essa rodada? ')

cartas_computador = []
cartas_jogador = []

# feature 2, para tirar a aposta escrevendo fim.
for i in score_jogador:
    if aposta == 'fim':
        print('Vc saiu do jogo. Vc saiu com R$ {0:.2f}'.format(sum(score_jogador)))
        break
    aposta = int(aposta)
    
    if aposta <= 0:
        print('Aposta invalida, aposte novamente') 
        aposta=int(input('Quanto vc quer apostar essa rodada? '))      
        break       
    if aposta > sum(score_jogador):
        print('Aposta invalida, aposte novamente')
        aposta=int(input('Quanto vc quer apostar essa rodada? '))  
        break

    # código das cartas do computador
    while len(cartas_computador) != 2:
        cartas_computador.append(random.randint(2, 11))
        if len(cartas_computador) == 2:
            print('As cartas dele são:{0} '.format(cartas_computador))
    # código das cartas do jogador
    while len(cartas_jogador) != 2:
        cartas_jogador.append(random.randint(2, 11))
        if len(cartas_jogador) == 2:
            print('Suas cartas são:{0} '.format(cartas_jogador))
    # soma das cartas do computador
    if sum(cartas_computador) == 21:
        score_jogador.append(-aposta)
        print('Computador venceu!')
    elif sum(cartas_computador) > 21:
        vitoria=aposta*1.5
        score_jogador.append(vitoria)
        print('Computador perdeu!')
    # soma das cartas do jogador
    while sum(cartas_jogador) < 21:
        escolha = str(input('Voce deseja tirar mais duas cartas? (s/n): '))
        if escolha == 's':
            cartas_jogador.append(random.randint(2, 11))
            cartas_jogador.append(random.randint(2, 11))
            print('Suas novas duas cartas são: {0} '.format(cartas_jogador[-2:]))
            print('Voce tem um total de: {0}'.format(sum(cartas_jogador)))
        if escolha == 'n':
            print('O computador tem um total de: {0}'.format(sum(cartas_computador)))
            print('Voce tem um total de: {0}'.format(sum(cartas_jogador)))
            if sum(cartas_computador) > sum(cartas_jogador):
                
                score_jogador.append(-aposta)
                print(score_jogador)
                print('Computador venceu!')
                break
            else:
                vitoria=aposta*1.5
                score_jogador.append(vitoria)       
                print('Voce venceu')
                break
    
    soma=0
    for i in score_jogador:
        soma+=i
    print('Vc possui R$ {0:.2f}'.format(soma))

    if sum(score_jogador) <= 0:
        print('Vc faliu')
        break 
    
    s= open('carteira.txt','w')
    s.writelines(str(soma))
    s.close()
 
    break
                   
        
if sum(cartas_jogador) > 21:
    score_jogador.append(-aposta)
    print('Voce perdeu!')
elif sum(cartas_jogador) == 21:
    vitoria=aposta*1.5
    score_jogador.append(vitoria)
    print('Blackjack, voce venceu!')
