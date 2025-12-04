# James Nickell

# Period 7

# Value Function Practice

# TOO LONG


# Defines the sum, difference, product, and quotient
def operation(num1, num2):
    sum = num1 + num2 
    difference =  num1 - num2
    product = num1 * num2 
    quotient = num1/num2 
    return sum, difference, product, quotient


# Asks for your 2 numbers
x = int(input("Enter a number: "))

y = int(input("Enter another number: "))


# Prints the answers
print(operation(x, y))
