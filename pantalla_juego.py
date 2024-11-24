import pygame
from constantes import *
from funciones_generales import *
from preguntas import *

caja_pregunta = {}
caja_pregunta["superficie"] = pygame.image.load(CAJA_PREGUNTA)
caja_pregunta["rectangulo"] = caja_pregunta["superficie"].get_rect()
caja_pregunta["rectangulo"].left = 1
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
#mezclar_lista(lista_preguntas)
bandera_respuesta = False #Todo dato inmutable en la funcion que muestra esa ventana, lo tengo que definir como global

def mostrar_juego(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
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
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(lista_botones)):
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    respuesta_seleccionada = (i + 1)

                    # print(f"LE DIO CLICK A LA RESPUESTA : {respuesta_seleccionada}")
                    
                    if verificar_respuesta(datos_juego,pregunta_actual,respuesta_seleccionada):
                        print("RESPUESTA CORRECTA")
                        #Ustedes van a manejar una imagen para esto
                        # lista_botones[i]["superficie"].fill(COLOR_VERDE)
                        # CLICK_SONIDO.play()
                    else:
                        print("RESPUESTA INCORRECTA") 
                        # retorno = "terminando"
                        #Ustedes van a manejar una imagen para esto
                        # lista_botones[i]["superficie"].fill(COLOR_ROJO)
                        # CLICK_ERROR.play()
                    
                    indice +=1
                    
                    if indice == len(lista_preguntas):
                        indice = 0
                        # mezclar_lista(lista_preguntas)
                    
                    bandera_respuesta = True

    # Actualizar
    sprites = pygame.image.load(SPRITES)
    sprite_posx = ((pregunta_actual["id"]-1)%12)*100
    sprite_posy = ((pregunta_actual["id"]-1)//12)*100
    sprite_cut = pygame.Rect(sprite_posx, sprite_posy, 100, 100)
    sprite_img = sprites.subsurface(sprite_cut)
    sprite_img = pygame.transform.scale_by(sprite_img, 5)

    if (not sprite_posy % 200 and not sprite_posx % 200) or (sprite_posy % 200 and sprite_posx % 200):
        sprite_img.set_colorkey((255,0,0))
       
        
    else:
        sprite_img.set_colorkey((0,255,0))
        
        
    
    sprite = {}
    sprite["superficie"] = sprite_img
    sprite["rectangulo"] = sprite["superficie"].get_rect()
    sprite["rectangulo"].left = (ANCHO / 2) - (sprite["superficie"].get_width() / 2)
    sprite["rectangulo"].top = 50

    pregunta_actual_render = FUENTE_24.render(pregunta_actual["pregunta"], True, COLOR_NEGRO)
    pregunta_actual_render_rect = pregunta_actual_render.get_rect()
    pregunta_actual_render_rect.center = (caja_pregunta["rectangulo"].left + (caja_pregunta["superficie"].get_width()/2), caja_pregunta["rectangulo"].top + (caja_pregunta["superficie"].get_height()/2) ) 

    respuesta_01_render = FUENTE_24.render(pregunta_actual["respuesta_1"].upper(), True, COLOR_NEGRO)
    respuesta_01_render_rect = respuesta_01_render.get_rect()
    respuesta_01_render_rect.center = (lista_botones[0]["rectangulo"].left + (lista_botones[0]["superficie"].get_width()/2), lista_botones[0]["rectangulo"].top + (lista_botones[0]["superficie"].get_height()/2) )

    respuesta_02_render = FUENTE_24.render(pregunta_actual["respuesta_2"].upper(), True, COLOR_NEGRO)
    respuesta_02_render_rect = respuesta_02_render.get_rect()
    respuesta_02_render_rect.center = (lista_botones[1]["rectangulo"].left + (lista_botones[1]["superficie"].get_width()/2), lista_botones[1]["rectangulo"].top + (lista_botones[1]["superficie"].get_height()/2) )


    respuesta_03_render = FUENTE_24.render(pregunta_actual["respuesta_3"].upper(), True, COLOR_NEGRO)
    respuesta_03_render_rect = respuesta_03_render.get_rect()
    respuesta_03_render_rect.center = (lista_botones[2]["rectangulo"].left + (lista_botones[2]["superficie"].get_width()/2), lista_botones[2]["rectangulo"].top + (lista_botones[2]["superficie"].get_height()/2) )

    respuesta_04_render = FUENTE_24.render(pregunta_actual["respuesta_4"].upper(), True, COLOR_NEGRO)
    respuesta_04_render_rect = respuesta_04_render.get_rect()
    respuesta_04_render_rect.center = (lista_botones[3]["rectangulo"].left + (lista_botones[3]["superficie"].get_width()/2), lista_botones[3]["rectangulo"].top + (lista_botones[3]["superficie"].get_height()/2) )

    # Dibujar
    pantalla.blit(constantes.FONDO_JUEGO, (0, 0))

    pantalla.blit(sprite["superficie"], sprite["rectangulo"])

    pantalla.blit(caja_pregunta["superficie"],caja_pregunta["rectangulo"])
    pantalla.blit(pregunta_actual_render, pregunta_actual_render_rect )

    pantalla.blit(lista_botones[0]["superficie"],lista_botones[0]["rectangulo"])
    pantalla.blit(respuesta_01_render, respuesta_01_render_rect)

    pantalla.blit(lista_botones[1]["superficie"],lista_botones[1]["rectangulo"])
    pantalla.blit(respuesta_02_render,respuesta_02_render_rect)

    pantalla.blit(lista_botones[2]["superficie"],lista_botones[2]["rectangulo"])
    pantalla.blit(respuesta_03_render,respuesta_03_render_rect)

    pantalla.blit(lista_botones[3]["superficie"],lista_botones[3]["rectangulo"])
    pantalla.blit(respuesta_04_render,respuesta_04_render_rect)

    # Bye
    return retorno
