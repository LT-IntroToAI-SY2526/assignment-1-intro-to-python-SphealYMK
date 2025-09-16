# Assignment 1: AI-Generated Python Problems
# Name: Matthew Kupiec

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
I'm learning Python basics in a high school programming class.
I'm new to programming. Can you create 5-7 practice problems that cover:
-Variables and basic data types
-Conditionals (if/elif/else)
-Loops (for and while)
-Functions
-Basic list operations

Make them progressively more challenging.
Make sure each problem has clear instructions and example inputs/outputs.
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: Variables and Basic Data Types
Description: Create a program that stores your name and age in variables. Then, print a sentence introducing yourself.
-Create a variable called name and assign your name to it (string).
-Create a variable called age and assign your age to it (integer).
-Print a sentence: "Hello, my name is <name> and I am <age> years old."

Example inputs/outputs:
Input:
name = "Alice"
age = 15
Output:
Hello, my name is Alice and I am 15 years old.

PROBLEM 2: Conditionals
Description:Write a program that takes a number and tells whether it is positive, negative, or zero.
-Create a variable num with an integer value.
-Use if/elif/else statements to print:
-Positive if num > 0
-Negative if num < 0
-Zero if num == 0

Example inputs/outputs:
Input:
num = -3
Output:
Negative

PROBLEM 3: Loops (for loop)
Description: Print all the even numbers from 2 to 20 inclusive.
-Use a for loop to iterate through numbers 2 to 20.
-Print only even numbers (divisible by 2).

Example inputs/outputs:
Output:
2
4
6
8
10
12
14
16
18
20

PROBLEM 4: Loops (while loop)
Description: Write a program that counts down from 10 to 1 using a while loop, then prints "Blast off!".
-Initialize a variable with 10.
-Use a while loop to print the countdown numbers.
-After the loop, print "Blast off!".

Example inputs/outputs:
Output:
10
9
8
7
6
5
4
3
2
1
Blast off!


PROBLEM 5:
Description: Write a function is_even(number) that takes a number as input and returns True if the number is even, and False otherwise.
-Define a function called is_even with one parameter.
-Use the modulo operator % to check if the number is even.
-Return True or False.

Example inputs/outputs:
Input:
print(is_even(4))
print(is_even(7))
Output:
True
False

PROBLEM 6: Basic List Operations
Description: Create a list of five favorite fruits. Write a program that prints each fruit on a separate line using a loop.
-Create a list variable fruits with 5 fruit names (strings).
-Use a loop to print each fruit.

Example inputs/outputs:
Output:
Apple
Banana
Cherry
Date
Elderberry
"""











# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
age = 17
name = "Matthew Kupiec"
print(f"Hello, my name is " {name} " and I am " {age} " years old")

print("\nTesting Problem 2:")
num = -3 
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

print("\nTesting Problem 3:")
for num in range(2, 21):  
    if num % 2 == 0: 
        print(num)

print("\nTesting Problem 4:")
count = 10
while count > 0:
    print(count)
    count -= 1 
print("Blast off!")

print("\nTesting Problem 5:")
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
        
print(is_even(4))
print(is_even(7))


print("\nTesting Problem 6:")
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

for fruit in fruits:
    print(fruit)

