import pygame
import random
import json
import os
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
    space = constantes.FUENTE_POKEMON_GB.size(' ')[0]
    for i in range(len(words)+1):
        if i == (len(words)):
            lines.append({"text":line_text.strip(), "width": line_width - space})
            break
        word = words[i].upper()
        word_width, word_height = constantes.FUENTE_POKEMON_GB.size(word)
        if line_width + word_width > max_width:
            lines.append({"text":line_text.strip(), "width": line_width - space})
            line_width = word_width
            line_text = word + " "
        else:
            line_width += word_width + constantes.FUENTE_POKEMON_GB.size(' ')[0]
            line_text += word + " "
        if word_height > line_height:
            line_height = word_height
    for i in range(len(lines)):
        pos_x = (max_width - lines[i]["width"]) / 2
        pos_y = ((max_height / len(lines)) * i) + ((max_height / len(lines))/2) - (line_height/2)
        line_surface = constantes.FUENTE_POKEMON_GB.render(lines[i]["text"], False, constantes.COLOR_NEGRO)
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


# def crear_boton_generico(ruta, ancho, alto) -> dict:
def crear_boton_generico(surface, ancho, alto) -> dict:

    boton_volver = {}
    imagen_original = boton_volver["superficie"] = surface
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


def leer_json(nombre_archivo : str) -> list:
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as archivo:
            lista = json.load(archivo)
        return lista
    else:
        return []

def registrar_partida_json(jugador: Jugador, nombre_archivo: str) -> bool:
    '''
    Función que registra los datos de una partida finalizada en un archivo JSON.
    Si el archivo ya contiene datos, agrega la nueva partida sin eliminar las existentes.
    '''
    nueva_partida = generar_lista_json(jugador)

    datos = leer_json(nombre_archivo)

    # Agregamos la nueva partida a la lista de datos
    datos.append(nueva_partida)

    # Sobrescribimos el archivo con la lista actualizada
    with open(nombre_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4)

    return True

def ordenar_matrices_segun_columna_descendente(matriz : list, columna : int) -> None:
    '''
    Función que recibe una matriz y un entero que representa una de sus columnas.
    Ordena esa matriz de mayor a menor.
    '''
    flag = 1
    
    while flag:
        flag = 0
        for i in range (len(matriz) - 1):
            if  matriz[i][columna] < matriz[i + 1][columna]:
                aux = matriz[i]
                matriz[i] = matriz[i + 1]
                matriz[i + 1] = aux
                flag = 1

def mostrar_ranking(lista_ranking : list, superficie) -> None:
    '''
    Función que recibe una lista de listas con los rankings y una superficie.
    Muestra en la superficie un máximo del 10 jugadores. En caso de no haber,
    lo informa.
    '''
    if len(lista_ranking) == 0:
        mostrar_texto(superficie, "Aún no hay registros", (200, 50), constantes.FUENTE_POKEMON_GB_16, constantes.COLOR_NEGRO)
    else:
        # Definimos la posición inicial
        posicion_x = 75
        posicion_y_inicial = 100
        espacio_entre_lineas = 50  # Espacio entre cada línea

        # Dibujamos el encabezado
        mostrar_texto(superficie, "Nombre       Puntos       Fecha", (75, 50), constantes.FUENTE_POKEMON_GB_16, constantes.COLOR_NEGRO)

        for i in range(min(len(lista_ranking), 10)): # toma el rango menor, con límita máximo en 10
            # Calculamos la posición vertical actual
            posicion_y = posicion_y_inicial + i * espacio_entre_lineas

            # Dibujamos el texto correspondiente al elemento actual
            mostrar_texto(superficie, f"{i+1} - {lista_ranking[i][0]} {lista_ranking[i][1]} {lista_ranking[i][2]}", (posicion_x, posicion_y), constantes.FUENTE_POKEMON_GB_16, constantes.COLOR_NEGRO)