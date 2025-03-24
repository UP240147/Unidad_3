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