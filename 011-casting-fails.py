def describe(variable):
    print("-" * 30)
    print(type(variable))
    print(variable)

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