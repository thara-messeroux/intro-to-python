# This is a comment! Python will ignore it.
"""
this is a
multiline comment
"""

'''
this is also a multiline comment
you can use either set of quotes
'''

# this is a
# multiline comment

print("Hello, world!") # prints: Hello, world!

num = 15
# movie
# returns: NameError: name 'movie' is not defined
# this is illegal syntax that cannot be used

# in Python, we use snake_case
my_number = 10

# in Python, we use camelCase
myNumber = 10
# in Python, we use PascalCase
MyNumber = 10
# in Python, we use UPPER_SNAKE_CASE
MY_NUMBER = 10

my_number = 15
print(my_number)
# prints: 15
my_number = -4
print(my_number)
# prints: -4
my_number = 3.14
print(my_number)

MY_FAVORITE_NUMBER = 5
print(MY_FAVORITE_NUMBER)
# prints: 5
MY_FAVORITE_NUMBER = 7
print(MY_FAVORITE_NUMBER)
# prints: 7

print(type("hello"))
# prints: <class 'str'>
print(type(3.14))
# prints: <class 'float'>

print(type(25))
# prints: <class 'int'>

print(type(3.14159))
# prints: <class 'float'>

print(type(25.))
# prints: <class 'float'>

print(type(True))
# prints: <class 'bool'>


# print(type(true))
# NameError: name 'true' is not defined. Did you mean: 'True'?


# None = null
print(type(None))
# prints: `<class 'NoneType'>`


# let numTacos = 25;
# let msg = "There are " + numTacos + " tacos.";
# // msg is the string: "There are 25 tacos."



# num_tacos = 25
# msg = "There are " + num_tacos + " tacos."
# TypeError: can only concatenate str (not "int") to str

# str(item)        # Converts `item` to a string
# int(item, base)  # Converts `item` to an integer with the provided `base`
# float(item)      # Converts `item` to a floating-point number
# hex(int)         # Converts `int` to a hexadecimal string
# oct(int)         # Converts `int` to an octal string
# tuple(item)      # Converts `item` to a tuple
# list(item)       # Converts `item` to a list
# dict(item)       # Converts `item` to a dictionary

result = 4 / 2
print(result)
# prints: 2.0
print(type(result))
# prints: <class 'float'>

result = 4 // 2
print(result)
# prints: 2 because the decimal ".0" is truncated

# this line of code:
num = num + 1
# can be written with this shortcut operator:
num += 1

# it also works for any of the other math operations:
num = num / 5
# can be rewritten like this:
num /= 5

# and this line:
num = num * 3
# can be written as this:
num *= 3
# and so on with the other operators

my_string = "A double-quoted string"
your_string = 'A single quoted string'


multiline_string = '''This is my string that
                      goes on multiple lines
                      for whatever reason'''

little_string = "bad"
medium_string = "super"
long_string = medium_string + little_string
print(long_string)
# prints: superbad

state = "Hawaii"
year = 1959
message = f"{state} was the last state to join the U.S. in {year}."
print(message)
# prints: Hawaii was the last state to join the U.S. in 1959.

print("ace of spades".split(" "))
# prints: ['ace', 'of', 'spades']

# however, this won't work:
print("abcd".split(""))
# ValueError: empty separator

# instead, use the list() function like this:
print(list("abcd"))
# prints: ['a', 'b', 'c', 'd']

# get the index of a substring:
print("abcd".index("c"))    
# prints: 2
# this method raises an error if the substring is not found:
print("abcd".index("e"))
# ValueError: substring not found

# .find() is similar to .index() but returns -1 if the substring is not found
# this behavior may be preferable to raising an error:
print("abcd".find("e"))
# prints: -1

print("boo".upper())
# prints: 'BOO'

print("WHY???".lower())
# prints: 'why???'

print("Then I went to the store I like".replace("I", "you"))
# prints: 'Then you went to the store you like'

print("eggs" in "green eggs and ham")
# prints: True

print(len("Tacos"))
# prints: 5






