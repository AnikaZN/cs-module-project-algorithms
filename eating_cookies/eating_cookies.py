'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    ways = 0

    if n <= 0:
        return "Oh no! There's no cookies in the cookie jar!"

    # Can always eat the cookies one at a time
    ways += 1

    if n // 2 

    pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
