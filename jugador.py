# Creamos la clase
class Jugador:
    # Definimos el constructor
    def __init__(self, nombre : str, vidas : int, puntos : int, comodin_x2 : bool, comodin_pasar : bool) -> None:
        # Atributos
        self.nombre = nombre
        self.vidas = vidas
        self.puntos = puntos
        self.comodin_x2 = comodin_x2
        self.comodin_pasar = comodin_pasar

    # Getters
    def get_nombre(self):
        return self.nombre    
    def get_vidas(self):
        return self.vidas
    def get_puntos(self):
        return self.puntos
    def get_comodin_x2(self):
        return self.comodin_x2
    def get_comodin_pasar(self):
        return self.comodin_pasar
    
    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_vidas(self, vidas):
        self.vidas = vidas
    def set_puntos(self, puntos):
        self.puntos = puntos
    def set_comodin_x2(self, comodin_x2):
        self.comodin_x2 = comodin_x2
    def set_comodin_pasar(self, comodin_pasar):
        self.comodin_pasar = comodin_pasar

