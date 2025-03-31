# NIVEL 1

# EJERCICIO 1

import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

print(random_user_id())

# EJERCICIO 2

def user_id_gen_by_user():
    num_chars = int(input("Ingrese el número de caracteres por ID: "))
    num_ids = int(input("Ingrese la cantidad de ID a generar: "))
    
    user_ids = [
        ''.join(random.choices(string.ascii_letters + string.digits, k=num_chars))
        for _ in range(num_ids)
    ]
    
    return "\n".join(user_ids)

print(user_id_gen_by_user())

# EJERCICIO 3

import random

def rgb_color_gen():
    r = random.randint(0, 255)  # Rojo (0-255)
    g = random.randint(0, 255)  # Verde (0-255)
    b = random.randint(0, 255)  # Azul (0-255)
    
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())

# NIVEL 2

# EJERCICIO 1

import random

def list_of_hexa_colors(n):
    hex_colors = [
        f'#{random.choice("0123456789ABCDEF")}{random.choice("0123456789ABCDEF")}{random.choice("0123456789ABCDEF")}'
        f'{random.choice("0123456789ABCDEF")}{random.choice("0123456789ABCDEF")}{random.choice("0123456789ABCDEF")}'
        for _ in range(n)
    ]
    return hex_colors

print(list_of_hexa_colors(5))  # Genera 5 colores hexadecimales

# EJERCICIO 2

import random

def list_of_rgb_colors(n):
    rgb_colors = [
        f"rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})"
        for _ in range(n)
    ]
    return rgb_colors

print(list_of_rgb_colors(5))  # Genera 5 colores RGB

# EJERCICIO  3

import random

def generate_colors(color_type, n):
    if color_type == 'hexa':
        return [f'#{random.randint(0, 255):02X}{random.randint(0, 255):02X}{random.randint(0, 255):02X}' for _ in range(n)]
    elif color_type == 'rgb':
        return [f"rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})" for _ in range(n)]
    else:
        return "Tipo de color no válido. Usa 'hexa' o 'rgb'."

# Pruebas
print(generate_colors('hexa', 3))  # ['#a3e12f', '#03ed55', '#eb3d2b']
print(generate_colors('hexa', 1))  # ['#b334ef']
print(generate_colors('rgb', 3))   # ['rgb(5, 55, 175)', 'rgb(50, 105, 100)', 'rgb(15, 26, 80)']
print(generate_colors('rgb', 1))   # ['rgb(33,79,176)']
 
# NIVEL 3

# EJERCICIO 1

import random

def shuffle_list(lst):
    random.shuffle(lst)  # Mezcla la lista en su lugar
    return lst

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(shuffle_list(my_list))  # Salida aleatoria, por ejemplo: [4, 9, 1, 6, 3, 8, 2, 7, 5]

# EJERCICIO 2 

import random

def unique_random_numbers():
    return random.sample(range(10), 7)  # Toma 7 números únicos del 0 al 9

# Prueba
print(unique_random_numbers())  # Ejemplo de salida: [3, 7, 1, 9, 5, 0, 6]
