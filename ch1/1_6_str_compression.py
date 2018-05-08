def str_compression(string):
	if len(string) == 0 or len(string) == 1:
		return string

	prev = None
	count = 1
	compressed = False
	result_str = ''

	for i, x in enumerate(string):
		current = x

		if prev is None:
			prev = current

		else:
			if current == prev:
				count += 1

			else:
				if count > 1:
					compressed = True
				result_str += prev + str(count)
				prev = current
				count = 1

	if count > 1:
		compressed = True
	result_str += prev + str(count)

	return result_str if compressed else string


if __name__ == '__main__':
	assert str_compression('aabcccccaaa') == 'a2b1c5a3'
	assert str_compression('abc') == 'abc'
	assert str_compression('abcdd') == 'a1b1c1d2'
	assert not str_compression('abcdd') == 'a1b1c1d4'
	
	print("All tests passed.")
