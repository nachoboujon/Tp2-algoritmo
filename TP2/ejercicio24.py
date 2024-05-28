class Personaje:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas

def posicion_personajes(pila, personaje1, personaje2):
    posicion_rocket = None
    posicion_groot = None
    contador = 1

    for personaje in pila:
        if personaje.nombre == personaje1:
            posicion_rocket = contador
        elif personaje.nombre == personaje2:
            posicion_groot = contador
        
        contador += 1
    
    return posicion_rocket, posicion_groot

def personajes_mas_de_5_peliculas(pila):
    personajes_mas_cinco = []

    for personaje in pila:
        if personaje.peliculas > 5:
            personajes_mas_cinco.append((personaje.nombre, personaje.peliculas))
    
    return personajes_mas_cinco

def peliculas_de_black_widow(pila):
    for personaje in pila:
        if personaje.nombre == "Viuda Negra":
            return personaje.peliculas
    return 0

def personajes_con_letras(pila, letras):
    personajes_letras = []

    for personaje in pila:
        if personaje.nombre[0] in letras:
            personajes_letras.append(personaje.nombre)
    
    return personajes_letras

pila_personajes = [
    Personaje("Iron Man", 8),
    Personaje("Capitán América", 6),
    Personaje("Viuda Negra", 7),
    Personaje("Hulk", 4),
    Personaje("Thor", 6),
    Personaje("Hawkeye", 5),
    Personaje("Rocket Raccoon", 4),
    Personaje("Groot", 3),
    Personaje("Doctor Strange", 3),
    Personaje("Spider-Man", 4)
]

# A
posicion_rocket, posicion_groot = posicion_personajes(pila_personajes, "Rocket Raccoon", "Groot")
print("Posición de Rocket Raccoon:", posicion_rocket)
print("Posición de Groot:", posicion_groot)

# B
print("Personajes que participaron en más de 5 películas:")
print(personajes_mas_de_5_peliculas(pila_personajes))

# C
print("Número de películas en las que participó Viuda Negra:", peliculas_de_black_widow(pila_personajes))

# D
print("Personajes cuyos nombres empiezan con C, D y G:")
print(personajes_con_letras(pila_personajes, ['C', 'D', 'G']))
