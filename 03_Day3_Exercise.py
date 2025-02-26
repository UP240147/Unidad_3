# Declarando variables 

edad = 19
altura = 1.81

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

