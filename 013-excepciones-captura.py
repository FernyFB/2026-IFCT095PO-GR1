a = 12
b = "This is an exceptional error"
b = 2
try:
    c = a + b
    c = 1 / 0
except TypeError:
    print("TypeError: No son del tipo adecuado")
    print(f"type: {type(a)} a: {a}")
    print(f"type: {type(b)} b: {b}")
except ZeroDivisionError:
    print("Denominador es 0")



for i in range(5):
    print("*")

raise TypeError("Final, se fuerza error por motivos didácticos")
print("Esta linea no se ejecutará")
