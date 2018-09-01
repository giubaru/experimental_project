'''
Desarrollar un programa para rellenar una matriz de N x N con números enteros al azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita.
Imprimir la matriz por pantalla.

1- Crear la matriz
    L> Directamente en el programa principal
      L> Llenar matriz n por n (por input) para calcupar filas y columnas
      
1.1- Cargar la matriz
    L> Por función
    L> De forma dinámica (dejarla llena con valor -1)

2 - Rellenar valores
      L> Puede ser con un random
      L> El valor no se tiene que repetir

3- Imprimir la matriz
    L> Por función
    L> Se puede acomodar con %3d
'''
import random as rm

def matrix_set(matrix, value):
  rows = len(matrix)
  columns = len(matrix[0])
  for row in range(rows):
    ins = rm.randint(0, (value**2)-1)
    for col in range(columns):
      if ins in matrix[row]:
        ins = rm.randint(0, (value**2)-1)
      else:
          matrix[row][col] = ins

def matrix_print(matrix): 
  rows = len(matrix)
  columns = len(matrix[0])
  for row in range(rows):
    for col in range(columns):
      print("%4d" %matrix[row][col], end="")
    print("")


inp_value = int(input("Value: "))
matrix = [[-1]*inp_value for row in range(inp_value)]
matrix_set(matrix, inp_value)
matrix_print(matrix)

