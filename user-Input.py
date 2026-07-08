# User Input Exercise
from os import name

# - Create a distance converter converting Km to miles

# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

name = input("Enter your name: ")
distance_km = float(input("Enter your distance in km: "))

distance_mile = distance_km / 1.609
print(f"Hello {name.title()} | Distance in Miles: {distance_mile:.2f} mile | Distance in KMs: {distance_km} km")