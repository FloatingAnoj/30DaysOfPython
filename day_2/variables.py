import math

"""Day 2: 30 Days of python programming"""
# Exercises level 1:

first_name = input("what's your first name? : ")
last_name = input("what's your last name? : ")
full_name = first_name + " " + last_name
country = input("what's your country? :")
city = "Austin"
age = input("what's your age? :")
year = 2026
is_married = False
is_true = True
is_light_on = True
sport, book, computer = "Basketball", "The Odyssey", "MacBook Pro"

# Exercises level 2:
# I'm not about to type print (type for all of these again..)

list_of_variables = [first_name, last_name, full_name, country, city, age, year, is_married, is_light_on, is_true, sport, book, computer]

for var in list_of_variables:
    print(var, "type is:", type(var))

first_name_length = len(first_name)
last_name_length = len(last_name)

if (first_name_length > last_name_length):
    print('first name is longer than last')
elif (first_name_length < last_name_length): 
    print("first name is shorter than last name")
else: 
    print("both first name and last name same length")

num_one = 5
num_two = 4

total = num_one + num_two

diff = num_one - num_two

product = num_one * num_two

division = num_one / num_two

remainder = num_two % num_one

exp = num_one ** num_two

floor_division = num_one // num_two

radius = int(input("what's the radius of your circle? : "))
area = math.pi*(radius ** 2)
circumference = 2*math.pi*radius

print(help('keywords'))

