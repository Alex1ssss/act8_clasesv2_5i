class informacion:

    def mi_lista(self):
        lista_nomperros=["body", "dollar", "fany"]
        for x in lista_nomperros:
            print(x)
    def mi_diccionario(self):
        carros = {
            "marca": "Ford",
            "modelo": "Mustang",
            "año": 1964
        }
        for x, z in carros.items():
            print(x,z)
    def mi_conjunto(self):
        lista_nomcomidas=["burrito", "tacos", "tortas"]
        for x in lista_nomcomidas:
            print(x)

    def mi_tupla(self):
        lista_nomcolores=("rojo", "negro", "blanco")
        for x in lista_nomcolores:
            print(x)

# creando el objeto
datos=informacion()
print("")
print("--LISTA--")
datos.mi_lista()
print("")
print("--DICCIONARIO--")
datos.mi_diccionario()
print("")
print("--CONJUNTO--")
datos.mi_conjunto()
print("")
print("--TUPLA--")
datos.mi_tupla()