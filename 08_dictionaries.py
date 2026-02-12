# DICTIONARIES
# A simple dictionary
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])

# Working with dictionaries
alien_0 = {"color": "green"}

# Accesing values in a dictionary
print(alien_0["color"])
"""Puedes tener un numero ilimitado de llaves-valor"""
alien_0 = {"color": "green", "points": 5}
new_points = alien_0["points"]
print(f"You just earned {new_points} points!")

# Adding new key-value pairs
"""Los diccionarios son estructuras dinamicas y podemos agregarle nuevas llaves-valor en cualquier momento."""
print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# Starting with an empty dictionary
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)
"""A menudo usaremos diccionarios vacios donde se almacenaran los datos que ha suministrado un usuario."""

# Modifying values in a dictionary
"""Para modificar un valor en un diccionario, usamos el nombre del diccionario seguido de los corchetes, luego el nuevo valor asociado a esa llave."""
alien_0 = {"color": "green"}
print(f"The alien is {alien_0["color"]}")
alien_0["color"] = "yellow"
print(f"The alien is {alien_0["color"]}")

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_0["x_position"]}")

# Mueve el alien a la derecha
# Determina que tanto se mueve el alien basado en su velocidad actual.
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

# La nueva posicion es la posicion anterior mas el incremento de velocidad.
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New position: {alien_0["x_position"]}")

# Removing Key-Value pairs
alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0["points"]
print(alien_0)

# A dictionary of similar objects
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}")

# Using get() to access values
"""Si usamos los corchetes para recibir el valor de dicha llave podria causar un error potencial: Si el valor no existe podriamos obtener un error."""
alien_0 = {"color": "green", "speed": "slow"}
# print(alien_0["points"])

"""El metodo get() requiere una key como primer valor, el segundo valor es opcional el cual puede retornar un valor si la key no existe."""
point_value = alien_0.get("points", "No point value assigned.")
print(point_value)

# Exercise
person_info = {
    "first_name": "david",
    "last_name": "campos",
    "age": 28,
    "city": "El Tigre",
}
print(person_info["first_name"])
print(person_info["last_name"])
print(person_info["age"])
print(person_info["city"])

favorite_numbers = {
    "david": 7,
    "jose": 10,
    "carlos": 18,
    "juan": 22,
    "mbappe": 20,
}
print(f"David favorite number is: {favorite_numbers['david']}")
print(f"Jose favorite number is: {favorite_numbers['jose']}")
print(f"Carlos favorite number is: {favorite_numbers['carlos']}")
print(f"Juan favorite number is: {favorite_numbers['juan']}")
print(f"Mbappe favorite number is: {favorite_numbers['mbappe']}")

# Looping through a dictionary
user_0 = {
    "username": "davidacs",
    "first": "david",
    "last": "campos",
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping Through all the keys in a dictionary
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for name in favorite_languages.keys():
    print(name.title())

"""Hacer un bucle a traves de las keys, es en realidad el comportamiento por defecto cuando hacemos un bucle a traves de un diccionario.

for name in favorite_languages:

es lo mismo que:

for name in favorite_languages.keys()
"""
friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

    if "erin" not in favorite_languages.keys():
        print("Erin, please take our poll!")

# Looping through a dictionary's keys in a particular order
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping through all values in a dictionary
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

"""Para solo mostrar los lenguages en el diccionario sin que se repitan usamos un set. Un set es una coleccion donde cada item deberia ser unico."""

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# Exercise
rivers = {
    "nile": "egypt",
    "amazonas": "south america",
    "mississippi": "united states",
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

for river in rivers.keys():
    print(river.title())

for river in rivers.values():
    print(river.title())

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

user_list = ["jen", "david", "sarah", "maria", "edward"]

for name in user_list:
    print(f"Hi {name.title()}")

    if name in favorite_languages.keys():
        print(f"I'm happy to see you, {name.title()}\n")
    if name not in favorite_languages.keys():
        print(f"Please {name.title()} I suggest you to take the poll\n")

# Nesting
## A list of dictionaries
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

"""Creamos una lista vacia para almacenar los aliens"""
aliens = []

"""Crea 30 aliens verdes"""
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15


"""Muestra los primeros 5 aliens"""
for alien in aliens[:5]:
    print(alien)
print("...")

"""Muestra cuantos aliens se han creado"""
print(f"Total number of aliens: {len(aliens)}")

# A list in a dictionary
"""Almacenamos informacion sobre la pizza que esta siendo ordenada"""
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}

"""Resumen de la orden"""
print(f"You ordered a {pizza["crust"]}-crust pizza " "with the following toppings:")

for topping in pizza["toppings"]:
    print(f"\t{topping}")

favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
    "david": ["python"],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is: {languages[0].title()}")

# A dictionary in a dictionary
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info["first"]} {user_info["last"]}"
    location = f"{user_info["location"]}"
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# Exercises
person_0 = {
    "first": "david",
    "last": "campos",
    "country": "venezuela",
}
person_0["city"] = "el tigre"
person_1 = {
    "first": "maria",
    "last": "garcia",
    "country": "colombia",
}
person_2 = {
    "first": "gary",
    "last": "doe",
    "country": "united states",
}

