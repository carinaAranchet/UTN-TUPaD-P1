# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. 

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general. 

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
# lo es. 

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)
    
# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
# último nivel con un solo bloque. 
 
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
# pirámide. 

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número. 

def contar_digito_ultimo(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        contador = 1 if ultimo == digito else 0
        return contador + contar_digito_ultimo(numero // 10, digito)
    

# Programa Principal 

# numero = int(input("Ingrese un número entero positivo: ")) 
# print(f"Factoriales del 1 al {numero}:")
# for i in range(1, numero + 1):
#     print(f"{i}! = {factorial(i)}")

# posicion = int(input("Ingrese una posición para la serie de Fibonacci: "))
# print(f"Serie de Fibonacci hasta la posición {posicion}:")
# for i in range(posicion + 1):
#     print(f"F({i}) = {fibonacci(i)}")


# base = int(input("Ingrese la base: "))
# exponente = int(input("Ingrese el exponente (entero positivo): "))

# resultado = potencia(base, exponente)
# print(f"{base}^{exponente} = {resultado}")

# numero = int(input("Ingrese un numero: "))
# binario = decimal_a_binario(numero)
# print(f"El numero {numero} en binario es: {binario}")

# texto = input("Ingrese una palabra: ").lower()
# if es_palindromo(texto):
#     print(f'"{texto}" es un palíndromo.')
# else:
#     print(f'"{texto}" no es un palíndromo.')

# numero = int(input("Ingrese un numero: "))
# print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")

# nivel_base = int(input("Ingrese la cantidad de bloques: "))
# print(f"Total de bloques necesarios: {contar_bloques(nivel_base)}")

numero = int(input("Ingrese un numero: "))
digito = int(input("Ingrese el digito a contar (0-9): "))
print(f"El dígito {digito} aparece {contar_digito_ultimo(numero,digito)} veces en {numero}.")