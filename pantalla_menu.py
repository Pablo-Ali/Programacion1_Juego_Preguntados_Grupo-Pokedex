import pygame
import constantes
import funciones_generales
import jugador 

class BotonMenu:
    def __init__(self, x:int, y:int, caption:str, retorno:str):
        self.superficie = constantes.BOTON_MENU_SUP
        self.superficie_hover = constantes.BOTON_MENU_SUP_HOVER
        self.caption = caption
        self.rect = pygame.Rect(0, 0, constantes.BOTON_MENU_ANCHO, constantes.BOTON_MENU_ALTO)
        self.rect.center = (x, y)
        self.hover = False
        self.retorno = retorno
    def dibujar(self, superficie:pygame.Surface):
        if self.hover:
            superficie.blit(self.superficie_hover, self.rect)
        else:
            superficie.blit(self.superficie, self.rect)
        texto_renderizado = constantes.FUENTE_POKEMON_GB.render(self.caption, True, constantes.COLOR_NEGRO)
        texto_rect = texto_renderizado.get_rect(center=self.rect.center)
        superficie.blit(texto_renderizado, texto_rect)

lista_botones = []
for i in range(4):
    boton_x = (constantes.ANCHO / 2)
    boton_y = (constantes.ALTO / 2) + 45 + (i * (constantes.BOTON_MENU_ALTO + 5))
    match i:
        case 0:
            boton_caption = "jugar".upper()
            boton_retorno = "juego"
        case 1:
            boton_caption = "ajustes".upper()
            boton_retorno = "configuraciones"
        case 2:
            boton_caption = "ranking".upper()
            boton_retorno = "rankings"
        case 3:
            boton_caption = "salir".upper()
            boton_retorno = "salir"
    boton = BotonMenu(boton_x, boton_y, boton_caption, boton_retorno)
    lista_botones.append(boton)

def mostrar_menu( pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event], jugador:jugador.Jugador) -> str:
    retorno = "menu"
    # Manejo de Eventos
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEMOTION:
            for i in range(len(lista_botones)):
                boton = lista_botones[i]
                boton.hover = False
                if boton.rect.collidepoint(evento.pos):
                    boton.hover = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(lista_botones)):
                boton = lista_botones[i]
                if boton.rect.collidepoint(evento.pos):
                    funciones_generales.reproducir_efecto_sonido(constantes.SELECT_SOUND, jugador.get_volumen_efectos())
                    pygame.time.delay(350)
                    retorno = boton.retorno
    # Actualizar
  
    # Dibujar
    pantalla.blit(constantes.FONDO_MENU, (0, 0))
    pantalla.blit(constantes.FONDO_MENU_TITLE, (((constantes.ANCHO / 2) - (constantes.FONDO_MENU_TITLE_ANCHO /2)), constantes.FONDO_MENU_TITLE_ALTO / 4)) 
    for boton in lista_botones:
        boton.dibujar(pantalla)

    # Bye
    return retorno