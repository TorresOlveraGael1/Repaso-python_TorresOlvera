# Punto 5

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Recibimos una lista de frutas del usuario

frutas = input("Introduce una lista de frutas separadas por comas: ").split(',')

#Limpiamos los espacios en blanco que pudieran existir alrededor de cada fruta

frutas = [fruta.strip() for fruta in frutas]

#Comprobamos si 'cereza' está en la lista

if "cereza" in frutas:

    print("Cereza SÍ está en la lista.")

else:

    print("Cereza NO está en la lista.")
