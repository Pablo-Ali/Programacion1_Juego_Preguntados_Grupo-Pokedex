import pygame
import constantes
import funciones_generales
from jugador import Jugador

pygame.init()

boton_volver = funciones_generales.crear_boton_generico(constantes.RUTA_IMAGEN_BOTON_VOLVER, 108, 108)

def mostrar_partida_finalizada(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event], jugador : Jugador) -> str:
    pygame.display.set_caption("¿Quién es ese Pokémon?")
    
    retorno = "terminado"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                retorno = "menu"
    

    pantalla.blit(constantes.FONDO_CONFIGURACIONES, (0, 0))

    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],constantes.POS_BOTON_VOLVER)
    return retorno