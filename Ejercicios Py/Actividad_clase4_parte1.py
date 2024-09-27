""" mi_bool = 5 >= 6
print(mi_bool)

mi_bool = 5 != 6
print(mi_bool)

mi_bool = 10 == 2*5
print(mi_bool)

mi_bool = 5 < 6
print(mi_bool)
 """

# Práctica Operadores de Comparación 1
# Crea dos variables (num1 y  num2) con los valores 36 y 17 respectivamente. Verifica si num1 es mayor o igual que num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool

num1 = 36
num2 = 21

mi_bool = num1 >= num2;
print(f"36 es igual o mayor a 21?: {mi_bool}")


# Práctica Operadores de Comparación 2
# Crea dos variables (num1 y  num2):

# Dentro de num1, almacena el resultado de la operación raíz cuadrada de 25

# Dentro de num2, almacena el número 5.

# Verifica si num1 es igual a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.

num1 = 25 ** 0.5
num2 = 5

mi_bool = num1 == num2
print(f"raiz de 25 es igual a 5?: {mi_bool}")

# Práctica Operadores de Comparación 3
# Crea dos variables (num1 y  num2):

# Dentro de num1, almacena el resultado de la operación 64 x 3

# Dentro de num2, almacena el resultado de la operación 24 x 8

# Verifica si num1 es diferente a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.

num1= 64 *3
num2 =24 * 8
mi_bool=num2!=num1
print(mi_bool)

#--------------------------------------------------------------------------------------------------------------------------

a = 6 > 5
b = 30 == 15*3

mi_bool = a and b
print(mi_bool)

mi_bool = a or b
print(mi_bool)

mi_bool = not a
print(mi_bool)

# Práctica Operadores Lógicos 1
# Crea tres variables (num1 ,  num2 y num3):

# Dentro de num1, almacena el valor 36

# Dentro de num2, almacena el resultado de la operación 72/2

# Dentro de num3, almacena el valor 48

# Verifica si num1 es mayor que num2, y menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.


num1=36
num2=72/2
num3=48

mi_bool = num1 > num2 and num1 < num3;
print(mi_bool)

# Práctica Operadores Lógicos 2
# Crea tres variables (num1 ,  num2 y num3):

# Dentro de num1, almacena el valor 36

# Dentro de num2, almacena el resultado de la operación 72/2

# Dentro de num3, almacena el valor 48

# Verifica si num1 es mayor que num2, o menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.

num1=36
num2=72/2
num3=48

mi_bool = num1 > num2 or num1 < num3
print(mi_bool) 

# Práctica Operadores Lógicos 3
# Verifica si las palabras almacenadas en las siguientes variables:

# palabra1 = "éxito", y

# palabra2 = "tecnología"

# no se encuentran en la frase a continuación, y almacena el resultado de esta comprobación (un booleano) en una variable llamada mi_bool:

# "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"

# Elon Musk

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool = palabra1 in frase and palabra2 in frase;
print(mi_bool)
#----------------------------------------------------------------------------------------------------------------------------


animal=input("ingrese que tipo de mascota tiene en casa (gato, perro, conejo) : ")

if animal=='gato':
    print("Usted tiene un gato")
elif animal=='perro':
    print("Usted tiene un perro")
elif animal=='conejo':
    print("Usted tiene un conejo")
else:
    print("No se que mascota tiene. ")



# Práctica Control de Flujo 1
# Utilizando las variables num1 y num2, que se alimentan con el input del usuario (tal como en el código ya proporcionado):

# Crea una estructura de control de flujo que compare los valores de las variables, y arroje un resultado de acuerdo al caso:

# "num1 es mayor que num2"

# "num2 es mayor que num1"

# "num1 y num2 son iguales"

# Debes mostrar en pantalla el valor de las variables ingresadas en lugar de num1 y num2.

# Aclaración:

# 1. No deben imprimirse strings adicionales a la respuesta del usuario.

# 2. Los ejercicios que contienen el la función input() deben ser probados con el botón: "Ejecutar pruebas".  Ya que el botón "Ecutar código" arrojará el siguiente error: "EOF when reading a line".

num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
elif num1 == num2:
    print(f"Los valores ingresados son iguales: {num1}")


# Práctica Control de Flujo 2
# Las leyes de un país establecen que un adulto puede conducir si tiene licencia para hacerlo, y para optar por una licencia para conducir, debe de tener 18 años o más.

# Crea una estructura condicional para verificar si una persona de 16 años sin licencia puede conducir, y muestra el resultado que corresponda en pantalla:

# "Puedes conducir"

# "No puedes conducir aún. Debes tener 18 años y contar con una licencia"

# "No puedes conducir. Necesitas contar con una licencia"

# Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones.

edad = int(input("Ingresa tu edad: "))
tiene_licencia = True

if edad < 18:
    tiene_licencia = False;

if tiene_licencia == True and edad >= 18:
    print("Puedes conducir")
elif edad < 18 and tiene_licencia == False:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
elif tiene_licencia == False and edad >= 18:
    print("No puedes conducir. Necesitas contar con una licencia")



# Práctica Control de Flujo 3
# Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz de programar en Python y tener conocimientos de inglés.

# Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:

# "Cumples con los requisitos para postularte"

# "Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

# "Para postularte, necesitas tener conocimientos de inglés"

# "Para postularte, necesitas saber programar en Python"

# Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones. Evalúa a un candidato que sabe inglés, pero no programa en Python.

habla_ingles = True
sabe_python = False

"Cumples con los requisitos para postularte"

"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

"Para postularte, necesitas tener conocimientos de inglés"

"Para postularte, necesitas saber programar en Python"


if habla_ingles == True and sabe_python == True:
    print("Cumples con los requisitos para postularte")
elif habla_ingles == True and sabe_python == False:
    print("Para postularte, necesitas saber programar en Python")
elif habla_ingles == False and sabe_python == True:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif habla_ingles == False and sabe_python == False:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")