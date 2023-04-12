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

#--------------------------------------------

import random

def main():
    
    padrao = input('Insira um padrão de 3 a 8 bit para que seja lido: ') #padrão a ser reconhecido na sequência aleatória
    n_testes = int(input('Insira quantas vezes deseja testar o número de jogadas aleatórias para o reconhecimento: ')) #número de tentativas para encontrar o padrão na sequência
    seq = "" #definição da sequência, começa vazia
    i = 0 #índice de contagem
    n_jogadas = 0 #contador do número total de jogadas
    
    
    while i < n_testes : #loop de tentativas para encontrar o padrão
        i +=1
        
        while len(seq) != len(padrao): #loop para montar uma sequência com o mesmo tamanho que o padrão desejado

            seq += str(random.randint(0, 1))
            n_jogadas += 1
            
        while seq != padrao: #loop tirando o primeiro e adicionando mais um bit até que encontre uma sequência eleatória igual ao padrão desejado
                
            seq = seq[1:] + str(random.randint(0, 1))
            n_jogadas += 1
            
        seq = ""    
        
    print ('A média de jogadas para encontrar seu padrão é: ', n_jogadas/n_testes)
    
#--------------------------------------------
main()