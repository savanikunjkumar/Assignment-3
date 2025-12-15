# Task 1: Calculate Factorial Using a Function

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result

# Calling the function with a sample number
number = 5
output = factorial(number)

print("Factorial of", number, "is:", output)