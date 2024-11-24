import pygame

pygame.init()

#########################################################
# GENERAL
#########################################################
ANCHO = 1000
ALTO = 700
VENTANA = (ANCHO,ALTO)
FPS = 60
POS_BOTON_VOLVER = (675, 25)
ICON_PATH = "recursos/imagenes/iconos/icono.png"

CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25

FUENTE_24 = pygame.font.Font("recursos/fuentes/PKMN RBYGSC.ttf",24)



#########################################################
# PANTALLA MENU
#########################################################
# - FONDOS
FONDO_MENU = pygame.transform.scale(pygame.image.load("recursos/imagenes/fondos/pantalla_menu.jpg"), VENTANA)
FONDO_MENU_TITLE =  pygame.image.load("recursos/imagenes/fondos/title.png")

# - BOTONES
BOTON_MENU_ANCHO = 200
BOTON_MENU_ALTO = 70

BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_RANKINGS = 2
BOTON_SALIR = 3

RUTA_IMAGENES_BOTONES_MENU = [
    "recursos/imagenes/botones/boton_JUGAR.png",
    "recursos/imagenes/botones/boton_RANKING.png",
    "recursos/imagenes/botones/boton_AJUSTES.png",
    "recursos/imagenes/botones/boton_SALIR.png"
]

SPRITES = "recursos/imagenes/sprites/sprites.png"

# - MUSICA
MUSICA_MENU = "recursos/audio/musica/pantalla_menu.mp3"

#########################################################
# PANTALLA JUEGO
#########################################################

# - BOTONES
# BOTON__ANCHO = 200
# BOTON_MENU_ALTO = 70

# RUTA_IMAGENES_BOTONES_MENU = [
#     "recursos/imagenes/botones/boton_JUGAR.png",
#     "recursos/imagenes/botones/boton_RANKING.png",
#     "recursos/imagenes/botones/boton_AJUSTES.png",
#     "recursos/imagenes/botones/boton_SALIR.png"
# ]


CAJA_PREGUNTA =  "recursos/imagenes/botones/question.png"
BOTON_RESPUESTA = "recursos/imagenes/botones/large_buttom.png"


# - FONDOS
FONDO_JUEGO = pygame.transform.scale(pygame.image.load("recursos/imagenes/fondos/pantalla_juego.png"), VENTANA)

# - MUSICA
MUSICA_JUEGO = "recursos/audio/musica/pantalla_juego.mp3"








# Jugador
CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 50

# Fondos
FONDO_CONFIGURACIONES = pygame.transform.scale(pygame.image.load("recursos/imagenes/fondo_10.jpg"), VENTANA)

FONDO_RANKINGS = pygame.transform.scale(pygame.image.load("recursos/imagenes/fondo_7.jpg"), VENTANA)



# Rutas

# Imagenes


RUTA_IMAGEN_BOTON_VOLVER = "recursos/imagenes/volver.png"

RUTA_IMAGENES_RESPUESTAS = [
    "recursos/imagenes/" #COMPLETAR
    "recursos/imagenes/"
    "recursos/imagenes/"
    "recursos/imagenes/"
]

# Audio
MUSICA_RANKINGS = "recursos/audio/Pokemon_Pallet_Town.mp3"
MUSICA_CONFIGURACION = "recursos/audio/Pokemon_Trainer_Battle.mp3"
MUSICA_PARTIDA_FINALIZADA = "recursos/audio/Pokemon_Ending.mp3"

# Fuentes
FUENTE_25 = pygame.font.SysFont("Arial Narrow",25)
FUENTE_30 = pygame.font.SysFont("Arial Narrow",30)






# Colores
COLOR_NEGRO = (0,0,0)
COLOR_BLANCO = (255,255,255)
COLOR_AMARILLO = (255, 255, 0)

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)