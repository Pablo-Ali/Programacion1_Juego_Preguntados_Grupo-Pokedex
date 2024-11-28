import pygame
import constantes 
import funciones_generales 
import jugador

# ###################################################################################################
# boton_volver = funciones_generales.crear_boton_generico(constantes.RUTA_IMAGEN_BOTON_VOLVER, 108, 108)  # BOTÓN VOLVER
# ###################################################################################################

lista_preguntas = []
with open(constantes.PREGUNTAS_PATH, mode="r", encoding="utf-8") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        line = lines[i]
        if i == 0:
            campos = line.split(';')
        else:
            valores = line.split(';')
            registro = {}
            for j in range(len(campos)):
                if valores[j].rstrip().isnumeric():
                    registro[campos[j].rstrip()] = int(valores[j])
                else:
                    registro[campos[j].rstrip()] = valores[j]
            lista_preguntas.append(registro)

funciones_generales.mezclar_lista(lista_preguntas)

class Pregunta:
    def __init__(self, x:int, y:int ):
        self.superficie = constantes.CAJA_PREGUNTA
        self.rect = self.superficie.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.caption = ""
    def dibujar(self, superficie):
        superficie.blit(self.superficie, self.rect)
        funciones_generales.mostrar_texto_largo_centrado(self.superficie, self.caption)

pregunta = Pregunta(1, constantes.ALTO - constantes.CAJA_PREGUNTA_ALTO - 10)

class BotonJugar:
    def __init__(self, x:int, y:int):
        self.superficie = constantes.BOTON_JUEGO_SUP
        self.superficie_hover = constantes.BOTON_JUEGO_SUP_HOVER
        self.superficie_correcta = constantes.BOTON_JUEGO_SUP_CORRECT
        self.superficie_incorrecta = constantes.BOTON_JUEGO_SUP_INCORRECT
        self.caption = ""
        self.rect = pygame.Rect(0, 0, constantes.BOTON_JUEGO_ANCHO, constantes.BOTON_JUEGO_ALTO)
        self.rect.left = x
        self.rect.top = y
        self.hover = False
        self.correct = False
    def dibujar(self, superficie:pygame.Surface, bandera_respuesta:bool):
        if bandera_respuesta:
            if self.correct:
                superficie.blit(self.superficie_correcta, self.rect)
            else:
                superficie.blit(self.superficie_incorrecta, self.rect)
        else:
            if self.hover:
                superficie.blit(self.superficie_hover, self.rect)
            else:
                superficie.blit(self.superficie, self.rect)
        texto_renderizado = constantes.FUENTE_POKEMON_GB.render(self.caption, True, constantes.COLOR_NEGRO)
        texto_rect = texto_renderizado.get_rect(center=self.rect.center)
        superficie.blit(texto_renderizado, texto_rect)

