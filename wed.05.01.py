#---Easy
#create a function that subtracts two numbers and alerts the difference

def subTwo(x, y):
    result = x - y 
    return result
result = subTwo(8, 3)
print(result)  # Output: 5



#create a function that divides three numbers and prints the quotient

def div_quotient(x, y, z):
    quotient = x / y / z
    print("Quotient:", quotient)
    return quotient
div_quotient(10, 2, 5)

#create a function that multiplys three numbers and returns the product
def mult_nums(x, y, z):
    result = x * y * z
    print("Multiplication result:", result)
    return result
mult_nums(2, 5, 2)

#---Medium
#create a function that takes in three numbers. Add the first two numbers and return the remainder of dividing the sum of the first two numbers by the third number

def add_and_remainder(x, y, z):
    # Add the first two numbers
    sum_xy = x + y
    
    # Calculate the remainder of dividing the sum by the third number
    remainder = sum_xy % z
    
    return remainder

# Example usage:
result = add_and_remainder(10, 5, 3)
print("Remainder:", result)

#---Hard
#create a function that takes in 4 numbers. Multiply the first two numbers. If the product is greater than 100 add the sum of the last two numbers and print the value. If the product is less that 100, subtract the difference of the last two numbers and print the value. If the product is 100, multiply the first three numbers together and print the remainder of dividing the fourth number
def complex_operation(a, b, c, d):
    product = a * b

    if product > 100:
        result = product + c + d
    elif product < 100:
        result = product - (c - d)
    else:
        result = (a * b * c) % d
    
    print("Result:", result)

# Example usage:
complex_operation(10, 5, 20, 4)