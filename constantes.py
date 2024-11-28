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
ICON_PATH = pygame.image.load("recursos/imagenes/iconos/pokeball.png")

CANTIDAD_VIDAS = 3
CANTIDAD_VIDAS_MAX = 6
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25
TIEMPO_INICIAL = 30     #SEGUNDOS
TIEMPO_INCREMENTO = 10   #SEGUNDOS

FUENTE_POKEMON_GB = pygame.font.Font("recursos/fuentes/Pokemon_GB.ttf",24)

FUENTE_POKEMON_GB_16 = pygame.font.Font("recursos/fuentes/Pokemon_GB.ttf",16)

SELECT_SOUND = "recursos/audio/sonidos/select.mp3"
SELECT_OK_SOUND = "recursos/audio/sonidos/correct.mp3"
SELECT_FAIL_SOUND = "recursos/audio/sonidos/fail.mp3"

#########################################################
# PANTALLA MENU
#########################################################
# - FONDOS
FONDO_MENU = pygame.transform.scale(pygame.image.load("recursos/imagenes/fondos/pantalla_menu.jpg"), VENTANA)
FONDO_MENU_TITLE =  pygame.image.load("recursos/imagenes/fondos/title.png")
FONDO_MENU_TITLE_ANCHO = FONDO_MENU_TITLE.get_width()
FONDO_MENU_TITLE_ALTO = FONDO_MENU_TITLE.get_height()
# - BOTONES
BOTON_MENU = pygame.image.load("recursos/imagenes/botones/small_buttom.png") 
BOTON_MENU_HOVER = pygame.image.load("recursos/imagenes/botones/small_buttom_hover.png") 
BOTON_MENU_ANCHO = BOTON_MENU.get_width()
BOTON_MENU_ALTO = BOTON_MENU.get_height()
# - MUSICA
MUSICA_MENU = "recursos/audio/musica/pantalla_menu.mp3"

#########################################################
# PANTALLA JUEGO
#########################################################
# - FONDOS
FONDO_JUEGO = pygame.transform.scale(pygame.image.load("recursos/imagenes/fondos/pantalla_juego.png"), VENTANA)
# - BOTONES
BOTON_TIPO_COMODIN_X2 = 1
BOTON_TIPO_COMODIN_NEXT = 2

BOTON_COMODIN_ESTADO_EN_ESPERA = 0
BOTON_COMODIN_ESTADO_ACTIVADO = 1
BOTON_COMODIN_ESTADO_ANULADO = 2

BOTON_COMODIN_X2 = pygame.image.load("recursos/imagenes/botones/comodin_x2.png") 
BOTON_COMODIN_X2_HOVER = pygame.image.load("recursos/imagenes/botones/comodin_x2_hover.png")
BOTON_COMODIN_X2_ACTIVADO = pygame.image.load("recursos/imagenes/botones/comodin_x2_enabled.png")
BOTON_COMODIN_X2_ANULADO = pygame.image.load("recursos/imagenes/botones/comodin_x2_disabled.png")

BOTON_COMODIN_NEXT = pygame.image.load("recursos/imagenes/botones/comodin_next.png") 
BOTON_COMODIN_NEXT_HOVER = pygame.image.load("recursos/imagenes/botones/comodin_next_hover.png")
BOTON_COMODIN_NEXT_ACTIVADO = pygame.image.load("recursos/imagenes/botones/comodin_next_enabled.png")
BOTON_COMODIN_NEXT_ANULADO = pygame.image.load("recursos/imagenes/botones/comodin_next_disabled.png")

BOTON_COMODIN_ANCHO = BOTON_COMODIN_X2.get_width()
BOTON_COMODIN_ALTO = BOTON_COMODIN_X2.get_height()

BOTON_JUEGO_SUP = pygame.image.load("recursos/imagenes/botones/large_buttom.png") 
BOTON_JUEGO_SUP_HOVER = pygame.image.load("recursos/imagenes/botones/large_buttom_hover.png") 
BOTON_JUEGO_SUP_CORRECT = pygame.image.load("recursos/imagenes/botones/large_buttom_green.png") 
BOTON_JUEGO_SUP_INCORRECT = pygame.image.load("recursos/imagenes/botones/large_buttom_red.png") 
BOTON_JUEGO_ANCHO = BOTON_JUEGO_SUP.get_width()
BOTON_JUEGO_ALTO = BOTON_JUEGO_SUP.get_height()

CAJA_PREGUNTA = pygame.image.load("recursos/imagenes/botones/question.png")
CAJA_PREGUNTA_ANCHO = CAJA_PREGUNTA.get_width()
CAJA_PREGUNTA_ALTO = CAJA_PREGUNTA.get_height()

SPRITES = pygame.image.load("recursos/imagenes/sprites/sprites.png")  

PREGUNTAS_PATH =  "recursos/config/preguntas.csv"

# - MUSICA
MUSICA_JUEGO = "recursos/audio/musica/pantalla_juego.mp3"

#########################################################




# Fondos
FONDO_CONFIGURACIONES = pygame.transform.scale(pygame.image.load("recursos/imagenes/fondo_10.jpg"), VENTANA)

FONDO_RANKINGS = pygame.transform.scale(pygame.image.load("recursos/imagenes/fondo_7.jpg"), VENTANA)



# Rutas

# Imagenes

BOTON_SONIDO_ON = pygame.image.load("recursos/imagenes/volumen_on.png") 
BOTON_SONIDO_MUTE = pygame.image.load("recursos/imagenes/volumen_off.png")  
BOTON_SONIDO_MAS = pygame.image.load("recursos/imagenes/volumen_mas.png")  
BOTON_SONIDO_MENOS = pygame.image.load("recursos/imagenes/volumen_menos.png")  


CARTEL_VOLUMEN_MUSICA = pygame.image.load("recursos/imagenes/cartel_vol_musica.png")
CARTEL_VOLUMEN_EFECTOS = pygame.image.load("recursos/imagenes/cartel_vol_efectos.png")

RUTA_IMAGEN_BOTON_VOLVER = pygame.image.load("recursos/imagenes/volver.png")

# RUTA_IMAGENES_RESPUESTAS = [
#     "recursos/imagenes/" #COMPLETAR
#     "recursos/imagenes/"
#     "recursos/imagenes/"
#     "recursos/imagenes/"
# ]

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