import pygame
import constantes
import funciones_generales

pygame.init()

pygame.init()

boton_volver = {}
imagen_original = boton_volver["superficie"] = pygame.image.load(constantes.RUTA_IMAGEN_BOTON_CONFIG)
boton_volver["superficie"] = pygame.transform.scale(imagen_original, (192, 120)) # 10%
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()

def mostrar_rankings(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event]) -> str:
    pygame.display.set_caption("RANKINGS")
    
    retorno = "rankings"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                retorno = "menu"
    

    pantalla.blit(constantes.FONDO_RANKINGS, (0, 0))

    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(600, 400))
    funciones_generales.mostrar_texto(boton_volver["superficie"],"VOLVER",(50, 50),constantes.FUENTE_30,constantes.COLOR_NEGRO)
    return retorno
