"""

Quiz.
1. What is a lambda function in Python?
    a) A named function defined using the lambda keyword.   <---
    b) An anonymous function defined using the def keyword.
    c) A function that can take multiple arguments.
    d) A function that returns multiple values.

2. Which of the following is a benefit of using a lambda function?
    a) It allows for complex logic and multiple statements. 
    b) It can be assigned a name for reusability.
    c) It is ideal for simple, one-line operations. <---
    d) It can accept an arbitrary number of arguments.

3. In Python, which type of argument requires the caller to provide a value when calling a function?
    a) Default argument
    b) Keyword argument
    c) Positional argument  <---
    d) Lambda argument 

4. What will the following code output?
    def multiply(a, b=2):
        return a * b

    result = multiply(3)
    print(result)

    a) 6  <---
    b) 9
    c) 3
    d) Error

5. Which of the following is a valid usage of a lambda function?
    a) Sorting a list of integers  <---
    b) Creating a dictionary
    c) Defining a class
    d) Iterating over a list  
    
6. In Python, what will the len() function return for the string "hello"?
    a) 5  <---
    b) 6
    c) 4
    d) 7

7. What is the purpose of a function in Python?
    a) To store variables.
    b) To perform a specific task or set of tasks.  <---
    c) To declare classes.
    d) To handle exceptions.

8. Which of the following is true about functions in Python?
    a) A function can only be defined using the def keyword.
    b) A function can return multiple values. <---
    c) A function cannot call other functions.
    d) A function can only accept a single argument.

9. What is the output of the following code?
    def greet(name):
        return f"Hello, {name}!"

    message = greet("Alice")
    print(message)

    a) "Hello, Alice!"  <---
    b) "Hello, name!"
    c) Error
    d) "Hello, world!"

10. Which of the following statements about keyword arguments is true?
    a) Keyword arguments must always come before positional arguments.
    b) Keyword arguments are specified using the key keyword.
    c) Keyword arguments provide a default value if not provided by the caller.  <---
    d) Keyword arguments are mandatory.

11. What is the purpose of the *args parameter in a function definition?
    a) To specify keyword arguments.
    b) To specify default values for arguments.
    c) To allow the function to accept an arbitrary number of positional arguments. <---
    d) To allow the function to accept an arbitrary number of keyword arguments.

12. In a lambda function, what does 'x' represent?
    a) The function itself.
    b) The argument being passed to the function.  <---
    c) The return value of the function.  
    d) The number of arguments the function can accept.

13. What will the following code output?
    text = "hello lambda"
    reverse_text = (lambda x: x[::-1])(text)
    print(reverse_text)

    a) "adamal olleh"  <---
    b) "ambda"
    c) "ah"
    d) Error

14. What is a default parameter in a function?
    a) A parameter that is automatically assigned a value if no value is provided by the caller.  <---
    b) A parameter that must always be specified by the caller.
    c) A parameter that has a fixed value and cannot be changed.
    d) A parameter that is only used for keyword arguments.

15. In which situation would using default parameters be most beneficial?
    a) When you want to ensure a parameter is always provided by the caller.
    b) When you want to assign a specific value to a parameter unless the caller provides a different value.  <---
    c) When you want to use a different function depending on the provided parameters.
    d) When you want to force the caller to use only keyword arguments.
    
16. What is the main difference between positional and keyword arguments in Python?
    a) Positional arguments are provided by specifying the argument value only, 
    while keyword arguments are specified with the parameter name and value.
    b) Positional arguments are mandatory, while keyword arguments are optional.  <---
    c) Positional arguments can be specified using the args keyword, while keyword 
    arguments use the kwargs keyword.
    d) Positional arguments can only be used for functions with a single parameter.
    
17. When should you use positional arguments over keyword arguments?
    a) When you want to provide arguments in a specific order.  <---
    b) When you want to ensure that the caller always provides a value for that argument.
    c) When you want to allow the caller to provide arguments in any order.
    d) When you want to provide a default value for an argument.
"""


