'''
Created on 3 feb. 2022

@author: Usuario
'''

def main():
    #Declaracion de variable
    
     
     
    #Leer datos de la matriz A
     
    print('Ingresar datos de la matriz A:')
     
    A = leeMatriz(4,6)
    print('Matriz A')
    print(A)
     
    print('Ingresar datos de la matriz B:')
     
    B = leeMatriz(4,6)
    print('Matriz B')
    print(B)
     
    mayorA= determinarMaximoValorMatrix(A)
    mayorB= determinarMaximoValorMatrix(B) 
    

    if mayorA == mayorB :
            print(f'Las 2 matrices tienen el mismo número mayor perteneciente a la serie Fibonacci: {mayorA}')
    else:
        print('Las 2 matrices no tienen el mismo número mayor perteneciente a la serie Fibonacci')
        print('Maximo valor de la matriz A:'+str(mayorA))
        print('Maximo valor de la matriz B:'+str(mayorB))     
  
         
def creaMatriz(n,m):
    matriz = []     
    for i in range(n):
        a = [0]*m
        matriz.append(a)
         
    return matriz  
 
def leeMatriz(n,m):
    A = creaMatriz(n,m)
    for i in range(n):
        for j in range(m):
            A[i][j] = int( input('Introduce dato (%d,%d): '%(i,j)))
    return A
 
def determinarMaximoValorMatrix(matriz):
    max_valor=[0][0]
    for x in matriz:
        for z in x:
            if z>max_valor and validarNumeroFibonnaci(z):
                max_valor=z 
    
    return max_valor
def validarNumeroFibonnaci(max_valor):
    n1=0
    n2=1
    n3=0
    f=[]
    flag=False
    for i in range (100):
        n3=n1+n2          
        f.append(n3)
        n1=n2;    
        n2=n3;
    for i in range (100): 
        if f[i-1] == max_valor:
            flag=True
           
    return flag

                   
    
if __name__ == '__main__':
        main()
