"""
Docstring para 01_variables

Las variables almacenan datos en la memoria del computador. Las variables deben ser faciles de recordar y de asociar. Una variable hace referencia a una direccion en la memoria donde los datos se encuentran almacenados. Los numeros al inicio, caracteres especiales y los guiones no estan permitidos para nombrar una variable. Una variable puede tener un nombre corto como (x,y,z), pero tambien uno mas descriptivo (firstname, lastname, age, country) son altamente recomendados.

# Reglas para nombrar variables:

* Una variable debe empezar con una letra o un guion bajo o piso (_).
* Una variable no puede empezar con un numero.
* Una variable solo puede contener caracteres alfanumericos y guiones bajo(_).
* Las variables se distinguen entre mayusculas y minusculas, por ejemplo: nombre, Nombre, NOMBRE) son variables diferentes.

En Python se usa el snake_case para nombrar variables, esto consiste en que cada vez que escribamos una palabra ira separada por un guion bajo(_) por ejemplo: last_name, first_name, print_this_variable ETC.


"""

message = "Welcome to python crash course!"
print(message)
new_message = "Hi from python crash course!"
print(message)

# Exercises: Level 1
# Declare a first name variable and assign a value to it
first_name = "David"

# Declare a last name variable and assign a value to it
last_name = "Campos"

# Declare a full name variable and assign a value to it
full_name = first_name + last_name

# Declare a country variable and assign a value to it
country = "Venezuela"

# Declare a city variable and assign a value to it
city = "El Tigre"

# Declare an age variable and assign a value to it
age = 28

# Declare a year variable and assign a value to it
year = 2026

# Declare a variable is_married and assign a value to it
is_married = False

# Declare a variable is_true and assign a value to it
is_true = True

# Declare a variable is_light_on and assign a value to it
is_light_on = True

# Declare multiple variable on one line
info = first_name + last_name + country + city
print(info)

# Exercises: Level 2
# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Using the len() built-in function, find the length of your first name
print(len(first_name))

# Compare the length of your first name and your last name
print(len(first_name))
print(len(last_name))

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# Subtract num_two from num_one and assign the value to a variable diff
substract = num_two - num_one

# Multiply num_two and num_one and assign the value to a variable product
multiply = num_two * num_one

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
modulus = num_two % num_one

# Calculate num_one to the power of num_two and assign the value to a variable exp
power = num_one**num_two

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# The radius of a circle is 30 meters.
radius = 30

# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 3.14 * radius**2

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * 3.14 * radius

# Take radius as user input and calculate the area.
radius = int(input(""))
area_of_circle = 3.14 * radius**2

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("")
last_name = input("")
country = input("")
age = int(input(""))
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help("keywords")
