import pygame
from constantes import *

lista_botones = []

for i in range(4):
    boton = {}
    boton["superficie"] = pygame.image.load(RUTA_IMAGENES_BOTONES_MENU[i])
    boton["rectangulo"] = boton["superficie"].get_rect()
    boton["rectangulo"].left = (ANCHO / 2) - (BOTON_MENU_ANCHO /2)
    boton["rectangulo"].top = (ALTO / 2) + 30 + (i*(BOTON_MENU_ALTO + 5)) 
    lista_botones.append(boton)

def mostrar_menu( pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event] ) -> str:
    retorno = "menu"
    # Control de Eventos
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(lista_botones)):
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    if i == BOTON_JUGAR:
                        retorno = "juego"
                    elif i == BOTON_CONFIG:
                        retorno = "configuraciones"
                    elif i == BOTON_RANKINGS:
                        retorno = "rankings"
                    elif i == BOTON_SALIR:
                        retorno = "salir"
    # Actualizar
    
    # Dibujar
    pantalla.blit(FONDO_MENU, (0, 0))
    pantalla.blit(FONDO_MENU_TITLE, (((ANCHO / 2) - (FONDO_MENU_TITLE.get_width() /2)), FONDO_MENU_TITLE.get_height() / 4)) 
    for boton in lista_botones: 
        pantalla.blit(boton["superficie"], boton["rectangulo"])
    # Bye
    return retorno