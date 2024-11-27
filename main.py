import pygame
import constantes
import funciones_generales
import pantalla_configuracion
import pantalla_juego
import pantalla_menu
import pantalla_partida_finalizada
import pantalla_rankings
from jugador import Jugador

# Inicializamos pygame
pygame.init()

# Nombre de la ventana
pygame.display.set_caption("¿Quién es ese Pokémon?")

# Ícono del juego
icono = pygame.image.load(constantes.ICON_PATH)
pygame.display.set_icon(icono)

# Creamos la pantalla
pantalla = pygame.display.set_mode(constantes.VENTANA)

# Creamos reloj
reloj = pygame.time.Clock()

# Creamos al jugador
jugador = Jugador("", constantes.CANTIDAD_VIDAS, 0, 25, 70, True, True, True)

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
            if jugador.get_musica_on():
                
                # Verificamos que la música esté activada y la reproducimos
                if musica_menu == False:
                    # Iniciamos la música de la pantalla
                    funciones_generales.iniciar_musica(constantes.MUSICA_MENU, jugador.get_volumen_musica())
            
                    # Cambiamos el valor de las banderas
                    musica_menu = True #True
                    musica_juego = False
                    musica_configuraciones = False
                    musica_rankings = False
                    musica_terminado = False
            else:
                # Detenemos la música
                pygame.mixer.music.stop()
            
            # Llamamos a la función que ejecuta la pantalla
            pantalla_actual = pantalla_menu.mostrar_menu(pantalla, cola_eventos, jugador)

        case "juego":
            if jugador.get_musica_on():
                if musica_juego == False:
                    funciones_generales.iniciar_musica(constantes.MUSICA_JUEGO, jugador.get_volumen_musica())
                    musica_menu = False
                    musica_juego = True #True
                    musica_configuraciones = False
                    musica_rankings = False
                    musica_terminado = False
            else:
                pygame.mixer.music.stop()

            pantalla_actual = pantalla_juego.mostrar_juego(pantalla, cola_eventos, jugador)

        case "configuraciones":
            if jugador.get_musica_on():
                if musica_configuraciones == False:
                    funciones_generales.iniciar_musica(constantes.MUSICA_CONFIGURACION, jugador.get_volumen_musica())
                    musica_menu = False
                    musica_juego = False
                    musica_configuraciones = True #True
                    musica_rankings = False
                    musica_terminado = False
            else:
                pygame.mixer.music.stop()
                
            pantalla_actual = pantalla_configuracion.mostrar_configuraciones(pantalla, cola_eventos, jugador)

        case "rankings":
            if jugador.get_musica_on():
                if musica_rankings == False:
                    funciones_generales.iniciar_musica(constantes.MUSICA_RANKINGS, jugador.get_volumen_musica())
                    musica_menu = False
                    musica_juego = False
                    musica_configuraciones = False
                    musica_rankings = True #True
                    musica_terminado = False
            else:
                pygame.mixer.music.stop()

            pantalla_actual = pantalla_rankings.mostrar_rankings(pantalla, cola_eventos)

        case "terminado":
            if jugador.get_musica_on():
                if musica_terminado == False:
                    funciones_generales.iniciar_musica(constantes.MUSICA_PARTIDA_FINALIZADA, jugador.get_volumen_musica())
                    musica_menu = False
                    musica_juego = False
                    musica_configuraciones = False
                    musica_rankings = False
                    musica_terminado = True #True
            else:
                pygame.mixer.music.stop()

            pantalla_actual = pantalla_partida_finalizada.mostrar_partida_finalizada(pantalla, cola_eventos, jugador)
        case "salir":
            corriendo = False
    
    # Actualizamos pantalla
    pygame.display.flip()

# Cerramos el juego
pygame.quit()