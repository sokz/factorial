
# The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. Solve this using both loops and recursion.

def factorial(num):
    result = 1
    while num != 0:
        result *= num
        num -= 1
    return result

if __name__== '__main__':
    number = int(input("Enter the number to calculate factorial: "))
    print(f"The factorial for {number} is {factorial(number)}")

