# Creamos la clase
class Jugador:
    # Definimos el constructor
    def __init__(self, nombre, vidas, puntos, dificultad) -> None:
        # Atributos
        self.nombre = nombre
        self.vidas = vidas
        self.puntos = puntos
        self.dificultad = dificultad

    # Getters
    def get_nombre(self):
        return self.nombre    
    def get_vidas(self):
        return self.vidas
    def get_puntos(self):
        return self.puntos
    def get_dificultad(self):
        return self.dificultad
    
    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_vidas(self, vidas):
        self.vidas = vidas
    def set_puntos(self, puntos):
        self.puntos = puntos
    def set_dificultad(self, dificultad):
        self.dificultad = dificultad

