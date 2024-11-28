import pygame
import constantes
import funciones_generales

pygame.init()

boton_volver = funciones_generales.crear_boton_generico(constantes.RUTA_IMAGEN_BOTON_VOLVER, 108, 108)
tabla = funciones_generales.crear_boton_generico(constantes.CAJA_PREGUNTA, 700, 600)

def mostrar_rankings(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event]) -> str:
    pygame.display.set_caption("¿Quién es ese Pokémon?")
    
    retorno = "rankings"

    # ordenamos el archivo json
    lista_ranking = funciones_generales.leer_json("prueba")

    #ordenamos la lista
    funciones_generales.ordenar_matrices_segun_columna_descendente(lista_ranking, 1)

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                retorno = "menu"

    pantalla.blit(constantes.FONDO_RANKINGS, (0, 0))

    # generamos en pantalla el botón de volver
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],constantes.POS_BOTON_VOLVER)

    # Dibjar los carteles en cada iteración para evitar superposición
    pantalla.blit(tabla["superficie"], (25, 25))

        # Limpiar la superficie de la tabla
    tabla["superficie"].blit(tabla["superficie"], (0, 0))
    
    # imprimimos el ranking
    funciones_generales.mostrar_ranking(lista_ranking, tabla["superficie"])

    # Actualizar pantalla principal
    pygame.display.flip()

    return retorno
