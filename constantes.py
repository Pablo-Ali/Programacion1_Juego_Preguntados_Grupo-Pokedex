import pygame

pygame.init()

# Pantalla
ANCHO = 800
ALTO = 600
VENTANA = (ANCHO,ALTO)
FPS = 60
POS_BOTON_VOLVER = (675, 25)

# Jugador
CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 50

# Fondos
FONDO_MENU = pygame.transform.scale(pygame.image.load("recursos/imagenes/fondo_9.jpg"), VENTANA)
FONDO_CONFIGURACIONES = pygame.transform.scale(pygame.image.load("recursos/imagenes/fondo_10.jpg"), VENTANA)
FONDO_JUEGO = pygame.transform.scale(pygame.image.load("recursos/imagenes/estadio.jpg"), VENTANA)
FONDO_RANKINGS = pygame.transform.scale(pygame.image.load("recursos/imagenes/fondo_7.jpg"), VENTANA)


# Botones del menú
BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_RANKINGS = 2
BOTON_SALIR = 3

# Rutas

# Imagenes
RUTA_IMAGENES_BOTONES_MENU = [
    "recursos/imagenes/boton_jugar.png",
    "recursos/imagenes/boton_rankings.png",
    "recursos/imagenes/boton_configuracion.png",
    "recursos/imagenes/boton_salir.png"
]

RUTA_IMAGEN_BOTON_VOLVER = "recursos/imagenes/volver.png"

RUTA_IMAGENES_RESPUESTAS = [
    "recursos/imagenes/" #COMPLETAR
    "recursos/imagenes/"
    "recursos/imagenes/"
    "recursos/imagenes/"
]


# Audio
MUSICA_MENU = "recursos/audio/Pokemon_Route_1.mp3"
MUSICA_JUEGO = "recursos/audio/Pokemon_Opening.mp3"
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