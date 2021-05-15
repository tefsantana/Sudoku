# ARCHIVO CREADO POR ESTEFANÍA SANTANA -

from mapas import MAPAS
from sudoku import *
import random

PLANTILLA_TABLERO = """
           1  2  3     4  5  6     7  8  9
        ╔══\══\══\══╦══\══\══\══╦══\══\══\══╗
     1  ║  {}  {}  {}  ║  {}  {}  {}  ║  {}  {}  {}  ║                    
     2  ║  {}  {}  {}  ║  {}  {}  {}  ║  {}  {}  {}  ║                    Instrucciones:
     3  ║  {}  {}  {}  ║  {}  {}  {}  ║  {}  {}  {}  ║                    
        ╠══\══\══\══╬══\══\══\══╬══\══\══\══╣                    Presionar Z para insertar un valor [ fila, columna, valor  |  salir ]:  
     4  ║  {}  {}  {}  ║  {}  {}  {}  ║  {}  {}  {}  ║                    Presionar X para borrar un valor [ fila, columna, valor  |   salir ]: 
     5  ║  {}  {}  {}  ║  {}  {}  {}  ║  {}  {}  {}  ║
     6  ║  {}  {}  {}  ║  {}  {}  {}  ║  {}  {}  {}  ║
        ╠══\══\══\══╬══\══\══\══╬══\══\══\══╣
     7  ║  {}  {}  {}  ║  {}  {}  {}  ║  {}  {}  {}  ║
     8  ║  {}  {}  {}  ║  {}  {}  {}  ║  {}  {}  {}  ║
     9  ║  {}  {}  {}  ║  {}  {}  {}  ║  {}  {}  {}  ║
        ╚══\══\══\══╩══\══\══\══╩══\══\══\══╝
     """

def mostrar_tablero(tablero):
   lista_de_valores = []
   for fila in tablero:
      for valor in fila:
         lista_de_valores.append(valor)

   tablero_cadena = PLANTILLA_TABLERO.format(*lista_de_valores)

   print(tablero_cadena)

def accionar(sudoku):
   accion = input("Ingresar acción: ")
         
   if accion == "Z":
      cadena_parametros = input("Ingrese 'fila, columna, valor' a insertar: ")
      parametros = cadena_parametros.split(",")
         
      if len(parametros) != 3:
         return sudoku
         
      fila,columna,valor = parametros
      fila,columna,valor = fila.strip(), columna.strip(), valor.strip()

      if not fila.isdigit() or not columna.isdigit() or not valor.isdigit():
         return sudoku

      fila,columna,valor = int(fila), int(columna), int(valor)

      if 1 <= fila <= 9 and 1 <= columna <= 9 and 1 <= valor <= 9:
         return insertar_valor(sudoku, fila-1, columna-1, valor)
      

   if accion == "X":
      cadena_parametros = input("Ingrese 'fila, columna' a borrar: ")
      parametros = cadena_parametros.split(",")
         
      if len(parametros) != 2: 
         return sudoku
         
      fila,columna = parametros
      fila,columna = fila.strip(), columna.strip()

      if not fila.isdigit() or not columna.isdigit(): 
         return sudoku

      fila,columna = int(fila), int(columna)

      if 1 <= fila <= 9 and 1 <= columna <= 9:
         return borrar_valor(sudoku, fila-1, columna-1)
      
   if accion == "salir":
      exit()
   return sudoku

JUEGO_COMPLETADO = """
   ¡Felicitaciones! Ganaste.
"""

def main():
   sudoku = crear_juego(random.choice(MAPAS))
   while not esta_terminado(sudoku):
      mostrar_tablero(sudoku)
      sudoku = accionar(sudoku)
   print(JUEGO_COMPLETADO)

main()

