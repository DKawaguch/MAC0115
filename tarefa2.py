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

import random #importação
import math   #importação

def main():
    
    n = input('Insira um padrão a ser testado: ') #padrão para achar um melhor
    i = 0 #índice
    n_testes = 100000 #int(input('Insira um valor grande o bastante de testes'))
    maior = -1 #menor número para descobrir um maior
    comp_n = '' #valor máximo em em binário de acordo com o comprimento do da sequência
    
    while len(comp_n) != len(n): #define o binário máximo com o número certo de algarismos
        comp_n = comp_n + '1'
        
    comp_n10 = conv2to10(int(comp_n)) #define o o número decimal máximo baseado no comprimento de n
    
    while i <= int(comp_n10): #loop para gerar sequências de 0 até o comprimento máximo binário
        
        m = str(conv10to2(i)) #transforma o índice que aumenta de 1 em 1 em binário
        
        while len(m) != len(n): #garante que o comprimento da sequência será igual ao no padrão
            
            m = '0' + m
            
        compara = comp(n, m) #compara a seq e o padrão
        
        if compara > maior and compara > (0.5+3*(math.sqrt(n_testes)/(2*n_testes))): #define a melhor sequência até o momento
           maior = compara
           melhor_seq = m
           
        i += 1 #aumenta o índice e define o valor decimal da próxima sequência binária
        
    print('Uma sequência melhor que a fornecida é: ' , melhor_seq) #mostra qual a melhor sequência encontrada
    
#------------------------------------------------------------------------------

def comp(n,m): #função que compara duas sequências e retorna o melhor resultado
    '''
    str,str ---> float
    a função devolve a maior probabilidade de ocorrência entre os dois padrões 
    '''
    
    if n == m:
        return float(0.5)
    
    n_testes = 100000
    seq = "" #definição da sequência, começa vazia
    i = 0 #índice de contagem
    n_1 = 0 #contador do número de "vitórias" de n  
    n_2 = 0 #contador do número de "vitórias" de m
    
    while i < n_testes :
        
        i +=1
        
        while len(seq) != len(n) : #define uma sequência aleatória de mesmo comprimento para começar o teste

            seq += str(random.randint(0, 1))
            
        if seq == n:
           n_1 = n_1 + 1
        if seq == m:
           n_2 = n_2 + 1
            
        while seq != n and seq != m : #refaz a sequência aleatória até encontrar um padrão coincidente
                
            seq = seq[1:] + str(random.randint(0, 1))
            if seq == n:
               n_1 = n_1 + 1
            if seq == m:
               n_2 = n_2 + 1
               
        seq = ""    
        
    probn = n_1/n_testes #calcula a primeira probabilidade
    probm = n_2/n_testes #calcula a segunda probabilidade
    if probm > probn: #retorna a maior probabilidade
        return probm
    else:
        return probn
#------------------------------------------------------------------------------

def conv10to2(n): #função que converte base decimal para binária
    '''
    (int) ---> int
    a função devolve a conversão de um número da base 10 na base 2 
    '''
    conv = 0
    pot = 1
    
    while n > 0:
        dig = n%2
        n = n//2
        conv = conv + dig*pot
        pot = pot*10
    return conv

#------------------------------------------------------------------------------

def conv2to10(n): #função que converte base binária para decimal
    '''
    (int) ---> int
    a função devolve a conversão de um número da base 2 na base 10 
    '''
    conv = 0
    pot = 1
    
    while n > 0:
        dig = n%10
        n = n//10
        conv = conv + dig*pot
        pot = pot*2
    return conv

#------------------------------------------------------------------------------
#if __name__='__main__':
main()