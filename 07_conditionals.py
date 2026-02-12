# Conditionals

cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# Checking for equality
car = "bmw"
print(car == "bmw")

# Ignoring case when checking for equality
car = "Audi"
print(car.lower() == "audi")

# Checking for inequality
requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies!")

# Numerical comparisons
age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

# Checking multiple conditions
# Using "and" to check multiple conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

# Using "or" to check multiple conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

# Checking whether a value is in a list
requested_topping = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_topping)
print("pepperoni" in requested_topping)

# Checking whether a value is not in a list
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Boolean Expresions
game_active = True
can_edit = False

# Exercises

user = "david"
print("is user == 'david'? I predict True.")
print(user == "david")

print("is user == 'joseph'? I predict False.")
print(user == "joseph")

age = 18
print(f"is {user} an adult? I predict True ")
print(age >= 18)

age = 15
print(f"is {user} an adult? I predict False ")
print(age >= 18)

pet = "dog"
print(f"{user} have a dog? I predict True")
print(f"{user} have a dog? {pet == "dog"}")

print(f"{user} have a cat? I predict False")
print(f"{user} have a cat? {pet == "cat"}")

car = "toyota"
print(f"{user} have a toyota? I predict True")
print(f"{user} have a toyota? {car == "toyota"}")

print(f"{user} have a toyota? I predict False")
print(f"{user} have a toyota? {car == "audi"}")

balance = 100
print(f"{user} have more than 100 bucks? I predict True")
print(balance >= 100)

balance = 40
print(f"{user} have more than 100 bucks? I predict False")
print(balance >= 100)

user = "maria"
print(user == "maria")
print(user != "maria")

user = "daniela"
print(user == "Daniela".lower())

age = 20
print(f"{user.title()} is over 18? {age > 18}")
print(f"{user.title()} is younger than 18? {age < 18}")
print(f"{user.title()} is greater than or equal to 18? {age >= 18}")
print(f"{user.title()} is less than or equal to 18? {age <= 18}")

age_1 = 30
age_2 = 22
print(age_1 > 21 and age_2 > 21)
print(age_1 >= 40 or age_2 > 20)

names = ["david", "maria", "juan"]
print("david" in names)
print("carlos" not in names)

# if-else Statements
age = 18
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# the if-elif-else chain
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

age = 3
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

# Using multiple elif blocks
age = 18
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

# Omitting the else block
age = 18
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")

# Testing multiple conditions
requested_topping = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_topping:
    print("Adding mushrooms.")
if "pepperoni" in requested_topping:
    print("Adding pepperoni.")
if "extra cheese" in requested_topping:
    print("Adding extra cheese")
print("\nFinished making your pizza!")

"""Si queremos que un solo bloque de codigo se ejecute usamos la cadena if-elif-else. Si necesitamos ejecutar mas de un bloque de codigo debemos hacer varios if independientes."""

# Exercise
alien_color = "green"
if alien_color == "green":
    print("You've earned 5 points")
if alien_color == "blue":
    print("You've earned 1000 points")

alien_color = "red"
if alien_color == "green":
    print("You've earned 5 points")
elif alien_color != "green":
    print("You've earned 10 points")

alien_color = "yellow"
if alien_color == "green":
    print("You've earned 5 points")
elif alien_color == "yellow":
    print("You've earned 10 points")
elif alien_color == "red":
    print("You've earned 15 points")

# age = int(input("enter age: "))
if age < 2:
    print("Is a baby")
elif age >= 2 and age < 4:
    print("Is a toddler")
elif age >= 4 and age < 13:
    print("Is a kid")
elif age >= 13 and age < 20:
    print("Is a teenager")
elif age >= 20 and age < 65:
    print("Is an adult")
else:
    print("Is an elder")

fruits = ["mango", "orange", "lemon", "pineapple", "strawberry"]
if "mango" in fruits:
    print("mango is in fruits")
if "orange" in fruits:
    print("orange is in fruits")
if "lemon" in fruits:
    print("lemon is in fruits")
if "pineapple" in fruits:
    print("pineapple is in fruits")
if "strawberry" in fruits:
    print("strawberry is in fruits")