people = [person_0, person_1, person_2]
for person in people:
    full_name = f"{person['first']} {person['last']}"
    country = f"{person['country']}"
    print(f"Full name: {full_name.title()}\nCountry: {country.title()}")

for person in people:
    print(f"Information about {person['first'].title()}:")
    for key, value in person.items():
        print(f"\t{key.capitalize()}: {value.title()}")

pet_0 = {
    "name": "lala",
    "type": "dog",
    "owner": "david",
    "breed": "akita",
    "age": 3,
}
pet_1 = {
    "name": "nano",
    "type": "cat",
    "owner": "jose",
    "breed": "american shorthair",
    "age": 5,
}
pet_2 = {
    "name": "lane",
    "type": "mitchell",
    "owner": "coco",
    "breed": "callejero",
    "age": 2,
}
pet_3 = {
    "name": "lobo",
    "type": "dog",
    "owner": "benito",
    "breed": "airedale terrier",
    "age": 1,
}

pets = [pet_0, pet_1, pet_2, pet_3]
for pet in pets:
    print(f"Information about: {pet['name'].title()}")
    for key, value in pet.items():
        if key == "name":
            continue
        if isinstance(value, str):
            print(f"\t{key.capitalize()}: {value.title()}")
        else:
            print(f"\t{key.capitalize()}: {value}")

favorite_places = {
    "david": ["tokyo", "sydney", "caracas"],
    "jose": ["barcelona", "paris", "amsterdam"],
    "carlos": ["londres", "bruselas", "kyoto"],
    "juan": ["londres"],
}
for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"\n{name.title()}, what's your favorites places?")
        print(f"Hi, I'm {name.title()} and my favorites places are:")
    else:
        print(f"\n{name.title()}, what's your favorite place?")
        print(f"Hi, I'm {name.title()} and my favorite place is:")
    for place in places:
        print(f"\t- {place.title()}\n")

favorite_numbers = {
    "david": [
        7,
        10,
        18,
    ],
    "jose": [
        10,
        11,
        12,
        15,
    ],
    "carlos": [
        18,
        44,
        33,
        11,
        23,
        54,
    ],
    "juan": [
        22,
        29,
        40,
        5,
        66,
        100,
    ],
    "mbappe": [
        20,
        99,
        33,
        11,
        22,
    ],
}
for names, numbers in favorite_numbers.items():
    print(f"{names.title()}'s favorite numbers are: ", *numbers)

for names, numbers in favorite_numbers.items():
    numbers_string = ", ".join(str(n) for n in numbers)
    print(f"{names.title()}'s favorite numbers are: {numbers_string}")

for names, numbers in favorite_numbers.items():
    print(f"{names.title()}'s favorite numbers are: ")
    for number in numbers:
        print(f"\t- {number}")

cities = {
    "tokyo": {
        "country": "japan",
        "population": 37400068,
        "fact": "It is the most populous metropolitan area in the world.",
    },
    "paris": {
        "country": "france",
        "population": 2161000,
        "fact": "It is known as the 'City of Light' (La Ville Lumière).",
    },
    "caracas": {
        "country": "venezuela",
        "population": 2082000,
        "fact": "It is located in a beautiful valley at the foot of the Avila mountain.",
    },
}

for city, city_info in cities.items():
    print(f"\n{city.title()}:")
    for key, value in city_info.items():
        if isinstance(value, str):
            print(f"\t{key.capitalize()} : {value.title()}")
        else:
            print(f"\t{key.capitalize()} : {value}")


# Create an empty dictionary called dog
dog = {}
print(type(dog))

# Add name, color, breed, legs, age to the dog dictionary
dog = {
    "name": "nano",
    "color": "grey",
    "breed": "wolf",
    "legs": 4,
    "age": 4,
}

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "david",
    "last_name": "campos",
    "gender": "male",
    "age": 28,
    "is_married": False,
    "skills": ["python", "javascript", "sql"],
    "country": "venezuela",
    "city": "caracas",
    "address": {
        "street": "space street",
        "zip_code": 10101,
    },
}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
skills = student.get("skills")
print(skills)
print(type(skills))

# Modify the skills values by adding one or two skills
skills.append("mongodb")
skills.append("fastapi")
print(skills)

# Get the dictionary keys as a list
keys = student.keys()
print(keys)

# Get the dictionary values as a list
values = student.values()
print(values)

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
del student["address"]
print(student.items())

# Delete one of the dictionaries
del student
