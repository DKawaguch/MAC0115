# -*- coding: utf-8 -*-
  
"""
     Nome do aluno:Danilo Ferreira Kawaguchi
     Número USP: 12558763
     Curso: Bacharelado em Física - Noturno - IF
     Disciplina: MAC0115 Introdução à Computação
     Turma T24
     Exercício-Programa: EP3 - Aquecimento

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

#importação
import math 

# variável global de gravitação
G = 6.67*10**(-11) 

def main():
    
    #definindo arquivos de entrada e saída
    file_name = input("Nome do arquivo de entrada: ")
    FILE_IN = open(file_name)
    FILE_OUT = open((file_name.split('.'))[0] + ".out", "w")
    
    #criação dos corpos
    bodies = [[[] for j in range(5)] for i in range(2)]
        
    #inputs necessários
    for i in range(2):
        
        bodies[i] = [float(x) for x in FILE_IN.readline().split()]
        
    T = int(FILE_IN.readline())
    dt = int(FILE_IN.readline())
    
    FILE_IN.close()
    
    FILE_OUT.write("{:.10e} {:.10e} ".format(bodies[1][0],bodies[1][1]))
    FILE_OUT.write('\n')
    
    #loop para gerar as novas coordenadas dos corpos
    for t in range(T//dt):
        
        Fx, Fy = Fg(bodies)
        bodies[1] = updt(bodies[1],Fx, Fy, dt)
           
        FILE_OUT.write("{:.10e} {:.10e} ".format(bodies[1][0],bodies[1][1]))
        FILE_OUT.write('\n')
    
    FILE_OUT.close()
#------------------------------------------------------------------------------

def dist(Ba,Bb):
    
    '''
	(list, list) -> (float)

	Esta função recebe dois corpos body_a, body_b.
	Retorna a distância entre os mesmos.
	'''	
    
    D = math.sqrt(distx(Ba, Bb)**2+disty(Ba, Bb)**2)
    
    return D

#------------------------------------------------------------------------------

def distx(Ba,Bb):
    
    '''
	(list, list) -> (float)

	Esta função recebe dois corpos body_a, body_b.
	Retorna a distância no eixo X entre os mesmos.
	'''	
    
    dx = (Bb[0]-Ba[0])
    
    return dx

#------------------------------------------------------------------------------

def disty(Ba,Bb):
    
    '''
	(list, list) -> (float)

	Esta função recebe dois corpos body_a, body_b.
	Retorna a distância no eixo Y entre os mesmos.
	'''	
    
    dy = (Bb[1]-Ba[1])
    
    return dy

#------------------------------------------------------------------------------

def Fg (bodies):
    
    '''
	(list) -> (float,float)

	Esta função recebe uma lista de
	corpos 'bodies'. Retorna  a força resultante na lua.
	'''
    
    Fx, Fy = 0,0
    
    D = dist(bodies[0],bodies[1])
    dx = distx(bodies[0],bodies[1])
    dy = disty(bodies[0],bodies[1])
    
    F = -((G)*(bodies[0][4]*bodies[1][4])/(D)**2)
    
    Fx = (F*dx)/D
    Fy = (F*dy)/D
    
    return Fx, Fy

#------------------------------------------------------------------------------

def updt (B,Fx,Fy,dt):
    
    '''
	(list, float, float, float) -> (list)

	Esta função recebe um corpo, as forças fx, fy
	atuando no mesmo e um intervalo	de tempo dt
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