Creating Variables
x = 5
y = "John"
print(x)
print(y)

Creating Variables
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x) #Sally

Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

Get the Type
x = 5
y = "John"
print(type(x))
print(type(y))

Single or Double Quotes?
x = "John"
# is the same as
x = 'John'

Case-Sensitive
a = 4
A = "Sally"
#A will not overwrite a


Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"

Camel Case
Each word, except the first, starts with a capital letter:
myVariableName = "John"

Pascal Case
Each word starts with a capital letter:
MyVariableName = "John"

Snake Case
Each word is separated by an underscore character:
my_variable_name = "John"

Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

Unpack a Collection
Unpack a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

Output Variables
The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)

In the print() function, you output multiple variables, separated by a comma:
Example
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

You can also use the + operator to output multiple variables:
Example
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

For numbers, the + character works as a mathematical operator:
Example
x = 5
y = 10
print(x + y)

In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
Example
x = 5
y = "John"
print(x + y)
The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
Example
x = 5
y = "John"
print(x, y)

Global Variables
Variables that are created outside of a function (as in all of the examples above) are known as global variables.
Example
Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

Create a variable inside a function, with the same name as the global variable
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x)
***
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
***
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
