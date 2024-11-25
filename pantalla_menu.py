import pygame
import constantes

lista_botones = []
for i in range(4):
    boton = {}
    boton["superficie"] = pygame.image.load(constantes.BOTON_SMALL)
    boton["superficie_hover"] = pygame.image.load(constantes.BOTON_SMALL_HOVER)
    boton["hover"] = False
    boton["rectangulo"] = boton["superficie"].get_rect()
    boton["rectangulo"].left = (constantes.ANCHO / 2) - (constantes.BOTON_MENU_ANCHO /2)
    boton["rectangulo"].top = (constantes.ALTO / 2) + 30 + (i*(constantes.BOTON_MENU_ALTO + 5)) 
    match i:
        case 0:
            boton["caption"] = "jugar".upper()
        case 1:
            boton["caption"] = "ajustes".upper()
        case 2:
            boton["caption"] = "ranking".upper()
        case 3:
            boton["caption"] = "salir".upper()
    lista_botones.append(boton)

def mostrar_menu( pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event] ) -> str:
    retorno = "menu"

    # Control de Eventos
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEMOTION:
            for i in range(len(lista_botones)):
                lista_botones[i]["hover"] = False
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    lista_botones[i]["hover"] = True            
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(lista_botones)):
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    constantes.SELECT_SOUND.play()
                    pygame.time.delay(350)
                    match i:
                        case constantes.BOTON_JUGAR:
                            retorno = "juego"
                        case constantes.BOTON_CONFIG:
                            retorno = "configuraciones"
                        case constantes.BOTON_RANKINGS:
                            retorno = "rankings"  
                        case constantes.BOTON_RANKINGS:
                            retorno = "salir"  
    # Actualizar
  
    # Dibujar
    pantalla.blit(constantes.FONDO_MENU, (0, 0))
    pantalla.blit(constantes.FONDO_MENU_TITLE, (((constantes.ANCHO / 2) - (constantes.FONDO_MENU_TITLE.get_width() /2)), constantes.FONDO_MENU_TITLE.get_height() / 4)) 
    for boton in lista_botones: 
        if boton["hover"]:
            pantalla.blit(boton["superficie_hover"], boton["rectangulo"])
        else:
            pantalla.blit(boton["superficie"], boton["rectangulo"])
        text_render = constantes.FUENTE_24.render(boton["caption"], True, constantes.COLOR_NEGRO)
        text_rect = text_render.get_rect(center=boton["rectangulo"].center)
        pantalla.blit(text_render, text_rect)  

    # Bye
    return retorno