# Checking for special items
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")

# Checking that a list is not empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == "green peppers":
            print("Sorry, we are out of green peppers right now.")
        else:
            print(f"Adding {requested_topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# Using multiple lists
available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "extra cheese",
]

requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

# Exercise
usernames = ["admin", "david10", "jose10", "pedro1", "maria69"]
if usernames:
    for user in usernames:
        if user == "admin":
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")

current_users = [
    "admin",
    "david10",
    "jose10",
    "pedro1",
    "maria69",
    "henricus",
    "kladius",
]
current_users_lower = [user.lower() for user in current_users]
new_users = ["patrondog", "kladius", "henricus", "zizu", "cocox"]
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"{user} currently unavailable")
    else:
        print(f"{user} is available")

numbers = [*range(1, 10)]
for n in numbers:
    if n == 1:
        print(f"{n}st")
    elif n == 2:
        print(f"{n}nd")
    elif n == 3:
        print(f"{n}rd")
    else:
        print(f"{n}th")
print(numbers)

# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# user_age = int(input("Enter your age: "))
# if user_age >= 18:
#     print("You are old enough to learn to drive.")
# else:
#     print(f"You need {18 - user_age} more years to learn to drive.")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# my_age = int(input("Enter my age: "))
# your_age = int(input("Enter your age: "))
# if my_age - your_age == 1:
#     print(f"I'm {my_age - your_age} year older than you")
# elif my_age > your_age:
#     print(f"I'm {my_age - your_age} years older than you")
# elif your_age > my_age == 1:
#     print(f"I'm {your_age - my_age} year older than me")
# elif your_age > my_age:
#     print(f"You're {your_age - my_age} years older than me")
# else:
#     print("We have the same age")


# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# number_one = int(input("enter number one: "))
# number_two = int(input("enter number two: "))

# if number_one > number_two:
#     print(f"{number_one} is greather than {number_two}")
# elif number_one < number_two:
#     print(f"{number_one} is smaller than {number_two}")
# else:
#     print(f"{number_one} is equal to {number_two}")

# Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# student_score = float(input("Enter score: "))
# if student_score >= 90 and student_score <= 100:
#     print("A")
# elif student_score >= 80 and student_score < 90:
#     print("B")
# elif student_score >= 70 and student_score < 80:
#     print("C")
# elif student_score >= 60 and student_score < 70:
#     print("D")
# elif student_score >= 0 and student_score < 60:
#     print("F")


# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]
# user_month = input("Enter month: ").title()

# if user_month in autumn:
#     print("Is Autumn")
# elif user_month in winter:
#     print("Is Winter")
# elif user_month in spring:
#     print("Is Spring")
# elif user_month in summer:
#     print("Is Summer")
# else:
#     print("Please enter a valid month")


# The following list contains some fruits:
fruits = ["banana", "orange", "mango", "lemon"]
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
# user_input = input("Enter fruit: ").lower()
# if user_input not in fruits:
#     fruits.append(user_input)
#     print(fruits)
# else:
#     print("That fruit already exist in the list")

# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
person = {
    "first_name": "David",
    "last_name": "Campos",
    "age": 28,
    "country": "Venezuela",
    "is_married": False,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person:
    mid_skill = len(person["skills"]) // 2
    print(person["skills"][mid_skill])

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person:
    if "Python" in person["skills"]:
        print("Python")

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
person = {
    "first_name": "David",
    "last_name": "Campos",
    "age": 28,
    "country": "Venezuela",
    "is_married": False,
    "skills": ["JavaScript", "React"],
    "address": {"street": "Space street", "zipcode": "02210"},
}


if "skills" in person:
    user_skills = set(person["skills"])
    if user_skills == {"JavaScript", "React"}:
        print("He is a frontend developer")
    elif {"Node", "Python", "MongoDB"}.issubset(user_skills):
        print("He is a backend developer")
    elif {"React", "Node", "MongoDB"}.issubset(user_skills):
        print("He is a fullstack developer")
    else:
        print("Unknow title")

#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
if person["is_married"] == False and person["country"] == "Venezuela":
    print(
        f"{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He isn't married"
    )
