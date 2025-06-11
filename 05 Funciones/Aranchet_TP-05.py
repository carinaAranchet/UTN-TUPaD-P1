import math # utilizo la libreria para el ejecicio 4, donde necesito el valor de PI

#1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

#2) Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

#3)Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio): 
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5)Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

# 6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la fun5ción.

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# 7) Crear una función llamada operaciones_basicas(a, b) que recibados números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

# 8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#  resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
#imprimir_hola_mundo()

# nombre_ingresado = input("Ingresá tu nombre: ")
# saludo = saludar_usuario(nombre_ingresado)
# print(saludo)

# nombre = input("Ingresá tu nombre: ")
# apellido = input("Ingresá tu apellido: ")
# edad = input("Ingresá tu edad: ")
# residencia = input("¿Dónde vivís?: ")

# informacion_personal(nombre, apellido, edad, residencia)

# radio = float(input("Ingresá el radio del círculo: "))
    
# area = calcular_area_circulo(radio)
# perimetro = calcular_perimetro_circulo(radio)

# print(f" Área: {area:.2f}")
# print(f" Perímetro: {perimetro:.2f}")

# segundos = float(input("Ingresá la cantidad de segundos: "))
# horas = segundos_a_horas(segundos)
# print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# numero = int(input("Ingresá un número para ver su tabla de multiplicar: "))
# tabla_multiplicar(numero)

# a = float(input("Ingresá el primer número: "))
# b = float(input("Ingresá el segundo número: "))

# resultados = operaciones_basicas(a, b)

# print("Resultados de las operaciones:")
# print(f"Suma: {resultados[0]}")
# print(f"Resta: {resultados[1]}")
# print(f"Multiplicación: {resultados[2]}")
# print(f"División: {resultados[3]}")


# peso = float(input("peso: "))
# altura = float(input("altura: "))

# imc = calcular_imc(peso, altura)
# print(f"Tu IMC es: {imc:.2f}")


# temp_celsius = float(input("Ingresá la temperatura en grados Celsius: "))
# temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
# print(f"{temp_celsius:.1f} °C equivalen a {temp_fahrenheit:.1f} °F.")

num1 = float(input("primer número: "))
num2 = float(input("segundo número: "))
num3 = float(input("tercer número: "))

promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de los tres números es: {promedio:.2f}")