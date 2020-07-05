"""
This solution is baswd on Problem statement from PEA Problem Number 5
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.
"""


def smallest_divisible():
    prime_products = 9699690
    for i in range(prime_products, 10000000000, 19):
        count = 0
        for num in range(2, 21):
            print(i, num)
            if i % num != 0:
                break
            else:
                count += 1
        print(count, "========================")
        if count == 19:
            return i


print(smallest_divisible())