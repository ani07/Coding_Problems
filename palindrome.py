# Python program to check if a string is palindrome or not

# def palindrom(s):
# 	rev_str = ''
# 	for i in s:
# 		rev_str = i + rev_str

# 	if rev_str == s:
# 		return True
# 	else:
# 		return False

# print(palindrom('malayalam'))


# Write a recursive function.
def isPalindrome(s):
	if len(s)<2:
		return True
	length = len(s)
	for i in s:
		if i == s[length-1]:
			return isPalindrome(s[1:-j])
		else:
			return False
	return True

print(isPalindrome('locol'))





# Using the reverse indexing.

# def is_palindrom(s):
# 	j = -1
# 	for i in s:
# 		if i  == s[j]:
# 			j -= 1
# 			continue
# 		else:
# 			return False
# 	return True

# print(is_palindrom('leveL'))

# Using iterative method

# def isPalindrome(str):
#     for i in range(0, int(len(str)/2)):
#         if str[i] != str[len(str)-i-1]:
#             return False
#     return True

# s = "malayalam"
# ans = isPalindrome(s)

# if (ans):
#     print("Yes")
# else:
#     print("No")


# Write the same code using index.

# def is_palindrom(s):
# 	length = len(s)
# 	for i in range(length):
# 		if s[i] == s[length-i-1]:
# 			continue
# 		else:
# 			return False
# 	return True

# print(is_palindrom('animesh'))