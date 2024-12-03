import pygame
from funciones import *
from variables import *

# INICIALIZAR PYGAME #
pygame.init()

'''
completar punto g y h
usar diccionarios
revelar celdas en blanco
sacar return vacio
'''

def main():
    # PANTALLA y TITULO #
    ventana = inicializar_ventana()

    # BANDERAS #
    corriendo = True
    musica = True
    reloj = pygame.time.Clock()

    # REPRODUCIR MUSICA #
    if musica:
        pygame.mixer.music.play(-1)

    # FONDO #
    imagen_fondo = pygame.image.load("1er_cuatrimestre/buscaminas/assets/imgs/pasto.png")
    ventana.blit(imagen_fondo, [0, 0])

    while corriendo == True:
        # MENU #
        puntaje = 0
        pygame.draw.rect(ventana, VERDE, (250, 80, 510, 400), 0, 25)
        pygame.draw.rect(ventana, GRIS, (250, 80, 510, 400), 10, 25)

        if crear_boton(NIVEL, 350, 130, 300, 55, ventana, GRIS, GRIS_CLARO, BLANCO, NEGRO):
            seleccionar_dificultad(ventana)
        if crear_boton(JUGAR, 350, 210, 300, 55, ventana, GRIS, GRIS_CLARO, BLANCO, NEGRO):
            nombre = pedir_nombre(ventana)
            seleccionar_jugar(ventana, reloj, dificultad[0], dificultad[1], dificultad[2])
            ventana.blit(imagen_fondo, [0, 0])
        if crear_boton(PUNTAJES, 350, 290, 300, 55, ventana, GRIS, GRIS_CLARO, BLANCO, NEGRO):
            seleccionar_puntajes(ventana)
        if crear_boton("<)))", 280, 370, 80, 55, ventana, GRIS, GRIS_CLARO, BLANCO, NEGRO):
            pass
        if crear_boton(SALIR, 445, 370, 120, 55, ventana, GRIS, GRIS_CLARO, BLANCO, NEGRO):
            corriendo = False

        # ACTUALIZAR VENTANA #
        pygame.display.flip()

        # EVENTO CIERRE X PRINCIPAL #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False

# ATRIBUTO ESPECIAL __name__ #
if __name__ == "__main__":
    main()

# CERRAR pygame #
pygame.quit()