# Es el mismo programa que 012-listas-playground, pero con el import

from import_libreria_comun import describe

mi_lista = ["Melocotón", "manzana", "plátano", "cereza", "Kiwi"]

describe(mi_lista)


print("=" * 40)
print("La lista tiene " + str(len(mi_lista)) + " elementos")
#             v v
print(mi_lista[0])
print(mi_lista[2])
print(mi_lista[1])
#             ^ ^

print("*" * 40)
for fruta in mi_lista:
    print(fruta)

print("·" * 40)
for mi_lista in mi_lista:
    print(mi_lista[0])

print("=" * 40)

# This will return the items from position 2 to 5.
# Remember that the first item is position 0,
# and note that the item in position 5 is NOT included
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "banana", "banana", "cherry", "orange", "kiwi",
            "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#                           v              [
#                           3              6
thislist = ["a", "b", "c", "d", "e", "f", "g"]
thislist[3:6] = ["azul", "rojo"]
print(thislist)
