import sys
import math

"""exercise level 2"""

# q1
print(sys.version)

#q2
print(3+3)
print(3-3)
print(9*2324)
print(3423%100)
print(34**2)
print(34//8)

#q3
print('jonathan')
print('silva')
print('usa')
print('i am enjoying 30 days of python')

#q4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asanbeneh','python','finland']))
print(type('jonathan'))
print(type('silva'))
print(type('usa'))

"""exercise lvl 3"""

print('Integer example')
print(type(3))
print('Float example')
print(type(34.0))
print('Complex example')
print(type(34+3j))
print('String example')
print(type('String example'))
print('Boolean example')
print(type(True))
print('List example')
print(type([3,2,3,4]))
print('Tuple example')
print(type((3,4,3,2,3)))
print('Set example')
print(type({3,4,5,6}))
print("Dictionary example")
print(type({"keyValue": 34,
            "keyValue2": 5,
            "keyValue": 7}))

# assuming two points p = (2,3) and q = (10,8)
# we can calculate the equclidean distance between the two points using the formula
# d(p,q) = sqrt((p1-q1)**2 + (p2 - q2)**2)

p1 = 2
p2 = 3
q1 = 10
q2 = 8

print(math.sqrt((p1-q1)**2 + (p2 - q2)**2))