# Lists

"""Las listas son una coleccion de elementos ordenados y modificables, es decir mutables. Podemos hacer listas que almacenen las letras del abecedario, numeros o simplemente los nombres de los integrantes de nuestra familia. Las listas pueden estar vacias o pueden tener diferentes tipos de datos(string, boolean, int, float)"""

# Creating lists
"""Se pueden crear de dos formas"""
lst = list()  # Es igual a una lista vacia.
print(lst)

lst_1 = []
print(lst_1)  # Otra lista vacia, pero declarada con corchetes.

"""Las listas suelen contener mas de un elemento. Asi que al declararlas es recomendable que sus nombres sean en plural. (letters, digits, names)."""
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

# Accessing Elements in a List
"""Las listas son colecciones ordenadas, es decir, que podemos acceder a cualquier elemento de la lista mediante su posicion o el index del elemento deseado. Para acceder a ese elemento solo debemos escribir el nombre de la lista seguido del numero de su posicion entre corchetes[]. Cabe resaltar que los indices de las listas empiezan en 0 y no en 1. Por ejemplo, 0,1,2,3,4,5,6,7,8"""
print(bicycles[0])
"""Tambien podemos agregar metodos a nuestra lista, en este caso ya que nuestra lista contiene strings, podemos usar sus respectivos metodos"""
print(bicycles[0].title())
"""Si queremos acceder al ultimo elemento de la lista sin saber cual es su posicion podemos hacerlo mediante la posicion o index [-1]. [-1] representa el ultimo elemento de la lista, tambien si queremos acceder al antepenultimo seria [-2], y asi sucesivamente."""
print(bicycles[-1].title())

# Using Individual Values from a List.
"""Podemos usar los elementos individuales de una lista como si fuesen otra variable"""
message = f"Mi primera bicicleta fue una {bicycles[0].title()}"
print(message)

# Exercises
friends = ["Daniel", "Juan", "Pedro", "Carlos", "Mbappe"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
greetins = "Hola, mi pana"
print(f"{greetins} {friends[0]}")
print(f"{greetins} {friends[1]}")
print(f"{greetins} {friends[2]}")
print(f"{greetins} {friends[3]}")
print(f"{greetins} {friends[4]}")
own_list = ["PS5", "RTX 5090", "Ryzen 9950X3D"]
message = "Me gustaria tener un"
print(f"{message} {own_list[0]}")
print(f"{message} {own_list[1]}")
print(f"{message} {own_list[2]}")

# Modifying, Adding, and Removing Elements
"""La mayoria de las listas que crearemos seran dinamicas, es decir, que podremos modificarla añadiendo o eliminando elementos desde el momento en el que se empieza a ejecutar el programa."""

# Modifying Elements in a List
"""La manera que podemos modificar un elemento de una lista es similar a la que accedemos a su posicion o indice en la lista."""
motorcycles = ["Honda", "Yamaha", "Suzuki"]
print(motorcycles)
motorcycles[0] = "Ducati"
print(motorcycles)

# Adding Elements to a List
"""Podemos hacer que aparezcan nuevos elementos en nuestra lista y para eso existen muchas formas de hacerlo."""

## Appending Elements to the End of a List
"""La manera mas sencilla de hacerlo es agregando un nuevo elemento al final de la lista usando el metodo append()"""
motorcycles = ["Honda", "Yamaha", "Suzuki"]
motorcycles.append("Ducati")
print(motorcycles)
fruits = ["banana", "orange", "mango", "lemon"]
fruits.append("apple")
print(fruits)
"""Con el metodo append() es una de las maneras mas faciles de crear listas dinamicas. Por ejemplo, creamos una lista vacia y podemos ir agregandole elementos."""
motorcycles = []
motorcycles.append("Honda")
motorcycles.append("Yamaha")
motorcycles.append("Suzuki")
print(motorcycles)

## Inserting Elements into a List
"""Podemos agregar elementos en cualquier posicion con el metodo insert(). Con este metodo especificamos primero el indice donde queremos agregar el elemento y luego el elemento que deseamos agregar."""
motorcycles = ["Honda", "Yamaha", "Suzuki"]
motorcycles.insert(1, "Ducati")
print(motorcycles)

# Removing Elements from a List
"""Cuando queremos eliminar un elemento o un conjunto de elementos de una lista. Podemos hacerlo segun su posicion en la lista o segun su valor"""

## Removing an Item Using the del Statement
"""Si sabemos la posicion del item en la lista podemos usar la declaracion del"""
motorcycles = ["Honda", "Yamaha", "Suzuki"]
del motorcycles[0]
print(motorcycles)

## Removing an Item Using the pop() Method
"""El metodo pop() nos permite borrar un elemento cuando se especifica su indice, o se elimina el ultimo elemento de la lista en caso de que el indice no sea especificado."""
motorcycles = ["Honda", "Yamaha", "Suzuki"]
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

"""Con el segundo print nos damos cuenta que aun tenemos acceso al item eliminado de la lista"""
"""Tambien nos puede ser util para indicarnos cual es el ultimo elemento de la lista como por ejemplo"""
motorcycles = ["Honda", "Yamaha", "Suzuki"]
last_owned = motorcycles.pop()
print(f"La ultima motocicleta que adquirimos fue {last_owned}")

"""Ahora usaremos el metodo pop() segun el indice del elemento en nuestra lista"""
first_owned = motorcycles.pop(0)
print(f"La primera motocicleta que adquirimos fue {first_owned}")

"""Es importante tener en cuenta que cada vez que usamos el metodo pop(), ese elemento no estara almacenado en la lista. Si no estas seguro si usar la declaracion del o el metodo pop(), solo debes saber que quieres hacer con el elemento. Si quieres eliminarlo de la lista y no usarlo mas nunca usa la declaracion del, si quieres usar el item despues de haberlo removido de la lista usa pop()"""

## Removing an Item by Value
"""En ocasiones no vas a saber la posicion del elemento que deseas eliminar, pero si sabes el valor del elemento puedes usar el metodo remove()"""
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)

