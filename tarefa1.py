# -*- coding: utf-8 -*-
  
"""
     Nome do aluno:Danilo Ferreira Kawaguchi
     Número USP: 12558763
     Curso: Bacharelado em Física - Noturno - IF
     Disciplina: MAC0115 Introdução à Computação
     Turma T24
     Exercício-Programa: EP1 - Padrões de Bits

     DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
     TODAS AS PARTES ORIGINAIS DESTE EXERCÍCIO-PROGRAMA FORAM
     DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
     DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
     OU PLÁGIO.
     DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS DESTE
     PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A SUA DISTRIBUIÇÃO.
     ESTOU CIENTE QUE OS CASOS DE PLÁGIO E DESONESTIDADE ACADÊMICA
     SERÃO TRATADOS SEGUNDO OS CRITÉRIOS DIVULGADOS NA PÁGINA DA
     DISCIPLINA.
  
"""

#------------------------------------------------------------------------------

import random

def main():
    
    alice = input('Padrão escolhido por Alice: ') #padrão a ser reconhecido na sequência aleatória pelo jogador 1
    beto = input('Padrão escolhido por Beto: ') #padrão a ser reconhecido na sequência aleatória pelo jogador 2
    if len(alice) != len(beto):
        beto = input('Escolha um padrão com o mesmo número de casas para o beto: ')
    n_testes = 1000000 #int(input('Insira quantas vezes deseja jogar: ')) #número de tentativas para encontrar os padrões 
    seq = "" #definição da sequência, começa vazia
    i = 0 #índice de contagem
    n_alice = 0 #contador do número de vitórias do alice  
    n_beto = 0 #contador do número de vitórias do beto
    
    while i < n_testes :#loop de contagem para n grande
        i +=1
        
        while len(seq) != len(alice) :#loop para gerar uma sequência de mesmo comprimento que os padrões dados

            seq += str(random.randint(0, 1))
            
        if seq == alice:
           n_alice = n_alice + 1
        if seq == beto:
           n_beto = n_beto + 1
            
        while seq != alice and seq != beto :#loop que gera mais bits para comparação ate um jogador ganhar
                
            seq = seq[1:] + str(random.randint(0, 1))
            if seq == alice:
               n_alice = n_alice + 1
            if seq == beto:
               n_beto = n_beto + 1
        seq = ""    
        
    probalice = n_alice/n_testes#probabilidade do alice ganhar
    #probbeto = n_beto/n_testes#probabilidade do beto ganhar
    print('As chances de Alice ganhar são {} '.format(probalice))
    #if probalice > probbeto:
        #print('O jogador 1 ganhou')
    #else:
        #print('O jogador 2 ganhou')
#------------------------------------------------------------------------------
main()