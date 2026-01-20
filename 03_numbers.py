# Numbers

# Integers - Numeros enteros
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)
print(3**2)
print(3**3)
print(10**6)
print(2 + 3 * 4)
print((2 + 3) * 4)

# Floats - Numeros decimales
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)
print(0.2 + 0.1)
print(3 * 0.1)

# Integers and Floats
"""Cuando se dividen dos numeros int, su resultado sera un float asi sea un integer"""
print(4 / 2)
"""Cuando se realizan operaciones entre int y float siempre el resultado sera un float. El float va a prevalecer, inclusive si el resultado es un int"""
print(1 + 2.0)
print(2 * 3.0)
print(3.0**2)

# Underscores in numbers
"""Cuando escribimos numeros demasiado grandes podemos agregarle underscores para hacer los numeros mas legibles"""
universe_age = 14_000_000_000
"""Cuando esto se imprime el resultado sera:"""
print(universe_age)
"""Python ignora los underscores cuando ese tipo de valores son almacenados. Inclusive si no los agrupas correctamente, el los ignora. Por ejemplo, 1_000 es lo mismo que 10_00"""

# Multiple Assignment
"""Se pueden asignar mas de un valor a una variable para hacer nuestros programas mas cortos y mas faciles de leer"""
x, y, z = 0, 1, 2

# Constants
"""Una constante es una variable que mantendra su valor igual durante toda la ejecucion del programa. Es decir, esa variable no puede cambiar. Para declarar esta variable se escribe en mayusculas."""
MAX_CONNECTIONS = 5000
PI = 3.14

# Exercise:
# Number Eight
print(5 + 3)
print(10 - 2)
print(4 * 2)
print(16 / 2)

# Favorite Number
favorite_number = 10
message = "Mi numero favorito es:"
print(f"{message} {favorite_number}")
