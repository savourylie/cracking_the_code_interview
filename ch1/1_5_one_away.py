def one_away(str1, str2):
	if str1 == str2:
		return False

	if len(str1) > len(str2):
		return one_insert_away(str1, str2)

	elif len(str1) < len(str2):
		return one_insert_away(str2, str1)

	else:
		return one_replace_away(str1, str2)


def one_insert_away(str1, str2):
	if len(str1) != len(str2) + 1:
		return False
		
	i, j = 0, 0
	diff_count = 0

	while i < len(str1):
		try:
			_ = str2[j]
		except IndexError:
			return True

		if str1[i] != str2[j]:
			diff_count += 1

			if diff_count > 1:
				return False

			i += 1

		else:
			i += 1
			j += 1

	return True


def one_replace_away(str1, str2):

	count = 0

	for i, x in enumerate(str1):
		if x != str2[i]:
			count += 1
	
	return False if count > 1 else True


if __name__ == '__main__':
	assert one_away('pale', 'ple')
	assert one_away('pales', 'pale')
	assert one_away('pale', 'bale')
	assert not one_away('pale', 'bake')

	print("All tests passed.")

