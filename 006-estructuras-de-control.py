# Ejemplo de if
"""
print("EMPEZAMOS")

dinero = 100
articulo = 36

tenemos_bastante = dinero > articulo
print(type(tenemos_bastante))


# if True:
if False:
    print("lo compro")
else:
    print("Nos vamos a casa")

print("FIN")
"""

# Ejemplo de while

## Contar hasta 10

min = 1
max = 10
posicion = min

print(posicion)
while posicion < max:
    posicion = posicion + 1
    print(posicion)
print(">>", posicion, "<<")

## Cuenta atras de un cohete

### Solución

min = 1
max = 10
posicion = max

print(posicion)
while posicion >= min:
    posicion = posicion - 1
    print(posicion)
print(">>", posicion, "<<")

### Mejor alternativa:
