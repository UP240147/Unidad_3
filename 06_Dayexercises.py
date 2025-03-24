# EJERCICIO 1
empty_tuple = ()
print(empty_tuple)

# EJERCICIO 2
tuple_of_brothers = ("José", "Pedro")
tuple_of_sisters = ("Carmela", "Marely")

# EJERCICIO 3
siblings = tuple_of_brothers + tuple_of_sisters
print(siblings)

# EJERCICIO 4
print(len(siblings))

# EJERCICIO 5
fathers_name = ("Pedrote" , "Carmelota")
family_members = fathers_name + siblings
print(family_members)


# EXERCICES: LEVEL 2

# EJERCICIO 1
family_members = ("José", "Pedro", "Carmela", "Marely", "Pedrote", "Carmelota")
*siblings, papa, mama = family_members
print("Los hermanos son ", siblings)
print("El padre es ", papa)
print("La madre es ", mama)

# EJERCICIO 2
frutas = ("Manzana", "Uvas", "Sandia", "Mandarina")
vegetales = ("Calabaza", "Apio")
animales = ("Bistec", "Ribay", "Milanesa", "Chuleta")
cosas_de_comida = frutas + vegetales + animales
print(cosas_de_comida)

# EJERCICIO 3
tuple_to_list = list(cosas_de_comida)
print(tuple_to_list)

# EJERCICIO 4
print(cosas_de_comida[4:6])

# EJERCICIO 5
print(cosas_de_comida[:3] + cosas_de_comida[-3:])

# EJERCICIO 6
tuple_to_tuple = tuple(cosas_de_comida)
del tuple_to_tuple

# EJERCICIO 7
paises_nordicos = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Estonia es un pais nordico:", "Estonia" in paises_nordicos)
print("Iceland es un pais nordico:", "Iceland" in paises_nordicos)
