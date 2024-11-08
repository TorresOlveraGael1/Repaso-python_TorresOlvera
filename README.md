# Repaso-python_TorresOlvera

Torres Olvera Gael

Repaso de python

# Punto 1

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Variable que almacena la edad
edad = int(input("Introduce tu edad: "))

#Comprobamos si la edad es mayor o igual a 18
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("NO eres mayor de edad.")

![image](https://github.com/user-attachments/assets/3627fd02-335c-41e9-9fb0-e273b4d97323)
![image](https://github.com/user-attachments/assets/825b49bb-7f4a-4cb3-83bf-8cc52102bcfe)

# Punto 2

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Variable que almacena la nota

nota = float(input("Introduce tu nota: "))

#Comprobamos el rango de la nota y asignamos el equivalente

if 0 <= nota < 5:

    print("SUSPENSO")

elif 5 <= nota < 6:

    print("SUFICIENTE")

elif 6 <= nota < 7:

    print("BIEN")

elif 7 <= nota < 9:

    print("NOTABLE")

elif 9 <= nota <= 10:

    print("SOBRESALIENTE")

else:

    print("NOTA NO VÁLIDA")

![image](https://github.com/user-attachments/assets/b95ca70b-8b57-409e-bfc7-2a9993f9dbcb)
![image](https://github.com/user-attachments/assets/929bc221-8725-4e35-b3f6-40027705001b)

# Punto 3

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Variables que almacenan el nombre y el apellido

nombre = input("Introduce tu nombre: ")

apellido = input("Introduce tu apellido: ")

#Comprobamos las condiciones

if nombre == "Daniel":

    if apellido == "Ramos":

        print("Nombre y apellido correctos.")

    else:

        print("Apellido incorrecto.")

else:
    
    print("Usuario desconocido.")

![image](https://github.com/user-attachments/assets/9830c167-1ad1-48e8-a4ea-e5df3762feab)
![image](https://github.com/user-attachments/assets/d8efd260-6a16-430e-b8fa-de71660103a7)

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

![image](https://github.com/user-attachments/assets/032f5f4a-cfee-4381-9748-51ab4c7b53e0)
![image](https://github.com/user-attachments/assets/f6725580-540a-44fa-9de0-cfcd76a6834f)

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

![image](https://github.com/user-attachments/assets/e7eb890f-3b14-4d67-8aa6-b2257d4a2449)
![image](https://github.com/user-attachments/assets/9fa11301-9ca3-45a4-892b-bc2532bf5af1)

# Punto 6

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Recibimos una lista de nombre y apellidos del usuario

nombre_apellidos = input("Introduce tu nombre y dos apellidos separados por espacios: ").split()

#Imprimimos los dos apellidos utilizando índices

#El primer apellido está en el índice 1, y el segundo apellido en el índice 2

print("Primer apellido:", nombre_apellidos[1])
print("Segundo apellido:", nombre_apellidos[2])

![image](https://github.com/user-attachments/assets/0960fe7f-7da5-475f-a446-1e18df5c70a9)
![image](https://github.com/user-attachments/assets/0239a074-508d-4dfd-aab6-2365a1403014)


# Punto 7

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Sumar los números pares desde el 2 hasta el 100 (inclusive)

suma = sum(range(2, 101, 2))

#Imprimir el resultado

print("La suma de los números pares desde el 2 hasta el 100 es:", suma)

![image](https://github.com/user-attachments/assets/84e8f749-5011-40a4-92a0-135549b19628)
![image](https://github.com/user-attachments/assets/8a082241-4910-42c7-ad35-f433ae23778d)

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

![image](https://github.com/user-attachments/assets/0c43a337-5c48-4969-9421-f21c0995428c)
![image](https://github.com/user-attachments/assets/90b30e14-f13d-48e1-b2f7-35bfafa2a9bb)

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

![image](https://github.com/user-attachments/assets/72437746-529e-4376-9f01-71d13e2e83c5)
![image](https://github.com/user-attachments/assets/94214efd-67c5-4f96-82c7-3eb4bd1be257)

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

![image](https://github.com/user-attachments/assets/0eb7ea3b-c2de-486e-8708-f14128a4b30c)
![image](https://github.com/user-attachments/assets/97914b5f-21cf-405e-862b-7282e5c7b825)

# Punto 11

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Recibimos una cadena de texto del usuario

cadena = input("Introduce una cadena de texto: ")

#Usamos un bucle for para imprimir cada carácter de la cadena

for caracter in cadena:
    
    print(caracter)

![image](https://github.com/user-attachments/assets/e56ebfc4-03f3-456b-b969-49f13f4e414c)
![image](https://github.com/user-attachments/assets/915ba0fd-82c6-4d3b-aef3-4e92b0963915)
![image](https://github.com/user-attachments/assets/186ef537-3ecd-4ba6-8ae4-9faac28d243e)

# Punto 12

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Parte ascendente del dibujo

for i in range(1, 6):

    print('*' * i)

#Parte descendente del dibujo

for i in range(4, 0, -1):

    print('*' * i)

![image](https://github.com/user-attachments/assets/bdc380ea-3c18-4f5b-930c-fbf8c35fe3e8)
![image](https://github.com/user-attachments/assets/ee59ab99-6ff4-48d2-beed-1bb5cbc9692f)
