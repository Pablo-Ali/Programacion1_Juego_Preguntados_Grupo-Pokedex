import pygame
import constantes
import funciones_generales

pygame.init()

lista_botones = []

for i in range(4):
    boton = {}
    imagen_original = boton["superficie"] = pygame.image.load(constantes.RUTA_IMAGENES_BOTONES[i])
    boton["superficie"] = pygame.transform.scale(imagen_original, (126, 177)) # 30% de la imagen original
    boton["rectangulo"] = boton["superficie"].get_rect()
    boton["rectangulo"].topleft = (35 + i * 200, 50 )
    lista_botones.append(boton)

def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    # Nombre de la ventana
    pygame.display.set_caption("MENU")

    retorno = "menu"
    
    # Gestion Eventos
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(lista_botones)):
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    if i == constantes.BOTON_JUGAR:
                        retorno = "juego"
                    elif i == constantes.BOTON_CONFIG:
                        retorno = "configuraciones"
                    elif i == constantes.BOTON_RANKINGS:
                        retorno = "rankings"
                    elif i == constantes.BOTON_SALIR:
                        retorno = "salir"

    # Dibujar fondo de pantalla
    pantalla.blit(constantes.FONDO_MENU, (0, 0))

    # Dibujar los botones
    for boton in lista_botones:
        pantalla.blit(boton["superficie"], boton["rectangulo"])

    funciones_generales.mostrar_texto(lista_botones[constantes.BOTON_JUGAR]["superficie"],"JUGAR",(30,120),constantes.FUENTE_25,constantes.COLOR_NEGRO)
    funciones_generales.mostrar_texto(lista_botones[constantes.BOTON_CONFIG]["superficie"],"CONFIGURAR",(5,120),constantes.FUENTE_25,constantes.COLOR_NEGRO)
    funciones_generales.mostrar_texto(lista_botones[constantes.BOTON_RANKINGS]["superficie"],"RANKINGS",(15,120),constantes.FUENTE_25,constantes.COLOR_NEGRO)
    funciones_generales.mostrar_texto(lista_botones[constantes.BOTON_SALIR]["superficie"],"SALIR",(35,120),constantes.FUENTE_25,constantes.COLOR_NEGRO)

    #pygame.display.flip()

    return retorno