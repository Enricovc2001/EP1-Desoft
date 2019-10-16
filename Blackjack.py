#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 14:43:54 2019

@author: enricocosta
"""
import random

def sorteia_carta():
    return random.randint(1, 13) # 1: A, 11: J, 12: Q, 13: K

def conta_pontos(cartas):
    
    total = 0
    
    for carta in cartas:
        if carta >=2 and carta <= 10:
            total += carta
        elif carta > 10:
            total += 10
            
    for carta in cartas:
        if carta == 1:
            if (total + 11) > 21:
                total += 1
            else:
                total += 11

                
    return total

def to_string_cartas(cartas):
    s = "[ "
    for carta in cartas:
        if carta == 1:
           s += "A "
        elif carta == 11:
           s += "J "
        elif carta == 12:
           s += "Q "
        elif carta == 13:
           s += "K "
        else:
           s += str(carta) + " "
    return s + "] = " + str(conta_pontos(cartas))
        
            
score = open('carteira.txt','r')
score2 = open('carteira2.txt','r') 
score_jogador=[float(score.readline())]
score_jogador2=[float(score2.readline())]
score.close()
score2.close()

multiplayer=input('Vc quer jogar sozinho ou em dupla? (s/d): ')


cartas_computador = []
cartas_jogador = []
cartas_jogador2 = []

# feature 2, para tirar a aposta escrevendo fim.
for i in score_jogador:
    while multiplayer != 'd':
        aposta=input('Quanto vc quer apostar essa rodada? ')
        #Se escrever fim na hora de fazer a primeira aposta termina o jogo.
        if aposta == 'fim':
            print('Vc saiu do jogo. Vc saiu com R$ {0:.2f}'.format(sum(score_jogador)))
            break
        aposta = float(aposta)

        # impossibilita nao fazer uma aposta, ou aposta estranha. E pergunta uma nova aposta.
        while aposta <= 0:
            print('Aposta invalida, aposte novamente') 
            aposta=int(input('Quanto vc quer apostar essa rodada? ')) 

        # impossibilita fazer uma aposta maior que o score_joagdor. E pergunta novamente a aposta.       
        while aposta > sum(score_jogador):
            print('Aposta invalida, aposte novamente')
            aposta=int(input('Quanto vc quer apostar essa rodada? '))  
            

            
                
        # código das cartas do jogador
        while len(cartas_jogador) != 2:
            cartas_jogador.append(sorteia_carta())
            if len(cartas_jogador) == 2:
                print('Suas cartas são: {0} '.format(to_string_cartas(cartas_jogador)))
        # soma das cartas do computador
        if conta_pontos(cartas_computador) == 21:
            score_jogador.append(-aposta)
            print('Computador venceu!')
        elif conta_pontos(cartas_computador) > 21:
            vitoria=aposta*2
            
            score_jogador.append(vitoria)
            print('Computador perdeu!')
            
                # código das cartas do computador
        while conta_pontos(cartas_computador) < 17:                
            cartas_computador.append(sorteia_carta())
            # print(cartas_computador, conta_pontos(cartas_computador))
            
        # soma das cartas do jogador
        while conta_pontos(cartas_jogador) < 21:
            escolha = str(input('Voce deseja tirar mais uma carta? (s/n): '))
            if escolha == 's':
                cartas_jogador.append(sorteia_carta())
                print('Sua nova carta é: {0} '.format(cartas_jogador[-1:]))
                print('Voce tem um total de: {0}'.format(conta_pontos(cartas_jogador)))
            if escolha == 'n':
                print('O computador tem um total de: {0}'.format(conta_pontos(cartas_computador)))
                print('Voce tem um total de: {0}'.format(conta_pontos(cartas_jogador)))
                
                if conta_pontos(cartas_computador) > conta_pontos(cartas_jogador): 
                    score_jogador.append(-aposta)
                    print('Computador venceu!')
                    break

                if conta_pontos(cartas_jogador) > conta_pontos(cartas_computador):
                    vitoria=aposta*2
                    score_jogador.append(vitoria)       
                    print('Voce venceu')
                    break

                if conta_pontos(cartas_jogador)==conta_pontos(cartas_computador):
                    print('Empatou')
                    break
            
        if conta_pontos(cartas_jogador) > 21:
            score_jogador.append(-aposta)
            print('Voce perdeu!')
            
        if conta_pontos(cartas_jogador) == 21:
            vitoria=aposta + aposta*1.5
            score_jogador.append(vitoria)
            print('Blackjack, voce venceu!')
            

        soma=0
        for i in score_jogador:
            soma+=i
        print('Vc possui R$ {0:.2f}'.format(soma))

        #Verifica se o jogador faliu.
        while conta_pontos(score_jogador) <= 0:
            print('Vc faliu, todo seu dinheiro acabou!')
            break 

        # abrindo o arquivo da carteira e guardando os valores de cada rodada.
        s= open('carteira.txt','w')
        s.writelines(str(soma))
        s.close()

        break

# adicionando o multiplayer no jogo.

    while multiplayer != 's':
        aposta=input('Quanto o jogador_1 quer apostar essa rodada? ')
        aposta2 = input('Quanto o jogador_2 quer apostar? ')

        #Se escrever fim na hora de fazer a primeira aposta termina o jogo.
        if aposta == 'fim' and aposta2 == 'fim':
            print('Os dois jogadores saíram')
        if aposta == 'fim':
            print('Jogador_1 saiu do jogo. Saiu com R$ {0:.2f}'.format(sum(score_jogador)))
            break
        if aposta2 == 'fim':
            print('Jogador_2 saiu do jogo. Saiu com R$ {0:.2f}'.format(sum(score_jogador2)))
            break

        aposta = float(aposta)
        aposta2 = float(aposta2)

        # impossibilita nao fazer uma aposta, ou aposta estranha. E pergunta uma nova aposta.
        while aposta <= 0:
            print('Aposta invalida, aposte novamente') 
            aposta=int(input('Quanto o jogador_1 quer apostar essa rodada? ')) 
        while aposta2 <= 0:
            print('Aposta invalida, aposte novamente') 
            aposta2=int(input('Quanto o jogador_2 quer apostar essa rodada? '))

        # impossibilita fazer uma aposta maior que o score_joagdor. E pergunta novamente a aposta.       
        while aposta > conta_pontos(score_jogador):
            print('Aposta invalida, aposte novamente')
            aposta=int(input('Quanto vc quer apostar essa rodada? '))
        while aposta2 > conta_pontos(score_jogador2):
            print('Aposta invalida, aposte novamente')
            aposta2=int(input('Quanto vc quer apostar essa rodada? '))  

        # código das cartas do jogador
        while len(cartas_jogador) != 2:
            cartas_jogador.append(sorteia_carta())
            if len(cartas_jogador) == 2:
                print('As cartas do jogador_1 são:{0} '.format(to_string_cartas(cartas_jogador)))

            #soma as cartas do jogaador_1.
            if conta_pontos(cartas_jogador) == 21:
                score_jogador2.append(-aposta2)
                vitoria = aposta + aposta*1.5
                score_jogador.append(vitoria)
                print('Jogador_1 venceu!')
                break

            elif conta_pontos(cartas_jogador) > 21:
                score_jogador.append(-aposta)
                vitoria2=aposta2*2
                score_jogador2.append(vitoria2)
                print('Jogador_2 venceu!')
                break

        # código das cartas do computador
        while len(cartas_jogador2) != 2:
            cartas_jogador2.append(sorteia_carta())
            if len(cartas_jogador2) == 2:
                print('As cartas do jogador_2 são:{0} '.format(to_string_cartas(cartas_jogador2)))
                
            # soma das cartas do computador
            if conta_pontos(cartas_jogador2) == 21:
                score_jogador.append(-aposta)
                vitoria2 = aposta2* aposta2*1.5
                score_jogador2.append(vitoria2)
                print('Jogador_2 venceu!')
                break

            elif conta_pontos(cartas_jogador2) > 21:
                score_jogador2.append(-aposta2)
                vitoria=aposta*2
                score_jogador.append(vitoria)
                print('Jogador_1 venceu!')
                break



        # soma das cartas do jogador
        while conta_pontos(cartas_jogador) < 21 and conta_pontos(cartas_jogador2) < 21:
            escolha = str(input('O jogador_1 deseja tirar mais uma carta? (s/n): '))
            escolha2 = str(input('O jogador_2 deseja tirar mais uma carta? (s/n): '))

            #jogador1 escolha das cartas e verificação.
            if escolha == 's':
                cartas_jogador.append(sorteia_carta())
                print('A nova  carta do jogador_1 é: {0} '.format(cartas_jogador[-1:]))
                print('O jogador_1 tem um total de: {0}'.format(conta_pontos(cartas_jogador)))

                if conta_pontos(cartas_jogador) > 21:
                    score_jogador.append(-aposta)
                    vitoria2=aposta2*2
                    score_jogador2.append(vitoria2)
                    print('Jogador_1 perdeu!')
                    

                if conta_pontos(cartas_jogador) == 21:
                    vitoria=aposta+ aposta*1.5
                    score_jogador.append(vitoria)
                    score_jogador2.append(-aposta2)
                    print('Blackjack, Jogador_1 venceu!')
                    

                while conta_pontos(cartas_jogador) <21 and conta_pontos(cartas_jogador2)<21:    
                    escolha = str(input('O jogador_1 deseja tirar mais uma carta? (s/n): '))
                    if escolha == 's':
                        cartas_jogador.append(sorteia_carta())
                        print('A nova carta jogador_1 é: {0} '.format(to_string_cartas(cartas_jogador[-1:])))
                        print('O jogador_1 tem um total de: {0}'.format(conta_pontos(cartas_jogador)))

                        if conta_pontos(cartas_jogador) > 21:
                            score_jogador.append(-aposta)
                            vitoria2=aposta2*2
                            score_jogador2.append(vitoria2)
                            print('Jogador_1 perdeu!')
                            break

                        if conta_pontos(cartas_jogador) == 21:
                            vitoria=aposta+aposta*1.5
                            score_jogador.append(vitoria)
                            score_jogador2.append(-aposta2)
                            print('Blackjack, Jogador_1 venceu!')
                            break

            if escolha == 'n':
                #print('O Jogador2 tem um total de: {0}'.format(sum(cartas_jogador2)))
                print('O jogador_1 tem um total de: {0}'.format(conta_pontos(cartas_jogador)))

            # jogador_2 escolha das cartas, e verificação.
            if escolha2 == 's':
                cartas_jogador2.append(sorteia_carta())
                print('A nova carta do jogador_2 é: {0} '.format(to_string_cartas(cartas_jogador2[-1:])))
                print('O jogador_2 tem um total de: {0}'.format(conta_pontos(cartas_jogador2)))

                if conta_pontos(cartas_jogador2) > 21:
                    score_jogador2.append(-aposta2)
                    vitoria=aposta*2
                    score_jogador.append(vitoria)
                    print('Jogador_2 perdeu!')
                    break
                if conta_pontos(cartas_jogador2) == 21:
                    vitoria2=aposta2 + aposta2*1.5
                    score_jogador2.append(vitoria2)
                    score_jogador.append(-aposta)
                    print('Blackjack, Jogador_2 venceu!')
                    break

                # se as cartas ainda tiverem menor que 21 pergunta outra vez.
                while conta_pontos(cartas_jogador2)<21 and conta_pontos(cartas_jogador)<21:           
                    escolha2 = str(input('O jogador_2 deseja tirar mais uma carta? (s/n): '))
                    if escolha2 == 's':
                        cartas_jogador2.append(sorteia_carta())
                        print('A nova carta do jogador_2 é: {0} '.format(to_string_cartas(cartas_jogador2[-1:])))
                        print('O jogador_2 tem um total de: {0}'.format(conta_pontos(cartas_jogador2)))

                        if conta_pontos(cartas_jogador2) > 21:
                            score_jogador2.append(-aposta2)
                            vitoria=aposta*2
                            score_jogador.append(vitoria)
                            print('Jogador_2 perdeu!')
                            break
                        if conta_pontos(cartas_jogador2) == 21:
                            vitoria2=aposta2 + aposta2*1.5
                            score_jogador2.append(vitoria2)
                            score_jogador.append(-aposta)
                            print('Blackjack, Jogador_2 venceu!')
                            break
                        
                    break

            if escolha2 == 'n':
                #print('O Jogador_1 tem um total de: {0}'.format(sum(cartas_jogador)))
                print('O jogador_2 tem um total de: {0}'.format(conta_pontos(cartas_jogador2)))
                
                if conta_pontos(cartas_jogador2) > conta_pontos(cartas_jogador) and conta_pontos(cartas_jogador)<21 and conta_pontos(cartas_jogador2)<21:
                    
                    score_jogador.append(-aposta)
                    vitoria2=aposta2*2
                    score_jogador2.append(vitoria2)
                    print('Jogador_2 venceu!')
                    break
                    
                elif conta_pontos(cartas_jogador2) < conta_pontos(cartas_jogador) and conta_pontos(cartas_jogador)<21 and conta_pontos(cartas_jogador2)<21:
                    score_jogador2.append(-aposta2)
                    vitoria=aposta*2
                    score_jogador.append(vitoria)       
                    print('Jogador_1 venceu')
                    break
                
                elif conta_pontos(cartas_jogador) == conta_pontos(cartas_jogador2):
                    print('Empatou')
                    break


        #soma dos dinheiros dos jogadores.
        soma=0
        for i in score_jogador:
            soma+=i
        print('O jogador_1 possui R$ {0:.2f}'.format(soma))

        soma2=0
        for e in score_jogador2:
            soma2+=e
        print('O jogador_2 possui R$ {0:.2f}'.format(soma2))

        #Verifica se o jogador faliu.
        while conta_pontos(score_jogador) <= 0:
            print('jogador_1 faliu, todo seu dinheiro acabou!')
            break
        while conta_pontos(score_jogador2) <= 0:
            print('Jogador_2 faliu, todo o seu dinheiro acabou')
            break 

        # abrindo o arquivo da carteira e guardando os valores de cada rodada.
        s= open('carteira.txt','w')
        s2 = open('carteira2.txt','w')
        s2.writelines(str(soma2))
        s.writelines(str(soma))
        s.close()
        s2.close()

        break

    break  
