import pygame

pygame.init()

#########################################################
# GENERAL
#########################################################
ANCHO = 1000
ALTO = 700
VENTANA = (ANCHO,ALTO)
FPS = 60
POS_BOTON_VOLVER = (875, 25)
ICON_PATH = "recursos/imagenes/iconos/pokeball.png"

CANTIDAD_VIDAS = 6
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25

FUENTE_24 = pygame.font.Font("recursos/fuentes/Pokemon_GB.ttf",24)

SELECT_SOUND = "recursos/audio/sonidos/select.mp3"
SELECT_OK_SOUND = "recursos/audio/sonidos/correct.mp3"
SELECT_FAIL_SOUND = "recursos/audio/sonidos/fail.mp3"


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

BOTON_SMALL = "recursos/imagenes/botones/small_buttom.png"
BOTON_SMALL_HOVER = "recursos/imagenes/botones/small_buttom_hover.png"

SPRITES = "recursos/imagenes/sprites/sprites.png"

# - MUSICA
MUSICA_MENU = "recursos/audio/musica/pantalla_menu.mp3"

#########################################################
# PANTALLA JUEGO
#########################################################

CAJA_PREGUNTA =  "recursos/imagenes/botones/question.png"
BOTON_LARGE = "recursos/imagenes/botones/large_buttom.png"
BOTON_LARGE_HOVER = "recursos/imagenes/botones/large_buttom_hover.png"
BOTON_LARGE_RED = "recursos/imagenes/botones/large_buttom_red.png"
BOTON_LARGE_GREEN = "recursos/imagenes/botones/large_buttom_green.png"

# - FONDOS
FONDO_JUEGO = pygame.transform.scale(pygame.image.load("recursos/imagenes/fondos/pantalla_juego.png"), VENTANA)

# - MUSICA
MUSICA_JUEGO = "recursos/audio/musica/pantalla_juego.mp3"







# Fondos
FONDO_CONFIGURACIONES = pygame.transform.scale(pygame.image.load("recursos/imagenes/fondo_10.jpg"), VENTANA)

FONDO_RANKINGS = pygame.transform.scale(pygame.image.load("recursos/imagenes/fondo_7.jpg"), VENTANA)



# Rutas

# Imagenes

BOTON_SONIDO_ON = "recursos/imagenes/volumen_on.png"
BOTON_SONIDO_MUTE = "recursos/imagenes/volumen_off.png"
BOTON_SONIDO_MAS = "recursos/imagenes/volumen_mas.png"
BOTON_SONIDO_MENOS = "recursos/imagenes/volumen_menos.png"
CARTEL_VOLUMEN_MUSICA = "recursos/imagenes/cartel_vol_musica.png"
CARTEL_VOLUMEN_EFECTOS = "recursos/imagenes/cartel_vol_efectos.png"

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
FUENTE_40 = pygame.font.SysFont("Arial Narrow",40)






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