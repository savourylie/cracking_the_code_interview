def is_unique(string):
	compare_dict = dict()

	for i, x in enumerate(string):
		if x in compare_dict:
			return False
		else:
			compare_dict[x] = 1

	return True

def is_unique_no_additonal(string):
	pass


if __name__ == '__main__':
	assert is_unique('abcdefg') == True
	assert is_unique('abcdabg') == False

	print("All tests passed.")
