from random import *

# lista inicial 
palitos = ['-','--','---','----']
# mezclar palitos 
def mezclar(lista):
    shuffle(lista)
    return lista

# pedirle intento
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)
# Comprobar intento 
def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("Te toco el 8")
    else:
        print("Te has salvado ")
    
    print(f"Te ha tocado {lista[intento-1]}")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)



# Práctica sobre Interacción entre Funciones 1
# Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

# La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

# Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

# Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

# Si la suma es menor o igual a 6:

# "La suma de tus dados es {suma_dados}. Lamentable"

# Si la suma es mayor a 6 y menor a 10:

# "La suma de tus dados es {suma_dados}. Tienes buenas chances"

# Si la suma es mayor o igual a 10:

# "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

# Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.

def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)

    return dado1, dado2

dados = lanzar_dados()

def evaluar_jugada(valores):
    suma_dados = sum(valores)
    
    if suma_dados <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable.")
    elif suma_dados > 6 and suma_dados < 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else: 
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

print(evaluar_jugada(dados))

# Práctica sobre Interacción entre Funciones 2
# Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.

# Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

# Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.


def reducir_lista(lista):
    lista_reducida = list(set(lista))
    lista_reducida.pop(-1)
    return lista_reducida

def promedio(lista_redu):
    suma_valores = sum(lista_redu)
    cantidad_valores = len(lista_redu)

    promedio_lista = suma_valores / cantidad_valores

    return promedio_lista



lista_numeros = [20, 30, 20, 10, 12, 13, 12, 8, 6, 7, 8]

lista_reducida = reducir_lista(lista_numeros)

print(promedio(lista_reducida))



# Práctica sobre Interacción entre Funciones 3
# Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

# Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).

# Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

# Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

# Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.


def lanzar_moneda():
    moneda = ["Cara", "Cruz"]
    lado_moneda = choice(moneda)
    return lado_moneda;


def probar_suerte(moneda, lista):
    print(moneda)

    if moneda == "Cara":
        print("La lista se autodestruira")
        lista = []
    elif moneda == "Cruz":
        print("La lista fue salvada")
    
    return lista

lista_numeros = [20, 30, 40, 50]

cara_cruz = lanzar_moneda()

print(probar_suerte(cara_cruz, lista_numeros))



####################################################################

def mi_funcion( *args):
    return sum(args)

resultado = mi_funcion(1,2,40,50)
print(resultado)


# Práctica sobre Argumentos Indefinidos (*args) 1
# Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.



# Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).

def suma_cuadrados(*args):
    valores = list(args)
    lista = []
    
    for n in valores:
        pontencia = n**2
        lista.append(pontencia)

    suma = sum(lista)

    return suma;


print(suma_cuadrados(1,2,3))

# Práctica sobre Argumentos Indefinidos (*args) 2
# Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).


def suma_absolutos(*args):
    lista_valores = list(args)
    suma = 0

    for n in lista_valores:
        suma += abs(n)

    return suma;

print(suma_absolutos(-10,-20,30))

# Práctica sobre Argumentos Indefinidos (*args) 3
# Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

# La función debe devolver el siguiente mensaje:

# "{nombre}, la suma de tus números es {suma_numeros}"

def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    print(f"{nombre}, la suma de tus numeros es {suma_numeros}")

print(numeros_persona("Matias", 20,20,30,30))

#############################################################################
def suma  (**kwargs):
    total = 0
    for clave,valor  in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor

    return total



print(suma(a=1,b=2,c=3))


def test(num1,num2,*args,**kwargs):

    print(f"el primer valor es {num1}")
    print(f"el segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")
    

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [100,200,300,400]


test(20,10,100,200,300,400,a=1,b=2,c=3)


# Práctica sobre Argumentos Indefinidos (**kwargs) 1
# Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.

def cantidad_atributos(**kwargs):
    return len(kwargs)

print(cantidad_atributos(nombre="Matias", edad=22, ciudad="Villa Carlos Paz"))


# Práctica sobre Argumentos Indefinidos (**kwargs) 2
# Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.

def lista_atributos(**kwargs):
    return list(kwargs.values())

print(lista_atributos(nombre="Matias", edad=22, ciudad="Villa Carlos Paz"))

# Práctica sobre Argumentos Indefinidos (**kwargs) 3
# Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

# Características de {nombre}:
# {nombre_argumento}: {valor_argumento}
# {nombre_argumento}: {valor_argumento}
# etc...
# Por ejemplo:

# describir_persona("María", color_ojos="azules", color_pelo="rubio")

# Mostrará en pantalla:

# Características de María:
# color_ojos: azules
# color_pelo: rubio

def describir_persona(nombre, **kwargs):
    print(f"Caracteristicas de {nombre}")

    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

    
describir_persona("María", color_ojos="azules", color_pelo="rubio", altura="1.65m", edad=30)


