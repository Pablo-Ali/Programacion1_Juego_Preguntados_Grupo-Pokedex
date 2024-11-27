import pygame
import constantes
import funciones_generales
from jugador import Jugador

pygame.init()

boton_volver = funciones_generales.crear_boton_generico(constantes.RUTA_IMAGEN_BOTON_VOLVER, 108, 108)
boton_enter = funciones_generales.crear_boton_generico(constantes.BOTON_SMALL, 140, 50)
caja_texto = funciones_generales.crear_boton_generico(constantes.CAJA_PREGUNTA, 400, 200)
caja_texto_mensaje = funciones_generales.crear_boton_generico(constantes.CAJA_PREGUNTA, 600, 200)

# variables globales

# variable auxiliar para almacenar el nombre
nombre = ""
# variables para permitir mantener teclas presionadas
tecla_presionada = None  # Variable para almacenar la tecla presionada
tiempo_ultima_ejecucion = 0  # Para controlar la velocidad de repetición
intervalo_repeticion = 50  # Milisegundos entre repeticiones

def mostrar_partida_finalizada(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event], jugador : Jugador) -> str:
    pygame.display.set_caption("¿Quién es ese Pokémon?")
    
    retorno = "terminado"

    global nombre, tecla_presionada, tiempo_ultima_ejecucion

    for evento in cola_eventos:
        # capturamos el evento
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                retorno = "menu"
            elif boton_enter["rectangulo"].collidepoint(evento.pos):
                if len(nombre) > 0:
                    jugador.set_nombre(nombre)
                    if funciones_generales.registrar_partida_json(jugador, "prueba"):
                        jugador.set_nombre("")
                        jugador.set_vidas(constantes.CANTIDAD_VIDAS)
                        jugador.set_puntos(0)
                        jugador.set_comodin_pasar(True)
                        jugador.set_comodin_x2(True)
                        retorno = "menu"
                else:
                    funciones_generales.reproducir_efecto_sonido(constantes.SELECT_FAIL_SOUND, jugador.get_volumen_efectos())
        elif evento.type == pygame.KEYDOWN:
            # almacena la tecla que se pulsa
            tecla_presionada = evento.key
        elif evento.type == pygame.KEYUP:
            # libera la tecla pulsada
            tecla_presionada = None

        # manejamos las teclas presionadas, permitiendo mantener puslado
        if tecla_presionada is not None:
            ahora = pygame.time.get_ticks()

            # tomamos el nombre de la tecla presionada
            nombre_tecla_presionada = pygame.key.name(tecla_presionada)

            if ahora - tiempo_ultima_ejecucion > intervalo_repeticion:
                    
                if nombre_tecla_presionada == "space":
                    if len(nombre) < 12:  # Máximo de 12 caracteres
                        nombre += " "
                    else:
                        funciones_generales.reproducir_efecto_sonido(constantes.SELECT_FAIL_SOUND, jugador.get_volumen_efectos())

                #elif tecla_presionada == pygame.K_BACKSPACE:
                elif nombre_tecla_presionada == "backspace": # probé con ambas versiones, pero sigo sin poder hacer funcionar el mantener presionado para borrar
                    if len(nombre) > 0:
                        nombre = nombre[0:-1] #Me elimina automaticamente el último
                        pantalla.blit(caja_texto["superficie"], (300, 400))# actualizamos la imagen del cuadro de texto
                    else:
                        funciones_generales.reproducir_efecto_sonido(constantes.SELECT_FAIL_SOUND, jugador.get_volumen_efectos())
                    
                elif len(nombre_tecla_presionada) == 1:  # Solo procesa letras y caracteres imprimibles
                    # Detectar si Shift o Caps Lock están activados
                    shift_presionado = bool(pygame.key.get_mods() & (pygame.KMOD_LSHIFT | pygame.KMOD_RSHIFT))
                    bloc_mayus = bool(pygame.key.get_mods() & pygame.KMOD_CAPS)

                    # Combinar Shift y Caps Lock para determinar el caso
                    if len(nombre) < 13:
                        if shift_presionado ^ bloc_mayus:  # XOR para alternar entre mayúsculas y minúsculas
                            nombre += nombre_tecla_presionada.upper()
                        else:
                            nombre += nombre_tecla_presionada.lower()
                    else:
                        funciones_generales.reproducir_efecto_sonido(constantes.SELECT_FAIL_SOUND, jugador.get_volumen_efectos())
                elif nombre_tecla_presionada == "return":
                    if len(nombre) > 0:
                        jugador.set_nombre(nombre)
                        if funciones_generales.registrar_partida_json(jugador, "prueba"):
                            jugador.set_nombre("")
                            jugador.set_vidas(constantes.CANTIDAD_VIDAS)
                            jugador.set_puntos(0)
                            jugador.set_comodin_pasar(True)
                            jugador.set_comodin_x2(True)
                            retorno = "menu"
                    else:
                        funciones_generales.reproducir_efecto_sonido(constantes.SELECT_FAIL_SOUND, jugador.get_volumen_efectos())
                # Actualizamos el tiempo de última ejecución después de cualquier acción
                tiempo_ultima_ejecucion = ahora
                

    pantalla.blit(constantes.FONDO_CONFIGURACIONES, (0, 0))
    
    #pantalla.blit(caja_texto["superficie"], (300, 100))

    #botones
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],constantes.POS_BOTON_VOLVER)
    boton_enter["rectangulo"] = pantalla.blit(boton_enter["superficie"], (425, 550))
    
    #cajas de texto
    caja_texto_mensaje["rectangulo"] = pantalla.blit(caja_texto_mensaje["superficie"],(200, 50))
    caja_texto["rectangulo"] = pantalla.blit(caja_texto["superficie"],(300, 300))

    #textos de cajas y botones
    funciones_generales.mostrar_texto(caja_texto_mensaje["superficie"],"Igresá tu nombre.\nEntre 1 y 13 caracactéres alfanuméricos",(100,25), constantes.FUENTE_24, constantes.COLOR_NEGRO)
    funciones_generales.mostrar_texto(boton_enter["superficie"], "Enter", (10, 10), constantes.FUENTE_24, constantes.COLOR_NEGRO)
    texto_nombre = constantes.FUENTE_24.render(nombre, True, constantes.COLOR_NEGRO)
    pantalla.blit(texto_nombre, (350, 375))

    #texto_mensaje = constantes.FUENTE_24.render("Ingresá tu nombre.", True, constantes.COLOR_NEGRO)
    #texto_mensaje_2 = constantes.FUENTE_24.render("Hasta 13 caracteres alfanuméricos.", True, constantes.COLOR_NEGRO)
     
    
    #pantalla.blit(texto_mensaje, (150, 150))
    #pantalla.blit(texto_mensaje_2, (150, 200))

    
    return retorno