""" La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir
algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
para adivinar cuál crees que es el número”. """

from random import *

##Variables
nombre = "";
numero = 0;
choice = ""
seguir_jugando = True

nombre = input("Hola! vamos a jugar un juego! ¿Cual es tu nombre? ")

##While para que corta el juego si no quiere seguir jugando al terminar una partida.
while seguir_jugando == True:
    ##Numero aleatorio y setear intentos en 0.
    numero_aleatorio = randint(1,100);
    intentos = 0;

    print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar, (perderas un intento si tu número es mayor a 100 o menor a 1) ¿cuál crees que es el número?")
    
    ##while para cuando no adivino el juego luego de 8 intentos, cada vuelta aumenta 1 intento.
    while intentos < 8:
        numero = int(input("Introduce un número: "))
        intentos = intentos+1;

        if numero < 1 or numero > 100:
            print(f"El número que seleccionaste es menor a 1 o mayor a 100, Ojo.  Intentos: {intentos}")
        elif numero == numero_aleatorio:
            print(f"Acertaste el número! El número era: {numero_aleatorio}. Lo lograste en {intentos} intentos!");
            break
        elif numero > numero_aleatorio:
            print(f"Tu número es mayor al que estoy pensando!  Intentos: {intentos}")
        elif numero < numero_aleatorio:
            print(f"Tu número es menor al que estoy pensando!  Intentos: {intentos}")

    if intentos == 8 and numero != numero_aleatorio:
        print(f"Agotaste tus intentos, el número correcto era: {numero_aleatorio}")


    ##Verificar si quiere seguir jugando, si pone "S" seguir_jugando pasa a true y vuelve a arrancar el juego, si pone "N" seguir_jugando pasa a false y termina el juego.
    while True:
        choice = input("¿Desea seguir jugando? S/N ").upper()
        if choice in ["S", "N"]:
            if choice == "S":
                print("Usted desea continuar!")
                seguir_jugando = True
                break
            elif choice == "N":
                print("Gracias por jugar! Hasta luego!")
                seguir_jugando = False
                break
        else:
            print("Entrada no válida, selecciona 'S' o 'N' ")


