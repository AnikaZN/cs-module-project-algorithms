# GOAL: Create a factorial function

# Understand:
# - What is a factorial?
# -- n! / n * (n - 1)...1

# Plan:
# - Recursively or iteratively?
# -- Recursion, since this is an unpredictably repeating problem
# --- Base case (n = 1), Move towards it (multiply by n - 1?), Call itself
#    (function_name(result))

# Execute:

def factorial_rec(n):
    if n == 1:
        return 1
    else:
        return n * factorial_rec(n - 1)

# Plan
# - Let's try it iteratively!
# -- Make a tracker: total, make a while loop to decrement n, multiply tracker
#    at every step, return tracker

# Execute:

def factorial_it(n):
    total = 1

    while n != 1:
        total *= n
        n -= 1

    return total

# Review:
# Space complexity: Iterative!
# Time complexity: O(n) for both!
# Readability: Subjective; I prefer recursive approach
# - Objectively, iterative approach is better
