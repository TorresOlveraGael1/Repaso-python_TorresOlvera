# Punto 8

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Almacenamos el número en una variable

numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

#Imprimimos la tabla de multiplicar utilizando un rango

for i in range(1, 11):  # El rango va de 1 a 10

    resultado = numero * i

    print(f"{numero} x {i} = {resultado}")
