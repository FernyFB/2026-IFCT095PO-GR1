lista_basica = [3, 7, 99, "patata"]
print(lista_basica)


tupla_basica = 3, 7, 99, "Melón"
# tupla_basica = (3, 7, 99, "Melón") -- Paréntesis opcional
print(tupla_basica)

# podemos acceder a cada elemento a traves de su índice
print(lista_basica[2])


# A la lista podemo añadirle elementos
lista_basica.append("cebolla")
print(lista_basica)
# Y quitarle

elemento = lista_basica.pop(0)
print(lista_basica)

# La tupla fallará al intentar añadir mas elementos
# Esto fallaria:
"""
tupla_basica.append("cebolla")
"""

# podemos acceder a cada elemento a traves de su índice
print(lista_basica[2])
