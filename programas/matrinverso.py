'''
Created on 3 feb. 2022

@author: Usuario
'''
from sys import stdout


def main():
    
    numeroFilas= int( input( "\nIngrese el número de filas: " )) 
    numeroColumnas= int( input( "\nIngrese el número de columnas: " )) 
    #Leer datos de la matriz 
    print('Ingresar datos de la matriz A:')
    
    A =[]
    for i in range(numeroFilas):
        a = [0]*numeroColumnas
        A.append(a)
    
    for i in range(numeroFilas):
        for j in range(numeroColumnas):
            A[i][j] = int( input('Ingrese los datos de la posición A (%d,%d): '%(i,j)))
            
    #Presentar datos de la matriz 
    print('Matriz Normal')
       
    for i in range(numeroFilas):
        for j in range(numeroColumnas):
            stdout.write(str(A[i][j])+" " )
        stdout.write("\n")    
    #Presentar matriz inversa 
    print('Matriz Inversa') 
    
    for i in range(numeroFilas,0,-1):
        for j in range(numeroColumnas,0,-1):
            stdout.write(str(A[i-1][j-1])+" " )
        stdout.write("\n")     
            
if __name__ == '__main__':
    main()