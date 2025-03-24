# Declarando variables 

edad = 19
altura = 1.81
import math

# Numero 4 Calcula el area de un triangulo
base = int(input ('Enter base: '))
height = int(input ('Enter height: '))
area = int (0.5 * base * height)
print ('the area of the triangle is:', area)

# Numero 5 Calcula el perimetro de un triangulo

lado_1 = int(input('Ingresa el lado 1 del triangulo: '))
lado_2= int(input('Ingresa el lado 2 del triangulo: '))
lado_3 = int(input('Ingresa el lado 3 del triangulo: '))
perimetro = int(lado_1 + lado_2 + lado_3)
print('El perimetro de el triangulo es: ', perimetro)

# Numero 6 Calcula el area y perimetro de un rectangulo

largo = int(input('Ingresa cuanto es el largo del rectangulo: '))
ancho = int(input('Ingresa cuanto es el ancho del rectangulo: '))

area = int(largo * ancho)
print('El area del rectangulo es: ', area)

perimetro = int(2 * (largo + ancho))
print('El perimetro del rectangulo es: ', perimetro)

# Numero 7 El area y circunferencia de un circulo

pi = 3.14
radio = int(input('Ingresa el valor de el radio de un circulo: '))

area = int(pi * radio * radio)
print('el area de el circulo es: ', area)

circunferencia = int(2 * pi * radio)
print('La circunferencia es de: ', circunferencia)

# EJERCICIO 8
# z = 2q - 2    q = x z = y
q1, z1, q2,z2 = 1, 0, 0, -2
FirstSlope = (z2 - z1) / (q2  - q1)
print("The slope is    ", FirstSlope)

#EJERCICIO 9
x1,y1,x2,y2 = 2,2,6,10
Second_Slope = (y2 - y1) / (x2 - x1)
print("The slope is" , Second_Slope)
euclidean_Distance = math.sqrt((x2 - x1) **2 + (y2-y1) ** 2)
print("La distancia Eucladiana es  ", euclidean_Distance)

# EJERCICIO 10
if (FirstSlope == Second_Slope):
    print("It is the same")
else: print("It is not the same, YOU ARE WRONG!")

# EJERCICIO 11
print("Evaluando la función y = x^2 + 6x + 9")
for x in range(-10, 11):  # Prueba con valores de x entre -10 y 10
    y = x**2 + 6*x + 9
    print(f"x = {x} -> y = {y}")
    if y == 0:
        print(f"Encontrado: y es 0 cuando x = {x}")



# EJERCICIO 12
word1 = len("Python")
word2 = len("dragon")
if (word1 != word2):
    print("It is a diferent length")
else: "It is the same length"

# EJERCICIO 13
print('on' in 'python' and 'on' in 'dragon')  # Output: True


# EJERCICIO 14
print("jargon" in "I hope this course is not full of jargon")

# EJERCICIO 15
print("no" in "dragon" and "no" in "Python")

# EJERCICIO 16
pythonLen = len("Python")
print(float(pythonLen))
print(int(pythonLen))

# EJERCICIO 17
number = float(input("Put a number"))
reminder = number % 2
if (reminder == 0):
    print("The number is divisible for 2") 
else: print("The number is not divisible for 2")

# EJERCICIO 18
floorDivision = 7 / 3
if floorDivision == int(2.7):
    print("It is not equal   ")
else: print("It is equal   ")

# EJERCICIO 19
# Definir valores
a = '10'  # Cadena
b = 10    # Entero
# Comparar tipos
result = type(a) == type(b)
# Mostrar resultado
print("¿El tipo de '10' es igual al tipo de 10?:", result)

# EJERCICIO 20
if "9.8" == 10:
    print(True)
else: False

# EJERCICIO 21
hours = float(input("¿Cuántas horas trabajas?"))
perHour = float(input("¿Cuánto te pagan por hora?"))
weeklyEarning = hours * perHour
print("Tu salario es de $  ", weeklyEarning)

# EJERCICIO 22
while True:
    try:
        yearsLived = int(input("¿Cuántos años tienes? (entre 0 y 100): "))
        if 0 <= yearsLived <= 100:
            break
        else:
            print("Ingresa un número entre 0 y 100.")
    except ValueError:
        print("Error: Ingresa un número entero.")
secondsInYourLife = yearsLived * 3153600000 
print("Has vivido por", secondsInYourLife, "segundos")

# EJERCICIO 23
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
