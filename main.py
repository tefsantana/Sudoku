from mapas import MAPAS
from sudoku import *
import random


def mostrar_tablero(juego):
    print("     1  2  3     4  5  6     7  8  9   ")
    print("  ╔══\══\══\══╦══\══\══\══╦══\══\══\══╗")
    for i in range(len(juego)):
        print(f"{i+1} ║   {juego[i][0]} {juego[i][1]} {juego[i][2]}   ║   {juego[i][3]} {juego[i][4]} {juego[i][5]}   ║   {juego[i][6]} {juego[i][7]} {juego[i][8]}   ║")
        if(i == 2 or i == 5):
            print("  ╠══\══\══\══╬══\══\══\══╬══\══\══\══╣")
    print("  ╚══\══\══\══╩══\══\══\══╩══\══\══\══╝")
    print("""
    Instrucciones:
    Presionar Z para insertar un valor [ fila, columna, valor  |  salir ]:
    Presionar X para borrar un valor [ fila, columna, valor  |   salir ]:
    """)

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


def main():
   sudoku = crear_juego(random.choice(MAPAS))
   while not esta_terminado(sudoku):
      mostrar_tablero(sudoku)
      sudoku = accionar(sudoku)
   print("""
   ¡Felicitaciones! Ganaste.
   """)

main()

