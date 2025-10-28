print("Hola desde main!")
print("Hola desde rama2!")
"""
Hacer un código que haga las tablas de multiplicar del 1 al 10, preguntando que tabla quiere ver
"""
numero = int(input("Ingresa el numero del que quieres conocer la tabla:"))

for i in range(1,11):
    print(f"{numero} X {i} = {numero * i} ")