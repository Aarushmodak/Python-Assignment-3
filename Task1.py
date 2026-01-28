# Task 1: Calculate Factorial Using a Function 

def factorial(num):
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    return factorial

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")