import pygame
import random
import constantes

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, _ = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height+25# Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def mostrar_texto_largo_centrado( surface:pygame.Surface, text:str ):
    words = text.split(' ')
    lines = []
    max_width, max_height = surface.get_size()
    line_width, line_height = (0,0)
    line_text = ""
    space = constantes.FUENTE_24.size(' ')[0]
    for i in range(len(words)+1):
        if i == (len(words)):
            lines.append({"text":line_text.strip(), "width": line_width - space})
            break
        word = words[i].upper()
        word_width, word_height = constantes.FUENTE_24.size(word)
        if line_width + word_width > max_width:
            lines.append({"text":line_text.strip(), "width": line_width - space})
            line_width = word_width
            line_text = word + " "
        else:
            line_width += word_width + constantes.FUENTE_24.size(' ')[0]
            line_text += word + " "
        if word_height > line_height:
            line_height = word_height
    for i in range(len(lines)):
        pos_x = (max_width - lines[i]["width"]) / 2
        pos_y = ((max_height / len(lines)) * i) + ((max_height / len(lines))/2) - (line_height/2)
        line_surface = constantes.FUENTE_24.render(lines[i]["text"], False, constantes.COLOR_NEGRO)
        surface.blit(line_surface, (pos_x, pos_y))    

def mezclar_lista(lista:list) -> None:
    '''
    Función que recibe una lista y mezcla sus elementos.
    '''
    random.shuffle(lista)

def generar_flotante_musica(volumen : int) -> float:
    '''
    Función que recibe un entero y lo divide por mil
    para generar un flotante y lo retorna.
    '''
    # Generamos un flotante a partir del entero cargado en el jugador
    volumen_float = volumen / 1000 # dividimos por 1000 ya que el volumen es demasiado alto

    return volumen_float

def iniciar_musica(ruta : str, volumen : int) -> None:
    '''
    Función que recibe la ruta de una pista musical y un entero.
    Carga la musica en el mixer de pygame, establece su volumen
    y la reproduce.
    '''
    # Generamos el float del volumen
    volumen_float = generar_flotante_musica(volumen)
    #Cargamos la pista musical
    pygame.mixer.music.load(ruta)
    # Seteamos el volumen
    pygame.mixer.music.set_volume(volumen_float)
    # La reproducimos en bucle
    pygame.mixer.music.play(-1)

def cambiar_volumen_musica(volumen : int) -> None:
    '''
    Función que permite modificar el volumen de la música
    a partir de un entero pasado por parámetro.
    '''
    volumen_float = generar_flotante_musica(volumen)
    pygame.mixer.music.set_volume(volumen_float)

def crear_boton_volver() -> dict:
    boton_volver = {}
    imagen_original = boton_volver["superficie"] = pygame.image.load(constantes.RUTA_IMAGEN_BOTON_VOLVER)
    boton_volver["superficie"] = pygame.transform.scale(imagen_original, (108, 108)) # 20%
    boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()

    return boton_volver

def mutear():
    pass

def verificar_respuesta(datos_juego:dict,pregunta_actual:dict,respuesta:int) -> bool:
    if pregunta_actual["respuesta_correcta"] == respuesta:
        datos_juego["puntuacion"] += constantes.PUNTUACION_ACIERTO
        retorno = True
    else:
        #SIN PUNTOS NEGATIVOS
        if datos_juego["puntuacion"] > constantes.PUNTUACION_ERROR:
            datos_juego["puntuacion"] -= constantes.PUNTUACION_ERROR
        
        #CON PUNTOS NEGATIVOS
        #datos_juego["puntuacion"] -= PUNTUACION_ERROR
        datos_juego["vidas"] -= 1
        retorno = False
    
    return retorno