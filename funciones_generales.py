import pygame
import random
import json
import constantes
from jugador import Jugador
from datetime import datetime


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

def reproducir_efecto_sonido(ruta : str, volumen : int) -> None:
    '''
    Función que recibe la ruta de un efecto de sonido y un entero.
    Carga el sonido en el mixer de pygame, establece su volumen
    y lo reproduce.
    '''
    # Generamos el float del volumen
    volumen_float = generar_flotante_musica(volumen)
    #Cargamos la pista musical
    efecto_sonido = pygame.mixer.Sound(ruta)
    # Seteamos el volumen
    efecto_sonido.set_volume(volumen_float)
    # La reproducimos una sola vez
    efecto_sonido.play()

def cambiar_volumen_musica(volumen : int) -> None:
    '''
    Función que permite modificar el volumen de la música
    a partir de un entero pasado por parámetro.
    '''
    volumen_float = generar_flotante_musica(volumen)
    pygame.mixer.music.set_volume(volumen_float)

def crear_boton_generico(ruta, ancho, alto) -> dict:
    boton_volver = {}
    imagen_original = boton_volver["superficie"] = pygame.image.load(ruta)
    boton_volver["superficie"] = pygame.transform.scale(imagen_original, (ancho, alto))
    boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()

    return boton_volver

def generar_fecha() -> str:
    '''
    Función que toma la fecha actual y la retorna
    como una cadena formateada como DD/MM/YYYY
    '''
    # Obtén la fecha actual
    fecha_actual = datetime.now()

    # Formateo
    fecha_formateada = fecha_actual.strftime("%d/%m/%Y")

    return fecha_formateada


def verificar_respuesta(jugador:Jugador,pregunta_actual:dict,respuesta:int) -> bool:
    if pregunta_actual["respuesta_correcta"] == respuesta:
        jugador.set_puntos(jugador.get_puntos() + constantes.PUNTUACION_ACIERTO)
        retorno = True
    else:
        #SIN PUNTOS NEGATIVOS
        if jugador.get_puntos() > constantes.PUNTUACION_ERROR:
            jugador.set_puntos(jugador.get_puntos() - constantes.PUNTUACION_ERROR)
        
        #CON PUNTOS NEGATIVOS
        #datos_juego["puntuacion"] -= PUNTUACION_ERROR
        jugador.set_vidas(jugador.get_vidas() - 1)
        retorno = False
    
    return retorno

def generar_lista_json(jugador : Jugador) -> list:
    '''
    Función que recibe una instancia de la clase Jugador
    y genera una lista con los datos a guardar en el registro
    de partidas finalizadas. Retorna la lista.
    '''
    fecha = generar_fecha()
    nombre = jugador.get_nombre()
    puntos = jugador.get_puntos()
    
    return [nombre, puntos, fecha]


def registrar_partida_json(jugador: Jugador, nombre_archivo: str) -> bool:
    '''
    Función que registra los datos de una partida finalizada en un archivo JSON.
    Si el archivo ya contiene datos, agrega la nueva partida sin eliminar las existentes.
    '''
    nueva_partida = generar_lista_json(jugador)

    try:
        # Intentamos leer los datos existentes
        with open(nombre_archivo, "r") as archivo:
            datos = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si no existe o está vacío, inicializamos una lista vacía
        datos = []

    # Agregamos la nueva partida a la lista de datos
    datos.append(nueva_partida)

    # Sobrescribimos el archivo con la lista actualizada
    with open(nombre_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4)

    return True