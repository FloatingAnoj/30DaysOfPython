"""PYTHON BACKGROUND"""

# python was created by Guido van Rossum
# first released in 1991
# an interpreted scripting language
    # this means it does not need to be compiled
    # it executes the code line by line in the shell

"""ENTERING AND EXITING THE PYTHON SHELL"""
# you enter the shell by writing python, though for your purposes use python3
    # after you open the shell with the python command you're greeted with these lines
    # >>>
    # this is where you write the code that will be executed..
        # for example

        # >>> 2+3
        # 5

# you type exit() to exit the shell


"""DIFFERENT DATA TYPES"""
# Integer: Integer (negative, zero, and postiive) numbers
integer_examples = [-3, -2, -1, 0, 1, 2, 3]

# Float: Decimal number
float_examples = [-3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5]

# Complex nums:
complex_num_examples = [1 + 1j, 2 + 4j]

# Strings:
    # A collection of one or more characters under a single OR double quote
        # if a string is more than one sentence then we use a triple quote

string_examples = ['Asabeneh', 'finland', 'python']

# Booleans: CAPITALIZED!!!

boolean_examples = [True, False]

# List:
    # an order collection which allows to store different data type items
    # similar to an array in javascript
    # important distinction here, you CAN change the length
    # syntax uses square BRACKETS and commas
    # CAN HAVE A MIX OF DATA TYPES!!
    # examples:

number_list = [0, 1, 2, 3, 4, 5]
fruit_list = ['Banana', 'Orange', 'Mango', 'Avocado']
mixed_data_type_list = ['Banana', 10, False, 9.81]

# Dictionary
    # an unordered collection of data in a key value pair format
    # uses curly braces, this is like a map!!
    # ex:

myDict = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'country': 'Finland',
    'age': 250,
    'is_married': True,
    'skills': ['JS', 'React', 'Node', 'Python']
}

# Tuple
    # a tuple is an ordered collection of different data types LIKE a list but typles CANNOT!! be modified once they are created
    # they are immutable
    # they use parenthesis!!

tupleEx = ('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya')
secondTupleEx = ('Earth', 'Jupiter', 'Neptune')

# Set
    # a set is a collection of data types similar to a list and a tuple.
    # unlike list and tuples, a set is NOT an ordered collection of items.
    # Like in mathematics, set in python stores ONLY unique items
    # WE ALSO USE CURLY BRACKETS ERE LIKE IN DICTS BUT ITS NOT a KEY-VALUE PAIR TYPE

setEx = {2,4,3,5}
secondSetEx = {2.14, 9.81, 2.7}

"""CHECKING DATA TYPES"""
# to check the data types of certain data/variables we use the type funciton

print(type(3))

""" NOTES ON THE EXERCISES"""
# when you divide it actually gives you the exact float division, not integer division like java
# floor dibision gives you well floor division.. 
# questions i have unanswered: why does the class change name, like why is the data type Integer but the class is int, why is String str??