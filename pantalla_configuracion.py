import pygame
import pygame.locals
import constantes
import funciones_generales
from jugador import Jugador

pygame.init()

# Variables auxiliares para manejar el volumen
mouse_presionado = False
boton_presionado = None
ultima_actualizacion = 0  # Para controlar la velocidad del cambio al mantener presionado

boton_parar_musica = funciones_generales.crear_boton_generico(constantes.BOTON_SONIDO_MUTE, 100, 100)
boton_prender_musica = funciones_generales.crear_boton_generico(constantes.BOTON_SONIDO_ON, 100, 100)
boton_volver = funciones_generales.crear_boton_generico(constantes.RUTA_IMAGEN_BOTON_VOLVER, 108, 108)
boton_mas_musica = funciones_generales.crear_boton_generico(constantes.BOTON_SONIDO_MAS, 100, 100)
boton_menos_musica = funciones_generales.crear_boton_generico(constantes.BOTON_SONIDO_MENOS, 100, 100)
boton_mas_efectos = funciones_generales.crear_boton_generico(constantes.BOTON_SONIDO_MAS, 100, 100)
boton_menos_efectos = funciones_generales.crear_boton_generico(constantes.BOTON_SONIDO_MENOS, 100, 100)
cartel_musica = funciones_generales.crear_boton_generico(constantes.CARTEL_VOLUMEN_MUSICA, 200, 200)
cartel_efectos = funciones_generales.crear_boton_generico(constantes.CARTEL_VOLUMEN_EFECTOS, 200, 200)

def mostrar_configuraciones(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], jugador: Jugador) -> str:

    global mouse_presionado, boton_presionado, ultima_actualizacion

    volumen_musica_actual = jugador.get_volumen_musica()

    pygame.display.set_caption("¿Quién es ese Pokémon?")

    retorno = "configuraciones"
    ahora = pygame.time.get_ticks()

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_presionado = True
            # Detectar qué botón fue presionado
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                retorno = "menu"
            elif boton_mas_musica["rectangulo"].collidepoint(evento.pos):
                boton_presionado = "musica_mas"
            elif boton_menos_musica["rectangulo"].collidepoint(evento.pos):
                boton_presionado = "musica_menos"
            elif boton_mas_efectos["rectangulo"].collidepoint(evento.pos):
                boton_presionado = "efectos_mas"
            elif boton_menos_efectos["rectangulo"].collidepoint(evento.pos):
                boton_presionado = "efectos_menos"
            elif boton_parar_musica["rectangulo"].collidepoint(evento.pos):
                if jugador.get_musica_on():
                    jugador.set_musica_on(False)
            elif boton_prender_musica["rectangulo"].collidepoint(evento.pos):
                if jugador.get_musica_on() == False:
                    jugador.set_musica_on(True)
        elif evento.type == pygame.MOUSEBUTTONUP:
            mouse_presionado = False
            boton_presionado = None

    # Detectar si se mantiene presionado y controlar la velocidad de repetición
    if mouse_presionado and boton_presionado:
        if ahora - ultima_actualizacion > 100:  # Intervalo en milisegundos
            if boton_presionado == "musica_mas" and jugador.get_volumen_musica() < 100:
                jugador.set_volumen_musica(jugador.get_volumen_musica() + 1)
                funciones_generales.reproducir_efecto_sonido(constantes.SELECT_SOUND, jugador.get_volumen_efectos())
            elif boton_presionado == "musica_menos" and jugador.get_volumen_musica() > 0:
                jugador.set_volumen_musica(jugador.get_volumen_musica() - 1)
                funciones_generales.reproducir_efecto_sonido(constantes.SELECT_SOUND, jugador.get_volumen_efectos())
            elif boton_presionado == "efectos_mas" and jugador.get_volumen_efectos() < 100:
                jugador.set_volumen_efectos(jugador.get_volumen_efectos() + 1)
                funciones_generales.reproducir_efecto_sonido(constantes.SELECT_SOUND, jugador.get_volumen_efectos())
            elif boton_presionado == "efectos_menos" and jugador.get_volumen_efectos() > 0:
                jugador.set_volumen_efectos(jugador.get_volumen_efectos() - 1)
                funciones_generales.reproducir_efecto_sonido(constantes.SELECT_SOUND, jugador.get_volumen_efectos())
            else:
                funciones_generales.reproducir_efecto_sonido(constantes.SELECT_FAIL_SOUND, jugador.get_volumen_efectos())
            ultima_actualizacion = ahora
    
    # Dibujar fondo
    pantalla.blit(constantes.FONDO_CONFIGURACIONES, (0, 0))

    # Dibujar botones
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],constantes.POS_BOTON_VOLVER)
    boton_menos_musica["rectangulo"] = pantalla.blit(boton_menos_musica["superficie"], (100, 150))
    boton_mas_musica["rectangulo"] = pantalla.blit(boton_mas_musica["superficie"], (600, 150))
    boton_menos_efectos["rectangulo"] = pantalla.blit(boton_menos_efectos["superficie"], (100, 350))
    boton_mas_efectos["rectangulo"] = pantalla.blit(boton_mas_efectos["superficie"], (600, 350))
    boton_parar_musica["rectangulo"] = pantalla.blit(boton_parar_musica["superficie"], (450, 550))
    boton_prender_musica["rectangulo"] = pantalla.blit(boton_prender_musica["superficie"], (250, 550))
    
    # Dibjar los carteles en cada iteración para evitar superposición
    pantalla.blit(cartel_musica["superficie"], (300, 100))
    pantalla.blit(cartel_efectos["superficie"], (300, 300))

    texto_musica = constantes.FUENTE_40.render(f"{jugador.get_volumen_musica()} %", True, constantes.COLOR_NEGRO)
    texto_efectos = constantes.FUENTE_40.render(f"{jugador.get_volumen_efectos()} %", True, constantes.COLOR_NEGRO)

    # Dibujar el texto en los carteles
    pantalla.blit(texto_musica, (380, 240))
    pantalla.blit(texto_efectos, (380, 440))

    # Actualizar el volumen de la música en esta pantalla
    if volumen_musica_actual != jugador.get_volumen_musica():
        funciones_generales.cambiar_volumen_musica(jugador.get_volumen_musica())
        volumen_musica_actual = jugador.get_volumen_musica()

    # Verificar el estado de la música y refrescar inmediatamente
    if not jugador.get_musica_on():
        if pygame.mixer.music.get_busy():  # Solo detener si está sonando
            pygame.mixer.music.stop()
    else:
        if not pygame.mixer.music.get_busy():  # Solo iniciar si no está sonando
            funciones_generales.iniciar_musica(constantes.MUSICA_CONFIGURACION, jugador.get_volumen_musica())

    return retorno

