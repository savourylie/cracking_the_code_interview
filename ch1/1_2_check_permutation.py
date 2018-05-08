from collections import defaultdict

def check_permutation(str1, str2):
	if not str1 and not str2:
		return True

	element_dict = defaultdict(int)

	for i, x in enumerate(str1):
		element_dict[x] += 1

	for i, x in enumerate(str2):
		element_dict[x] -= 1

	for key in element_dict:
		if element_dict[key] != 0:
			return False

	return True


if __name__ == '__main__':
	assert check_permutation('aaaba', 'baaaa') == True
	assert check_permutation('aaacba', 'bcaaaa') == True
	assert check_permutation('aaabac', 'dbaaaa') == False
	assert check_permutation('', 'dbaaaa') == False
	assert check_permutation('', '') == True

	print("All tests passed.")