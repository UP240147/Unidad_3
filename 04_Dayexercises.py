# Ejercicio 1
Word1 , Word2 , Word3 , Word4 = 'Thirty','Days','Of', 'Phyton'
single_string = Word1 + " " + Word2 + " " + Word3 + " " + Word4
print(single_string)

# Ejercicio 2
Word_1 , Word_2 , Word_3 = 'Coding','For','All'
single_string2 = Word_1 + " " + Word_2 + " " + Word_3 + "."
print(single_string2)

# Ejercicio 3
company = 'Coding For All'

# Ejercicio 4
print(company)

# Ejercicio 5
print(len(company))

# Ejercicio 6
text = 'company'
A_word = text.upper()
print(A_word)

# Ejercicio 7
text_2 = 'SCHOOL'
B_word = text_2.lower()
print(B_word)

# Ejercicio 8
text_3 = 'afuera de mi casa hay un puesto de tacos'
print(text_3.capitalize())
print(text_3.title())
print(text_3.swapcase())

# Ejercicio 9
text_4 = 'Coding For All'
palabra = text_4.replace('Coding', ' ')
print(palabra)

# Ejercicio 10
if text_4.find('Coding') == 0:
    print(True)
else:
    print(False)

# Ejercicio 11
replaceWord = text_4.replace("Coding" , "Python")
print(replaceWord)

# Ejercicio 12
moreReplaceWord = replaceWord.replace("Python", "Everyone").replace("All", "Python")
print(moreReplaceWord)

# Ejercicio 13
splitText = text_4.split()
print(splitText)
#Esto hace que genere una lista espaciada
#Existen diferentes párametros que pueden ponerse en el .split()
#Algunos parametros son split.(separador, maxsplit , "," , " ", )

# Ejercicio 14
empresas = "Facebook, Google, Microsoft, Apple, IBM, ORacle, Amazon"
splitEmpresas = empresas.split(",")
print(splitEmpresas)

# Ejercicio 15
forAll = "Coding For All"
onlyOne = forAll[0]
print(onlyOne)

# Ejercicio 16
lastOne = forAll[-1] #Al ser un index negativom empieza desde atras
print(lastOne)

# Ejercicio 17
idexten = forAll[10]
print(idexten)

# Ejercicio 18
textoo = "Python For Everyone"
acronym = "".join(word[0] for word in textoo.split())
print(acronym)

# Ejercicio 19
mastexto = "Coding For All"  #Declaras la variable de tu texto
masacronimos = "".join(word[0] for word in mastexto.split()) 
print(masacronimos)

# Ejercicio 20
eltexto = "Coding For All"
position = eltexto.index("C")
print(position)

# Ejercicio 21
position2 = eltexto.index("F")
print(position2)

# Ejercicio 22
eltesto = "Coding For All"
encontrareltesto = eltesto.find("l")
print(encontrareltesto)

# Ejercicio 23
text = "You cannot end a sentence with because because because is a conjunction"
posicion = text.find("because") 
print(posicion)

# Ejercicio 24
text = "You cannot end a sentence with because because because is a conjunction"
anotherposition = text.rindex("because")-1
print(anotherposition)

# Ejercicio 25
textocortado = "You cannot end a sentence with because because because is a conjunction"
#Lo reemplazara por un espacio vacío
textoepico = textocortado.replace("because because because", "")
print(textoepico)

# Ejercicio 26
text = "You cannot end a sentence with because because because is a conjunction"
posicion = text.find("because") 
print(posicion)

# Ejercicio 27
textocortado = "You cannot end a sentence with because because because is a conjunction"
textoepico = textocortado.replace("because because because", "")
print(textoepico)
 
# Ejercicio 28
substring = "Coding For All"
if substring.find("Coding") == 0:
    print(True)
else: print(False)

# Ejercicio 29
substring = "Coding For All"
if substring.find("coding") == 11:
    print(True)
else: print(False)

# Ejercicio 30
removeSpaces = "   Coding For All   "
removidosJeje = removeSpaces.replace("   ", "")
print(removidosJeje)

# Ejercicio 31
var1 = '30DaysOfPython'
print(var1.isidentifier()) # Falso
var2 = 'thirty_days_of_python'
print(var2.isidentifier()) # Verdadero
# La función isidentifier checa si puede o no ser un nombre valido para crear una variable

# Ejercicio 32
librerias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# Unir la lista con "# " como separador
result = " # ".join(librerias)
print(result)

# Ejercicio 33
separar = "I am enjoying this challenge.\nI just wonder what is next."
print(separar)
#La función \n hace un espacio en diferentes lineas

# Ejercicio 34
tabular = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(tabular)
#La función \t sirve para que tabule las palabras y esten alineadas correctamente

# Ejercicio 35
radius = 10
area = 3.14 * radius ** 2
# Formateando con f-string
formatear = f"The area of a circle with radius {radius} is {area} meters square."
print(formatear)
#La letra f hace que toda la cadena siguiente se haga un string
#{} todo dentro de la llave sera visto como una expresión

#  Ejercicio 36
masformateointenso = f"Las operaciones aritmeticas de 8 y 6 son su suma de {8+6},\n su resta es {8-6}, la multiplicación de \n{8*6}, su division de {8%6}, su {8//6} y su potencia de {8**6} "
print(masformateointenso)
