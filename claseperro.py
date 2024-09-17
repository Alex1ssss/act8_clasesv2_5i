print("Clase version 2 el constructor")
class perro:
    # funcion constructor
    def __init__(self, color, edad):
        self.color=color
        self.edad=edad
    # funciones creadas por el usuario
    def morder(self):
        print("Chale el perro me mordio")
    def chatperro(mensaje):
        print(f"chat perro: {mensaje}")
    def chatperra(mensajep):
        print(f"chat perra: {mensajep}")
    def datos(self):
        print(f"color: {self.color}")
        print(f"edad: {self.edad}")
#llamadas a funciones
chihuas=perro("negro",2)
#llamada a funcion
chihuas.datos()
chihuas.morder()