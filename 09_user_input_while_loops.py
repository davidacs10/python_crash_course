# User input while loops
# How the input() function works
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")

# prompt = "If you share your name, we can personalize the message you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print(f"\nHello, {name}!")
"""Este ejemplo nos muestra una manera de crear un string multilinea."""

# Using int() to accept numerical input
"""Cuando usamos la funcion input() python interpreta todo lo que ingresa el usuario como un string."""
# age = input("How old are you? ")
# print(type(age))
# print(age)

""">>> age = input("How old are you? ")
How old are you? 21
>>> age >= 18
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: '>=' not supported between instances of 'str' and 'int'"""
"""Tenemos que envolver el input con la funcion int() para que sea convertido de string a un valor int"""
# age = int(age)
# print(type(age))
# print(age >= 18)

# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# The modulo operator
"""Este modulo divide un numero entre otro numero y da como resultado el sobrante"""
print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)

# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")

# Exercise
# rental_car = input("What kind of rental car would you like? ")
# print(f"\nLet me see if I can find you a {rental_car}")

# restaurant = int(input("How many people are in their dinner group? "))
# if restaurant >= 8:
#     print("You'll have to wait for a table.")
# else:
#     print("Your table is ready.")

# multiples_of_ten = int(input("Enter a number: "))
# if multiples_of_ten % 10 == 0:
#     print("It is a multiple of ten")
# else:
#     print("Isn't a multiple of ten")

# Introducing while loops
"""El bucle for toma una coleccion de elementos y ejecuta un bloque de codigo una vez por cada elemento dentro de la coleccion. En caso, el bucle while se ejecuta mientras una determinada condicion sea cierta (True)."""

# The while loop in action
"""Puedes usar un bucle while para contar a traves de una serie de numeros por ejemplo, el siguiente bucle while cuenta desde 1 al 5."""

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Letting the user choose when to quit
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != "quit":
#     message = input(prompt)
#     if message == "quit":
#         break
#     print(message)

# Using a flag
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# # message = ""
# while active:
#     message = input(prompt)
#     if message == "quit":
#         active = False
#     else:
#         print(message)

# Using break to exit a loop
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#     city = input(prompt)

#     if city == "quit":
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# Using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(f"continue: {current_number}")

# Avoiding infinite loops
x = 1
while x <= 5:
    print(x)
    x += 1

"""Este bucle se ejecutara por siempre"""
# x = 1
# while x <= 5:
#     print(x)

# Exercise
# prompt = "\nPlease, enter all toppings you want in your pizza!"
# prompt += "\n(Enter 'quit' when you are finished.) "
# prompt += "\nAdd topping: "

# while True:
#     topping = input(prompt)

#     if topping == "quit":
#         break
#     else:
#         print(f"\nYou'll add {topping} to their pizza")

# active = True
# while active:
#     age = input("Enter your age: ").lower().strip()
#     if age == "quit":
#         break
#     else:
#         if not age.isdigit():
#             print("Please enter a valid age (numbers only).")
#             continue
#         elif int(age) <= 3:
#             print("Your ticket is free! Enjoy the movie!")
#         elif int(age) > 3 and int(age) <= 12:
#             print("Your ticket cost $10")
#         else:
#             print("Your ticket cost $15")

# Using a while loop with lists and dictionaries
"""El problema con for: Imagina que estás contando personas en una fila mientras la gente entra y sale. Te confundirías, ¿verdad? Python igual. Si intentas borrar o agregar elementos a una lista mientras un for la recorre, el programa puede saltarse elementos o dar errores.

La solución con while: El while es perfecto para situaciones donde el tamaño de la lista cambia. Es ideal para "vaciar" una lista de tareas pendientes y pasar los elementos a una lista de tareas terminadas."""

# Moving items from one list to another
"""Empieza con usuarios que necesitan ser verificados, y una lista vacia para almacenar los usuarios confirmados."""
# unconfirmed_users = ["alice", "brian", "candace"]
# confirmed_users = []

"""Verifica cada usuario hasta que no haya mas usuarios sin confirmar. Mueve cada usuario verificado hacia la lista de usuarios confirmados."""
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# """Muestra todos los usuarios confirmados"""
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# Removing all instances of specific values from a list
# pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
# print(pets)

# while "cat" in pets:
#     pets.remove("cat")

