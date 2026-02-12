# Looping Through an Entire List
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

# Doing More Work Within a for Loop
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    # Doing Something After a loop
print("Thank you, everyone. That was a great magic show!\n")

# Exercises
pizza_list = ["margarita", "peperoni", "napolitana"]
for i in pizza_list:
    print(i)

for i in pizza_list:
    print(f"I like so much pizza {i}")
print("I really love pizza")

animals = ["Dog", "Cat", "Wolf"]
for animal in animals:
    print(animal)

for animal in animals:
    print(f"{animal} would make a great pet")

print("Those animals have four legs")

# Using the range() Function
for value in range(1, 5):
    print(value)
"""off-by-one behavior"""

for value in range(1, 6):
    print(value)

# Using range() to Make a List of Numbers
numbers = list(range(1, 6))
print(numbers)

"""Print even numbers"""
even_numbers = list(range(2, 11, 2))
print(even_numbers)

"""square list"""
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

"""to write more concisely"""
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)

# Exercises
for n in range(1, 21):
    print(n)

# for n in range(1, 1000001):
#     print(n)

numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

for n in range(1, 21, 2):
    print(n)

threes_list = []
for n in range(1, 11):
    threes_list.append(n * 3)
print(threes_list)

for n in range(1, 11):
    print(n**3)

cubes = [n**3 for n in range(1, 11)]
print(cubes)

# Working with Part of a List

## Slicing a List
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
print(players[1:4])
print(players[0:4])
print(players[2:])
print(players[-3:])

## Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

## Copying a List
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
my_foods.append("cannoli")
friend_foods.append("ice cream")
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
print(id(my_foods))
print(id(friend_foods))

# Exercises
food = ["eggs", "milk", "spagetti", "rice", "meat", "chicken", "bread"]
print(f"Food list items: {food}")
print(f"The first three items in the list are: {food[:3]}")
print(
    f"The items from the middle of the list are: {food[(len(food) // 2)-1:(len(food) // 2)+2]}"
)
print(f"The last three items in the list are: {food[-3:]}")

friend_pizza = pizza_list[:]
pizza_list.append("hawaina")
friend_pizza.append("fugazza")
print("My favorite pizzas are:")
for pizza in pizza_list:
    print(pizza.title())
print("My friend's favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza.title())
print("My list of ingredients:")
for ingredient in food:
    print(ingredient.title())
