#Variables en phyton

primer_nombre = 'Joel'
apellidos = 'Marmolejo Lopez'
pais = 'Mexico'
ciudad = 'Aguascalientes'
edad = 19 
estas_casado = False
habilidades = {'Phyton', 'Arduino'}
informacion_personal =  {
    'first_name':'Joel',
    'last_name':'Marmolejo Lopez',
    'country':'Mexico',
    'city':'Aguascalintes'
    }

print ('hello' ,',', 'World')

print('Mi nombre es:', primer_nombre)
print('Mis apellidos son:', apellidos)
print('mi pais es:', pais)
print('mi ciudad es:', ciudad)
print('mi edad:', edad)
print('¿estoy casado?', estas_casado)
print('mis habilidades', habilidades)
print('mi informacion personal', informacion_personal)

#Getting user input using the input() built-in funtion.

first_name = input('¿Cual es tu nombre?')
age = input('¿Cuantos años tienes?')

print(first_name)
print(age)