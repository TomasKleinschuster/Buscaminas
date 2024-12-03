import random
from variables import *
from json import *

### VISUALES ###
def inicializar_ventana():
    '''
    Inicializa la ventana principal
    '''
    ventana = pygame.display.set_mode(RESOLUCION_VENTANA, pygame.SCALED)
    pygame.display.set_caption(TITULO)
    return ventana

# CREAR BOTON #
def crear_boton(texto: str, x: int, y: int, ancho: int, alto: int, ventana: pygame.Surface,
                color_boton: str, color_hover: str, color_click: str, color_texto_click: str):
    '''
    Crea un boton interactivo con texto y colores personalizados
    Cambia su apariencia segun el estado del cursor (normal, hover o clic)
    Retorna True si es presionado o False en caso contrario
    '''
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    boton_rect = pygame.Rect(x, y, ancho, alto)
    texto_boton = font.render(texto, True, color_texto_click)
    texto_rect = texto_boton.get_rect(center = (x + ancho // 2, y + alto // 2))
    es_click = False

    if boton_rect.collidepoint(cursor):
        pygame.draw.rect(ventana, color_hover, boton_rect, 0, 5)
        if click[0]:  # Click izquierdo
            pygame.draw.rect(ventana, color_click, boton_rect, 0, 5)
            es_click = True
    else:
        pygame.draw.rect(ventana, color_boton, boton_rect, 0, 5)

    ventana.blit(texto_boton, texto_rect)
    return es_click


# VENTANA PUNTAJES #
def seleccionar_puntajes(ventana: pygame.Surface):
    '''
    Muestra la ventana de puntajes
    Crea un cuadro para contener los puntajes
    Crea un boton "VOLVER" para volver al menu
    '''
    while True:
        pygame.draw.rect(ventana, VERDE, (250, 80, 510, 400), 0, 25)
        pygame.draw.rect(ventana, GRIS, (250, 80, 510, 400), 10, 25)
        if crear_boton(VOLVER, 570, 370, 150, 55, ventana, GRIS, GRIS_CLARO, BLANCO, NEGRO):
            return

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

# PUNTAJE #
def mostrar_puntaje(ventana: pygame.Surface, puntaje: int):
    '''
    Muestra el puntaje en la ventana
    '''
    pygame.draw.rect(ventana, GRIS, (600, 55, 275, 50), 0, 10)
    texto_puntaje = font.render(f"Puntaje: {puntaje:04d}", True, NEGRO)
    ventana.blit(texto_puntaje, (625, 58))
    puntajes = puntaje

    

# TIMER #
def mostrar_tiempo(ventana: pygame.Surface, tiempo: int):
    '''
    Muestra el tiempo en la ventana
    '''
    pygame.draw.rect(ventana, GRIS, (125, 55, 200, 50), 0, 10)
    texto_timer = font.render(f"Tiempo: {tiempo:02d}", True, NEGRO)
    ventana.blit(texto_timer, (130, 58))

# CAMBIAR DIFICULTAD # INCOMPLETO #
def cambiar_dificultad():
    pass

# VENTANA SELECCION DIFICULTAD #
def seleccionar_dificultad(ventana: pygame.Surface):
    '''
    Muestra la ventana para seleccionar la dificultad del juego
    Crea botones para elegir entre "FACIL", "MEDIO" y "DIFICIL"
    Crea un boton "VOLVER" para volver al menu
    '''
    while True:
        pygame.draw.rect(ventana, VERDE, (250, 80, 510, 400), 0, 25)
        pygame.draw.rect(ventana, GRIS, (250, 80, 510, 400), 10, 25)
        if crear_boton(FACIL, 350, 130, 300, 55, ventana, GRIS, GRIS_CLARO, BLANCO, NEGRO):
            pass
        if crear_boton(MEDIO, 350, 210, 300, 55, ventana, GRIS, GRIS_CLARO, BLANCO, NEGRO):
            pass
        if crear_boton(DIFICIL, 350, 290, 300, 55, ventana, GRIS, GRIS_CLARO, BLANCO, NEGRO):
            pass
        if crear_boton(VOLVER, 570, 370, 150, 55, ventana, GRIS, GRIS_CLARO, BLANCO, NEGRO):
            return
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

# REINICIAR TABLERO #
def reiniciar_tablero(filas: int, columnas: int, minas: int)-> tuple:
    '''
    Reinicia el tablero llamando las funciones dentro de variables que luego se retornan
    '''
    matriz = colocar_minas(minas, filas, columnas, 0)
    matriz_minada = actualizar_matriz(matriz)
    celdas_visibles = crear_matriz(filas, columnas, False)
    banderas = crear_matriz(filas, columnas, False)
    return matriz_minada, celdas_visibles, banderas

# MOSTRAR MENSAJE PERSONALIZADO #
def mostrar_mensaje(ventana: pygame.Surface, texto: str):
    '''
    Muestra un mensaje dentro de un recuadro
    '''
    pygame.draw.rect(ventana, BLANCO, (250, 80, 510, 400), 0, 25)
    pygame.draw.rect(ventana, GRIS_CLARO, (250, 80, 510, 400), 10, 25)
    font = pygame.font.SysFont(FUENTE_TIPO, 60, True)
    texto_mensaje = font.render(texto, True, ROJO)
    ventana.blit(texto_mensaje, (340, 225))
    pygame.display.flip()

def comprobar_ganador(celdas_visibles, matriz):
    '''
    Verifica si todas las celdas sin minas fueron descubiertas
    '''
    for fila in range(len(matriz)):
        for col in range(len(matriz[0])):
            if matriz[fila][col] != -1 and not celdas_visibles[fila][col]:
                return False
    return True

# DIBUJAR CELDAS DEL TABLERO #
def dibujar_celdas(ventana: pygame.Surface, filas: int, columnas: int, ancho_tablero: int, alto_tablero: int,
                    banderas: list, celdas_visibles: list, matriz: list):
    '''
    Itera sobre cada celda del tablero
    Dibuja el estado actual de las celdas (bandera, celda cubierta, mina o numero)
    '''
    for fila in range(filas):
        for col in range(columnas):
            x = ancho_tablero + (col * TAMANO_CELDA)
            y = alto_tablero + (fila * TAMANO_CELDA)

            if banderas[fila][col]:
                ventana.blit(celda_bandera, (x, y))
            elif not celdas_visibles[fila][col]:
                ventana.blit(celda, (x, y))
            else:
                match matriz[fila][col]:
                    case -1:
                        ventana.blit(celda_mina, (x, y))
                    case 0:
                        ventana.blit(celda_vacia, (x, y))
                    case 1:
                        ventana.blit(celda1, (x, y))
                    case 2:
                        ventana.blit(celda2, (x, y))
                    case 3:
                        ventana.blit(celda3, (x, y))
                    case 4:
                        ventana.blit(celda4, (x, y))
                    case 5:
                        ventana.blit(celda5, (x, y))
                    case 6:
                        ventana.blit(celda6, (x, y))
                    case 7:
                        ventana.blit(celda7, (x, y))
                    case 8:
                        ventana.blit(celda8, (x, y))
                    case _:
                        print("ERROR: numero de celda fuera de rango")

# DIBUJAR TABLERO #
def dibujar_tablero(ventana: pygame.Surface, reloj: pygame.time.Clock, filas: int, columnas: int, minas: int,
                    banderas: list, celdas_visibles: list, puntaje: int, matriz: list):
    '''
    Calcula el centro del tablero con el tamaño de las celdas y la ventana
    Maneja eventos clic izquierdo y derecho
    Actualiza el estado descubrir celdas o poner/quitar banderas
    Boton reiniciar el juego
    Boton volver al menu principal
    Renderiza en loop (celdas, puntaje y temporizador)
    '''
    banderas_colocadas = 0

    while True:
        ancho_tablero = (VENTANA_ANCHO - (columnas * TAMANO_CELDA)) // 2
        alto_tablero = (VENTANA_ALTO - (filas * TAMANO_CELDA)) // 2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_x, cursor_y = pygame.mouse.get_pos()
                col = (cursor_x - ancho_tablero) // TAMANO_CELDA
                fila = (cursor_y - alto_tablero) // TAMANO_CELDA

                if (0 <= fila < filas) and (0 <= col < columnas):
                    if event.button == 1:  # evento click izquierdo
                        if not banderas[fila][col]:
                            celdas_visibles[fila][col] = True
                            if matriz[fila][col] == -1:
                                mostrar_mensaje(ventana, "Perdiste!")
                                pygame.time.wait(2000)
                            else:
                                puntaje += 1
                                celdas_visibles[fila][col] = True
                                if celdas_visibles == 0:
                                    pass
                                    # revelar_celdas_vacias(fila, col, matriz, celdas_visibles)
                            if comprobar_ganador(celdas_visibles, matriz):
                                mostrar_mensaje(ventana, "Ganaste!")
                                pygame.time.wait(2000)
                    elif event.button == 3:  # evento click derecho
                        if not celdas_visibles[fila][col]:
                            if not celdas_visibles[fila][col]:
                                if banderas[fila][col]:
                                    banderas[fila][col] = False
                                    banderas_colocadas -= 1
                                elif banderas_colocadas < minas: 
                                    banderas[fila][col] = True
                                    banderas_colocadas += 1

        pygame.draw.rect(ventana, BLANCO, (100, 30, 800, 500), 0, 25)
        pygame.draw.rect(ventana, GRIS, (100, 30, 800, 500), 10, 25)

        mostrar_puntaje(ventana, puntaje)
        mostrar_tiempo(ventana, 00)

        if crear_boton("REINICIAR",  125, 450, 200, 55, ventana, GRIS, GRIS_CLARO, BLANCO, NEGRO):
            matriz, celdas_visibles, banderas = reiniciar_tablero(filas, columnas, minas)
            banderas_colocadas = 0
            puntaje = 0
        
        if crear_boton(VOLVER, 725, 450, 150, 55, ventana, GRIS, GRIS_CLARO, BLANCO, NEGRO):
            return
        
        dibujar_celdas(ventana, filas, columnas, ancho_tablero, alto_tablero, banderas, celdas_visibles, matriz)
        
        pygame.display.flip()

# VENTANA JUEGO #
def seleccionar_jugar(ventana: pygame.Surface, reloj: pygame.time.Clock, filas: int, columnas: int, minas: int):
    '''
    Se crea la matriz del tablero con minas y actualizando celdas con numeros
    Crea matrices para celdas visibles y banderas
    Llama la función "dibujar_tablero"
    '''
    matriz = colocar_minas(minas, filas, columnas, 0)
    matriz_minada = actualizar_matriz(matriz)
    puntaje = 0
    celdas_visibles = crear_matriz(filas, columnas, False)
    banderas = crear_matriz(filas, columnas, False)

    dibujar_tablero(ventana, reloj, filas, columnas, minas, banderas, celdas_visibles, puntaje, matriz_minada)

# CREACION MATRIZ #
def crear_matriz(filas: int, columnas: int, elemento) -> list:
    '''
    Crea una matriz del elemento especificado con la cantidad de filas y columnas especificadas
    '''
    matriz = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            fila.append(elemento)
        matriz.append(fila)

    return matriz

def colocar_minas(minas: int, max_filas: int, max_columnas: int, elemento) -> list:
    '''
    Coloca una cantidad de minas(-1) en la matriz de forma aleatoria 
    '''
    matriz_minada = crear_matriz(max_filas, max_columnas, elemento)
    minas_colocadas = 0
    while minas_colocadas < minas:
        fila_aleatoria = random.randint(0, max_filas - 1)
        columna_aleatoria = random.randint(0, max_columnas - 1)

        if matriz_minada[fila_aleatoria][columna_aleatoria] != -1:
            matriz_minada[fila_aleatoria][columna_aleatoria] = -1
            minas_colocadas += 1

    return matriz_minada

def contar_minas_adjacentes(matriz: list, fila: int, columna: int) -> int:
    '''
    Cuenta la cantidad de minas que hay en las celdas adyacentes a
    la celda en la posición (fila, columna) de la matriz
    '''
    filas = len(matriz)
    columnas = len(matriz[0])
    minas_adjacentes = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            fila_adjacente = fila + i
            columna_adjacente = columna + j
            if 0 <= fila_adjacente < filas and 0 <= columna_adjacente < columnas:
                if matriz[fila_adjacente][columna_adjacente] == -1:
                    minas_adjacentes += 1
    return minas_adjacentes

def actualizar_matriz(matriz: list) -> list:
    '''
    Actualiza la matriz para que en cada celda se muestre la cantidad de minas
    que hay en las celdas adyacentes a ella
    '''
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == 0:
                minas_adjacentes = contar_minas_adjacentes(matriz, i, j)
                matriz[i][j] = minas_adjacentes
    return matriz

def pedir_nombre(ventana: pygame.Surface):
    """
    Ingresar nombre antes o despues del juego
    """
    nombre = ""
    corriendo = True

    while corriendo == True:
        texto_titulo = font.render("INGRESAR NOMBRE", True, NEGRO)
        texto_parrafo = font.render("Presione 'ENTER' al finalizar", True, NEGRO)
        pygame.draw.rect(ventana, VERDE, (250, 80, 510, 400), 0, 25)
        pygame.draw.rect(ventana, GRIS, (250, 80, 510, 400), 10, 25)
        ventana.blit(texto_titulo, (330, 100))
        texto_nombre = font.render(nombre, True, NEGRO)
        ventana.blit(texto_nombre, (400, 300))
        ventana.blit(texto_parrafo, (275, 400))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    corriendo = False
                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += event.unicode

    return nombre

def guardar_puntaje_y_nombre(nombre: str, puntaje: int, archivo="./assets/puntajes.json"):
    """
    Guarda el nombre y puntaje del usuario en un archivo
    """
    with open(archivo, "a") as file:
        file.write(f"{nombre}: {puntaje}\n")

def cargar_puntajes(path:str)->list:
    '''
    Carga un archivo json y devuelve una lista
    '''
    with open(path, "r") as archivo:
        datos = load(archivo)
    return datos