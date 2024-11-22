import pygame
import constantes
import funciones_generales
import pantalla_configuracion
import pantalla_juego
import pantalla_menu
import pantalla_partida_finalizada
import pantalla_rankings
import jugador

# Inicializamos pygame
pygame.init()

# Nombre de la ventana
pygame.display.set_caption("Preguntados Pokédex")

# Ícono del juego
icono = pygame.image.load("recursos/imagenes/pokeball.png")
pygame.display.set_icon(icono)

# Creamos la pantalla
pantalla = pygame.display.set_mode(constantes.VENTANA)

# Creamos reloj
reloj = pygame.time.Clock()

# Creamos al jugador
jugador = jugador.Jugador("", 3, 0, 50, True, True)

# Inicializamos mixer para la música
pygame.mixer.init()

# Banderas
corriendo = True
musica_menu = False
musica_juego = False
musica_configuraciones = False
musica_rankings = False
musica_terminado = False
pantalla_actual = "menu"

# Iniciamos el bucle principal
while corriendo:
    # Creamos la cola de eventos
    cola_eventos = pygame.event.get()

    # Iniciamos el reloj
    reloj.tick(constantes.FPS)

    # Verificamos la pantalla a mostrar
    match pantalla_actual:
        case "menu":
            # Verificamos que la música esté activada y la reproducimos
            if musica_menu == False:
                funciones_generales.iniciar_musica(constantes.MUSICA_MENU, jugador.get_volumen_musica())
                musica_encendida = True

            # Llamamos a la función que ejecuta la pantalla
            pantalla_actual = pantalla_menu.mostrar_menu(pantalla, cola_eventos)

        case "juego":
            if musica_juego == False:
                funciones_generales.iniciar_musica(constantes.MUSICA_JUEGO, jugador.get_volumen_musica())
                musica_encendida = True

        case "configuraciones":
            if musica_configuraciones == False:
                funciones_generales.iniciar_musica(constantes.MUSICA_CONFIGURACION, jugador.get_volumen_musica())
                musica_encendida = True

        case "rankings":
            if musica_rankings == False:
                funciones_generales.iniciar_musica(constantes.MUSICA_RANKINGS, jugador.get_volumen_musica())
                musica_encendida = True

        case "terminado":
            if musica_terminado == False:
                funciones_generales.iniciar_musica(constantes.MUSICA_PARTIDA_FINALIZADA, jugador.get_volumen_musica())
                musica_encendida = True

        case "salir":
            corriendo = False
    
    # Actualizamos pantalla
    pygame.display.flip()

# Cerramos el juego
pygame.quit()
