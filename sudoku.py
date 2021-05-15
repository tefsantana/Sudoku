# ARCHIVO CREADO POR ESTEFANÍA SANTANA -

VACIO = 0

ALTO_TABLERO = 9
ANCHO_TABLERO = 9

ALTO_CUADRANTE = 3
ANCHO_CUADRANTE = 3

def crear_juego(representacion):
    '''
    Dada una representación en cadena de un juego de Sudoku,
    devuelve un juego de Sudoku.

    El juego de Sudoku se representa como una matriz de 9x9
    donde cada elemento es un número entero o la constante
    VACIO para indicar que no se escribió ningún número en 
    esa posición.

    La representación es una cadena con el siguiente formato:

    003020600
    900305001
    001806400
    008102900
    700000008
    006708200
    002609500
    800203009
    005010300

    Donde un 0 significa que la casilla está vacía.
    '''
    sudoku = []
    sudoku_a_terminar = representacion.split("\n")
    for k in sudoku_a_terminar:
        if not k:
            continue
        i = []
        for j in k:
            i.append(int(j))
        sudoku.append(i)
    return sudoku

def hay_valor_en_fila(sudoku, fila, valor):
    '''
    Devuelve True si ya hay un casillero con el valor
    'valor' en la fila 'fila'.

    Por ejemplo para fila = 3 deberán revisar todas las
    siguientes celdas:
    (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)
    '''
    if valor in sudoku[fila]:
        return True
    return False 
        

def hay_valor_en_columna(sudoku, columna, valor):
    '''
    Devuelve True si ya hay un casillero con el valor 'valor'
    en la columna 'columna'.

    Por ejemplo para columna = 3 deberán revisar todas las
    siguientes celdas:
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3)
    '''
    for fila in sudoku:
        if fila[columna] == valor:
            return True
    return False

    
def obtener_origen_region(fila, columna):
    '''
    Devuelve la posición de la celda de la esquina superior izquierda
    de la región en que se encuentra la celda en (fila, columna).

    Las regiones se agrupan de la siguiente forma:
   *[0,0] [0,1] [0,2] *[0,3] [0,4] [0,5] *[0,6] [0,7] [0,8]
    [1,0] [1,1] [1,2]  [1,3] [1,4] [1,5]  [1,6] [1,7] [1,8]
    [2,0] [2,1] [2,2]  [2,3] [2,4] [2,5]  [2,6] [2,7] [2,8]

   *[3,0] [3,1] [3,2] *[3,3] [3,4] [3,5] *[3,6] [3,7] [3,8]
    [4,0] [4,1] [4,2]  [4,3] [4,4] [4,5]  [4,6] [4,7] [4,8]
    [5,0] [5,1] [5,2]  [5,3] [5,4] [5,5]  [5,6] [5,7] [5,8]

   *[6,0] [6,1] [6,2] *[6,3] [6,4] [6,5] *[6,6] [6,7] [6,8]
    [7,0] [7,1] [7,2]  [7,3] [7,4] [7,5]  [7,6] [7,7] [7,8]
    [8,0] [8,1] [8,2]  [8,3] [8,4] [8,5]  [8,6] [8,7] [8,8]

    Las celdas marcadas con un (*) son las celdas que deberá 
    devolver esta función para la correspondiente región.

    Por ejemplo, para la posición (fila = 1, columna = 4) la función
    deberá devolver (0, 3).
    '''

    if fila <=2:
        fila = 0
    if columna <=2:
        columna = 0
    if 3 <= fila <= 5:
        fila = 3
    if 6 <= fila <= 8:
        fila = 6
    if 6 <= columna <= 8:
        columna = 6
    if 3 <= columna <= 5:
        columna = 3
    return (fila, columna)


