# Defining a function
def greet_user():
    print("Hello!")


greet_user()


# Passing information to a function
def greet_user(username):
    print(f"Hello, {username.title()}!")


greet_user("david")

# Arguments and parameters
"""
Los parametros: son las variables que definimos en la funcion greet_user().
Los argumentos: son los valores que le damos a nuestra variable greet_user("david")
"""


# Exercise
def display_message():
    print("I learn about functions in this chapter 8.")


display_message()


def favorite_book(title):
    print(f"One of my favorite book is {title}")


favorite_book("Alice in Wonderland")

# Passing Arguments
"""Porque una definicion de una funcion puede tener multiples parametros, y una llamada a la funcion puede necesitar multiples argumentos. Podemos pasar argumentos a nuestras funciones de muchas maneras. Podemos usar argumentos posicionales, el cual necesitan estar en el mismo orden en el que los parametros fueron escritos; O los keyword arguments, donde cada argumento consiste en una variable clave valor."""


# Positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("dog", "nano")
# Multiple function calls
describe_pet("dog", "lane")
describe_pet("dog", "lala")

# Order matters in positional arguments
describe_pet("harry", "hamster")

# Keyword arguments
"""El orden no importa porque python sabe donde va cada valor. Cuando usemos los keyword arguments debemos estar seguros de usar los mismos nombres de los parametros."""
describe_pet(animal_type="dog", pet_name="nano")
describe_pet(pet_name="nano", animal_type="dog")


# Default values
def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name="lelo ")
"""Para describir otro animal que no sea perro"""
describe_pet(pet_name="harry", animal_type="hamster")
"""Cuando usamos valores por defecto, cualquier parametro con valores por defecto deben ser creados justo despues de los que no tienen valores. Esto permite a python continuar interpretando los argumentos posicionales correctamente."""

# Equivalent funciton calls
# A dog named Willie.
describe_pet("willie")
describe_pet(pet_name="willie")
# A hamster named Harry.
describe_pet("harry", "hamster")
describe_pet(pet_name="harry", animal_type="hamster")
describe_pet(animal_type="hamster", pet_name="harry")


# exercise
def make_shirt(size, text):
    print(f"\nThe size of your shirt is: {size}\nThe text of your shirt is: {text}")


make_shirt("M", "Hello Python!")
make_shirt(text="Californication", size="XL")


def make_shirt(size="large", text="i love Python"):
    print(
        f"\nThe size of your shirt is: {size.title()}\nThe text of your shirt is: {text.title()}"
    )


make_shirt()


def describe_city(city, country="spain"):
    print(f"{city.title()} is in {country.title()}")


describe_city("barcelona")
describe_city("valencia", "spain")
describe_city("madrid", "spain")

# Return values
"""Una funcion no siempre debe mostrar el output directamente. En su lugar, puede procesar algun dato y luego retornarlo a un valor o un conjunto de valores. La declaracion return, toma un valor dentro de la funcion y la devuelve a la linea donde fue llamada esa funcion."""


# Returning a simple value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)


# Making an argument optional
def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("john", "lee", "hooker")
print(musician)
musician = get_formatted_name("jimi", "hendrix")
print(musician)


# Returning a dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    return person


musician = build_person("jimi", "hendrix")
print(musician)

"""El siguiente ejemplo te permitira almacenar la edad"""


def build_person(first_name, last_name, age=None):
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person("jimi", "hendrix", age=27)
print(musician)


# Using a function with a while loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# while True:
#     print("\nPlease tell me your name: ")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name: ")

#     if f_name == "q":
#         break
#     l_name = input("Last name: ")
#     if l_name == "q":
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name.title()}")


# Exercises
def city_country(city, country):
    return f"{city.title()}, {country.title()}"


city_and_country = city_country("santiago", "chile")
print(city_and_country)
city_and_country = city_country("caracas", "venezuela")
print(city_and_country)
city_and_country = city_country("bogota", "colombia")
print(city_and_country)


def make_album(artist_name, album_title, number_of_songs=None):
    album = {
        "artist": artist_name,
        "album": album_title,
    }
    if number_of_songs:
        album["number_of_songs"] = number_of_songs
    return album


album = make_album("bad bunny", "x100pre")
print(album)
album = make_album("bad bunny", "yhlqmdlg")
print(album)
album = make_album("rauw alejandro", "afrodisiaco")
print(album)
album = make_album("anuel", "real hasta la muerte", number_of_songs=12)
print(album)

