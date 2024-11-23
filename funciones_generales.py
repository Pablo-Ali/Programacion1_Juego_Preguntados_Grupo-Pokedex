import pygame
import random


def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
    
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

