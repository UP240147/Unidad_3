# LEVEL 1

# EJERCICIO 1
"""Declare a function add_two_numbers. It takes two parameters and it returns a sum."""
def add_two_numbers(num1, num2): #Declaro la función con 2 parametros 
    total = num1 + num2     #hago que sume esos 2 parametros
    return total            # El "Return" devolverá un valor cuando se llame
print(add_two_numbers(1,2)) #Imprime esos 2 numeros y los suma

# EJERCICIO 2
"""Area of a circle is calculated as follows: area = π x r x r. 
Write a function that calculates area_of_circle."""
def area_of_circle(): #Declaras la función 
    pi = 3.14
    r = 10
    circle_area = pi * (r**2)
    print(circle_area)
area_of_circle() #Llamas a la función 

# EJERCICIO 3
"""Write a function called add_all_nums which takes arbitrary 
number of arguments and sums all the arguments. 
Check if all the list items are number types. If not do give a reasonable feedback."""
def add_all_nums(num1,num2,num3,num4):
    total_nums = num1 + num2 + num3 + num4
    if total_nums == int:
        print("Todos son numeros")
    else: print("No todos son numeros")
    return total_nums
print(add_all_nums(1,2,3,4))

# EJERCICIO 4
"""Temperature in °C can be converted to °F using this formula:
°F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit."""
def convert_celsius_to_fahrenheit():
    celsius = 25.6
    fahrenheit = (celsius*9/5) + 32
    print(fahrenheit)
convert_celsius_to_fahrenheit()

# EJERCICIO 5
"""Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer."""
def check_season(month):
    seasons = "Autumn", "Winter", "Spring", "Summer"
    return seasons
print(check_season("Autumn, Winter, Spring or Summer"))


# EJERCICIO 6
"""Write a function called calculate_slope
which return the slope of a linear equation"""
def calculate_slope():
    x1,y1,x2,y2 = 1,2,3,4
    m = (y2 - y1) / (x2-x1)
    print(m)
calculate_slope()


# EJERCICIO 7
"""Quadratic equation is calculated as follows: ax² + bx + c = 0. 
Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn."""
import cmath  
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c  
    sqrt_discriminant = cmath.sqrt(discriminant)  

    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)

    return (x1, x2) if x1 != x2 else (x1,)  
print(solve_quadratic_eqn(1, -3, 2))  # (2.0, 1.0)


# EJERCICIO 8
"""Declare a function named print_list. It takes a list as a 
parameter and it prints out each element of the list."""
def print_list(lista):
    for listas in lista:
        print(listas)
print_list(["Bazinga", "Epopeya", "Breaking Bad 2", True])

# EJERCICIO 9
def reverse_list(matriz):
    for i in matriz:
        matriz.reverse()
        return matriz
print(reverse_list([1, 2, 3, 4, 5]))

# EJERCICIO 10
def capitalize_list_items(lista):
    return[item.capitalize() for item in lista]
print(capitalize_list_items(["bazinga", "el pepe", "jose"]))

# EJERCICIO 11
def add_item(lista, objeto):
    lista.append(objeto)
    return lista
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat')) 

# EJERCICIO 12
def remove_item(lista, objeto):
    lista.remove(objeto)
    return lista
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  

# EJERCICIO 13
def sum_of_numbers(num1):
    suma = 0
    for i in range(0,num1 + 1):
        suma += i
    return suma
print(sum_of_numbers(5))  # 15

# EJERCICIO 14
def sum_of_odds(odd): #Impares
    suma = 0
    for i in range(0,odd + 1, 2):
       suma += i
    return suma
print(sum_of_odds(100))

# EJERCICIO 15
def sum_of_even(even):
    suma = 0
    for i in range(0,even, 2):
        suma += i
    return suma
print(sum_of_even(100))


# LEVEL 2
#  EJERCICIO 1
def evens_and__odds(numeros):
    suma_pares = 0
    suma_impares = 0
    for i in range(numeros + 1):
        if i %2 == 0:
            suma_pares += 1
        else: suma_impares += 1
    return suma_pares, suma_impares
print(evens_and__odds(100))

# EJERCICIO 1
def factorial(n):
    if n == 0 or n == 1:  
        return 1
    result = 1
    for i in range(2, n + 1):  
        result *= i
    return result
print(factorial(5)) 

# EJERCICIO 2
def is_empty(value):
    return not bool(value)
print(is_empty(""))      

# EJERCICIO 3
from statistics import mean, median, mode, variance
from math import sqrt

def calculate_mean(numbers):
    return mean(numbers)

def calculate_median(numbers):
    return median(numbers)

def calculate_mode(numbers):
    try:
        return mode(numbers)
    except:
        return "No unique mode found"

def calculate_range(numbers):
    return max(numbers) - min(numbers)

def calculate_variance(numbers):
    return variance(numbers)

def calculate_std(numbers):
    return sqrt(calculate_variance(numbers))

numbers = [1, 2, 2, 3, 4, 5, 5, 5, 6]
print("media:", calculate_mean(numbers))
print("Mediana:", calculate_median(numbers))
print("Moda:", calculate_mode(numbers))
print("Rango:", calculate_range(numbers))
print("Variación:", calculate_variance(numbers))
print("Desviaci[on Estandar", calculate_std(numbers))

# LEVEL 3
# EJERCICIO 1
def numero_primo(numero):
    if numero in [1, 3, 5, 7, 11, 13]:
        print("Es primo")
    else:
        print("Es falso")
numero_primo(2)  

# EJERCICIO 2
def unicos(lst):
    return len(lst) == len(set(lst))
unique_numbers = [1, 2, 3, 4, 5]
print(unicos(unique_numbers))

# EJERCICIO 3
def same_data_type(lst):
    return len(set(type(x) for x in lst)) == 1
print(same_data_type([1, 2, 3, 4, 5]))  

# EJERCICIO 4
import keyword

def is_valid_variable(name):
    if not isinstance(name, str):
        return False
    if keyword.iskeyword(name):
        return False
    if not name.isidentifier():
        return False
    return True
print(is_valid_variable("variable"))

# EJERCICIO 5

def lenguas_más_habladas(n=10):
    language_counts = {'Inglés': 1500, 'Español': 500, 'Francés': 280, 'Chino': 1200, 'Arabe': 600}
    return sorted(language_counts.items(), key=lambda x: x[1], reverse=True)[:n]


def paises_mas_importantes(n=10):
    country_population = {'China': 1400, 'India': 1380, 'EEUU': 330, 'Indonesia': 270, 'Brasil': 212}
    return sorted(country_population.items(), key=lambda x: x[1], reverse=True)[:n]


print("Top 10 idiomas más hablados:")
for idioma, hablantes in lenguas_más_habladas(10):
    print(f"{idioma}: {hablantes} millones de hablantes")


print("\nTop 10 países más importantes:")
for pais, poblacion in paises_mas_importantes(10):
    print(f"{pais}: {poblacion} millones de personas")
