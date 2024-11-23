import pygame
from constantes import *
from funciones_generales import *
from preguntas import *

# boton_volver = funciones_generales.crear_boton_volver()

caja_pregunta = {}
caja_pregunta["superficie"] = pygame.image.load(CAJA_PREGUNTA)
caja_pregunta["rectangulo"] = caja_pregunta["superficie"].get_rect()
caja_pregunta["rectangulo"].left = 1#(ANCHO / 2) - (BOTON_MENU_ANCHO /2)
caja_pregunta["rectangulo"].top = ALTO - caja_pregunta["superficie"].get_height() - 10

lista_botones = []
for i in range(4):
    boton = {}
    boton["superficie"] = pygame.image.load(BOTON_RESPUESTA)
    boton["rectangulo"] = boton["superficie"].get_rect()
    boton["rectangulo"].left = 1 + caja_pregunta["superficie"].get_width() + 4 +  ((i//2) * (boton["superficie"].get_width() + 4 ))
    boton["rectangulo"].top = (ALTO - caja_pregunta["superficie"].get_height() - 10) + ((i%2) * (boton["superficie"].get_height() + 4))
    lista_botones.append(boton)





indice = 0 #Todo dato inmutable en la funcion que muestra esa ventana, lo tengo que definir como global
mezclar_lista(lista_preguntas)
bandera_respuesta = False #Todo dato inmutable en la funcion que muestra esa ventana, lo tengo que definir como global


def mostrar_juego(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    # pygame.display.set_caption("JUGAR")


    global indice
    global bandera_respuesta


    retorno = "juego"


    pregunta_actual = lista_preguntas[indice]
    if bandera_respuesta:
        pygame.time.delay(500)
        bandera_respuesta = False

    # caja_pregunta["superficie"].fill(COLOR_ROJO)





    # for i in range(len(lista_botones)):
    #     lista_botones[i]["superficie"].fill(COLOR_AZUL)

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(lista_botones)):
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    respuesta_seleccionada = (i + 1)
                    print(f"LE DIO CLICK A LA RESPUESTA : {respuesta_seleccionada}")
                    
                    if verificar_respuesta(datos_juego,pregunta_actual,respuesta_seleccionada):
                        print("RESPUESTA CORRECTA")
                        #Ustedes van a manejar una imagen para esto
                        lista_botones[i]["superficie"].fill(COLOR_VERDE)
                        CLICK_SONIDO.play()
                    else:
                        print("RESPUESTA INCORRECTA") 
                        retorno = "terminando"
                        #Ustedes van a manejar una imagen para esto
                        lista_botones[i]["superficie"].fill(COLOR_ROJO)
                        CLICK_ERROR.play()
                    
                    indice +=1
                    
                    if indice == len(lista_preguntas):
                        indice = 0
                        mezclar_lista(lista_preguntas)
                    
                    bandera_respuesta = True


    # Cargar la imagen
    sprites = pygame.image.load(SPRITES)
    sprite_cut = pygame.Rect(0, 0, 100, 100)

    sprite_img = sprites.subsurface(sprite_cut)
    sprite_img = pygame.transform.scale_by(sprite_img, 5)
    sprite_img.set_colorkey((198,224,208))
    





    sprite = {}
    sprite["superficie"] = sprite_img
    sprite["rectangulo"] = sprite["superficie"].get_rect()
    sprite["rectangulo"].left = (ANCHO / 2) - (sprite["superficie"].get_width() / 2)
    sprite["rectangulo"].top = 0


    pantalla.blit(constantes.FONDO_JUEGO, (0, 0))

    pantalla.blit(sprite["superficie"],sprite["rectangulo"])


    mostrar_texto(caja_pregunta["superficie"],pregunta_actual["pregunta"],(20,20),FUENTE_30,COLOR_NEGRO)

    pantalla.blit(caja_pregunta["superficie"],caja_pregunta["rectangulo"])






    mostrar_texto(lista_botones[0]["superficie"],pregunta_actual["respuesta_1"],(20,20),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(lista_botones[1]["superficie"],pregunta_actual["respuesta_2"],(20,20),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(lista_botones[2]["superficie"],pregunta_actual["respuesta_3"],(20,20),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(lista_botones[3]["superficie"],pregunta_actual["respuesta_4"],(20,20),FUENTE_25,COLOR_NEGRO)
    
    for boton in lista_botones:
        pantalla.blit(boton["superficie"], boton["rectangulo"])



    # lista_botones[0]["rectangulo"] = pantalla.blit(lista_botones[0]["superficie"],(125,245))#r1
    # lista_botones[1]["rectangulo"] = pantalla.blit(lista_botones[1]["superficie"],(125,315))#r2
    # lista_botones[2]["rectangulo"] = pantalla.blit(lista_botones[2]["superficie"],(125,385))#r3

    # mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),FUENTE_25,COLOR_NEGRO)
    # mostrar_texto(pantalla,f"VIDAS: {datos_juego['vidas']}",(10,40),FUENTE_25,COLOR_NEGRO)
    




    # for evento in cola_eventos:
    #     if evento.type == pygame.QUIT:
    #         retorno = "salir"
    #     elif evento.type == pygame.MOUSEBUTTONDOWN:
    #         if boton_volver["rectangulo"].collidepoint(evento.pos):
    #             retorno = "menu"
    






    # boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],constantes.POS_BOTON_VOLVER)
    return retorno
