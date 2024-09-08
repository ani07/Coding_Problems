# Prime Numbers = No dividble by 1 and itself.

def is_prime(n):
	flag = True
	if n <= 1:
		return False
	for i in range(2, n):
		if n % i == 0 and n != i:
			flag = False
			break
	return flag



print(is_prime(int(input())))