# while True:
#     artist_name = input("Enter your artist name: ")
#     if artist_name == "q":
#         break
#     album_title = input("Enter your album title: ")
#     if album_title == "q":
#         break

#     album = make_album(artist_name, album_title)
#     print(f"{album}")


# Passing a list
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ["david", "eduardo", "henricus"]
greet_users(usernames)

# Modifiying a list in a function
"""Start with some designs that need to be printed."""
unprinted_designs = ["phone case", "robot pedant", "dodecahedron"]
completed_models = []

"""Simulate printing each design, until none are left"""
"""Move each design to completed_models after printing."""

while unprinted_designs:
    current_design = unprinted_designs.pop(0)
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

"""Display all complete2d models."""
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model.title())

"""Podemos reorganizar este codigo escribiendo dos funciones, cada una para un trabajo en especifico."""


def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop(0)
        print(f"Printing model: {current_design.title()}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model.title())


unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a function from modifiying a list
"""Si queremos guardar nuestra lista original de unprinted design para un registro deberiamos mandarle una copia de esa lista a nuestra funcion
function_name(list_name[:])
"""
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []
print_models(unprinted_designs[:], completed_models)
print(unprinted_designs)

# Exercises
msg = [
    "todo saldra bien",
    "eres increible",
    "sigue adelante",
    "sigue trabajando",
    "lo estas haciendo bien",
    "menos es mas",
    "lo lograste",
]


def show_messages(msg):
    print("Printing messages: ")
    for m in msg:
        print(f"\t{m.title()}.")


show_messages(msg)
msg = [
    "todo saldra bien",
    "eres increible",
    "sigue adelante",
    "sigue trabajando",
    "lo estas haciendo bien",
    "menos es mas",
    "lo lograste",
]
sent_messages = []


def send_messages(msg, sent_messages):
    while msg:
        current_msg = msg.pop(0)
        print(f"Sending message: {current_msg.title()}")
        sent_messages.append(current_msg)


send_messages(msg, sent_messages)
show_messages(sent_messages)

msg = [
    "todo saldra bien",
    "eres increible",
    "sigue adelante",
    "sigue trabajando",
    "lo estas haciendo bien",
    "menos es mas",
    "lo lograste",
]
sent_messages = []

send_messages(msg[:], sent_messages)
show_messages(msg)
show_messages(sent_messages)
print(len(sent_messages))
print(len(msg))


# Passing an arbitrary number of arguments
def make_pizza(*toppings):
    print(toppings)


make_pizza("pepperoni")
make_pizza("pepperoni", "mushrooms", "green peppers", "extra cheese")


def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"\t- {topping.title()}")


make_pizza("pepperoni")
make_pizza("pepperoni", "mushrooms", "green peppers", "extra cheese")


# Mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"\t- {topping}")


make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# Using arbitrary keyword arguments
def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "david", "campos", location="venezuela", field="computer science", age=28
)
print(user_profile)


# Exercise
def sandwich(*items):
    print(f"\nPreparing your sandwich:")
    for item in items:
        print(f"\t -{item.title()}.")


sandwich("pepperoni", "cheese", "pork", "tomato")
sandwich("hot sauce", "cheese", "pork", "tomato", "letucce", "onion")
sandwich("beef", "cheese", "tomato")


def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "david", "campos", age=28, city="El Tigre", country="Venezuela"
)

print(user_profile)


def make_car(manufacturer, model_name, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model_name"] = model_name
    return car_info


car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)

# Storing your functions in modules
"""Almacenar tus funciones en un archivo separado nos permite ocultar los detalles de nuestro programa y enfocarnos en la logica de alto nivel. Esto tambien nos permitira reusar las funciones en muchos programas diferentes. Cuando almacenamos nuestras funciones en archivos separados podemos compartir esos archivos con otros programadores sin tener que compartir todo el programa entero. Sabiendo como importar funciones tambien nos permite usar librerias que otros programadores han escrito."""

# Importing an entire module
"""Para empezar vamos a crear un modulo. Un modulo es un archivo que termina en .py que contiene el codigo que uno quiere importar a nuestro programa. En este caso vamos a crear el programa pizza.py y making_pizza.py"""

