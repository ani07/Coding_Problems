# Fibbonnic series 0,1,1,2,3,5,8,13, ...................

def fib_series(n):
	initial = 0
	next_ele = 1
	fib = [0, 1]
	while n != 0:
		fib.append(initial + next_ele)
		temp = initial
		initial = next_ele
		next_ele += temp
		n -= 1
	return fib


print(fib_series(11))