"""Podemos usar el metodo remove()"""
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# Exercises
people = ["Pedro", "Carlos", "Armani"]
invite_message = "te gustaria venir a cenar a mi casa?"
print(f"{people[0]}, {invite_message}")
print(f"{people[1]}, {invite_message}")
print(f"{people[2]}, {invite_message}")
print(f"{people[0]} no podra venir a la cena.")
people[0] = "Alex"
print(f"{people[0]}, {invite_message}")
print(f"{people[1]}, {invite_message}")
print(f"{people[2]}, {invite_message}")
print("Encontre una mesa mas grande para tener mas invitados")
people.insert(0, "Juan")
people.insert(len(people) // 2, "Maria")
people.append("CrisMJ")
print(f"{people[0]}, {invite_message}")
print(f"{people[1]}, {invite_message}")
print(f"{people[2]}, {invite_message}")
print(f"{people[3]}, {invite_message}")
print(f"{people[4]}, {invite_message}")
print(f"{people[5]}, {invite_message}")
print(
    "Solo puedo invitar a 2 personas a cenar porque no me pudieron hacer la reservacion de la mesa"
)
people.pop()
people.pop()
people.pop()
people.pop()
still_invited = "aun sigues invitado a cenar"
print(f"{people[0]}, {still_invited}")
print(f"{people[1]}, {still_invited}")
del people[0]
del people[0]
print(people)

# Sorting a List
"""sort() modifica la lista original"""
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)
print(cars)
"""sorted() retorna una lista ordenada sin modificar la original"""
cars = ["bmw", "audi", "toyota", "subaru"]
print("Lista original")
print(cars)
print("\nLista ordenada")
print(sorted(cars))
print("\nLista original de nuevo")
print(cars)

# Reverse Order
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
cars.reverse()
print(cars)

# Length of a List
cars = ["bmw", "audi", "toyota", "subaru"]
print(len(cars))

# Exercises
places = ["Shibuya", "Nagasaki", "Yokohama", "Osaka", "Nagoya"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

people = ["Pedro", "Carlos", "Armani"]
print(len(people))

# Declare an empty list
lst = []
lst = list()

# Declare a list with more than 5 items
things = ["Phone", "GPU", "CPU", "TV", "Python"]
# Find the length of your list
print(len(things))
# Get the first item, the middle item and the last item of the list
print(things[0])
print(things[len(things) // 2])
print(things[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["David", 28, 1.75, False, "Caracas"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(companies)

# Print the number of companies in the list
print(len(companies))

# Print the first, middle and last company
print(companies[0])
print(companies[len(companies) // 2])
print(companies[-1])

# Print the list after modifying one of the companies
companies[len(companies) // 2] = "Sony"
print(companies)

# Add an IT company to it_companies
companies.append("Apple")

# Insert an IT company in the middle of the companies list
companies.insert(len(companies) // 2, "Samsung")

# Change one of the it_companies names to uppercase (IBM excluded!)
companies[3] = companies[3].upper()
print(companies)

# Join the it_companies with a string '#;  '
it_companies = "#;  ".join(companies)
print(it_companies)

# Check if a certain company exists in the it_companies list.
print("Amazon" in companies)

# Sort the list using sort() method
companies.sort()
print(companies)

# Reverse the list in descending order using reverse() method
companies.reverse()
print(companies)

# Slice out the first 3 companies from the list
first_3 = companies[0:3]
print(first_3)

# Slice out the last 3 companies from the list
last_3 = companies[-3:]
print(last_3)

# Slice out the middle IT company or companies from the list
middle_company = companies[len(companies) // 2]
print(middle_company)

# Remove the first IT company from the list
companies.pop(0)

# Remove the middle IT company or companies from the list
del companies[len(companies) // 2]

# Remove the last IT company from the list
companies.pop()

# Remove all IT companies from the list
companies.clear()
print(companies)

# Destroy the IT companies list
del companies

# Join the following lists:

front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
front_end.extend(back_end)
print(front_end)
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end
full_stack.append("Python")
full_stack.append("SQL")
print(full_stack)

# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
print(ages)

# Add the min age and the max age again to the list
ages.append(min(ages))
ages.append(max(ages))
print(ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
print(ages)
middle_item = ages[len(ages) // 2]
print(middle_item)
median_age = middle_item / 2
print(median_age)

import statistics

print(statistics.median(ages))

# Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)
print(average_age)
# Find the range of the ages (max minus min)
range_ages = max(ages) - min(ages)
print(range_ages)
# Compare the value of (min - average) and (max - average), use abs() method
min_average = abs(min(ages) - average_age)
max_average = abs(max(ages) - average_age)
print(min_average)
print(max_average)
# Find the middle country(ies) in the countries list
from countries import countries as countries_list

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
middle_countries_list = len(countries_list) // 2
first_half = countries_list[: middle_countries_list + 1]
print(first_half)
second_half = countries_list[middle_countries_list + 1 :]
print(second_half)
print(f"first half has: {len(first_half)}")
print(f"second half has: {len(second_half)}")
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries_pack = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
cn, rs, us, *scandic_countries = countries_pack
print(scandic_countries)