# print(pets)

# Filling a dictionary with user input
# responses = {}
# """Creamos una flag para indicar que la encuesta esta activa"""
# polling_active = True

# while polling_active:
#     """El prompt del nombre de la persona y la respuesta"""
#     name = input("\nWhat's your name? ")
#     response = input("Which mountain would you like to climb someday? ")

#     """Almacenamos la respuesta en el diccionario"""
#     responses[name] = response

#     """Averiguamos si alguien mas va a tomar la encuesta."""
#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == "no":
#         polling_active = False

# """La encuesta esta completada. Mostrar los resultados."""
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name.title()} would like to climb {response.title()}.")

sandwich_orders = [
    "cheese",
    "club house",
    "blt",
    "cubano",
    "tuna",
    "caprese",
    "roast beef",
]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(f"Your {sandwich.title()} is ready")

sandwich_orders = [
    "pastrami",
    "cheese",
    "club house",
    "blt",
    "cubano",
    "pastrami",
    "tuna",
    "caprese",
    "roast beef",
    "pastrami",
]

finished_sandwiches = []

print("deli has run out of pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == "pastrami":
        continue
    print(f"I made your {current_sandwich.title()}!")
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(f"Your {sandwich.title()} Sandwich is ready")

# responses = {}

# polling_active = True
# while polling_active:
#     username = input("What's your name: ")
#     response = input("If you could visit one place in the world, where would you go? ")

#     responses[username] = response

#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == "no":
#         polling_active = False

# print("\n----- Poll results -----")
# for name, response in responses.items():
#     print(f"{name.title()} would like to go to {response.title()} someday.")

# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
for n in range(11):
    print(n)

n = 0
while n < 11:
    print(n)
    n = n + 1

# Iterate 10 to 0 using for loop, do the same using while loop.
for n in range(10, -1, -1):
    print(n)

n = 10
while n >= 0:
    print(n)
    n -= 1
# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
for n in range(8):
    print("#" * n)

# Use nested loops to create the following:

# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
for n in range(8):
    for k in range(8):
        print("#", end=" ")
    print()

# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for n in range(11):
    print(f"{n} x {n} = {n*n}")

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
frameworks = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for i in frameworks:
    print(i)

# Use for loop to iterate from 0 to 100 and print only even numbers
for n in range(101):
    if n % 2 == 0:
        print(n)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for n in range(101):
    if n % 2 == 1:
        print(n)

# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
result = 0
for n in range(101):
    result += n
print(f"The sum of all numbers is: {result}.")

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even_numbers = 0
odd_numbers = 0
for n in range(101):
    if n % 2 == 0:
        even_numbers += n
    else:
        odd_numbers += n
print(
    f"The sum of all evens is {even_numbers}. And the sum of all odds is {odd_numbers}."
)

# The sum of all evens is 2550. And the sum of all odds is 2500.
# Exercises: Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from data.countries import countries

for country in countries:
    if country.endswith("land"):
        print(country)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ["banana", "orange", "mango", "lemon"]
reverse_list = []
for fruit in range(len(fruits) - 1, -1, -1):
    reverse_list.append(fruits[fruit])
print(reverse_list)

# Go to the data folder and use the countries_data.py file.
from data.countries_data import countries_data
from collections import Counter

# What are the total number of languages in the data
languages = set()
for country in countries_data:
    languages.update(country["languages"])

total_languages = len(languages)
print(f"Total of languages in data is: {total_languages}")
# Find the ten most spoken languages from the data
languages = []
# counter = {}
for country in countries_data:
    for language in country["languages"]:
        languages.append(language)

counter_languages = Counter(languages)


# for l in languages:
#     if l in counter:
#         counter[l] += 1
#     else:
#         counter[l] = 1
# ranking_ordenado = sorted(counter.items(), key=lambda item: item[1], reverse=True)
# print(counter)
# print(ranking_ordenado)
for language, total in counter_languages.most_common(10):
    print(f"{language}: {total}")
# Find the 10 most populated countries in the world
# population_countries = {}
# for country in countries_data:
#     population_countries[country["name"]] = country["population"]
top_10 = sorted(countries_data, key=lambda c: c["population"], reverse=True)[:10]
for i, country in enumerate(top_10, 1):
    name = country["name"]
    population = country["population"]
    print(f"{i}. {name}: {population:,}")
