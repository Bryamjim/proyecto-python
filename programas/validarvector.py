'''
Created on 3 feb. 2022

@author: Usuario
'''

from sys import stdin, stdout
def main():
    
    vector = []
    stdout.write('Ingresar números enteros para el vector:\n')
    # Leer número entero desde el teclado, para almacenaros en un vector
    for i in range(1,7):
        nuevoDato = int( input( " Dato numero {}: ".format(i) ))
        vector.append(nuevoDato)
  
    print ('El vector tiene los siguientes datos: ')
    print (vector)
    # Leer número entero desde el teclado
    numero = int( input( "\nIngresar un número entero: ".format(i) )) 
             
    # Presentar resultado de  la compracion
    cantidadRepeticion=ContarNumerosRepetidos(vector,numero)
    stdout.write('\nEl número '+str(numero)+" se repite: "+str(cantidadRepeticion));  
    
    if cantidadRepeticion>1:
        stdout.write(' veces')
    else:
        stdout.write(' vez')

# Funcion para contar las veces que se repite el número ingresado    
def ContarNumerosRepetidos(vector,numero):
    contador=0
    for i in range(1,7):    
        if vector[i-1]==numero:
            contador+=1
    return   contador              

if __name__ == '__main__':
    main()