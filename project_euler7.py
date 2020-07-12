""" 
This solution is baswd on Problem statement from PEA Problem Number 7
What is the 10 001st prime number.
"""


def xprime_number():
    prime_list = []
    for i in range(2, 1000000000):
        for j in range(2, i//2+1):
            if i%j == 0:
                break
        else:
            prime_list.append(i)
        print(prime_list)
        if len(prime_list) == 10001:
            break
    return prime_list[-1]


print(xprime_number())