"""- Functions -
A. Create a function 'greet_user' that takes a name as an argument and 
prints a greeting message with the provided name. The function should 
have a default parameter of "User" for the name."""


def greet_user(name="User"):
    print(f"Hello {name}")

greet_user()


"""B. Create a function calculate_sum that calculates the sum of an 
arbitrary number of integers passed as arguments. The function should use 
the *args parameter to accept a variable number of arguments."""


def calculate_sum(*args):
    return sum(args)


result = calculate_sum(1, 2, 3, 4, 5)
print("Sum:", result) 



"""C. Create a function display_info that takes a person's information 
(name, age, and city) as keyword arguments and prints the information."""

def display_info(name, age, city):
    print(f"Name: {name},\nAge; {age},\nLive: {city}")

display_info("ALi", 21, "Baku")


"""D. Create a function make_sandwich that takes the type of sandwich, and 
optional toppings and prints the details of the sandwich. The function 
should have a default parameter for the sandwich type and use keyword 
arguments for toppings."""

def make_sandwich(s_type="ham", **topings):
    print(f"Making {s_type} sandwich")
    if topings:
        print("Adding toppings:")
        for tooping, amount in topings.items():
            print(f"- {tooping}: {amount}")
    else:
        print("No additional toopings")

make_sandwich("Chicken", onion=1, tomato=3)


"""E. Create a function show_details that takes a person's name as a fixed 
parameter, followed by an arbitrary number of hobbies using the *args 
parameter. The function should print the person's name and their hobbies."""

def show_details(name, *args):
    print({"name": name, "hobbies": args})

show_details("Bob", "gaming", "videos")


"""F. Implement a function sort_numbers that takes a list of numbers as an 
argument and returns a sorted list in ascending order. Use the * operator 
to unpack the list."""

def sort_numbers(*numlist):
    return sorted(numlist)

numbers = [2, 3, 4, 9, 1, 10, 12, 8, 5, 6]

new_nums = sort_numbers(*numbers)
print(new_nums)


"""G. Create a function create_user that takes the user's name, age, and email 
as keyword arguments and prints a message welcoming the user. Ensure to handle 
missing or invalid email addresses."""


def create_user(**info):
    name = info.get("name")
    age = info.get("age")
    email = info.get("email")

    if (email) and ("@" in email):
        print(f"Hello {name}.\nYou're {age} years old.\nEmail: {email}")
    else:
        print(f"Hello {name}.You're {age} years old. Your email are missing")
              
create_user(name="Asiman", age="23", email="hayday@gmail.com")


"""H. Create a function generate_invoice that generates an invoice for a customer's 
purchase. The function should take the customer's name and purchase amount as 
required arguments, with an optional discount as a keyword argument. Calculate 
the final amount after applying the discount if provided."""

def generate_invoice(name, price, **discount):
    if 'discount' in discount:
        percentage = discount["discount"]
        discounted_price = price - (price * percentage/100)
        print(f"Invoice for {name}:\nPrice: {price}$\nDiscounted_price: {discounted_price}$")
    else:
        print(f"Invoice for {name}:\nPrice: {price}$")

generate_invoice("Asiman", 30, discount=2)


"""I. Create a function create_circle that creates a circle with specified properties 
(radius and color). Use keyword arguments to allow specifying these properties and 
validate the input."""


import math

class Circle:
    def __init__(self, radius=1, color='blue'):
        self.radius = radius
        self.color = color

    def create_circle(self):
        if not isinstance(self.radius, (int, float)):
            raise ValueError("Radius must be a number")
        if self.radius <= 0:
            raise ValueError("Radius must be greater than zero")
        if not isinstance(self.color, str):
            raise ValueError("Color must be a string")
        
        return self.radius, self.color

radius = 2.5
color = 'red'
circle = Circle(radius=radius, color=color)


circle_radius, circle_color = circle.create_circle()

