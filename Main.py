import pygame
import Constantes
import Pantalla_configuracion
import Pantalla_juego
import Pantalla_menu
import Pantalla_partida_finalizada
import Pantalla_rankings

# Inicializamos pygame
pygame.init()

# Nombre de la ventana
pygame.display.set_caption("Preguntados Pokédex")

# Ícono del juego
icono = pygame.image.load("Recursos/Imagenes/pokeball.png")
pygame.display.set_icon(icono)

# Creamos la pantalla
pantalla = pygame.display.set_mode(Constantes.VENTANA)

# Creamos reloj
reloj = pygame.time.Clock()

# Creamos los datos del juego (sea con un diccionario, sea con la instanciación de una clase) 

# Inicializamos mixer para la música
pygame.mixer.init()

# Banderas
corriendo = True
bandera_musica = False
pantalla_actual = "menu"

# Iniciamos el bucle principal
while corriendo:
    # Creamos la cola de eventos
    cola_eventos = pygame.event.get()

    # Iniciamos el reloj
    reloj.tick(Constantes.FPS)

    # Verificamos la pantalla a mostrar

    match pantalla_actual:
        case "menu":
            pass
        case "juego":
            pass
        case "configuraciones":
            pass
        case "rankings":
            pass
        case "terminado":
            pass
        case "salir":
            corriendo = False
    
    # Actualizamos pantalla
    pygame.display.flip()

# Cerramos el juego
pygame.quit()