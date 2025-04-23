name = str(input("Ingrese el nombre del usuario: "))
name1 = str(input("Ingrese el nombre del segundo usuario: "))

age = int(input("Ingrese la edad del usuario: "))
age1 = int(input("Ingrese la edad del segundo usuario: "))

if age > age1:
    print(f"{name} es mayor")
elif age1 > age:
    print(f"{name1} es mayor")
else:
    print("Tienen la misma edad")

if age >= 18:
    print(f"{name} es mayor de edad")
else:
    print(f"{name} es menor de edad ")

if age1 >= 18:
    print(f"{name1} es mayor de edad")
else:
    print(f"{name1} es menor de edad ")