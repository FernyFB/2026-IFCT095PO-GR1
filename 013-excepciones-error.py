a = 10
b = 0

try:
    b = int(input("Indroduce un num: "))
except ValueError:
    print("Debe ser un número")


print(a + b)
