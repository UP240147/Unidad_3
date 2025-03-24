# EJERCICIO 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


# EJERCICIO 2
it_companies.add("Twitter")
print(it_companies)

# EJERCICIO 3
it_companies.update(["pinteres", "Instagram"])
print(it_companies)

# EJERCICIO 4
it_companies.remove("pinteres")
print(it_companies)

# EJERCICIO 5
# Discard no lanza un error si un elemento no está


# EXERCICES: LEVEL 2

# EJERCICIO 6
a = {"A", "E", "I" , "O", "U"}
b = {"C", "A", "H" , "I", "J"}
ab = b.union(a)
print(ab)

# EJERCICIO 7
print(a.intersection(b))

# EJERCICIO 8
print(b.issubset(a))
print(a.issubset(b))

# EJERCICIo 9
print(a.isdisjoint(b))

# EJERCICIO 10
union_ab = a | b  
print("A unido con B:", union_ab)
union_ba = b | a  
print("B unido con A:", union_ba)

# EJERCICIO 11
print(b.symmetric_difference(a))

# EJERCICIO 12
del a
del b

# EXERCICES: LEVEL 3

# EJERCICIO 13
age = [22, 19, 24, 25, 26, 24, 25, 24]
set_age = set(age)

if len(age) > len(set_age):
    print("Es más grande la lista")
else: print("Es más grande el set")

# EJERCICIO 14
#El STRING es una secuencia de caracteres
#La LISTA es una colección ordenada y mutable de elementos
#La TUPLA es una colección ordenada pero inmutable de elementos

# EJERCICIO 15
texto = "I am a teacher and I love to inspire and teach people"
# Dividir la oración en palabras
palabras = texto.split()
# Convertir la lista de palabras en un set para obtener palabras únicas
unicas_palabras = set(palabras)
# Contar el número de palabras únicas
print(f"El numero de palabras es: {len(unicas_palabras)}")
