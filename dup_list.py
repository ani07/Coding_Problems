#Program to print duplicates from a list of integers

def dup_list(li):
	every_element = []
	dup_list = []
# 	for i in li:
# 		if i in every_element and i not in dup_list:
# 			dup_list.append(i)
# 		else:
# 			every_element.append(i)
# 	return dup_list



# Using counter method from collection

# from collections import Counter
 
# l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
# d = Counter(l1)
# print(d)
 
# new_list = list([item for item in d if d[item]>1])
# print(new_list)

# Using count method or countof
	for i in li:
		if li.count(i) > 1 and i not in dup_list:
			dup_list.append(i)
	return dup_list

print(dup_list([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]))
