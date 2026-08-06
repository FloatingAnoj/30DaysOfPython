import math

age = 22
height = 70.0
complex_num = 32 +2j

base = float(input("input triangle base (as a number): "))
height = float(input("input the triangle's height (as a number): "))
print("The area of your triangle is ", 0.5 * base * height)

side_a = float(input("input the length of the first side of the triangle (as a number): "))
side_b = float(input("input the length of the second side of the triangle (as a number): "))
side_c = float(input("input the length of the third side of the triangle (as a number): "))

print("The perimeter of the triangle is: ", side_a + side_b + side_c)

length = float(input("what's the length of your rectangle (as a number): "))
width = float(input("what's the width of your rectangle (as a number): "))

print("the area of this rectangle is ", length * width)
print ("while the perimeter is ", length+width)

radius = float(input("what's the radius of your circle (as a number!!)"))

print("the radius of your circle is about", 3.14 * (radius **2))
print("the circumference is ", 2*3.14*radius)


# the slope of y = 2x-2 is 2, the y intercept is -2, and the x intercept is 0 = 2x-2 -> 2 =2x -> x = 1
# to find the euclidean distance between two points we use the formula sqrt((p1-q1)^2 + (p2-q2)^2))
# so for (2,2) and (6,10) we have

p1 = 2 # x1
p2 = 2 # y1
q1 = 6 # x2
q2 = 10 # y2

euclidean_distance = math.sqrt(((p1 - q1)**2) + ((q1 - q2)**2))
slope = (q2-p2)/(q1-p2)
print("the euclidean distance is", euclidean_distance )
print("the slope is", slope )
print("the slop formular subtracts the first from the second rather than the second from the first, like the euclidean distance formula")

x = 3
y = x**2 + 6*x + 9
print("this should be 0:", y)

# y = x^2 + 6x + 9
# y = (x + 3)(x + 3)
# y = x^2 + 3x +3x + 9

length_of_python= len("python")
length_of_dragon= len("dragon")

lengths_are_equal = length_of_dragon == length_of_python
print("are lengths of 'python' and 'dragon' equal?", lengths_are_equal)
on_found_in_both_words = "on" in "python" and "on" in "dragon"
print("is 'on' in both words 'python' and 'dragon'", on_found_in_both_words)
is_jargon_in_this_sentence = "jargon" in "I hope this course is not full of jargon"
print("is 'jargon' in 'I hope this course is not full of jargon", is_jargon_in_this_sentence)
on_not_found_in_both_words = "on" not in "python" and "on" not in "dragon"
print("is 'on' not found in both words 'python' and 'dragon'", on_not_found_in_both_words)

str(float(len('python')))

# you can use the modulo operator to check if theres a remainder when you divide by 2

print(7//3 == int(2.7))
print(type('10')==type(10)) 
print(int(float(('9.8'))) == 10) # should be false

hours = float(input("how many hours do you work a week?:"))
rate = float(input("what's your hourly rate?: "))
print("Your weekly earning is ", hours * rate)

years = float(input("Enter number of years you have lived:"))

# 365 just for estimate
print("you've lived for ", years * 365 * 24 * 60, "seconds")


for n in range(1, 6): 
    # calculate the powers from 0 to 3 in a list
    row = [n, n**0, n**1, n**2, n**3]
    # print the row elements joined by a space
    print(*(row))
