# Punto 9

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Recibimos la lista como entrada del usuario

entrada = input("Introduce una lista de elementos separados por comas: ")

#Convertimos la entrada en una lista usando split

lista = entrada.split(',')

#Usamos un bucle for para imprimir cada elemento de la lista

for elemento in lista:

    print(elemento)
