
# EJERCICIO 1
empytList = []

# EJERCICIO 2
list5_items = ["Hola" , 4 , True, "Adios", 12j]

# EJERCICIO 3
print(len(list5_items))

# EJERCICIO 4
getTheItem = [list5_items[i] for i in [0, 2, 4]]
print(getTheItem)  
#Selecciona el lugar y los imprime

# EJERCICIO 5
mixed_data_types = ["José Ángel", 18, 1.78, "Single", "Que te importa"]

# EJERCICIO 6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# EJERCICIO 7
print(it_companies)

# EJERCICIO 8
print(len(it_companies))

# EJERCICIO 9 
getTheCompanies = [it_companies[i] for i in [0,3, 6]]

# EJERCICIO 10
it_companies[0] = "Removido"
print(it_companies)

# EJERCICIO 11
it_companies.insert(1, "Agregado")
print(it_companies)

# EJERCICIO 12
it_companies.insert(4, "IT ")
print(it_companies)

# EJERCICIO 13
it_companies = [company.upper() for company in it_companies]
print(it_companies)

# EJERCICIO 14
listaUnida = "#;  ".join(it_companies)
print(listaUnida)

# EJERCICIO 15
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
if it_companies[1] == "Google":
    print("Existe")
else: print("No Existe")

# EJERCICIO 16
it_companies.sort()
print(it_companies)

# EJERCICIO 17
it_companies.reverse()
print(it_companies)

# EJERCICIO 18
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
sliceFirstCompanies = it_companies[:3]
print(sliceFirstCompanies)

# EJERCICIO 19
sliceLastCompanies = it_companies[3:]
print(sliceLastCompanies)

# EJERCICIO 20
it_companies = ["Facebook", "Google", "Microsoft", "IT", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.remove("IT")
print(it_companies)

# EJERCICIO 21
it_companies.remove("Facebook")
print(it_companies)

# EJERCICIO 22
it_companies.remove("Apple")
print(it_companies)

# EJERCICIO 23
it_companies.remove("Amazon")
print(it_companies)

# EJERCICIO 24
it_companies.clear()
print(it_companies)

# EJERCICIO 25
it_companies = None
print(it_companies)

# EJERCICIO 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
# Unir las listas
full_stack = front_end + back_end
print(full_stack)

# EJERCICIO 27
full_stack_copy = full_stack.copy()  # Copiar la lista unida
# Encotrar el índice de "Redux" y luego insertar los nuevos elementos después de él
redux_index = full_stack_copy.index("Redux")
# Insertar "Python" y "SQL" después de "Redux"
full_stack_copy.insert(redux_index + 1, "Python")
full_stack_copy.insert(redux_index + 2, "SQL")
print(full_stack_copy)

# Nivel 2 de ejercicios
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

ages.reverse()
print(ages)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Promedio (average)
average_age = sum(ages) / len(ages)

# Rango (range)
age_range = max(ages) - min(ages)

# Comparar min - average y max - average con abs()
min_to_average = abs(min(ages) - average_age)
max_to_average = abs(max(ages) - average_age)

# Imprimir resultados
print("Promedio de las edades:", average_age)
print("Rango de las edades:", age_range)
print("Diferencia entre min y promedio:", min_to_average)
print("Diferencia entre max y promedio:", max_to_average)

countries = [

  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

num_countries = len(countries)
middle_index = num_countries // 2

if num_countries % 2 == 0:
    middle_countries = [countries[middle_index - 1], countries[middle_index]]
else:
    middle_countries = [countries[middle_index]]

# Ejercicio 29 Dividir la lista en dos mitades
first_half = countries[:middle_index + (1 if num_countries % 2 != 0 else 0)]
second_half = countries[middle_index + (1 if num_countries % 2 != 0 else 0):]

# Ejercicio 30 Desempaquetar los tres primeros países y asignar el resto como países Escandinavos
first_three, *scandic_countries = first_half[:3], *second_half

print("Middle country(ies):", middle_countries)
print("First three countries:", first_three)
print("Scandic countries:", scandic_countries)
