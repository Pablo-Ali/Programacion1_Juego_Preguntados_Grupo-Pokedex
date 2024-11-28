# Creamos la clase
class Jugador:
    # Definimos el constructor
    def __init__(self, nombre : str, vidas : int, puntos : int, volumen_musica : int, volumen_efectos : int, musica_on : bool, comodin_x2 : bool, comodin_pasar : bool) -> None:
        # Atributos
        self.nombre = nombre
        self.vidas = vidas
        self.puntos = puntos
        self.volumen_musica = volumen_musica
        self.volumen_efectos= volumen_efectos
        self.musica_on = musica_on
        self.comodin_x2 = comodin_x2
        self.comodin_pasar = comodin_pasar

    # Getters
    def get_nombre(self):
        return self.nombre    
    def get_vidas(self):
        return self.vidas
    def get_puntos(self):
        return self.puntos
    def get_volumen_musica(self):
        return self.volumen_musica
    def get_volumen_efectos(self):
        return self.volumen_efectos
    def get_musica_on(self):
        return self.musica_on
    # def get_comodin_x2(self):
    #     return self.comodin_x2
    # def get_comodin_pasar(self):
    #     return self.comodin_pasar
    
    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_vidas(self, vidas):
        self.vidas = vidas
    def set_puntos(self, puntos):
        self.puntos = puntos
    def set_volumen_musica(self, volumen_musica):
        self.volumen_musica = volumen_musica
    def set_volumen_efectos(self, volumen_efectos):
        self.volumen_efectos = volumen_efectos
    def set_musica_on(self, musica_on):
        self.musica_on = musica_on
    # def set_comodin_x2(self, comodin_x2):
    #     self.comodin_x2 = comodin_x2
    # def set_comodin_pasar(self, comodin_pasar):
    #     self.comodin_pasar = comodin_pasar