# Importing specific functions
"""Tambien podemos importar una funcion en especifico de un modulo. 
from module_name import function_name
Puedes importar tantas funciones como quieras de un modulo separando cada nombre de la funciones con una coma
from module_name import function_0, function_1, function_2 
"""

# Using as to give a function an alias
"""Si el nombre actual de la funcion que estas importando tiene un conflicto con un nombre existente en tu programa, o el nombre de la funcion es muy larga. Podemos usar un alias unico para esa funcion.
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

La manera general de usar los alias es:
from module_name import function_name as fn

"""

# Using as to give a module an alias
"""Tambien le podemos dar alias al modulo. Darle al modulo un alias corto como p for pizza, nos permitira llamar al modulo mas rapido. Llamando p.make_pizza() es mas conciso que llamar pizza.make_pizza():

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

Esto tambien nos permite redirigir nuestra atencion a los nombres descriptivos de sus funciones.

La sintaxis general para este enfoque es:
import module_name as mn
"""

# Import all functions in a module
"""Podemos decirle a python que importe todas las funciones de dicho modulo con el asterisco (*)

from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from module_name import *
"""

# Styling functions
"""
Nombres descriptivos: Las funciones deben tener nombres que expliquen claramente su propósito. Esto facilita que tú y otros programadores entiendan la intención del código.

Convenciones de escritura: Tanto los nombres de las funciones como los de los módulos deben escribirse exclusivamente con letras minúsculas y guiones bajos (nombre_de_mi_funcion).

Uso de docstrings: Cada función debe incluir un comentario conciso inmediatamente después de su definición, utilizando el formato de docstring (  '''comentario''').

Documentación autosuficiente: Un buen docstring debe permitir que otros programadores utilicen la función sin necesidad de leer el código interno. Solo necesitan conocer:

El nombre de la función.

Los argumentos que requiere.

El tipo de valor que devuelve.
"""


# Exercises: Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num_1, num_2):
    result = num_1 + num_2
    return result


print(add_two_numbers(2, 2))


# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    PI = 3.14
    result = PI * r**2
    return result


print(area_of_circle(4))


# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    for n in nums:
        if not isinstance(n, (int, float)):
            return "Please enter only numbers."
    result = sum(nums)
    return result


print(add_all_nums(4, 3, 1, 3))
print(add_all_nums(4, 3, "hola", 3))


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(c):
    f = c * 9 / 5 + 32
    return f


print(convert_celsius_to_fahrenheit(41))


# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    autumn = ["September", "October", "November"]
    winter = ["December", "January", "February"]
    spring = ["March", "April", "May"]
    summer = ["June", "July", "August"]
    if month.title() in autumn:
        return "Is Autumn"
    elif month.title() in winter:
        return "Is Winter"
    elif month.title() in spring:
        return "Is Spring"
    elif month.title() in summer:
        return "Is Summer"
    else:
        return "Please enter a valid month"


print(check_season("JuLy"))


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for i in lst:
        print(i)


summer = ["June", "July", "August"]
print_list(summer)


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list(["A", "B", "C"]))
# # ["C", "B", "A"]
def reverse_list(lst):
    empty_lst = []
    for i in lst[::-1]:
        empty_lst.append(i)
    return empty_lst


print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    capitalize_lst = []
    for i in lst:
        if i.isalpha():
            capitalize_lst.append(i.capitalize())
    return capitalize_lst


print(capitalize_list_items(["node", "express", "mongodB"]))


# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst, item):
    lst.append(item)
    return lst


# print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))
food_stuff = ["Potato", "Tomato", "Mango", "Milk"]
print(add_item(food_stuff, "Meat"))


# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, item):
    lst.remove(item)
    return lst


food_stuff = ["Potato", "Tomato", "Mango", "Milk"]
print(remove_item(food_stuff, "Mango"))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(nums):
    num = 0
    for i in range(nums + 1):
        num += i
    return num


print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100))  # 5050


# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    odds_nums = 0
    for i in range(num + 1):
        if i % 2 == 1:
            odds_nums += i
    return odds_nums


# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_evens(num):
    evens_nums = 0
    for i in range(num + 1):
        if i % 2 == 0:
            odds_nums += i
    return evens_nums


# Exercises: Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(num):
    evens = 0
    odds = 0
    for n in range(num + 1):
        if n % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The numbers of odds are: {odds}.\nThe numbers of evens are: {evens}."


print(evens_and_odds(100))


