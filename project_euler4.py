"""

This solution is baswd on Problem statement from Project Euler Problem Number 4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

"""

class CheckLargestPalindrome():

    def largestthreedigit(self):
        palindrome_list = []
        for i in range(999,100,-1):
            for j in range(999,100,-1):
                rev = 0
                product = i*j
                print(i, j, product)
                temp = product
                while temp > 0:
                    rev = rev *10 + temp%10
                    temp //= 10
                print (rev, product, end = '\n')
                if rev == product:
                    palindrome_list.append(product)
        return max(palindrome_list)


ans = CheckLargestPalindrome()
print(ans.largestthreedigit())


"""
Consider the digits
of P – let them be x, y and z. P must be at least 6 digits long since the
palindrome 111111 = 143×777 – the product of two 3-digit integers. Since P is
palindromic:
P=100000x10000y1000z100z10yx
P=100001x10010y1100z
P=119091x910y100z
Since 11 is prime, at least one of the integers a or b must have a factor of 11.
So if a is not divisible by 11 then we know b must be. Using this information
we can determine what values of b we check depending on a:
"""