lista_botones = []
for i in range(4):
    boton_x = 1 + constantes.CAJA_PREGUNTA_ANCHO + 4 +  ((i//2) * (constantes.BOTON_JUEGO_ANCHO + 4 ))
    boton_y = (constantes.ALTO - constantes.CAJA_PREGUNTA_ALTO - 10) + ((i%2) * (constantes.BOTON_JUEGO_ALTO + 4))
    boton = BotonJugar(boton_x, boton_y)
    lista_botones.append(boton)

class Sprite:
    def __init__(self, x:int, y:int):
        self.fullsprite = pygame.transform.scale_by(constantes.SPRITES, 5) 
        self.rect = pygame.Rect(x, y, 500, 500)
        self.img_id = 0
    def dibujar(self, superficie:pygame.Surface):
        sprite_posx = ((self.img_id-1)%12)*500
        sprite_posy = ((self.img_id-1)//12)*500
        sprite_cut = pygame.Rect(sprite_posx, sprite_posy, 500, 500)
        sprite_surface = self.fullsprite.subsurface(sprite_cut)
        if (not sprite_posy % 200 and not sprite_posx % 200) or (sprite_posy % 200 and sprite_posx % 200):
            sprite_surface.set_colorkey((255,0,0))
        else:
            sprite_surface.set_colorkey((0,255,0))
        superficie.blit(sprite_surface, self.rect)

sprite = Sprite((constantes.ANCHO / 2)-250 , 50)

class Intentos:
    def __init__(self, x:int, y:int):
        self.caption = "intentos:".upper()
        self.cantidad = constantes.CANTIDAD_VIDAS
        self.surface = pygame.transform.scale_by(constantes.ICON_PATH, .1) 
        self.pos_x = x
        self.pos_y = y 
    def dibujar(self, superficie:pygame.Surface):
        caption_render = constantes.FUENTE_POKEMON_GB.render(self.caption, True, constantes.COLOR_NEGRO)  
        fix_pos_y = constantes.ALTO - constantes.CAJA_PREGUNTA_ALTO - caption_render.get_height() - self.surface.get_height() - self.pos_y - 10
        superficie.blit(caption_render, (self.pos_x, fix_pos_y))
        for i in range(self.cantidad):
            surface_rect = self.surface.get_rect()
            surface_rect.left = self.pos_x + ((self.surface.get_width() + 5) * i)
            surface_rect.top = fix_pos_y + caption_render.get_height() + 5
            superficie.blit(self.surface, surface_rect)                

intentos = Intentos(10,10)

class Puntaje:
    def __init__(self, x:int, y:int):
        self.caption = "puntaje:".upper()
        self.puntos = 0
        self.pos_x = x
        self.pos_y = y 
    def dibujar(self, superficie:pygame.Surface):
        caption_render = constantes.FUENTE_POKEMON_GB.render(self.caption, True, constantes.COLOR_NEGRO)  
        caption_render_rect = caption_render.get_rect()
        caption_render_rect.right = self.pos_x
        caption_render_rect.top = self.pos_y
        superficie.blit(caption_render, caption_render_rect)
        caption_render_score = constantes.FUENTE_POKEMON_GB.render(f"{self.puntos:08}", True, constantes.COLOR_NEGRO)
        caption_render_score_rect = caption_render_score.get_rect()
        caption_render_score_rect.right = self.pos_x
        caption_render_score_rect.top = self.pos_y + caption_render.get_height() + 5
        superficie.blit(caption_render_score, caption_render_score_rect)

puntaje = Puntaje(constantes.ANCHO - 10, 10)

class Tiempo:
    def __init__(self, x:int, y:int):
        self.caption = "Tiempo".upper()
        self.tiempo_de_inicio = 0
        self.tiempo_de_inicio_seteado = False
        self.tiempo_inicial = constantes.TIEMPO_INICIAL
        self.tiempo_restante = self.tiempo_inicial
        self.pos_x = x
        self.pos_y = y
        self.tiempo_incremenetado = 0 
    def setear_tiempo(self, tiempo_de_inicio:int):
        if not self.tiempo_de_inicio_seteado:
            self.tiempo_de_inicio = tiempo_de_inicio
            self.tiempo_de_inicio_seteado = True
            self.tiempo_restante = self.tiempo_inicial
            self.tiempo_incremenetado = 0
    def verificar_fin_tiempo(self)->bool:
        if self.tiempo_restante <= 0:
            self.tiempo_de_inicio_seteado = False
            return True
        return False
    def limpiar_tiempo(self):
        self.tiempo_de_inicio = 0
        self.tiempo_de_inicio_seteado = False
        self.tiempo_restante = self.tiempo_inicial
        self.tiempo_incremenetado = 0
    def incrementar_tiempo(self):
        self.tiempo_incremenetado += constantes.TIEMPO_INCREMENTO
    def dibujar(self, superficie:pygame.Surface):
        caption_render = constantes.FUENTE_POKEMON_GB.render(self.caption, True, constantes.COLOR_NEGRO)  
        caption_render_rect = caption_render.get_rect()
        caption_render_rect.left = self.pos_x
        caption_render_rect.top = self.pos_y
        superficie.blit(caption_render, caption_render_rect)
        tiempo_transcurrido = (pygame.time.get_ticks() - self.tiempo_de_inicio) / 1000
        self.tiempo_restante = (self.tiempo_inicial + self.tiempo_incremenetado )- round(tiempo_transcurrido)
        caption_render_tiempo_restante = constantes.FUENTE_POKEMON_GB.render(f"{self.tiempo_restante:06}", True, constantes.COLOR_NEGRO)
        caption_render_tiempo_restante_rect = caption_render_tiempo_restante.get_rect()
        caption_render_tiempo_restante_rect.left = self.pos_x
        caption_render_tiempo_restante_rect.top = self.pos_y + caption_render.get_height() + 5
        superficie.blit(caption_render_tiempo_restante, caption_render_tiempo_restante_rect)

tiempo = Tiempo(10,10)

class Comodin:
    def __init__(self, x:int, y:int, tipo_comodin:int):
        if tipo_comodin == constantes.BOTON_TIPO_COMODIN_X2:
            self.superficie = constantes.BOTON_COMODIN_X2
            self.superficie_hover = constantes.BOTON_COMODIN_X2_HOVER
            self.superficie_activado = constantes.BOTON_COMODIN_X2_ACTIVADO
            self.superficie_anulado = constantes.BOTON_COMODIN_X2_ANULADO
        elif tipo_comodin == constantes.BOTON_TIPO_COMODIN_NEXT:
            self.superficie = constantes.BOTON_COMODIN_NEXT
            self.superficie_hover = constantes.BOTON_COMODIN_NEXT_HOVER
            self.superficie_activado = constantes.BOTON_COMODIN_NEXT_ACTIVADO
            self.superficie_anulado = constantes.BOTON_COMODIN_NEXT_ANULADO
        else:
            return TypeError
        self.hover = False
        self.estado = constantes.BOTON_COMODIN_ESTADO_EN_ESPERA
        self.pos_x = x
        self.pos_y = y
        self.rect = self.superficie.get_rect()
    def dibujar(self, superficie:pygame.Surface):
        self.rect.left = self.pos_x
        self.rect.top = self.pos_y
        if self.estado == constantes.BOTON_COMODIN_ESTADO_EN_ESPERA:
            if self.hover:
                superficie.blit(self.superficie_hover, self.rect)
            else:
                superficie.blit(self.superficie, self.rect)
        elif self.estado == constantes.BOTON_COMODIN_ESTADO_ACTIVADO:
            superficie.blit(self.superficie_activado, self.rect)
        elif self.estado == constantes.BOTON_COMODIN_ESTADO_ANULADO:
            superficie.blit(self.superficie_anulado, self.rect)
                
comodin_next = Comodin(constantes.ANCHO - constantes.BOTON_COMODIN_ANCHO - 1, constantes.ALTO - constantes.CAJA_PREGUNTA_ALTO - constantes.BOTON_COMODIN_ALTO - 14, constantes.BOTON_TIPO_COMODIN_NEXT)
comodin_X2 = Comodin(constantes.ANCHO - (constantes.BOTON_COMODIN_ANCHO * 2) - 5, constantes.ALTO - constantes.CAJA_PREGUNTA_ALTO - constantes.BOTON_COMODIN_ALTO - 14, constantes.BOTON_TIPO_COMODIN_X2)

indice = 0 #Todo dato inmutable en la funcion que muestra esa ventana, lo tengo que definir como global
contador_correctas = 0
bandera_respuesta = False #Todo dato inmutable en la funcion que muestra esa ventana, lo tengo que definir como global

def mostrar_juego( pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event], jugador:jugador.Jugador ) -> str:
    global indice
    global bandera_respuesta
    global contador_correctas

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
                boton = lista_botones[i]
                boton.hover = False
                if boton.rect.collidepoint(evento.pos):
                    boton.hover = True
            
            comodin_next.hover = False
            if comodin_next.rect.collidepoint(evento.pos):
                comodin_next.hover = True
                
            comodin_X2.hover = False
            if comodin_X2.rect.collidepoint(evento.pos):
                comodin_X2.hover = True                
                
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(lista_botones)):
                boton = lista_botones[i]
                if boton.rect.collidepoint(evento.pos):
                    respuesta_seleccionada = (i + 1)
                    multiplicador = 2 if comodin_X2.estado == constantes.BOTON_COMODIN_ESTADO_ACTIVADO else 1
                    if funciones_generales.verificar_respuesta( jugador, pregunta_actual, respuesta_seleccionada, multiplicador ):
                        # print("RESPUESTA CORRECTA")
                        funciones_generales.reproducir_efecto_sonido(constantes.SELECT_OK_SOUND, jugador.get_volumen_efectos())
                        contador_correctas += 1
                        if contador_correctas == 5:
                            tiempo.incrementar_tiempo()
                            if jugador.get_vidas() < constantes.CANTIDAD_VIDAS_MAX:
                                 jugador.set_vidas(jugador.get_vidas() + 1)
                            contador_correctas = 0
                    else:
                        # print("RESPUESTA INCORRECTA") 
                        funciones_generales.reproducir_efecto_sonido(constantes.SELECT_FAIL_SOUND, jugador.get_volumen_efectos())
                        contador_correctas = 0
                        if jugador.get_vidas() == 0:
                            tiempo.limpiar_tiempo()
                            comodin_next.estado = constantes.BOTON_COMODIN_ESTADO_EN_ESPERA
                            comodin_X2.estado = constantes.BOTON_COMODIN_ESTADO_EN_ESPERA
                            funciones_generales.mezclar_lista(lista_preguntas)
                            retorno = "terminado"

                    if comodin_X2.estado == constantes.BOTON_COMODIN_ESTADO_ACTIVADO:
                        comodin_X2.estado = constantes.BOTON_COMODIN_ESTADO_ANULADO    

                    indice +=1

                    if indice == len(lista_preguntas):
                        indice = 0
                        # mezclar_lista(lista_preguntas)

                    bandera_respuesta = True
            
            if comodin_next.rect.collidepoint(evento.pos):
                if comodin_next.estado == constantes.BOTON_COMODIN_ESTADO_EN_ESPERA:
                    indice +=1
                    if indice == len(lista_preguntas):
                        indice = 0
                    comodin_next.estado = constantes.BOTON_COMODIN_ESTADO_ANULADO
            if comodin_X2.rect.collidepoint(evento.pos):
                if comodin_X2.estado == constantes.BOTON_COMODIN_ESTADO_EN_ESPERA:
                    comodin_X2.estado = constantes.BOTON_COMODIN_ESTADO_ACTIVADO
                elif comodin_X2.estado == constantes.BOTON_COMODIN_ESTADO_ACTIVADO:
                    comodin_X2.estado = constantes.BOTON_COMODIN_ESTADO_EN_ESPERA                    



    #     elif evento.type == pygame.MOUSEBUTTONDOWN: ### BOTÓN VOLVER ###################
    #         if boton_volver["rectangulo"].collidepoint(evento.pos): ### BOTÓN VOLVER ###
    #             retorno = "menu" ### BOTÓN VOLVER ######################################
   
    # Actualizar
    sprite.img_id = pregunta_actual["img_id"]

    tiempo.setear_tiempo(pygame.time.get_ticks())
    if tiempo.verificar_fin_tiempo():
        comodin_X2.estado = constantes.BOTON_COMODIN_ESTADO_EN_ESPERA
        comodin_next.estado = constantes.BOTON_COMODIN_ESTADO_EN_ESPERA
        contador_correctas = 0
        funciones_generales.mezclar_lista(lista_preguntas)
        retorno = "terminado"
    
    intentos.cantidad = jugador.get_vidas()

    puntaje.puntos = jugador.get_puntos()

    pregunta.caption = pregunta_actual["pregunta"]
    for i in range(len(lista_botones)):
        boton = lista_botones[i]
        boton.correct = True if i+1 == pregunta_actual["respuesta_correcta"] else False
        match i:
            case 0:
                boton.caption = pregunta_actual["respuesta_1"].upper()
            case 1:
                boton.caption = pregunta_actual["respuesta_2"].upper()
            case 2:
                boton.caption  = pregunta_actual["respuesta_3"].upper()
            case 3:
                boton.caption  = pregunta_actual["respuesta_4"].upper()


    # Dibujar
    pantalla.blit(constantes.FONDO_JUEGO, (0, 0))

    sprite.dibujar(pantalla)

    tiempo.dibujar(pantalla)

    puntaje.dibujar(pantalla)

    intentos.dibujar(pantalla)

    comodin_next.dibujar(pantalla)

    comodin_X2.dibujar(pantalla)

    pregunta.dibujar(pantalla)

    for boton in lista_botones:
        boton.dibujar(pantalla, bandera_respuesta)

    # #################################################################################################################
    # boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],constantes.POS_BOTON_VOLVER) # BOTÓN VOLVER
    # ##################################################################################################################

    # Bye
    return retorno