#     # The number of odds are 50.
#     # The number of evens are 51.
# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(nums):
    factorial_numbers = 1
    for n in range(1, nums + 1):
        factorial_numbers *= n
    return factorial_numbers


print(factorial(5))


# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(lst):
    len(lst) == 0
    return "Is empty"


hola = ["hola", "222"]
print(is_empty(hola))


# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(lst):
    mean = 0
    for i in lst:
        mean += i
    result = mean / len(lst)
    return result


print(calculate_mean([8, 9, 10, 7, 9]))


def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr


def calculate_median(arr):
    arr_sort = bubblesort(arr)
    n = len(arr_sort)
    half = n // 2
    if n % 2 != 0:
        return arr_sort[half]
    else:
        value_1 = arr_sort[half - 1]
        value_2 = arr_sort[half]
        return (value_1 + value_2) / 2


data = [15, 3, 7, 6, 1, 9]
print(f"Sort array: {bubblesort(data)}")
print(f"Mediam: {calculate_median(data)}")


def calculate_mode(data):
    frecuency = {}
    for value in data:
        frecuency[value] = frecuency.get(value, 0) + 1

    max_freq = max(frecuency.values())
    modes = [key for key, value in frecuency.items() if value == max_freq]
    return modes


def calculate_range(data):
    return max(data) - min(data)


def calculate_variance(data):
    if len(data) < 2:
        return 0
    n = len(data)
    mean = sum(data) / n
    deviations_squared = sum((x - mean) ** 2 for x in data)
    return deviations_squared / n


def calculate_std(data):
    variance = calculate_variance(data)
    return variance**0.5


mis_datos = [10, 12, 23, 23, 16, 23, 21, 16]

print(f"Moda: {calculate_mode(mis_datos)}")
print(f"Rango: {calculate_range(mis_datos)}")
print(f"Varianza: {calculate_variance(mis_datos):.2f}")
print(f"Desviación Estándar: {calculate_std(mis_datos):.2f}")


# Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
#     greet()
#     # "Hello, Guest!
#     greet("Alice")
#     # "Hello, Alice!"
def greet(name="Guest"):
    return f"Hello, {name}!"


greets = greet()
print(greets)
print(greet("David"))


# Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
# show_args(name="Alice", age=30, city="New York")
# # Received: name: Alice, age: 30, city: New York
# show_args(name="Bob", pet="Fluffy, the bunny")
# # Received: name: Bob, pet: Fluffy, the bunny
def show_args(**kwargs):
    items = [
        f"{key}: {value.title() if isinstance(value, str) else value}"
        for key, value in kwargs.items()
    ]
    result = ", ".join(items)
    return f"Received: {result}"


print(show_args(name="david", pet="nano", age=30))
print(show_args(name="david", pet="nano lalokita"))


# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.
def is_prime(numbers):
    if numbers < 2:
        return False
    for i in range(2, numbers):
        if numbers % i == 0:
            return False
    return True


print(is_prime(7))


# Write a functions which checks if all items are unique in the list.
def unique_items(arr):
    lst_len = len(arr)
    set_len = len(set(arr))
    return lst_len == set_len


# Write a function which checks if all the items of the list are of the same data type.
def same_data_type(arr):
    first_type = type(arr[0])
    for item in arr:
        if type(item) != first_type:
            return False
    return True


print(same_data_type([1, 2, 3]))


# Write a function which check if provided variable is a valid python variable
def valid_variable(var):
    return var.isidentifier()


print(valid_variable("1123"))
# Go to the data folder and access the countries-data.py file.
from data.countries_data import countries_data
from collections import Counter


# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_languages(data, n):
    spoken_languages = {}
    for country in data:
        for language in country["languages"]:
            spoken_languages[language] = spoken_languages.get(language, 0) + 1
    # return spoken_languages

    sorted_languages = sorted(
        spoken_languages.items(), key=lambda x: x[1], reverse=True
    )
    for k, v in sorted_languages[:n]:
        print(f"{k}: {v}")


most_spoken_languages(countries_data, 10)
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.


def most_populated_countries(data, n):
    country_population = {}
    for country in data:
        country_population[country["name"]] = country["population"]

    sorted_countries_population = sorted(
        country_population.items(), key=lambda x: x[1], reverse=True
    )

    for k, v in sorted_countries_population[:n]:
        print(f"{k}: {v}")


most_populated_countries(countries_data, 20)
