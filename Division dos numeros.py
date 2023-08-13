# Programa general de division

# Literal a: Si la division es exacta
# Literal b: Si se trata de un cociente Par o Impar
# Literal c: Si el cociente es impar, mostrar cual es el residuo

print("Calculo de la division de dos numeros")

# Definicion de variables

num1 = 0
num2 = 0

num1 = float(input("Ingrese el valor del primer numero: "))
num2 = float(input("Ingrese el valor del segundo numero: "))

if num2 != 0:    
    #Literal a: Si la division es exacta
    if num1 % num2 == 0:
        print("La division es exacta porque el residuo es: ", num1 % num2)
    else:
        print("La division no es exacta porque el residuo es: ", num1 % num2)
    # Literal b: Si se trata de un cociente Par o Impar
    if (num1 / num2) % 2 == 0:
        print("El cociente {} es par".format(num1/num2))
    else:
    # Literal c: Si el cociente es impar, mostrar cual es el residuo
        print("El cociente {} es impar".format(num1/num2))
else:
    print("La ejecución termina porque el divisor es igual a 0")

# Literal d: Comparar numero 1 y numero 2 con un tercer numero

num3 = float(input("Ingrese el valor del tercer numero: "))

#Forma dificil

"""if num1 > num2:
    if num1 > num3:
        print("El numero 1 es el mayor de los tres numeros")
    else:
        print("El numero 3 es el mayor de los tres numeros")
elif num2 > num1:
    if num2 > num3:
        print("El numero 2 es el mayor de los tres numeros")
    else:
        print("El numero 3 es el mayor de los tres numeros")"""

#Forma facil

if num1 > num2 and num1 > num3:
    print("El numero 1 es el mayor de los tres numeros")
elif num2 > num1 and num2 > num3:
    print("El numero 2 es el mayor de los tres numeros")
else:
    print("El numero 3 es el mayor de los tres numeros")
