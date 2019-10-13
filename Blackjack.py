#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 14:43:54 2019

@author: enricocosta
"""
import random

cartas_computador = []
cartas_jogador = []
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
    print('Computador venceu!')
elif sum(cartas_computador) > 21:
    print('Computador perdeu!')
# soma das cartas do jogador
while sum(cartas_jogador) < 21:
    escolha = str(input('Voce deseja tirar mais uma carta? s/n'))
    if escolha == 's':
        cartas_jogador.append(random.randint(2, 11))
        cartas_jogador.append(random.randint(2, 11))
        print('Voce tem um total de: {0}'.format(sum(cartas_jogador)))
    if escolha == 'n':
        print('O computador tem um total de: {0}'.format(sum(cartas_computador)))
        print('Voce tem um total de: {0}'.format(sum(cartas_jogador)))
        if sum(cartas_computador) > sum(cartas_jogador):
            print('Computador venceu!')
        else:
            print('Voce venceu')
            break
        
if sum(cartas_jogador) > 21:
    print('Voce perdeu!')
elif sum(cartas_jogador) == 21:
    print('Blackjack, voce venceu!')
         