def hay_valor_en_region(sudoku, fila, columna, valor):
    '''
    Devuelve True si hay algún casillero con el valor `valor`
    en la región de 3x3 a la que corresponde la posición (fila, columna).

    Ver como se agrupan las regiones en la documentación de la función
    obtener_origen_region.
    
    Por ejemplo, para la posición (fila = 0, columna = 1) deberán revisar 
    si está `valor` en todas las siguientes celdas:
    (0, 0), (0, 1) (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2).
    '''
    fila_origen, columna_origen = obtener_origen_region(fila, columna)
    for coordenada_1 in range(fila_origen, fila_origen + 3):
        for coordenada_2 in range(columna_origen, columna_origen + 3):
            if sudoku[coordenada_1][coordenada_2] == valor:
                return True
    return False
    

def es_movimiento_valido(sudoku, fila, columna, valor):
    '''
    Devuelve True si se puede poner 'valor' en la posición
    (fila, columna) y el Sudoku sigue siendo válido; o False
    en caso contrario.

    'valor' se puede ubicar en la posición (fila, columna) si
    se cumple lo siguiente:
     - Ningún otro elemento que esté en la misma fila es igual a 'valor'
     - Ningún otro elemento que esté en la misma columna es igual a 'valor'
     - Ningún otro elemento que esté en la misma región es igual a 'valor'
    
    No modifica el Sudoku recibido.
    '''
    if hay_valor_en_fila(sudoku, fila, valor) and hay_valor_en_columna(sudoku, columna, valor) and hay_valor_en_region(sudoku, fila, columna, valor):
        return False
    return True


def insertar_valor(sudoku, fila, columna, valor):
    '''
    Intenta insertar el valor de la celda en la posición 
    (fila, columna). 
    
    Si el movimiento es válido se devolverá un nuevo Sudoku
    con el valor cambiado. En caso contrario se devolverá el
    mismo Sudoku que se recibió por parámetro.
    '''
    sudoku_cambiado = []
    for fs in sudoku:
        if not fs:
            continue
        f = []
        for cs in fs:
            f.append(int(cs))
        sudoku_cambiado.append(f)

    if es_movimiento_valido(sudoku, fila, columna, valor):
        sudoku_cambiado[fila][columna] = valor
        return sudoku_cambiado
    
    else:
        return sudoku

def borrar_valor(sudoku, fila, columna):
    '''
    Borra el valor de la celda que está en la posición
    (fila, columna).

    No modifica el Sudoku recibido por parámetro, devuelve uno
    nuevo con la modificación realizada.
    '''
    sudoku_nuevo = []
    for fs in sudoku:
        if not fs:
            continue
        f = []
        for cs in fs:
            f.append(int(cs))
        sudoku_nuevo.append(f)
    
    sudoku_nuevo[fila][columna] = VACIO
    return sudoku_nuevo
    

def esta_terminado(sudoku):
    '''
   Devuelve True si el Sudoku está completado
   correctamente.

   Un Sudoku está completado correctamente cuando todas 
   sus celdas tienen números y todos los números son válidos
   (es decir, no hay repetidos en la columna, ni en la fila
   ni en la región).
    '''
    for fila in sudoku:
        for elemento in fila:
            if elemento == VACIO:
                return False
    return True

def obtener_valor(sudoku, fila, columna):
    '''
    Devuelve el número que se encuentra en la celda (fila, columna)
    o la constante VACIO si no hay ningún número en dicha celda.
    '''
    if sudoku[fila][columna] != 0:
        return sudoku[fila][columna]
    return VACIO

def hay_movimientos_posibles(sudoku):
    '''
    Devuelve True si hay al menos un movimiento posible
    en el estado actual del juego.

    Que exista un movimiento posible no implica que el juego
    pueda completarse correctamente, sólamente indica que hay
    al menos una posible inserción.
    '''
    for fila in range(0, ANCHO_TABLERO - 1):
        for columna in range(0, ALTO_TABLERO - 1):
            for valor in range(0, ANCHO_TABLERO - 1):
                if sudoku[fila][columna] == VACIO and es_movimiento_valido(sudoku, fila, columna, valor):
                    return True
    return False

