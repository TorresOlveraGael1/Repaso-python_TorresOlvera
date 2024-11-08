# Punto 4

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Recibimos una lista de notas del usuario

notas = list(map(float, input("Introduce las notas separadas por espacio: ").split()))

#Encontramos la nota más baja y la más alta

nota_baja = min(notas)

nota_alta = max(notas)

#Imprimimos los resultados

print("La nota más baja es:", nota_baja)

print("La nota más alta es:", nota_alta)
