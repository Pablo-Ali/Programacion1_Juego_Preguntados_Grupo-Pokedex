# Creamos la clase
class Jugador:
    # Definimos el constructor
    def __init__(self, nombre, vidas, puntos) -> None:
        # Atributos
        self.nombre = nombre
        self.vidas = vidas
        self.puntos = puntos

    # Getters
    def get_nombre(self):
        return self.nombre    
    def get_vidas(self):
        return self.vidas
    def get_puntos(self):
        return self.puntos
    
    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_(self, vidas):
        self.vidas = vidas
    def set_(self, puntos):
        self.puntos = puntos

