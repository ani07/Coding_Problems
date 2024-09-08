# Python Program to check Armstrong Number
# Each digit raised to the power of number of digit.

def armstrong(n):
	total = 0
	temp = n
	length = len(str(n))
	while n > 0:
		rem = n % 10
		total += rem**length
		n //= 10
	if temp == total:
		return True
	else:
		return False 

print(armstrong(int(input())))
