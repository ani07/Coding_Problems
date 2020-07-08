"""
This solution is baswd on Problem statement from PEA Problem Number 6
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
"""

def difference():
    sum_square = 0
    square_of_num = 0

    for num in range(1,101):
        sum_square += num
        square_of_num += num ** 2

    diff = sum_square ** 2 - square_of_num
    return  diff

print(difference())

"""
One more way is 
limit = 100
sum = limit(limit + 1)/2
sum sq = (2limit + 1)(limit + 1)limit/6
print sum2 − sum sq
"""