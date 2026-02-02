def introducir_coche():
    print("Introduce los datos de tu coche")
    modelo = input("Modelo: ")
    anyo = input("Año: ")
    color = input("color: ")

    return {
      "modelo": modelo,
      "anyo": anyo,
      "color": color
    }


ferry = []
for i in range(3):
    coche = introducir_coche()
    ferry.append(coche)

print("=" * 80)

print(ferry)
