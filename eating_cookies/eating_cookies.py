'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here

    if n <= 0:
        return 1

    if n == 1:
        return 1

    if n == 2:
        return 2

    if n > 2:
        sequence = [1, 1, 2]
        for x in range(n - 2):
            sequence.append(sum(sequence))
            sequence.pop(0)

        return sequence[2]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
