# -*- coding: utf-8 -*-
  
"""
     Nome do aluno:Danilo Ferreira Kawaguchi
     Número USP: 12558763
     Curso: Bacharelado em Física - Noturno - IF
     Disciplina: MAC0115 Introdução à Computação
     Turma T24
     Exercício-Programa: EP3 - Problema dos 3 Corpos

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

#importações
import math 

# variável global de gravitação
G = 6.67*10**(-11)

def main():
    
    # abrindo arquivos de entrada e saída
    file_name = input()
    FILE_IN = open(file_name)
    FILE_OUT = open((file_name.split('.'))[0] + ".out", "w")
    
    #criação de corpos
    bodies = [[[] for j in range(5)] for i in range(3)]
    bodies_copy = [[[] for j in range(5)] for i in range(3)]
    
    #inputs necessários
    for i in range(3):
        
        bodies[i] = [float(x) for x in FILE_IN.readline().split()]
        
    T = int(FILE_IN.readline())
    dt = int(FILE_IN.readline())
    
    #fechando arquivo de entrada
    FILE_IN.close()
    
    #escrevendo a primeira linha de coordenadas
    for i in range(3):
        
        FILE_OUT.write("{:.10e} {:.10e} ".format(bodies[i][0], bodies[i][1]))
    FILE_OUT.write('\n')
    
    #loop para gerar as novas coordenadas dos corpos
    for t in range((T//dt)+1):
        
        #cálculo das forças e aualização de corpos
        for i in range (3):
            
            Fx, Fy = Fg(i,bodies)
            bodies_copy[i] = updt(bodies[i],Fx, Fy, dt)
                
        bodies = bodies_copy
           
        #escrevendo as demais linha de coordenadas
        for i in range(3):
            
            FILE_OUT.write("{:.10e} {:.10e} ".format(bodies[i][0], bodies[i][1]))
        FILE_OUT.write('\n')
         
    #fechando o arquivo de saída
    FILE_OUT.close()
    
#------------------------------------------------------------------------------

def dist(Ba,Bb):
    
    '''
	(list, list) -> (float)

	Esta função recebe dois corpos Body_a, Body_b.
	Retorna a distância entre os mesmos.
	'''	
    
    D = math.sqrt(distx(Ba, Bb)**2+disty(Ba, Bb)**2)
    
    return D

#------------------------------------------------------------------------------

def distx(Ba,Bb):
    
    '''
	(list, list) -> (float)

	Esta função recebe dois corpos Body_a, Body_b.
	Retorna a distância no eixo X entre os mesmos.
	'''	
    
    dx = (Bb[0]-Ba[0])
    
    return dx

#------------------------------------------------------------------------------

def disty(Ba,Bb):
    
    '''
	(list, list) -> (float)

	Esta função recebe dois corpos Body_a, Body_b.
	Retorna a distância no eixo Y entre os mesmos.
	'''	
    
    dy = (Bb[1]-Ba[1])
    
    return dy

#------------------------------------------------------------------------------

def Fg(key,bodies):
    
    '''
	(int, list) -> (float,float)

	Esta função recebe um inteiro 'key', uma lista de
	corpos 'bodies'. Retorna  a força resultante no 
	corpo bodies[key].
	'''
    
    Fx, Fy = 0, 0
    
    for i in range (len(bodies)):
        
        if i != key:
            
            dx = distx(bodies[i],bodies[key])
            dy = disty(bodies[i],bodies[key])
            D = dist(bodies[i],bodies[key])
            
            F = -((G)*(bodies[i][4]*bodies[key][4])/(D)**2)
            
            Fxi = (F*dx)/(D)
            Fyi = (F*dy)/(D)
            
            Fx += Fxi
            Fy += Fyi
    
    return Fx, Fy

#------------------------------------------------------------------------------

def updt (B,Fx,Fy,dt):
    
    '''
	(list, float, float, int) -> (list)

	Esta função recebe um corpo, as forças Fx, Fy
	atuando no mesmo e um intervalo	de tempo 'dt'
	e retorna o corpo atualizado após o intervalo.
	'''
    
    ax = Fx/B[4]
    ay = Fy/B[4]
    
    vx = B[2] + ax*dt
    vy = B[3] + ay*dt
    
    rx = B[0] + vx*dt
    ry = B[1] + vy*dt
    
    NB = [rx,ry,vx,vy,B[4]]
    
    return NB

#------------------------------------------------------------------------------

#if __name__='__main__':
main()