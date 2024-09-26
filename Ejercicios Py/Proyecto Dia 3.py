ingreso_texto = "";
letra_a = "";
letra_b = "";
letra_c = "";
lista_letras = [];

print("Ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un poema, lo que quiera.")
ingreso_texto = input().lower()

print("Seleccione 3 letras para ver cuantas veces se encuentran en el texto.")
letra_a = input().lower()
letra_b = input().lower()
letra_c = input().lower()

lista_letras = [letra_a, letra_b, letra_c];

print(
    f"Primera letra: '{lista_letras[0]}' " + f"Se repite: {ingreso_texto.count(lista_letras[0])} veces. " + 
    f"Segunda letra: '{lista_letras[1]}' " + f"Se repite: {ingreso_texto.count(lista_letras[1])} veces. " + 
    f"Tercera letra: '{lista_letras[2]}' " + f"Se repite: {ingreso_texto.count(lista_letras[2])} veces."
);

text_list = list(ingreso_texto.split())
##print(text_list)

contador_palabras = len(text_list)
print(f"El texto contiene: {contador_palabras} palabras.")

primer_letra_texto = ingreso_texto[0]
ultima_letra_texto = ingreso_texto[-1]

print(f"Primera letra del texto es: {primer_letra_texto}")
print(f"Ultima letra del texto es: {primer_letra_texto}")


reverse_text = " ".join(text_list[::-1])
print(reverse_text)


boolean = "python" in ingreso_texto

dic={
    True:"La palabra python esta",
    False:"La palabra python no esta"
}

print(f"{dic[boolean]}")

if text_list.count("python") != -1 : 
    print("La palabra Python se encuentra en tu texto!")
else:
    print("Python no se encuentra en tu texto.")