# LEVEL 1

# EJERCICIO 1
cuentas = 0
while cuentas < 11:  
    print(cuentas)   
    cuentas = cuentas + 1 

cuentas = [0,1,2,3,4,5,6,7,8,9,10]
for cuenta in cuentas:
    print(cuenta)

# EJERCICIO 2
cuenta = 10
while cuenta != -1:
    print(cuenta)
    cuenta = cuenta - 1

cuentas = [10,9,8,7,6,5,4,3,2,1,0]
for cuentocuenta in cuentas:
    print(cuentocuenta)

# EJERCICIO 3
for i in range(1, 8): # Un Loop del 1 al 7  
    print("#" * i)  # Imprime un # repetido por las i veces

# EJERCICIO 4
for i in range(8):  # 8 Filas
    for j in range(8):  # 8 Columnas
        print("#", end=" ")  # Imprime el # con espacio
    print()  # Mueve a la siguiente fila al acabar 


# EJERCICIO 5
for i in range(11):  # Del 1 al 10
    print(f"{i} x {i} = {i * i}")  #i empieza con un valor de 1

# EJERCICIO 6
lista =  ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lista:
    print(i)

# EJERCICIO 7
for i in range(0, 101, 2):  # Empieza en 0 hasta 100 en un incremento de 2 en 2
    print(i)

# EJERCICIO 8
for i in range(101):  # Iterar desde 0 hasta 100
    if i % 2 != 0:  # Verificar si el número es impar
        print(i)

# LEVEL 2

# EJERCICIO 9
suma = 0
for i in range(101):
   suma += i

print("La suma es : " , suma)

# EJERCICIO 10
suma_pares = 0  
suma_imparares = 0   

for i in range(101):  
    if i % 2 == 0:  
        suma_pares += i
    else:  
        suma_imparares += i

print("La Suma de los numeros pares es: ", suma_imparares)


# LEVEL 3

# EJERCICIO 12
frutas = ['banana', 'orange', 'mango', 'lemon']
for i in frutas:
    reversed_i = i[::-1]  # Reverse the string using slicing
    print(reversed_i)