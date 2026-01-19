"""
Docstring para 02_strings
"""

"""
La variable name almacena un string en minusculas. El metodo title() aparece despues de la variable en la funcion print(). Un metodo es la accion que Python puede realizar sobre un fragmento de dato. El punto(.) despues de la variable name le dice a Python que ejecute el metodo title sobre la variable name. Cada metodo es seguido de un par de parentesis porque a menudo los metodos necesitan informacion adicional para cumplir su funcion, esa informacion es proporcionada dentro de los parentesis. El metodo title() no necesita informacion adicional, asi que los parentesis estan vacios.
"""
name = "ada lovelace"
print(name.title())


name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# Usando variables en strings
"""
En algunas situaciones vamos a querer usar variables dentro de un string. Por ejemplo, quieres usar dos variables para representar first_name y last_name y al combinar esas variables, mostraremos el full_name.
"""
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
"""
Para insertar variables dentro de un string, hay que colocar la letra f justamente antes de las comillas. Abrimos llaves alrededor de el nombre de las variables o cualquier variable que quieras usar dentro del string. Python reemplazara cada variable con su valor cual el string es impreso.

Estos strings son llamados f-strings. La f es para formato, porque Python formatea el string, reemplazando el nombre de cada variable entre llaves con su valor

Se pueden hacer mucho con f-string. Por ejemplo, quieres usar f-string para componer un mensaje completo asociado a la informacion de las variables.
"""
print(f"Hola, {full_name.title()}!")
"""
Tambien podemos usar f-strings para componer un mensaje, y asignar el mensaje completo a una variable.
"""
message = f"Hola, {full_name.title()}!"
print(message)

# Agregando espacios en blanco a un string con tabs y newlines
"""
El programacion los espacios en blanco (whitespace). Hace referencia a cualquier caracter que no se imprime, como los espacios, tabuladores y simbolos de fin de linea. Podemos usar los espacios en blanco para organizar nuestra salida para que sea mas facil de leer para el usuario.

Para agregar tab a nuestro texto usamos la combinacion de caracteres \t
"""
print("Python")
print("\tPython")
"""
Para agregar una nueva linea al string, usamos la combinacion \n
"""
print("Lenguajes:\nPython\nC\nJavaScript")
"""
Tambien podemos combinar tabuladores con nuevas lineas en un solo string con la siguiente combinacion \n\t
"""
print("Lenguajes:\n\tPython\n\tC\n\tJavaScript")
"""
Un espacio en blanco extra puede ser confuso para nuestros programas. Para los programadores 'Python' y 'Python ' parecen ser lo mismo. Pero para un programa son dos strings diferentes. Python detecta el espacio en blanco extra y considera que no es importante avisarte.

Es importante tomar en cuenta a los espacios en blanco, porque normalmente querras comparar dos string para determinar si son los mismos. Por ejemplo, una instancia importante de nuestro programa necesita analizar los usuarios de las personas cuando ellos ingresan en una pagina web. El espacio en blanco extra puede ser confuso en muchas situaciones. Afortunadamente, Python lo hace facil al momento de eliminar el espacio en blanco extra para los datos que ha ingresado las personas.

Python puede buscar un espacio en blanco extra en el lado izquierdo y derecho de un string. Para asegurarnos que no existe un espacio en blanco del lado derecho del string, usamos el metodo rstrip():
"""
favorite_lenguage = "Python "
print(favorite_lenguage)
print(favorite_lenguage.rstrip())
"""
Tambien se pueden remover los espacios en blanco del lado izquierdo usando lstrip() o podemos remover los de ambos lados usando el metodo strip()
"""
favorite_lenguage = " Python "
print(favorite_lenguage.rstrip())
print(favorite_lenguage.lstrip())
print(favorite_lenguage.strip())
"""
Tambien podemos remover prefijos de un string con el metodo removeprefix().
"""
nostarch_url = "https://nostarch.com"
print(nostarch_url.removeprefix("https://"))

# Personal Message
name = "David"
print(f"Hola {name}, te gustaria aprender algo de Python hoy?")

# Name cases
print(name.lower())
print(name.upper())
print(name.title())

# Famous Quote
famous_name = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."
print(f'{famous_name} once said, "{quote}"')

# Stripping Names
person_name = "\t\n\tDavid\n\n\t\t"
print(person_name)
print(person_name.rstrip())
print(person_name.lstrip())
print(person_name.strip())

# File extension
file_name = "python_notes.txt"
print(file_name.removesuffix(".txt"))

# Exercises
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string_1 = "Thirty"
string_2 = "Days"
string_3 = "Of"
string_4 = "Python"
single_string = string_1 + " " + string_2 + " " + string_3 + " " + string_4
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string_1 = "Coding"
string_2 = "For"
string_3 = "All"
single_string = string_1 + " " + string_2 + " " + string_3
# Declare a variable named company and assign it to an initial value "Coding For All".
company = single_string
# Print the variable company using print().
print(company)
# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
print(company.upper())
# Change all the characters to lowercase letters using lower() method.
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# Cut(slice) out the first word of Coding For All string.
print(company[6:])
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index("Coding"))
print(company.rindex("Coding"))
print(company.find("Coding"))
print(company.rfind("Coding"))
# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Hello"))
# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
message = "Python for Everyone"
print(message.replace("Everyone", "All"))
# Split the string 'Coding For All' using space as the separator (split()).
message = "Coding For All"
print(message.split(" "))
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))
# What is the character at index 0 in the string Coding For All.
print(message[0])
# What is the last index of the string Coding For All.
print(message[-1])
# What character is at index 10 in "Coding For All" string.
print(message[10])
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
print("Python For Everyone"[0:-1:2])
# Create an acronym or an abbreviation for the name 'Coding For All'.
print(message[0:-1:2])
# Use index to determine the position of the first occurrence of C in Coding For All.
print(message.index("C"))
# Use index to determine the position of the first occurrence of F in Coding For All.
print(message.index("F"))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(message.rfind("l"))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex("because"))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])
# Does 'Coding For All' start with a substring Coding?
print("Coding For All".startswith("Coding"))
# Does 'Coding For All' end with a substring coding?
print("Coding For All".endswith("Coding"))
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print("   Coding For All      ".strip())
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
var1 = "30DaysOfPython".isidentifier()
var2 = "thirty_days_of_python".isidentifier()
print(var1)
print(var2)
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("# ".join(python_libraries))
# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
sentences = "I am enjoying this challenge.\nI just wonder what is next."
# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
info = "Name\tAge\tCountry\t\tCity\nDavid\t28\tVenezuela\tCaracas"
print(info)
# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius**2
# The area of a circle with radius 10 is 314 meters square.
print(f"The area of a circle with radius {radius} is {area} meters square.")
# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
print(
    f"8 + 6 = {8+6}\n8 - 6 = {8-6}\n8 * 6 = {8*6}\n8 / 6 = {8/6:.2f}\n8 % 6 = {8%6}\n8 // 6 = {8//6}\n8**6 = {8**6}"
)
