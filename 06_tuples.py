# TUPLES
# Create a tuple
empty_tuple = ()
empty_tuple = tuple()
fruits = ("banana", "orange", "mango", "lemon")

# Tuple length
tpl = ("item1", "item2", "item3")
print(len(tpl))

# Accessing tuple items
tpl = ("item1", "item2", "item3")
first_item = tpl[0]
second_item = tpl[1]

fruits = ("banana", "orange", "mango", "lemon")
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Negative indexing
tpl = ("item1", "item2", "item3")
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

# Slicing tuples
tpl = ("item1", "item2", "item3", "item4")
all_items = tpl[0:4]
all_items = tpl[0:]
middle_two_items = tpl[1:3]

fruits = ("banana", "orange", "mango", "lemon")
all_fruits = fruits[0:4]
all_fruits = fruits[0:]
orange_mango = fruits[1:3]
orange_to_the_rest = fruits[1:]

# Range of Negative Indexes
tpl = ("item1", "item2", "item3", "item4")
all_items = tpl[-4:]
middle_two_items = tpl[-3:-1]

fruits = ("banana", "orange", "mango", "lemon")
all_fruits = fruits[-4:]
orange_mango = fruits[-3:-1]
orange_to_the_rest = fruits[-3:]

# Changing tuples to list
tpl = ("item1", "item2", "item3", "item4")
lst = list(tpl)

fruits = ("banana", "orange", "mango", "lemon")
fruits = list(fruits)
fruits[0] = "apple"
print(fruits)
fruits = tuple(fruits)
print(fruits)

# Checking an Item in a tuple
tpl = ("item1", "item2", "item3", "item4")
print("item2" in tpl)

fruits = ("banana", "orange", "mango", "lemon")
print("orange" in fruits)
print("apple" in fruits)

# Joining Tuples
tpl1 = ("item1", "item2", "item3")
tpl2 = ("item4", "item5", "item6")
tpl3 = tpl1 + tpl2

fruits = ("banana", "orange", "mango", "lemon")
vegetables = ("Tomato", "Potato", "Cabbage", "Onion", "Carrot")
fruits_and_vegetables = fruits + vegetables

# Deleting tuples
tpl1 = ("item1", "item2", "item3")
del tpl1

fruits = ("banana", "orange", "mango", "lemon")
del fruits

# ---------------------------------------------------------------#
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping Through all values in a tuple
for dimension in dimensions:
    print(dimension)

# Writing over a tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

"""Usa las tuplas cuando quieras almacenar un conjunto de valores que no deberian cambiar a lo largo de la ejecucion del programa."""

# Exercises
restaurant_menu = ("Pizza", "Spagetti", "Cake", "Cookie", "Burger")
for food in restaurant_menu:
    print(food)
# restaurant_menu[0] = "Hot Dog"
restaurant_menu = ("Pizza", "Spagetti", "rice", "hot dog", "Burger")
for food in restaurant_menu:
    print(food)

# Exercises: Level 1
# Create an empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Leon", "Kennedy", "David")
sisters = ("Maria", "Valeria")

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.append("Flor")
siblings.append("Arcadio")
family_members = siblings
family_members = tuple(family_members)
print(family_members)

# Exercises: Level 2
# Unpack siblings and parents from family_members
siblings = family_members[:5]
parents = family_members[5:]
print(siblings)
print(parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("orange", "apple", "mango")
vegetables = ("potato", "tomato", "onion")
animal_products = ("meat", "chicken", "egg")
food_stuff_tp = fruits + vegetables + animal_products

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_items = len(food_stuff_tp) // 2
print(middle_items)
print(food_stuff_tp[middle_items])

# Slice out the first three items and the last three items from food_stuff_lt list
first_three_items = food_stuff_tp[:3]
last_three_items = food_stuff_tp[-3:]
print(first_three_items)
print(last_three_items)

# Delete the food_stuff_tp tuple completely
del food_stuff_tp
# Check if an item exists in tuple:
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
# Check if 'Estonia' is a nordic country
print("Estonia" in nordic_countries)
# Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries)
