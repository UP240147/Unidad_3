# LEVEL 1

# Ejercicio 1
edad = int(input("Coloca tu edad: "))  
if edad >= 19:
    print("Eres lo suficientemente mayor para conducir")
else: print("Aún eres menor, espera", 19 - edad, "años más")

# Ejercicio 2
tu_edad = int(input("Coloca tú edad"))
if tu_edad == 19:
    print("Tenemos la misma edad")
elif tu_edad > 19:
    print("Me ganas por ", tu_edad - 19, " años")
else: print("Te gano por " ,19 - tu_edad , " años")

# Ejercicio 3
number1 = int(input("Ingresa un número"))
number2 = int(input("Ingresa otro número"))
if number1 == number2:
    print("Los números son iguales")
elif number1 > number2:
    print(number1, " es mayor a " , number2)
else: print(number2, " es mayor que " , number1)

# LEVEL 2

# Ejercicio 4
puntuacion = int(input("Coloca tu calificación "))  
if 80 <= puntuacion <= 100:
    grade = "A"
elif 70 <= puntuacion <= 79:
    grade = "B"
elif 60 <= puntuacion <= 69:
    grade = "C"
elif 50 <= puntuacion <= 59:
    grade = "D"
elif 0 <= puntuacion <= 49:
    grade = "F"
else: grade = "Invalid puntuacion"  
print("Tu puntuación es: " ,grade)

# Ejercicio 5
estacion = input("Coloca un mes del año: ")

if estacion in ["Septiembre", "Octubre", "Noviembre"]:
    print("Estamos en otoño")
elif estacion in ["Diciembre", "Enero", "Febrero"]:
    print("Estamos en invierno")
elif estacion in ["Marzo", "Abril", "Mayo"]:
    print("Estamos en primavera")
elif estacion in ["Junio", "Julio", "Agosto"]:
    print("Estamos en verano")
else:
    print("No existe el mes ingresado")

# Ejercicio 6
fruits = ['banana', 'orange', 'mango', 'lemon']
ingresa_Fruta = input("Ingresa una fruta")
if ingresa_Fruta in fruits:
    print("Existe la fruta dentro de la lista")
else: 
    fruits.append(ingresa_Fruta)
    print("Fruta Agregada", fruits)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills_list = person['skills']
    middle_index = len(skills_list) // 2
    print("Middle skill:", skills_list[middle_index])

if 'skills' in person and 'Python' in person['skills']:
    print("Python skill found:", True)
else:
    print("Python skill found:", False)

skills = set(person['skills']) if 'skills' in person else set()

if skills == {'JavaScript', 'React'}:
    print("He is a front end developer")
elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
    print("He is a backend developer")
elif {'React', 'Node', 'MongoDB'}.issubset(skills):
    print("He is a fullstack developer")
else:
    print("Unknown title")

if person.get('is_marred') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")