print("Circle Radius:", circle_radius)
print("Circle Color:", circle_color)


"""J. Implement a function calculate_score that takes a student's scores in various 
subjects as keyword arguments and calculates their total score. Use the ** operator 
to handle an arbitrary number of subject scores."""

def calculate_score(**kwargs):
    total = sum(kwargs.values())
    return total

math = 90
history = 80
chemtry = 30

score = calculate_score(math_score=math, history_score=history, chemtry_score=chemtry)
print(score)


"""K. Write a function calculate_volume that calculates the volume of a cylinder using 
its radius and height. Use keyword arguments for the radius and height."""

import math

def calculate_volume(radius=3.0, height=4.0):
    V = math.pi * radius**2 * height
    return round(V, 2)

cylinder_volume = calculate_volume()
print(cylinder_volume)


"""L. Create a function print_person_info that takes a person's name as a positional 
argument and their age and city as keyword arguments. Print the person's name, age, and city."""


def print_person_info(name, age=None, city=None):
    print(f"Name: {name}\nAge: {age}\nCity:{city}")

print_person_info("Asiman", age=90, city="AUYe")


"""M. Implement a function show_order_details that takes the order number as a positional argument, 
followed by a dictionary of order items as keyword arguments. Print the order number and the 
items in the order."""

def show_order_details(order_number, **order_items):
    print("Order Number:", order_number)
    print("Order Items:")
    for item, quantity in order_items.items():
        print(f"{item}: {quantity}")


order_number = "23456"
order_items = {
    "Product 1": 2,
    "Product 2": 1,
    "Product 3": 3
}

show_order_details(order_number, **order_items)


"""N. Write a function that checks whether the given pattern from the user is a substring of
the 'Cybersecurity in Programming' phrase."""

def check_pattern(pattern):
    phrase = 'Cybersecurity in Programming'
    return pattern in phrase

pattern = input("Enter a pattern to check: ")
if check_pattern(pattern):
    print(f"The pattern '{pattern}' is a substring 'Cybersecurity in Programming'.")
else:
    print(f"The pattern '{pattern}' is not a substring 'Cybersecurity in Programming'.")


"""O. Write a function that raises all numbers from the passed list to the power of two."""

def power_of_list(arg):
    return pow(arg, 2)

numlist = [1, 2, 3, 4]
result = list(map(power_of_list, numlist))
print(result)


"""- Lambda Functions -
A. Write a brief explanation of what a lambda function is and when it's useful.

lambda is a one line simple anonim function.They are often used as arguments to higher-order functions 
(functions that take other functions as arguments), such as map(), filter(), and sorted()

"""


"""B. Create a lambda function that adds two numbers and test it with example inputs."""

add_nums = lambda x, y: x+y

print(add_nums(5, 11))


"""C. Create a lambda function that squares a given number and test it with example inputs."""

square = lambda x: x**2

print(square(5))


"""D. Create a lambda function that takes three parameters (a, b, c) and calculates 'a x b + c'."""

calculate = lambda a, b, c: (a * b) + c

print(calculate(3, 4, 5))


"""E. Create a lambda function that reverses a given string and test it with example inputs."""

descending_order = lambda x: x[::-1]

word = "World"

reverse_word = descending_order(word)
print(reverse_word)


"""F. Create a lambda function that capitalizes the first letter of a string and test it with 
example inputs."""

capitalize_first_letter = lambda x: x.capitalize()

print(capitalize_first_letter("ahmed"))


"""G. Create a lambda function that counts the number of vowels (a, e, i, o, u) in a given 
string and test it with example inputs."""


count_vowels = lambda x: len([char for char in x if char.lower() in 'aeiou'])

word = "Hello World"

print(count_vowels(word))


"""H. Create a lambda function that counts the number of words in a given string and test it 
with example inputs."""


count_words = lambda x: len(x.split())

words = "Hello, this is for test"
print(words)
result = count_words(words)
print(f"Total words: {result}")