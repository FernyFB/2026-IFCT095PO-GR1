# lista: accedemos por valor y por índice
"""
lista = [
    0 - rojo
    1 - verde
    2 - azul
]
"""

lista = ["rojo", "verde", "azul"]

for color in lista:
    print(color)
print()

# accedemos al valor (contenido) por su índice
for i in range(len(lista)):
    print(lista[i])
print()


# Los diccionarios, en vez de índice tienen una LLAVE (key, value)
diccionario = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": lista[0],
    "year": 2004        # Solo se guarda el ultimo valor

}
diccionario["color"] = "cyan" # Solo se guarda el ultimo valor


# Al igual que las listas, los diccionarios son iterables
for llave in diccionario:
    print(llave.ljust(14), diccionario[llave])


variable = "Citröen"
anyos_citroen = [1993, 1995, 2001]

coche = {
    "brand": variable,
    "model": "C3",
    "year": anyos_citroen,
    "color": lista[1],
}

print(coche)


camion = {
    "brand": "Mercedes",
    "model": "C3",
    "year": 2000,
    "motor": {
        "cilindrada": [10000, 150000],
        "potencia": [2500, 3500]
    },
}


lista_de_listas = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
]

lista_de_listas_de_listas = [
    [
        [0, 1],
        [2, 3]
    ],
    [
        [4, 5],
        [6, 7]
    ]
]
