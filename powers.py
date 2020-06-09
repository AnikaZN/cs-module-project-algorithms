# GOAL: Given a and b, return a^b, without using **

# Understand
# - What is a^b doing?
# -- a * a, b times
# - What are valid/invalid inputs?
# -- Invalid: Letters, Valid: All non-negative numbers

# Plan
# We have two positive numbers
# Iterative first
# - While loop: decrement b to approach 0, multiply a by a, maintain original a

# Execute:

def powers_it(a, b):
    value = a

    if b == 0:
        return 1

    while b != 1:
        value *= a
        b -= 1

    return value

# Review:
# - How can we handle negative values in the place of b?

# Plan:
# Decimal values
# - Check if b is an integer, otherwise return error
# Negative numbers

def powers_it_plus(a, b):
    value = a
    invert = False

    if type(b) != int:
        return 'Error! Please enter a whole number!'

    if b == 0:
        return 1

    if b < 0:
        b *= -1
        invert = True

    while b != 1:
        value *= a
        b -= 1

    if invert:
        return 1 / value
    else:
        return value
