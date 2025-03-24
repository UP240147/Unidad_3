# Un Diccionario es una colección desordenada y modificable

# Ejercicio 1
apple = {}

# Ejercicio 2
apple = {
    "Name" : "Ramon",
    "Color" : "Blanco",
    "Breed" : True,
    "Legs" : 4,
    "Age" : 3
}

# Ejercicio 3
student_dictionary = {
    "First Name" : "Joel",
    "Last Name" : "Marmolejo Lopez",
    "Gender" : "Masculino",
    "Age" : 19,
    "Martial Status" : "Single",
    "Skills" : ["Python", "Leer", "Socializar", "Ingles"],
    "Country" : "México",
    "City" : "Aguascalientes", 
    "Adress"  : "AV Morelos #138 El Cinegal"
}

# Ejercicio 4
print(len(student_dictionary))

# Ejercicio 5
valor_habilidades = student_dictionary["Skills"]
print(valor_habilidades)  
print(type(valor_habilidades))  

# Ejercicio 6

student_dictionary["Skills"].append("Godot")
student_dictionary["Skills"].append("SolidWorks")
print(student_dictionary)

# Ejercicio 7
values = student_dictionary.values()
print(values)

# Ejercicio 8 
values_list = list(student_dictionary.values())
print(values_list)

# Ejercicio 9
print(student_dictionary.items())

# Ejercicio 10
student_dictionary.pop("Age")
print(student_dictionary)

# Ejercicio 11
del student_dictionary