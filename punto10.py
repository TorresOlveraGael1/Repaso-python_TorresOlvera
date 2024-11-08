# Punto 10

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Recibimos la lista como entrada del usuario

entrada = input("Introduce una lista de elementos separados por comas: ")

#Convertimos la entrada en una lista usando split

lista = entrada.split(',')

#Usamos un bucle while para imprimir cada elemento de la lista

i = 0  #Inicializamos el índice

while i < len(lista):

    print(lista[i])  #Imprime el elemento en el índice i

    i += 1  #Incrementamos el índice para pasar al siguiente elemento
