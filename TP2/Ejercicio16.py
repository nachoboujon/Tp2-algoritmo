def interseccion_pilas(pila1, pila2):
    set_pila1 = set(pila1)
    set_pila2 = set(pila2)
    interseccion = set_pila1.intersection(set_pila2)
    return list(interseccion)

pila_episodio_v = ["Luke Skywalker", "Princess Leia", "Han Solo", "Darth Vader", "Yoda"]
pila_episodio_vii = ["Rey", "Finn", "Kylo Ren", "Han Solo", "Princess Leia"]

personajes_interseccion = interseccion_pilas(pila_episodio_v, pila_episodio_vii)

print("Personajes que aparecen en ambos episodios:")
for personaje in personajes_interseccion:
    print(personaje)
