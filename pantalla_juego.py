import pygame
import constantes 
from funciones_generales import *
from preguntas import *
from jugador import Jugador

pregunta = {}
pregunta["superficie"] = pygame.image.load(constantes.CAJA_PREGUNTA)
pregunta["rectangulo"] = pregunta["superficie"].get_rect()
pregunta["rectangulo"].left = 1
pregunta["rectangulo"].top = constantes.ALTO - pregunta["superficie"].get_height() - 10

lista_botones = []
for i in range(4):
    boton = {}
    boton["superficie"] = pygame.image.load(constantes.BOTON_LARGE)
    boton["superficie_hover"] = pygame.image.load(constantes.BOTON_LARGE_HOVER)
    boton["hover"] = False
    boton["superficie_correcta"] = pygame.image.load(constantes.BOTON_LARGE_GREEN)
    boton["superficie_incorrecta"] = pygame.image.load(constantes.BOTON_LARGE_RED)
    boton["correct"] = False
    boton["rectangulo"] = boton["superficie"].get_rect()
    boton["rectangulo"].left = 1 + pregunta["superficie"].get_width() + 4 +  ((i//2) * (boton["superficie"].get_width() + 4 ))
    boton["rectangulo"].top = (constantes.ALTO - pregunta["superficie"].get_height() - 10) + ((i%2) * (boton["superficie"].get_height() + 4))
    boton["caption"] = ""
    lista_botones.append(boton)

sprite = {}
sprite["fullsprite"] = pygame.image.load(constantes.SPRITES)
sprite["fullsprite"] = pygame.transform.scale_by(sprite["fullsprite"], 5)
sprite["superficie"] = ""
sprite["rectangulo"] = pygame.Rect((constantes.ANCHO / 2)-250 , 50, 500, 500)

lista_intentos = []
for i in range(constantes.CANTIDAD_VIDAS):
    intento = {}
    intento["superficie"] = pygame.image.load(constantes.ICON_PATH)
    intento["superficie"] = pygame.transform.scale_by(intento["superficie"], .1)
    intento["rectangulo"] = intento["superficie"].get_rect()
    intento["rectangulo"].left = 10 + ((intento["superficie"].get_width() + 5) * i)
    intento["rectangulo"].top = 50
    intento["show"] = True
    lista_intentos.append(intento)

mezclar_lista(lista_preguntas)

indice = 0 #Todo dato inmutable en la funcion que muestra esa ventana, lo tengo que definir como global
bandera_respuesta = False #Todo dato inmutable en la funcion que muestra esa ventana, lo tengo que definir como global

def mostrar_juego( pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event], jugador:Jugador) -> str:
    global indice
    global bandera_respuesta

    retorno = "juego"
    
    # Control de Eventos
    pregunta_actual = lista_preguntas[indice]
    
    if bandera_respuesta:
        pygame.time.delay(500)
        bandera_respuesta = False

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEMOTION:
            for i in range(len(lista_botones)):
                lista_botones[i]["hover"] = False
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    lista_botones[i]["hover"] = True  
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(lista_botones)):
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    respuesta_seleccionada = (i + 1)
                    if verificar_respuesta( jugador, pregunta_actual, respuesta_seleccionada ):
                        print("RESPUESTA CORRECTA")
                        reproducir_efecto_sonido(constantes.SELECT_OK_SOUND, jugador.get_volumen_efectos())
                    else:
                        print("RESPUESTA INCORRECTA") 
                        # retorno = "terminado"
                        reproducir_efecto_sonido(constantes.SELECT_FAIL_SOUND, jugador.get_volumen_efectos())
                        if jugador.get_vidas() == 0:
                            retorno = "terminado"
                    indice +=1
                    
                    if indice == len(lista_preguntas):
                        indice = 0
                        # mezclar_lista(lista_preguntas)
                    
                    bandera_respuesta = True

    # Actualizar
    sprite_posx = ((pregunta_actual["id"]-1)%12)*500
    sprite_posy = ((pregunta_actual["id"]-1)//12)*500
    sprite_cut = pygame.Rect(sprite_posx, sprite_posy, 500, 500)
    sprite["superficie"] = sprite["fullsprite"].subsurface(sprite_cut)

    if (not sprite_posy % 200 and not sprite_posx % 200) or (sprite_posy % 200 and sprite_posx % 200):
        sprite["superficie"].set_colorkey((255,0,0))
    else:
        sprite["superficie"].set_colorkey((0,255,0))

    for i in range(len(lista_intentos)):
        intento = lista_intentos[i]
        intento["show"] = True
        if i+1 > jugador.get_vidas():
            intento["show"] = False

    for i in range(len(lista_botones)):
        boton = lista_botones[i]
        boton["correct"] = False
        if i+1 == pregunta_actual["respuesta_correcta"]:
            boton["correct"] = True
        match i:
            case 0:
                boton["caption"] = pregunta_actual["respuesta_1"].upper()
            case 1:
                boton["caption"] = pregunta_actual["respuesta_2"].upper()
            case 2:
                boton["caption"] = pregunta_actual["respuesta_3"].upper()
            case 3:
                boton["caption"] = pregunta_actual["respuesta_4"].upper()

    # Dibujar
    pantalla.blit(constantes.FONDO_JUEGO, (0, 0))
    
    intentos_caption = constantes.FUENTE_24.render("intentos:".upper(), True, constantes.COLOR_NEGRO)
    pantalla.blit(intentos_caption, (10,10))  
    for intento in lista_intentos:
        if intento["show"]:
            pantalla.blit(intento["superficie"], intento["rectangulo"])

    pantalla.blit(sprite["superficie"], sprite["rectangulo"])

    pantalla.blit(pregunta["superficie"],pregunta["rectangulo"])
    mostrar_texto_largo_centrado(pregunta["superficie"],pregunta_actual["pregunta"].upper())

    for boton in lista_botones:
        if bandera_respuesta:
            if boton["correct"]:
                pantalla.blit(boton["superficie_correcta"], boton["rectangulo"])
            else:
                pantalla.blit(boton["superficie_incorrecta"], boton["rectangulo"])
        else:
            if boton["hover"]:
                pantalla.blit(boton["superficie_hover"], boton["rectangulo"])
            else:
                pantalla.blit(boton["superficie"], boton["rectangulo"])
        text_render = constantes.FUENTE_24.render(boton["caption"], True, constantes.COLOR_NEGRO)
        text_rect = text_render.get_rect(center=boton["rectangulo"].center)
        pantalla.blit(text_render, text_rect)  

    # Bye
    return retorno