# Python program to find Cumulative sum of a list

def cum_sum(li):
	add = 0
	result = []
	for i in li:
		add += i 
		result.append(add)
	return result


print(cum_sum([10, 20, 30, 40, 50]))