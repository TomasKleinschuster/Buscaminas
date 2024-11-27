import pygame

pygame.font.init()
pygame.mixer.init()

# Resolución ventana
VENTANA_ANCHO = 1024
VENTANA_ALTO = 576
RESOLUCION_VENTANA = (VENTANA_ANCHO, VENTANA_ALTO)

# Frames Per Second
FPS = 60

# Colores
GRIS_CLARO = (166, 172, 175)
GRIS = (121, 125, 127)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Font
FUENTE_TEXTO_TAMANO = 30
FUENTE_TIPO = "arialblack"
font = pygame.font.SysFont(FUENTE_TIPO, FUENTE_TEXTO_TAMANO)

# Textos
TITULO = "xX Buscaminas Xx"
NIVEL = "Nivel"
JUGAR = "Jugar"
PUNTAJES = "Ver Puntajes"
SALIR = "Salir"
FACIL = "Fácil"
MEDIO = "Medio"
DIFICIL = "Difícil"
VOLVER = "< MENU"

# Minas
MINAS_FACIL = 10
MINAS_MEDIO = 40
MINAS_DIFICIL = 100

# Filas
FILAS_FACIL = 8
FILAS_MEDIO = 16
FILAS_DIFICIL = 16

# Columnas
COLUMNAS_FACIL = 8
COLUMNAS_MEDIO = 16
COLUMNAS_DIFICIL = 30

# Dificultad
dificultad = [FILAS_FACIL, COLUMNAS_FACIL, MINAS_FACIL]

# Celda
TAMANO_CELDA = 30
ANCHO_CELDA = 15
ALTO_CELDA = 15

# Imagenes
celda = pygame.transform.scale(pygame.image.load("1er_cuatrimestre/buscaminas/assets/imgs/celda.png"), (TAMANO_CELDA, TAMANO_CELDA))
celda_vacia = pygame.transform.scale(pygame.image.load("1er_cuatrimestre/buscaminas/assets/imgs/celda_vacia.png"), (TAMANO_CELDA, TAMANO_CELDA))
celda_mina = pygame.transform.scale(pygame.image.load("1er_cuatrimestre/buscaminas/assets/imgs/celda_mina.png"), (TAMANO_CELDA, TAMANO_CELDA))
celda_explosion = pygame.transform.scale(pygame.image.load("1er_cuatrimestre/buscaminas/assets/imgs/celda_mina_explosion.png"), (TAMANO_CELDA, TAMANO_CELDA))
celda_bandera = pygame.transform.scale(pygame.image.load("1er_cuatrimestre/buscaminas/assets/imgs/celda_bandera.png"), (TAMANO_CELDA, TAMANO_CELDA))
celda1 = pygame.transform.scale(pygame.image.load("1er_cuatrimestre/buscaminas/assets/imgs/celda1.png"), (TAMANO_CELDA, TAMANO_CELDA))
celda2 = pygame.transform.scale(pygame.image.load("1er_cuatrimestre/buscaminas/assets/imgs/celda2.png"), (TAMANO_CELDA, TAMANO_CELDA))
celda3 = pygame.transform.scale(pygame.image.load("1er_cuatrimestre/buscaminas/assets/imgs/celda3.png"), (TAMANO_CELDA, TAMANO_CELDA))
celda4 = pygame.transform.scale(pygame.image.load("1er_cuatrimestre/buscaminas/assets/imgs/celda4.png"), (TAMANO_CELDA, TAMANO_CELDA))
celda5 = pygame.transform.scale(pygame.image.load("1er_cuatrimestre/buscaminas/assets/imgs/celda5.png"), (TAMANO_CELDA, TAMANO_CELDA))
celda6 = pygame.transform.scale(pygame.image.load("1er_cuatrimestre/buscaminas/assets/imgs/celda6.png"), (TAMANO_CELDA, TAMANO_CELDA))
celda7 = pygame.transform.scale(pygame.image.load("1er_cuatrimestre/buscaminas/assets/imgs/celda7.png"), (TAMANO_CELDA, TAMANO_CELDA))
celda8 = pygame.transform.scale(pygame.image.load("1er_cuatrimestre/buscaminas/assets/imgs/celda8.png"), (TAMANO_CELDA, TAMANO_CELDA))

# Musica
pygame.mixer.music.load("1er_cuatrimestre/buscaminas/assets/sounds/musica_inicio.ogg", "ogg")
pygame.mixer.music.set_volume(0.2) # 0 - 1 | 0.2 == 20%