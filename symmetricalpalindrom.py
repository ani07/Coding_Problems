# to check whether the string is Symmetrical or Palindrome

def sympal(s):
	length = len(s)
	sym = True
	if length%2 == 0:
		if s[:length//2] == s[length//2:]:
			sym = True
		else:
			sym = False
	else:
		sym = False

	def pali(s):
		pal = True
		length = len(s)
		if length<2:
			pal = True
		elif s[0] == s[length-1]:
			return pali(s[1:length-1])
		else:
			pal = False
		return pal
	pali = pali(s)
	return pali, sym

print(sympal('khokho'))