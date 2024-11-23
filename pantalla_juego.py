import pygame
import constantes
import funciones_generales

pygame.init()

pygame.init()

boton_volver = funciones_generales.crear_boton_volver()

def mostrar_juego(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event]) -> str:
    pygame.display.set_caption("JUGAR")
    
    retorno = "juego"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                retorno = "menu"
    

    pantalla.blit(constantes.FONDO_JUEGO, (0, 0))

    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],constantes.POS_BOTON_VOLVER)
    return retorno
