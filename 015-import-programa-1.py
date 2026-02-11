# Es el mismo programa que 011-casting-fails, pero con el import

from import_libreria_comun import describe


x = int(1)
y = int(3200.994123174)
z = int("341")

for variable in x, y, z:
    describe(variable)

print("=" * 40)

x = float(1)
y = float(3200.994123174)
z = float("341")

for variable in x, y, z:
    describe(variable)

print("=" * 40)

x = str(1)
y = str(3200.994123174)
z = str("341")

for variable in x, y, z:
    describe(variable)

describe("Con cien cañonens por banda viento en popa a toda vela, no corta el mar...")
describe(["Melocotón", "manzana", "plátano", "cereza", "Kiwi"])
